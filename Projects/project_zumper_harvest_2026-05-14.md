---
name: zumper-harvest-2026-05-14
description: New Zumper scraper for Friday Pack — JSON-LD telephone extraction, schema-compatible with broader_harvest.py
metadata:
  type: project
---

# Zumper Harvest Scraper — Shipped 2026-05-14

New scraper at `C:\Users\samth\projects\landlord-outreach\scripts\zumper_harvest.py`. Schema-compatible with [[broader-harvest]] so `build_friday_pack_delivery.py` consumes either source.

**Why:** Zumper lookups had been manual via Claude agents; this automates them. Per [[reference_scraper_techniques]] the `telephone` field in Zumper JSON-LD hits ~87% even when "Request Tour" UI hides it.

**How to apply:** Add to weekly Friday Pack pipeline alongside broader_harvest. Output CSV merges into the same per-owner aggregation step.

## CLI

```
uv run python scripts/zumper_harvest.py --market miami_fl --dry-run
uv run python scripts/zumper_harvest.py --market miami_fl --limit 200
```

## First-run results (Miami, limit 30)

- 113 unique listing URLs from 5 paginated city pages
- 28 detail fetches → 28 kept, 17 with phones (61% phone yield)
- 0 jsonld_missing, 0 captcha hits

## Implementation gotchas (worth keeping)

1. **`/apartments-for-rent/zip-XXXXX` 301-redirects to homepage.** Use `/apartments-for-rent/<city-state-slug>` + `?page=N` for pagination. Per-zip URL `/apartments-for-rent/miami-fl/zip-33160` returns 200 but listings are XHR-loaded — server HTML has zero anchors.
2. **Skip `/address/` paths entirely.** They surface in search results but carry no listing JSON-LD (only `ImageObject` blocks). Regex-fallback phones from /address pages risk pulling Zumper's own contact number — silent pollution.
3. **scrapling `get_all_text()` returns empty for `<script>` nodes.** Use raw regex (`JSONLD_RE`) on response body to extract JSON-LD blocks.
4. **JSON-LD is split across multiple blocks per listing.** `ApartmentComplex` carries telephone/geo/address; `Product` carries `offers.lowPrice`. `extract_listing` falls back across all blocks per field.
5. **Captcha guard, no silent skip** (per [[feedback_silent_skip_pattern]]): detects `verify you are human` / `cf-chl-` / `captcha-delivery` / `px-captcha`, backoff 60s, retry once, then `sys.exit(3)` with loud message.

## Output schema (matches broader_harvest)

`market, score, phone, owner_name, building_type, rent, bedrooms, bathrooms, available_units, building_total_units, address, zip, hoa_likely, lease_min_months, str_signals, title, url, post_date, desc_excerpt`

`available_units`, `building_total_units`, `lease_min_months`, `str_signals` left blank — Zumper JSON-LD doesn't expose them. `hoa_likely` always `?`.

## TODO (deferred — needs new dep)

`_stub_str_permit_flag()` raises NotImplementedError. Parsing Zumper's permit/STR-allowed flags would need an authenticated API client. Sam-decide before adding.
