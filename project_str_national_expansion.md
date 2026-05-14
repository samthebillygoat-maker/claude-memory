---
name: STR National Expansion — Markets & Research
description: National STR arbitrage market research, 70-market scraper config, top 25 rankings, high-demand/low-supply gems
type: project
date: 2026-04-22
---

## What Changed Today

The DealScout tool was fully expanded from Florida-only to **national** (70 markets across 20+ states).

### Files Updated
- `data/scraper.py` — MARKET dict expanded to 70 cities; zip regex fixed to `\d{5}` (any US zip); `state` field added to all entries and lead output; save path → `national_leads.json`
- `pages/11_🗺️_National_Leads.py` — renamed from Florida_Leads; all FL hardcodes removed; URL builders (gmaps, ff, airdna, skip trace) now use `lead.get('state')`
- `data/scraper.py` MARKET — Las Vegas and Honolulu REMOVED (regulatory collapse 2025)

---

## Dead Markets (Do Not Target)

| Market | Reason |
|--------|--------|
| **Las Vegas, NV** | Clark County eliminated 99% of STRs Sept 1, 2025 |
| **Honolulu, HI** | 90-day minimum rental law Sept 30, 2025 kills short-term model |
| **NYC** | 30-day minimum, illegal arbitrage |
| **San Francisco** | Owner-occupied only |
| **Boston** | Primary residence required |
| **Myrtle Beach, SC** | 16,000+ listings, tourism down 10.8% in 2025 |

---

## Top 25 Arbitrage Markets (Ranked by Revenue/Rent Ratio)

| # | City | State | ADR | Occ | Rev/mo | Max Rent | Ratio | Trend |
|---|------|-------|-----|-----|--------|----------|-------|-------|
| 1 | Jackson | WY | $880 | 55% | $14,520 | $1,200 | **12.1x** | ↑ |
| 2 | Blue Ridge | GA | $284 | 54% | $4,600 | $700 | **6.6x** | ↑↑ |
| 3 | Tuscaloosa | AL | $310 | 45% | $4,185 | $700 | **6.0x** | ↑ football |
| 4 | St. Augustine | FL | $315 | 64% | $6,048 | $1,100 | **5.5x** | ↑ |
| 5 | Pigeon Forge | TN | $260 | 56% | $4,368 | $800 | **5.5x** | → |
| 6 | McMinnville | OR | $327 | 55% | $5,395 | $1,000 | **5.4x** | ↑ wine |
| 7 | Red River Gorge | KY | $214 | 56% | $3,659 | $700 | **5.2x** | ↑ climbing |
| 8 | Stowe | VT | $420 | 48% | $6,048 | $1,200 | **5.0x** | → ski |
| 9 | Estes Park | CO | $396 | 46% | $5,464 | $1,100 | **5.0x** | → NP |
| 10 | Waco | TX | $231 | 57% | $3,950 | $800 | **4.9x** | ↑ |
| 11 | Tucson | AZ | $235 | 63% | $4,441 | $900 | **4.9x** | → snowbird |
| 12 | Telluride | CO | $520 | 42% | $6,552 | $1,400 | **4.7x** | ↑ supply cap |
| 13 | Moab | UT | $326 | 47% | $4,596 | $1,000 | **4.6x** | ↑↑ |
| 14 | Bar Harbor | ME | $310 | 44% | $4,092 | $900 | **4.6x** | ↑ Acadia |
| 15 | Key West | FL | $420 | 68% | $8,568 | $2,000 | **4.3x** | → premium |
| 16 | Vail | CO | $480 | 46% | $6,624 | $1,600 | **4.1x** | → ski |
| 17 | Flagstaff | AZ | $292 | 52% | $4,555 | $1,100 | **4.1x** | ↑ demand > supply |
| 18 | Branson | MO | $190 | 50% | $2,850 | $700 | **4.1x** | → family |
| 19 | Gatlinburg | TN | $290 | 70% | $6,090 | $1,500 | **4.1x** | → highest TN occ |
| 20 | Missoula | MT | $172 | 57% | $2,992 | $800 | **3.7x** | ↑ only 281 listings |
| 21 | Santa Fe | NM | $310 | 48% | $4,464 | $1,200 | **3.7x** | → hard cap 1,000 permits |
| 22 | Columbus | GA | $140 | 62% | $2,604 | $700 | **3.7x** | ↑↑ military |
| 23 | Eureka Springs | AR | $204 | 42% | $2,570 | $700 | **3.7x** | ↑ hidden gem |
| 24 | Memphis | TN | $163 | 51% | $2,493 | $700 | **3.6x** | ↑↑ window open |
| 25 | Bozeman | MT | $304 | 49% | $4,468 | $1,300 | **3.4x** | ↑ Yellowstone |

---

## High Demand / Low Supply Markets

Markets with constrained supply but strong fill rates — best arbitrage entry points:

| City | State | Active Listings | Occ | Why Constrained |
|------|-------|----------------|-----|-----------------|
| Jackson | WY | ~400 | 55% | Geographic isolation, limited housing |
| Missoula | MT | **281** | 58% | Tiny city, low awareness |
| Red River Gorge | KY | **695** | 57% | Rural, national park, few hosts |
| Tuscaloosa | AL | **366** | avg 45% / **70%+ gamedays** | College town, nobody doing arbitrage |
| Columbus | GA | ~200 | 62% | Military town, PCS demand, no STRs |
| Waco | TX | ~400 | 57% | Magnolia Market demand, supply lagging |
| Telluride | CO | **598** | 42% | Just voted to CAP new permits |
| Santa Fe | NM | hard capped at 1,000 | 48% | Permit hard cap = artificial scarcity |
| McMinnville | OR | ~500 | 55% | Wine country, less saturated than Napa |
| Fort Collins | CO | 521 | 49% | CSU college town, ADR rising despite supply growth |

---

## Columbus, GA Deep Dive

**Why:** Fort Moore (US Army) drives extended-stay demand — PCS rotations, TDY, family visits. ~200 active Airbnb listings for entire city.

**STR model:** $140/nt ADR × 62% occ = **$2,604/mo revenue**

### 15 Live Listings Found (April 22, 2026)

| # | Property | Rent | Net/mo | Ratio | Address | Link |
|---|----------|------|--------|-------|---------|------|
| 1 | 3BR/1BA Spacious Home | $550 | **$2,054** | 4.7x | 1708 28th Ave | https://columbusga.craigslist.org/apa/d/phenix-city-spacious-home-and-move-in/7928244744.html |
| 2 | 2BR/1BA Apartment | $600 | **$2,004** | 4.3x | Near Lumpkin Rd | https://columbusga.craigslist.org/apa/d/columbus-ready-to-be-rented-bedroom/7925631165.html |
| 3 | 3BR/1BA Country Home | $700 | **$1,904** | 3.7x | 1708 28th Ave | https://columbusga.craigslist.org/apa/d/phenix-city-bedroom-country-home/7928242356.html |
| 4 | 1BR/1BA No Deposit | $729 | $1,875 | 3.6x | Near Uptown CSU | https://columbusga.craigslist.org/apa/d/columbus-no-deposit1-bed-bath-apartment/7923936248.html |
| 5 | 3BR/2BA Lumpkin Park | $878 | $1,726 | 3.0x | 3351 N Lumpkin Rd | https://columbusga.craigslist.org/apa/d/columbus-managers-special-first-month/7928378224.html |
| 6 | 3BR/1BA Charming Home | $899 | $1,705 | 2.9x | North Columbus | https://columbusga.craigslist.org/apa/d/columbus-charming-home-with-modern/7923873151.html |
| 7 | 2BR/1BA Uptown/CSU | $979 | $1,625 | 2.7x | Near CSU | https://columbusga.craigslist.org/apa/d/columbus-uptown-apartment-walking/7929023896.html |
| 8 | 3BR/2BA Lumpkin Park | $1,000 | $1,604 | 2.6x | 3351 N Lumpkin Rd | https://columbusga.craigslist.org/apa/d/columbus-managers-special-first-month/7929179121.html |
| 9 | 2BR/1BA Near CSU | $1,057 | $1,547 | 2.5x | CSU area | https://columbusga.craigslist.org/apa/d/columbus-move-in-special-spacious/7929249668.html |
| 10 | 2BR/2BA Phenix City | $1,095 | $1,509 | 2.4x | Phenix City, AL | https://columbusga.craigslist.org/apa/d/phenix-city-house-for-rent-in-phenix/7921559264.html |
| 11 | 2BR/1BA Brick Beauty | $1,150 | $1,454 | 2.3x | 3822 Howard Ave | https://columbusga.craigslist.org/apa/d/columbus-1-brick-beauty/7929018302.html |
| 12 | 3BR/1BA + Bonus Room | $1,159 | $1,445 | 2.3x | East Columbus | https://columbusga.craigslist.org/apa/d/columbus-1-home-with-bonus-room/7929169964.html |
| 13 | 3BR/2BA 901 Joy Rd | $1,199 | $1,405 | 2.2x | 901 Joy Rd | https://columbusga.craigslist.org/apa/d/columbus-bed-bath-1199-mo-security/7929322492.html |
| 14 | 3BR/2BA Lumpkin Park | $1,000 | $1,604 | 2.6x | 3351 N Lumpkin Rd | https://columbusga.craigslist.org/apa/d/columbus-managers-special-first-month/7928301098.html |
| 15 | 3BR/1BA + Bonus Room | $1,159 | $1,445 | 2.3x | East Columbus | https://columbusga.craigslist.org/apa/d/columbus-1-home-with-bonus-room/7925356568.html |

**Note:** Phone numbers on CL require logged-in session — click listing → click "reply" to get contact info.

### Columbus GA Outreach Script
> "Hi, I saw your rental on Craigslist. I run a furnished rental business that serves military families and contractors at Fort Moore — PCS moves, TDY stays, that kind of thing. I'd love to discuss a longer-term lease with sublease rights built in. I'll pay on time every month, take excellent care of the property, and can sign a 12-month lease. Would you be open to talking?"

---

## Regulation Notes (2026)

| Market | Status | Notes |
|--------|--------|-------|
| Tennessee (all cities) | ✅ Friendly | No statewide ban; local zoning; permits $500-1000/yr |
| Florida (most) | ✅ Friendly | State preemption law; some cities capped |
| Arizona | ✅ Friendly | State preemption; permit $150-250/yr |
| Utah | ✅ Friendly | Minimal state regs; Moab favorable |
| Georgia | ✅ Friendly | $150/yr permit Savannah; Columbus very open |
| Colorado | ⚠️ Moderate | Permits required; Telluride just capped |
| Texas | ⚠️ Moderate | Austin: 1,000ft spacing rule Oct 2025; licensed July 2026 |
| Austin TX | ⚠️ Caution | Supply cap 7,500 permits; new licensing July 1, 2026 |
| California | ❌ Restrictive | SD lottery; Palm Springs best option ($100/yr, no residency req) |
| Las Vegas | ❌ Dead | 99% of STRs eliminated Sept 2025 |
| Honolulu | ❌ Dead | 90-day minimum Sept 2025 |

---

## Key Insight: Military Town Strategy

Columbus, GA proved the model: Fort Moore drives **extended-stay demand** (30-90 nights) that almost no STR hosts are serving. Same logic applies to:
- **San Antonio, TX** — Lackland AFB, Fort Sam Houston
- **Fayetteville, NC** — Fort Liberty (formerly Bragg)
- **Killeen, TX** — Fort Cavazos (formerly Hood)
- **Clarksville, TN** — Fort Campbell
- **Junction City, KS** — Fort Riley

All have 62%+ occupancy potential, rents under $900, and almost zero STR competition.
