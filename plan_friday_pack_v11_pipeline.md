# Friday Pack v1.1 — One-Command Pipeline

**Status:** Tomorrow project (2026-05-15+). Tonight's build (v1.0) shipped manually, took ~10 hours. v1.1 collapses it to one command.

## What v1.1 must do

Single command:
```bash
make_friday_pack.py --group miami_metro [--manual ~/Desktop/manual.csv]
```

…produces a `Friday_Pack_<market>_<date>.zip` on Desktop. Orchestrates:

1. **Parallel harvests** across all markets in the group (per `markets.yaml` `groups:` block).
2. **Merge** all source CSVs.
3. **`group_by_owner`** for cross-source dedup.
4. **Optionally** merge a manual-agent CSV (if `--manual` passed).
5. **`enrich_pack`** for county-records portfolio + tags + tailored opener.
6. **`build_friday_pack_delivery`** with strict quality gate.
7. **Zip** the final folder.
8. **Print** "X leads ready at ~/Desktop/Friday_Pack_<market>_<date>.zip"

## Key changes needed

### 1. markets.yaml — add groups + per-market allowed/banned zips
```yaml
groups:
  miami_metro:
    markets: [miami_fl, miami_wynwood, miami_metro_north, miami_downtown, fort_lauderdale_fl]
    allowed_zips: [33009, 33019, 33020, 33021, 33024, 33127, 33141, 33160, 33172, 33178, 33180, 33181, 33301, 33304, 33305, 33308, 33312, 33316, 33334, 33130, 33131, 33132, 33137]
    banned_zips: [33125, 33133, 33134, 33136, 33139, 33140, 33142, 33154, 33161]
  smokies:
    markets: [sevierville_tn, gatlinburg_tn]
    allowed_zips: [...]
    banned_zips: [...]
```

### 2. `scripts/make_friday_pack.py` — new orchestrator
- Subprocess.run each `broader_harvest.py --market X` in parallel via concurrent.futures
- Each writes to a temp CSV
- Merge after all complete
- Then sequential: group → optional manual merge → enrich → build → zip

### 3. `scripts/build_friday_pack_delivery.py` — generalize zip config
- Pull `allowed_zips` / `banned_zips` from markets.yaml `groups:` block, NOT hardcoded.

### 4. Manual blocklist serialization
- `data/manual_blocklist.yaml` with phone numbers + reason + date_added
- `build_friday_pack_delivery.py` loads it instead of hardcoded `MANUAL_PHONE_BLOCKLIST`

### 5. Manual-row scoring within score=100
- Don't tie all manual rows at 100. Compute a sub-score:
  - n_listings_seen >= 5: +20
  - n_listings_seen 3-4: +15
  - 2+ in notes mentions "multi-unit": +15
  - is_entity (LLC in owner name): +10
  - "absentee" or out-of-area area code: +5
- Top of pack = strongest multi-unit owner-direct row, not first alphabetically.

### 6. Print friendly run summary
End of run, print:
```
Friday Pack — Miami Metro — Week of YYYY-MM-DD
─────────────────────────────────────────────
Total candidates:     359
Quality-filtered:     287 (175 no phone, 33 fake, 10 blocklist, ...)
Final pack:            65 verified landlords
Multi-unit (3+):       11
Top of pack:           Lauder Management (4 units)
Cost:                  $X.XX LLM + 0 Apify
Wall-clock:            42 min
Output:                ~/Desktop/Friday_Pack_Miami_Metro_2026-05-22.zip
```

## Stretch — v1.2 (not v1.1)

- Replicate the manual Zumper/Apartments agent research as automated Playwright + Hermes
- Move enrichment to Broward County PA API (currently fails on Hollywood/FL/Hallandale)
- Hosted tracker URL (Vercel) to eliminate Safari `file://` localStorage issue

## Testing checklist (before v1.1 trust)

Before letting v1.1 run unsupervised on Friday morning:
- Run on Miami Metro twice, diff outputs (should be stable + within ~5% lead count variance week-to-week)
- Manually QA the top 20 leads each run for any pattern of slip-through
- Confirm cost cap: alert if any single run exceeds $5 in LLM
- Run with `--dry-run` flag that skips LLM calls but exercises the rest

## Why v1.1 matters
Tonight at 10 hours of hands-on time, Friday Pack isn't a product — it's a project. v1.1 brings it down to ~45 min wall-clock + 5 min QA. THAT is when it scales to weekly delivery for paying customers.
