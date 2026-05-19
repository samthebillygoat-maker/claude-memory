---
name: Tampa New Scrape — 2026-05-18
description: Fresh Bayshore/Hyde Park lead scrape for Tampa trip starting 2026-05-19. Verified 3 new leads via Reality Checker. 1 blacklist addition (RangeWater).
type: project
created: 2026-05-18
trip: Tampa 2026-05-19 to 2026-05-25
---

# Tampa New Scrape — 2026-05-18

## Outcome (FINAL, top of file)

**28 verified callable Monday leads** after 3 rounds of HomeHarvest + Zumper + Craigslist + Apartments.com pipelines and 3 Reality Checker audit passes.

- **9 Tier 1 PASS** (owner-direct SFH/duplex, no HOA)
- **12 Tier 2/3 NEEDS-CALL** (agent gatekeeper or HOA-screen)
- **6 existing-plan leads** (TEJ, BC Tampa, Casablanca, Roy's, Dave Winter, Hyde Park Apts Inc)
- **1 late Zumper addition** (4211 W North A St — same street as Dale Hunter PASS)

**Reality Checker double-pass:** caught 14+ fantasy traps — Bayshore Royal high-rise HAS an explicit HOA STR ban, San Carlos Place is condo-titled, Schooner Cove is HOA-controlled, Camden Preserve slipped past Zumper's corp filter, etc. **See [[reference_tampa_hoa_blacklist_2026-05-18]] for the full pattern set.**

**See [[tampa_avm_201_columbia_dealsheet_2026-05-18]] for per-lead deep-dive on AVM Properties #5 (the partnership / Maid for You play).**

**MASTER CSV (single source of truth):** `data/tampa_MASTER_call_sheet_2026-05-18.csv`
**PDF (Desktop, phone-readable):** `Desktop/Tampa_Trip_2026-05-19.pdf`

### Call Monday in this order

| # | Verdict | Phone | Owner / Building | Address | Rent | Why |
|---|---|---|---|---|---|---|
| 1 | PASS | (305) 510-9619 | Teresa Williams (Miami absentee) | 3819 W Gray St, 33609 | $2,300 | SFH bungalow, no HOA, out-of-state owner = dream STR target. **TOP** |
| 2 | PASS | (813) 831-7368 | David Lowrey | 306 Danube Ave Apt 2, 33606 | $1,375 | Davis Islands, walking to TGH, dirt cheap. Same street as 211 Danube — walk both same afternoon |
| 3 | PASS | (845) 709-9245 | Claudia Amanuel (NY absentee) | 2002 S Habana Ave Apt C, 33629 | $2,500 | Quadplex 1948, no HOA, out-of-state owner |
| 4 | PASS | (813) 568-8020 | Palm Communities | 211 Danube Ave + 104 S Armenia (one call, 2 bldgs) | $1,650 | 12-unit boutique owner-direct |
| 5 | PASS | (813) 244-4056 | AVM Properties (Monica McLaughlin) | 201 Columbia Dr, 33606 | $2,550 | 3-unit furnished, **owner ALSO runs Maid for You cleaning co — partnership pitch** (see deal sheet) |
| 6 | NEEDS-CALL | (813) 336-3350 | Sam Chandler (Smith & Assoc agent) | 3818 W Euclid Ave, 33629 | $2,850 | SFH 1947 no HOA, but agent gatekeeper |
| 7 | NEEDS-CALL | (407) 279-0038 | Alyssa McIntyre (Orlando absentee) | 305 S Westland Ave Unit B, 33606 | $2,000 | Small 1923 condo, HOA-screen on call first |
| 8 | NEEDS-CALL | (813) 887-0747 | MaryAnn Hoffman | 603 S Melville Ave Apt 1, 33606 | $2,500 | Hamilton Place Condos — HOA-screen first |
| 9 | NEEDS-CALL | (727) 910-5081 | TLR Group | 511 S Westland Ave #16, 33606 | $1,650 | Ask for asset mgr, not on-site |

**Dropped (do NOT call):**
- **2109 Bayshore Blvd Unit 606** — Bayshore Royal 1924 high-rise condo with **explicit HOA STR ban**. Absentee-owner-trap caught by Reality Checker.
- **2117 W Dekle Ave** — Melrose Landing historic condo + listing-agent gatekeeper (double-no)
- **510 N Rome Ave / The Gray** — RangeWater (100k-unit institutional). Blacklisted.

## STR Legal Check (passed before scraping)

- Florida vacation rental statute kicks in at **<30-day stays >3x/yr**
- Sam's actual model = 30-day min + 12-mo lease → falls *outside* vacation rental regulation entirely
- Tampa residential zoning has a 7-night minimum (irrelevant; cleared 4x)
- No city-level STR registration program; no annual day cap
- Avoid: HOA-governed condos/townhomes (separate building-level restrictions)
- **Verdict: GO for Sam's 30+ day corporate housing in residential apartments**

## What I scraped

Tightened scope per Sam ("stick to bayshore hyde park area") to **33606 / 33609 / 33629 only**.

| Source | Script | Output | Yield |
|---|---|---|---|
| Craigslist (broader sweep) | `broader_harvest.py --market tampa_fl --limit 250` | `data/broader_tampa_fl_2026-05-18.csv` | 46 candidates, 7 phones, 0 in target |
| Zumper city-wide | `zumper_harvest.py --market tampa_fl --limit 150` | `data/zumper_tampa_fl_2026-05-18_citywide.csv` | 56 candidates, 44 phones, ~3 in target |
| Zumper neighborhood-targeted | `zumper_harvest.py --market tampa_fl --limit 300` (after adding `zumper_neighborhoods`) | `data/zumper_tampa_fl_2026-05-18.csv` | 34 candidates, 25 phones, ~5 in target |
| **HomeHarvest (Realtor.com + Redfin + Zillow MLS)** | `tampa_homeharvest_rentals.py` (new) | `data/homeharvest_tampa_fl_2026-05-18.csv` | **100 listings, 83 phones, 16 in target after corp filter** — *the killer source* |
| Apartments.com (scrapling) | `tampa_apartments_com_harvest.py` (new) | partial — search pages 200 OK, detail pages 403 | Search-card data only; phones blocked on detail |
| Zillow direct WebFetch | — | — | **403 blocked** |
| Realtor.com direct WebFetch | — | — | **whitelisted-blocked** |
| HotPads direct WebFetch | — | — | **403 blocked** |

LLM cost: $0.21 (Hermes 4 405B for Craigslist extraction). HomeHarvest = free (uses official-ish endpoints).

**Killer pipeline upgrade:** `homeharvest` (PyPI v0.8.18 / `ZacharyHampton/HomeHarvest`) supports `listing_type="for_rent"` with ZIP targeting and returns `agent_phone`, `agent_name`, `agent_email`, `office_phones`, `broker_name`. Pulls Realtor.com / Redfin / Zillow MLS data without bot-protection trouble. This is now Sam's best fresh-rental source.

## What I changed

1. **`markets.yaml` — added `zumper_neighborhoods` for tampa_fl** — 10 neighborhood slugs (hyde-park, bayshore-gardens, soho, palma-ceia, davis-islands, courier-city-oscawana, north-hyde-park, parkland-estates, beach-park, sunset-park). City-wide Zumper search is corporate-heavy; neighborhood pages bypass that.
2. **Corporate blacklist additions** (`markets.yaml`):
   - mosaic westshore (slipped through; corporate)
   - rpm living
   - adagio at westshore
   - niche luxury
   - **rangewater / rangewater residential** (managed The Gray Tampa)
   - **richland communities** (institutional owner of The Gray)
3. **`scripts/tampa_dedup_and_filter.py`** — new file:
   - Loads phone universe from all existing TAMPA*.csv + tampa_*.csv + broader_tampa_*.csv
   - Filters to 33606/33609/33629 OR Bayshore/Hyde Park regex match
   - Rejects fake phones (INT_MAX = 2147483646 surfaced today from a corrupted JSON-LD)
   - Extra corporate regex catches names not yet in markets.yaml
4. **Hard-coded phone fake-list** — `PHONE_FAKE = {"2147483646", ...}` — Niche Luxury Apts had INT_MAX as its phone in the JSON-LD; never call.

## Gotchas this run

- **Niche Luxury Apartments** had phone `2147483646` = `INT_MAX` = corrupted JSON-LD numeric overflow. The Zumper harvest's `telephone` field accepts integers, and this site published it as a poisoned value. Added to PHONE_FAKE set.
- **`zumper_neighborhoods` was missing** from tampa_fl config — city-wide search dumps you into Camden/Greystar territory. After adding 10 neighborhood slugs the in-target ratio jumped from 5% to ~25%.
- **Same phone, 2 buildings**: 813-568-8020 appears on both 211 Danube Ave and 104 S Armenia listings — Palm Communities portfolio. Dedup keeps the first; the second is the same owner reachable on the same call.
- **TLR Group**: not on the blacklist but functionally mid-size local PM with 90-unit buildings. Marked NEEDS-CALL not auto-FAIL — there's a path to a corporate housing addendum if you reach the asset manager, but on-site leasing agents won't help.

## Files

- **Final CSV:** `C:\Users\samth\projects\landlord-outreach\data\tampa_new_leads_2026-05-18_FINAL.csv` (4 rows, verdict column)
- Raw dedup: `data/tampa_new_leads_2026-05-18.csv` (4 rows pre-Reality-Checker)
- Source scrapes: `data/broader_tampa_fl_2026-05-18.csv`, `data/zumper_tampa_fl_2026-05-18.csv`, `data/zumper_tampa_fl_2026-05-18_citywide.csv`
- Updated config: `markets.yaml` (zumper_neighborhoods + corporate_blacklist additions)
- Dedup/filter script: `scripts/tampa_dedup_and_filter.py`

## Monday call order (combined with existing trip plan)

From this scrape (new):
1. **(813) 568-8020 — Palm Communities** — ask about 211 Danube AND 104 S Armenia in one call
2. **(813) 244-4056 — AVM Properties** — 201 Columbia Dr, furnished 2BR — lean into "take over your furnished setup" framing
3. **(727) 910-5081 — TLR Group** — 511 S Westland — ask for asset manager, NOT on-site

From `tampa_trip_handoff_2026-05-19.md` (already planned):
4. BC Tampa / WRH — bctampamgr@wrhrealty.com (email already drafted)
5. TEJ / Tara — 813-440-8618 (already signing)
6. Backup list — Casablanca, Innovo (Innovo is now blacklisted — drop), Roy's, Dave Winter, Hyde Park Apts Inc

## Honest gaps

- **Zillow FRBO is fully 403-blocked** to WebFetch — couldn't tap that pool
- **Apartments.com** same — blocked
- Net yield 3 actionable from one scrape pass; this market is owner-direct-thin at this price band on any given day
- Did NOT search Tampa Bay condo HOAs for STR-permissive buildings — that's a Google Lens / AirDNA workflow, not a CL/Zumper scrape
- Friend-Seminole lead is in `tampa_trip_handoff_2026-05-19.md`; not addressed here

## Related

- [[tampa_trip_handoff_2026-05-19]] — main trip plan
- [[tampa_negotiation_pregame_2026-05-19]] — Ackerman ladders (apply same method to these 3 new leads)
- [[tampa_showing_checklist_2026-05-19]] — on-site walkthrough
- [[tampa_backup_call_list_2026-05-19]] — phone scripts (corporate housing framing)
- [[project_tampa_south_scout_2026-05-14]] — previous Tampa lead build
- [[reference_str_deal_criteria]] — Double Rent Rule, regulations checklist
- [[reference_friday_pack_lead_criteria]] — $950+, owner-direct, no condos/townhomes
