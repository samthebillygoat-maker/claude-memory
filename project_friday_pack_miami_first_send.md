# Friday Pack — First Real Send (Miami, Tabare Sotomayor)

**Date:** 2026-05-15 ~1:30am PT
**Recipient:** Tabare Sotomayor (`tabaresotomayor@gmail.com`)
**Pack:** Miami Metro, 65 verified landlords
**Delivery:** Gmail draft + `Friday_Pack_Miami_2026-05-15.zip` (22 KB) on Desktop

## Context
- Tabare = 85K IG + ~1,000 paying students in BNB KNOW HOW Whop course at $7,500
- Affiliate deal closed verbally during Zoom 2026-05-14: 30% Weekly+Pro / 12-mo tail / 40% one-offs
- Tonight he's NOT buying — just having someone call the numbers and report results
- Real ask for the affiliate: prove the leads convert
- Coach intel says "judge advice by results" is his catchphrase → tonight's framing

## Pack composition (65 leads)
Markets: Sunny Isles, Aventura, Doral, Wynwood, Hollywood, Hallandale, Lauderdale-by-the-Sea, Brickell, Downtown, Fort Lauderdale.

Top 3 to lead with:
1. **Lauder Management** — 4 units, (754) 354-8386
2. **George Rodriguez** — 6 units Eastern Shores, (786) 267-2291 · per county: Joseph Speziale
3. **Larisa** — 2 units, (305) 975-4132 · per county: Joseph Speziale

Multi-unit stars also in pack: **Tamara Sabbagh** (6 units Lauderdale-by-the-Sea), **Lorraine Llobet** (2 furnished Wynwood units, 5-parcel portfolio per county records).

## Source mix
- 24 manual-curated from Zumper/Apartments.com (score 100, top of pack)
- ~17 Miami main CL harvest
- ~13 Hollywood/Hallandale CL
- ~10 Fort Lauderdale CL
- ~8 Wynwood
- ~2 Downtown Miami (Brickell-area very corporate-heavy)

## Quality bar enforced (11 layers)
1. Phone required + not fake/templated
2. Owner_name OR real address (not just URL) — phone-only callable rows allowed
3. Not in banned zip (33139/33140 Miami Beach, 33125/33130/33133/33134 City of Miami residential, 33161/33154 effective STR bans per zoning audit)
4. Not in out-of-target zip (33175 West Kendall, 33186, 33144, 33162, 33166, 33334 — Wilton Manors 33334 later allowed)
5. Manual phone blocklist (10 numbers: 4 from Sam's earlier review of 49 dropped + 4 templated 786-458-* "easy-approval"/"completely-remodeled" CL spam + 1 NoVA dupe + Ziprent tech-PM 786-313-5471)
6. Fake-phone regex: 4+ repeated digits, 1234, 0000
7. Descriptive-phrase owner_name rejection ("retired bilingual professional" style)
8. Rent floor $1,500 (per `reference_friday_pack_lead_criteria.md`)
9. Vacation/short-term keyword filter
10. 30-day freshness via CL sAPI epoch math (`min_posted_date + item[1]`)
11. Corporate-brand blacklist (40+ brands, brand-anchored not bare words)

## Tracker (v2 dark editorial)
`friday_pack_tracker.html` — dark `#0A0A0A` bg, Fraunces serif headers/owner names, JetBrains Mono numerals, deep-green `#1C3F2E` phone CTA, amber `#E8A33D` "WHY" highlights.

Action buttons: Left VM / Interested / Pitch sent / Follow up / Pass / Reset. Active button highlights amber (is-active class). All 8 filter tabs working: All / With phone / Not called / Left VM / Interested / Pitch sent / Follow up / Pass.

LocalStorage persists status + notes per browser. CSV export has UTF-8 BOM (Excel-safe), preserves real addresses via `dataset.csvAddrs` (not "Link Link Link"), keeps statuses.

Production-verified via Playwright end-to-end test before send.

## Why ship at 65 not 75
- 359 raw landlord candidates total
- 287 dropped through 11-layer quality gate (235 no phone, 33 fake/templated phones, 10 manual blocklist, 7 out-of-target zips)
- 65 is what defensible looks like for STR-friendly Miami metro this week without bending quality
- Frame to coach: "Quality over fake quantity per your 'judge by results' framing"

## Follow-up plan
- **Tuesday morning:** Sam follows up if Tabare hasn't responded
- **If positive feedback:** Send `Miami_STR_Operator_Quickstart.md` as "for your students" + `Tabare_Payout_Projection.md` as dream-planting
- **If negative or quiet:** Hand-pick the 1-2 leads that DID convert, ask what we missed

## Files on Desktop ready for future reference
- `Friday_Pack_Miami_2026-05-15.zip` (the shipped pack)
- `FridayPack_Affiliate_Onepager.pdf`
- `FridayPack_Affiliate_Terms.md` (40%/30%/12-mo tail)
- `Friday_Pack_ROI_Onepager.md` (Tabare's students' break-even math)
- `Miami_STR_Operator_Quickstart.md` (cold call script + voicemail + SMS + lease addendum)
- `Tabare_Promo_Swipe_Kit_v2.md` (his promotion assets for when he agrees to push)
- `coach_intel_tabare.md` (research file — NEVER send)
- `miami_str_zoning_per_zip.md` (zoning audit that drove banned/allowed zips)
- `coach_email_drafts.md` (3 tone variants)
