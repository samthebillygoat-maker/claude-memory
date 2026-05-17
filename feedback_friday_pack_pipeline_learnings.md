# Friday Pack Pipeline Learnings — 2026-05-15 build

Hard-won lessons from tonight's marathon build. Apply to v1.1 architecture.

## Quality-bar lessons

1. **Geo filter must be a HARD GATE on output, not just a score boost on harvest.** Original `broader_harvest.py` used target-zip as +15 score boost only. Result: out-of-target leads (33175 West Kendall, 33186, Hialeah) leaked to top of pack because they had strong scores from other signals. Fixed by adding `out_of_target_zip` filter in `build_friday_pack_delivery.py:passes_quality_gate()` that drops any row whose LLM-extracted zip OR address-text-mentioned zip isn't in `ALLOWED_MIAMI_METRO_ZIPS`.

2. **"Owner name" from LLM extraction is unreliable.** LLM frequently grabs descriptive phrases ("retired bilingual medical professional", "Sun-May" from "Sun-May Properties Inc" parse), persona descriptions, or random text. Added `looks_like_real_name()` filter in `build_friday_pack_delivery.py` that rejects: any name containing FAKE_OWNER_TOKENS (retired/professional/bilingual/homeowner/investor/etc), names with >4 words, names without capital start. When rejected, the row stays but `owner_name` is blanked (still callable via listing URL).

3. **Phone repeat-digit threshold matters.** Original 5+ repeated digits regex missed real spam like `786-478-9999` (4 nines) and `786-477-7000` (4 zeros). Tightened to 4+ repeats. Tradeoff: occasional false positive on real phones with 4 same digits in a row. Acceptable.

4. **CL listings without phone are mostly leasing-office posts.** Re-LLM-pass on 268 no-phone rows recovered **1 phone**. Not worth re-running. The original Hermes prompt already targets obfuscated phones. No-phone rows = "apply online" PMS posts, genuinely uncallable.

5. **Manual agent research yields ~5× the lead quality of automated CL scraping.** Tonight's 24 Zumper/Apartments hand-curated rows had 100% phone-attached, 95% owner-direct, several confirmed 4-6 unit owners. Automated CL had ~30% phone rate, mixed owner-direct percentage, mostly 1-2 unit rows. Manual research costs (1) burns Claude subscription quota, (2) doesn't scale weekly without automation, but (3) is the actual moat for premium tier.

## CL sAPI lessons

6. **`item[1]` is seconds OFFSET from `decode.minPostedDate`, NOT a full epoch.** Original epoch parser checked for ms/sec absolute epoch ranges and returned None for the actual offset values (0-700000 range). Freshness filter was a silent no-op for weeks. Fixed by threading `min_posted_date` through `parse_item` and computing `epoch = min_posted_date + item[1]`. Verify any freshness work going forward against a known-stale set.

7. **CL sAPI postal+distance search captures listings from adjacent zips too.** Searching postal=33127 with search_distance=4 pulled listings from 33139 Miami Beach (the Robert Rice case). Don't trust the search postal as a geo signal — must verify zip per-lead in the delivery builder.

## Scraper source lessons

8. **Zumper bot-walls headless scraping but exposes phones in JSON-LD on detail pages.** Built `scripts/zumper_harvest.py` that works on neighborhood-slug pages (`/apartments-for-rent/sunny-isles-beach-fl`). Tested with 16 listings, mostly corporate-branded (Camden/Promenade/Moda/Leksa). Zip-suffix pages (`/zip-XXXXX`) return 200 but listings load via XHR — not scrapable statically. For v1.1 quality, need a non-headless Playwright path OR keep Zumper as manual-research-only source.

9. **Apartments.com is heavily bot-walled.** Tonight's manual session used WebFetch and got 25 verified leads in ~45 min. Automated apartments.com via `scrape_apartments_apify.py` requires Apify credits (Sam was out tonight).

10. **Florida Miami-Dade Property Appraiser API moved domain + changed param format.** Old: `www.miamidade.gov/Apps/PA/PApublicServiceProxy/PaServicesProxy.ashx`. New: `apps.miamidadepa.gov/PApublicServiceProxy/PaServicesProxy.ashx`. Critical fix: **don't pass `myCity`** (triggers 400). Use `params={}` dict with httpx, set `Referer` + `Origin` headers, detect HTML error responses (the proxy returns `text/html` for errors instead of 4xx). Working endpoints documented in `scripts/enrich_pack.py`.

11. **MD-PA only matches ~20% of leads tonight** because most CL listing bodies don't include street addresses (LLM can't extract). When MD-PA does match, the owner-of-record vs listing-contact mismatch is gold ("George Rodriguez · per county: JOSEPH SPEZIALE" surfaces real intel: caller can mention Joseph by name).

## CSS/JS pitfalls (v2 redesign)

12. **Python f-strings convert `\n` and `\b` to real characters.** The v2Polish JS had `let csv = '...\n';` and `match(/<span\b.../)` inside the f-string. Python silently converted to actual newline and backspace, breaking JS syntax. Fix: double-escape `\\n` and `\\b` in source. Verify rendered HTML has the right escape sequence by visual inspection if any breakage suspected.

13. **localStorage on `file://` URLs may be blocked in Safari.** Pack opens fine but status/notes won't persist between page reloads in Safari. Chrome/Firefox/Edge work. For v1.1: consider hosting tracker at a URL (Vercel route) to eliminate this risk.

## Architecture for v1.1

14. **Pack-builder needs to be ONE COMMAND.** Tonight required running:
    - 6 separate `broader_harvest.py` invocations (5 markets + 1 extended)
    - Manual zip-list editing as new market needs surfaced
    - Manual CSV merging
    - `group_by_owner.py` invocation
    - `enrich_pack.py` invocation
    - `build_friday_pack_delivery.py` invocation
    - Manual zip step
    
    For v1.1: `make_friday_pack.py --group miami_metro [--manual <csv>] [--output zip]` should orchestrate all of it. Tomorrow project.

15. **Manual blocklist needs to be reviewable.** It accumulated 10 phones tonight via Sam's manual QA. Future: serialize to a YAML file (`manual_blocklist.yaml`) so corrections aren't lost in code edits.

16. **Score 100 for manual rows is too coarse.** All 24 manual rows tied at 100 → ordering was arbitrary (sometimes Ziprent at top, sometimes Lauder). For v1.1: score manual rows based on (a) n_listings_seen, (b) presence of multi-unit signal in notes field, (c) owner-direct vs PM classification. Manual top-of-pack should be the strongest multi-unit owner-direct rows, not the first alphabetically.

17. **Banned zip list should be markets.yaml-driven, not hardcoded.** Tonight: hardcoded `BANNED_ZIPS_MIAMI` and `ALLOWED_MIAMI_METRO_ZIPS` in `build_friday_pack_delivery.py`. When pack expands to Smokies/PCB/etc, this won't scale. v1.1: pull from a per-market `allowed_zips` / `banned_zips` config block in markets.yaml.
