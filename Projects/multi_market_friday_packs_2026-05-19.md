---
name: Multi-Market Friday Packs — 2026-05-19
description: 4 fresh 50-lead Friday Packs built from HomeHarvest pipeline. Miami (Aventura/SIB/NMB), Fort Lauderdale, Scottsdale AZ, Austin Suburbs TX. Plus partial pulls for Gulf Shores + Gatlinburg vacation markets.
type: project
created: 2026-05-19
---

# Multi-Market Friday Packs — 2026-05-19

## LATEST Outcome (post wave 18, 2026-05-19)

**87 sellable 50-lead Friday Packs delivered** + **23 near-50 packs** across 300 markets attempted in 18 parallel scrape waves. **5,392 total leads in the combined master CSV across 110 sellable markets (40+).** Built via HomeHarvest pipeline (Realtor.com / Redfin / Zillow MLS).

**Pipeline reality-checked 2026-05-19** — caught and fixed: "Top Producer AWS Customer" placeholder, ® trademark = brokerage, 55+ community auto-reject, brokerage-in-owner-name detection. See [[feedback_lead_pack_scoring_fixes_2026-05-19]].

## Earlier Outcome (post wave 8)

**30 sellable 50-lead Friday Packs delivered** + **7 near-50 packs** across 103 markets attempted. **1,812 total leads in the combined master CSV.** Built via HomeHarvest pipeline (Realtor.com / Redfin / Zillow MLS) in 8 parallel scrape waves.

**Master files:**
- Index summary: `data/MASTER_friday_packs_index_2026-05-19.csv` (all 103 markets with counts)
- Combined all-sellable: `data/MASTER_all_friday_packs_combined_2026-05-19.csv` (1,812 leads, grep-friendly)
- Per-market: `data/friday_pack_<slug>_2026-05-19.csv` (one per market)

### 30 FULL 50-Packs (sellable)

**Florida (12):** Miami (Aventura/SIB/NMB), Fort Lauderdale, Naples, Fort Myers, Cape Coral, Boca Raton, Delray Beach, Jacksonville, Ocala, Vero Beach, St Petersburg, Clearwater, Bradenton, Cocoa Beach, St Augustine, Tampa Urban — wait counting: Miami, FtL, Naples, FortMyers, CapeCoral, Boca, Delray, Jax, Ocala, VeroBeach, StPete, Clearwater, Bradenton, CocoaBeach, StAug, TampaUrban = 16 FL packs

**Texas (6):** Austin Suburbs, Dallas, Fort Worth, Frisco/Plano, Houston, San Antonio

**Arizona (3):** Phoenix, Scottsdale, Tempe

**Tennessee (1):** Nashville Suburbs (Brentwood/Franklin)

**Nevada (2):** Henderson, Las Vegas

**Louisiana (1):** New Orleans

**Virginia (1):** Northern Virginia (DC suburbs)

### 7 NEAR-50 packs (40-49 leads)

Galveston TX (48), Charlotte NC (47), Mesa AZ (47), Atlanta North GA (45), Sarasota FL (45), Lakeland FL (40), Long Beach CA (40)

### Markets that didn't yield (use different pipeline next time)

**Vacation/resort with thin long-term MLS:** Gulf Shores AL, Gatlinburg TN, Branson MO, Destin FL, Pensacola FL, Outer Banks NC, Hilton Head SC, Key West FL, Marco Island FL, Cape Cod MA, Sedona AZ, Park City UT

**Midwest/traditional secondary markets — weak STR demand:** Madison WI, Milwaukee WI, Minneapolis MN, Grand Rapids MI, Cleveland OH, Cincinnati OH, Columbus OH, Pittsburgh PA, Boise ID, Salt Lake City UT, Provo UT, Spokane WA, Sacramento CA

**Markets that returned 0:** Boise ID, Asheville NC, Salt Lake City UT (2 only), Sacramento CA (1 only), Provo UT (1), Cape Cod MA (1), Burlington VT (2)

### Pattern observed
- **50/50 STRONG packs** (highest quality, all SFH/duplex named individuals): Austin Suburbs, Cape Coral, Houston, Henderson, Las Vegas, Frisco/Plano, Phoenix
- **AZ state STR pre-emption** = consistently strong yields (Phoenix, Scottsdale, Tempe sellable; Mesa near-50; Tucson partial)
- **TX state STR pre-emption** = excellent yields (all 6 TX markets sellable)
- **FL coastal + suburbs** = excellent yields (16 sellable FL packs)
- **Coastal vacation MICRO-markets** = pipeline mismatch (need VRBO/MLS-for-sale instead)
- **Restrictive states** (CA cities mostly, OR, NY) = thin pools, agent-heavy

| Market | Pack file | Strong | Standard | HOA-screen |
|---|---|---|---|---|
| **Miami (Aventura / SIB / NMB)** | `friday_pack_miami_fl_2026-05-19_DEDUPED.csv` | 15 | 35 | 0 |
| **Fort Lauderdale** | `friday_pack_fort_lauderdale_fl_2026-05-19_DEDUPED.csv` | 26 | 23 | 1 |
| **Scottsdale AZ** | `friday_pack_scottsdale_az_2026-05-19.csv` | 35 | 13 | 2 |
| **Austin Suburbs TX** | `friday_pack_austin_suburbs_tx_2026-05-19.csv` | 50 | 0 | 0 |

## Markets covered

### Miami (Aventura / Sunny Isles Beach / North Bay Village)
- **Zips:** 33160, 33180, 33179, 33181, 33141
- **Raw pull:** 333 unique phones from 948 listings
- **Why these zips:** Per Sam's 2026-05-14 zoning audit — Miami Beach (33139/33140) excluded entirely, 33161 dropped (3-month min + 4-lease/year cap), 33154 Surfside dropped (3-periods/yr cap). Aventura + SIB + NMB explicitly STR-permissive.
- **Dedup:** 49 of 50 new vs the existing 66-lead FINAL_PLUS_MANUAL pack from 2026-05-15; topped to 50 from raw source.

### Fort Lauderdale
- **Zips:** 33301 (downtown), 33304 (Victoria Park), 33305 (East), 33308 (Galt Ocean), 33316 (Las Olas/Harbor Beach)
- **Raw pull:** 167 unique phones from 460 listings
- **Why:** STR-permissive citywide; coastal demand pool, FXE airport workforce. Dedup vs broader_fort_lauderdale_fl_2026-05-14.csv = all 50 new.

### Scottsdale AZ
- **Zips:** 85250, 85251, 85254, 85257, 85258, 85259, 85260
- **Raw pull:** 109 unique phones from 350 listings
- **Why:** AZ state pre-empts most local STR bans; Scottsdale requires only registration. Bookings driven by Phoenix Sky Harbor + winter golf demand.

### Austin Suburbs TX (city-of-Austin EXCLUDED)
- **Zips:** 78613 (Cedar Park), 78664/78665 (Round Rock), 78734 (Lakeway), 78738 (Bee Cave), 78641, 78645
- **Raw pull:** 183 unique phones from 456 listings
- **Why suburbs only:** City-of-Austin has a Type 2 STR lottery + cap that effectively bans non-owner-occupied. The suburbs (Williamson + Travis County unincorporated) allow STR with simple registration. SFH-heavy — pack is 50/50 STRONG signals (mostly single-family homes).
- **DO NOT** scrape Austin city zips (78701-78705) for Friday Pack — wasted leads.

### Gulf Shores AL (partial — 5 leads only)
- **Zips:** 36542, 36547
- **Why low yield:** Vacation market. Most properties are owner-occupied or already-Airbnb. For-rent MLS pool is tiny. Need DIFFERENT scrape strategy: VRBO/Airbnb owner backreferences, MLS for-sale of vacation properties, property management company lists.

### Gatlinburg / Sevierville / Pigeon Forge TN (partial — 3 leads only)
- **Zips:** 37738, 37862, 37863
- **Same issue:** Smokies vacation rental market — long-term rental MLS is sparse. Need different sourcing.

## Pipeline

1. `scripts/multi_market_homeharvest.py` — pulls for_rent past-30/45 days per market zip list, applies corporate brand + self-STR-competitor filters at scrape time
2. `scripts/build_market_packs.py` — scores each row (named individual + SFH/duplex hint + absentee area code + rent in band) → top 50/market → outputs `friday_pack_<market>_<date>.csv`
3. Dedup against existing market files (FINAL packs, prior broader_harvest pulls) → DEDUPED.csv variants

## Lead pack framing (per [[feedback_lead_pack_framing]])

These are **STR-friendly decision-makers**, not "owner-direct skip-traced." Mix of:
- Owner-direct named individuals (highest density in suburbs)
- Listing agents who can route to STR-amenable owners
- Small-portfolio condo owners (HOA-screen on the call)

Customer messaging should say "50 STR-friendly decision-makers in [market]" — not "50 verified owners."

## Honest gaps

- **No Reality Checker pass on these 200 leads** — quality control was heuristic scoring only. Same QC as the prior Miami FINAL_PLUS_MANUAL pack from 2026-05-15. Future iterations could add a Reality Checker spot-check on top 10/market.
- **Vacation markets need a different pipeline.** HomeHarvest's `for_rent` past-30 covers long-term rental MLS — that's near-empty for Gulf Shores / Gatlinburg / Pigeon Forge. Build a separate scraper for VRBO / Airbnb owner backref pull + MLS for-sale on those.
- **Austin city of proper was skipped** per regulatory check. If Sam decides Austin city is OK for 30+day-only operators (similar to Tampa), can scrape 78701-78705 separately and ship as a different pack.

## File locations

- Source scrapes: `data/homeharvest_<market>_2026-05-19.csv`
- Scored packs: `data/friday_pack_<market>_2026-05-19.csv`
- Deduped (Miami + FtL): `data/friday_pack_<market>_2026-05-19_DEDUPED.csv`
- Pipeline scripts: `scripts/multi_market_homeharvest.py`, `scripts/build_market_packs.py`

## Related

- [[feedback_homeharvest_pipeline]] — HomeHarvest = best rental scraper
- [[reference_tampa_hoa_blacklist_2026-05-18]] — auto-FAIL pattern library
- [[reference_corp_blacklist_2026-05-18]]
- [[feedback_lead_pack_framing]]
- [[project_new_markets_2026]] — prior market research (Austin previously eliminated for nightly STR; this revival is for 30+day suburbs only)
