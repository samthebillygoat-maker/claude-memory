"""Priority ranker for Friday Pack delivery.

Uses only signals already in the by-owner CSV + enrichment.json — no new
data sources. Replaces opaque "Score 85" with a transparent A/B/C tier
plus a numeric priority score so the customer knows which calls to make first.

Signals and weights:
  portfolio_size    : max(CL listings, county parcels), capped at 10  -> up to 60 pts
  LLC / entity      : sophisticated, won't spook on lease addendum    ->     12 pts
  absentee phone    : owner wants hands-off cash flow                 ->     10 pts
  multi-phone       : 2+ contacts on listing = business operation     ->      4 pts
  county-confirmed  : mdpa_parcels >= 2                               ->      3 pts

Tiers (intentionally generous A so the top of every pack feels like the
priority list, not the long tail):
  A: priority_score >= 30   ("CALL FIRST")
  B: priority_score >= 15   ("STRONG")
  C: priority_score <  15   ("OPPORTUNISTIC")

Tiebreaks: portfolio_size desc, then agg_score desc, then alphabetical owner.
"""
from __future__ import annotations


def _int(v, default=0) -> int:
    try:
        return int(v or default)
    except (ValueError, TypeError):
        return default


def priority_score(row: dict, enrichment_entry: dict | None = None) -> tuple[int, str, dict]:
    """Return (numeric_score, tier_letter, breakdown_for_debug).

    `row` is one record from by_owner CSV. `enrichment_entry` is the matching
    enrichment.json entry (may be None).
    """
    e = enrichment_entry or {}
    tags = e.get("tags") or []

    n_props = _int(row.get("n_unique_addresses"), 1)
    mdpa_parcels = _int(e.get("mdpa_parcels"), 0)
    portfolio = max(n_props, mdpa_parcels)

    is_entity = (row.get("entity") or "").lower() == "yes" or "LLC owner" in tags
    # enrich_pack sets is_local_area=True by default; only False when phone area
    # code differs from market area codes -> absentee owner.
    is_absentee = e.get("is_local_area") is False

    phones_str = (row.get("phones") or "")
    n_phones = sum(1 for p in phones_str.split(";") if p.strip())

    pts = 0
    bd = {}
    bd["portfolio"] = min(portfolio, 10) * 6
    pts += bd["portfolio"]

    bd["entity"] = 12 if is_entity else 0
    pts += bd["entity"]

    bd["absentee"] = 10 if is_absentee else 0
    pts += bd["absentee"]

    bd["multi_phone"] = 4 if n_phones >= 2 else 0
    pts += bd["multi_phone"]

    bd["county_confirmed"] = 3 if mdpa_parcels >= 2 else 0
    pts += bd["county_confirmed"]

    if pts >= 30:
        tier = "A"
    elif pts >= 15:
        tier = "B"
    else:
        tier = "C"
    return pts, tier, bd


def sort_by_priority(rows: list[dict], enrichment: dict) -> list[dict]:
    """Sort by priority desc, then portfolio desc, then agg_score desc, then owner.

    Mutates each row to add `_priority_score`, `_priority_tier`, `_portfolio`
    so the caller (build_html) can render them without recomputing.

    `enrichment` is the loaded enrichment.json: {"1": {...}, "2": {...}, ...}
    where the key is the rank string the row had on input.
    """
    # First pass: stamp each row with priority. Use original input order as
    # the lookup key into enrichment (matches how build_friday_pack_delivery.py
    # currently joins enrichment by rank).
    for i, r in enumerate(rows, 1):
        ent = enrichment.get(str(i)) or {}
        pts, tier, _bd = priority_score(r, ent)
        r["_priority_score"] = pts
        r["_priority_tier"] = tier
        r["_portfolio"] = max(
            _int(r.get("n_unique_addresses"), 1),
            _int(ent.get("mdpa_parcels"), 0),
        )

    rows.sort(
        key=lambda r: (
            -r["_priority_score"],
            -r["_portfolio"],
            -_int(r.get("agg_score"), 0),
            (r.get("owner_name") or "").lower(),
        )
    )

    # Re-key enrichment to the NEW order so build_html still finds it by rank.
    # Build a new dict mapping new_rank_str -> original enrichment payload.
    new_enrichment = {}
    for new_rank, r in enumerate(rows, 1):
        # Find which original rank this row had — we can re-derive from the
        # row's own fields, but simpler: stash original_rank on the row above.
        pass
    return rows


def rekey_enrichment(rows_before_sort: list[dict], rows_after_sort: list[dict],
                     enrichment: dict) -> dict:
    """After sorting, rebuild enrichment dict so its keys match new ranks.

    Matches rows by sample_url (unique per landlord in the pack) since the
    by-owner CSV doesn't have a stable id column.
    """
    url_to_orig_rank = {}
    for i, r in enumerate(rows_before_sort, 1):
        u = r.get("sample_url") or r.get("owner_name") or f"row{i}"
        url_to_orig_rank[u] = str(i)

    new = {}
    for new_rank, r in enumerate(rows_after_sort, 1):
        u = r.get("sample_url") or r.get("owner_name") or ""
        orig_rank = url_to_orig_rank.get(u)
        if orig_rank and orig_rank in enrichment:
            new[str(new_rank)] = enrichment[orig_rank]
    return new


def tier_label(tier: str) -> str:
    return {
        "A": "CALL FIRST",
        "B": "STRONG",
        "C": "OPPORTUNISTIC",
    }.get(tier, "")


if __name__ == "__main__":
    # Smoke test
    sample_rows = [
        {"owner_name": "Big Portfolio LLC", "n_unique_addresses": "12",
         "entity": "yes", "phones": "305-555-0001; 305-555-0002",
         "agg_score": "70", "sample_url": "u1"},
        {"owner_name": "Tiny", "n_unique_addresses": "1", "entity": "no",
         "phones": "954-555-0010", "agg_score": "55", "sample_url": "u2"},
        {"owner_name": "Absentee Mike", "n_unique_addresses": "3",
         "entity": "no", "phones": "212-555-0099",
         "agg_score": "60", "sample_url": "u3"},
    ]
    enr = {
        "1": {"mdpa_parcels": 14, "is_local_area": True, "tags": ["LLC owner"]},
        "2": {"mdpa_parcels": 0, "is_local_area": True, "tags": []},
        "3": {"mdpa_parcels": 2, "is_local_area": False,
              "tags": ["absentee — 212 area code"]},
    }
    before = [dict(r) for r in sample_rows]
    after = sort_by_priority(list(sample_rows), enr)
    for r in after:
        print(f"{r['_priority_tier']}  {r['_priority_score']:>3}  "
              f"portfolio={r['_portfolio']:>2}  {r['owner_name']}")
