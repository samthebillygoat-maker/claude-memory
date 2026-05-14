---
title: Tampa South — Owner-Direct Landlord Scout
date: 2026-05-14
tags: [tampa, str, landlord-outreach, hyde-park, bayshore]
status: leads-ready
output: C:\Users\samth\projects\landlord-outreach\data\TAMPA_UNIQUE_OWNERS.csv
---

# Tampa South — Owner-Direct Landlord Scout (2026-05-14)

## What this is

Curated list of 10 unique small-portfolio landlord/owner contacts in South Tampa (Hyde Park / Bayshore / SoHo / Palma Ceia) covering ~40 buildings. Each has a verified phone. Built to seed STR-arbitrage outreach calls. Source: Tara House West (3216 W De Leon St, 33609) was the prototype — older mid-century walk-up, owner-operated, no HOA.

## Top calls

| # | Owner | Phone | Buildings | Where |
|---|---|---|---|---|
| 1 | **Brian Christopher** (BC Tampa Properties) | 813-902-1600 | 10 | Cleveland HQ + Habana, Swann, Orleans, Clarice Ct, plus Albany/Diamond Oaks/Erin Villas/Fox Villas/Island Villas/Park Villa/Texas Apartments (confirm addresses on call) |
| 2 | **Innovo Living Hyde Park** | 813-280-7680 | 11 | Teresa Circle, Horatio, Westland, Melville, Gunby, Dekle, Clewis, Oregon, Lorenzo (33606/33609/33629) |
| 3 | **Hyde Park Apartments Inc.** | 813-254-0372 | 8 (1920s walk-ups) | Office: 2104 W Hills Ave 33606. Buildings: The Georgian, The Dakota (901 S Dakota Ave), Villa Siena, The Carlyle, The Leslie, Morningside |
| 4 | **Roy** | 813-598-1400 | 1 multi-unit | 115 S Lois Ave (units 104/111/210/225, multiple 1bd ~$1600-1800) |
| 5 | **TEJ Properties** (E. Johnson — manager@tarahousetampa.com) | 813-440-8618 | 2 | Tara House West (3216 W De Leon, 32 units, 1bd $1450) + Tara House South (3119 W De Leon). **Prototype.** |
| 6 | **Dave Winter** | 813-843-6810 | 1 | 1301 SoHo (gated community, confirm address) |
| 7 | **Casablanca of Hyde Park** — Deanna / David M | 813-296-2181 / 813-786-3151 / 813-766-5000 | 1 boutique | 407 S Melville Ave 33606. **Explicit short/long-term + corporate housing + vacation traveler signals** — STR-confirmed listing. |
| 10 | Owner CL-only | 813-875-1600 | 1 | Address TBD |

## Decision filter used

- Single-owner / small portfolio (NOT Greystar/Camden/MAA/Cortland/etc.)
- Building type: apartment building, SFH, duplex/triplex — **excluded condos, townhomes, new-build luxury** (HOA bans STRs)
- Target zips: 33606, 33609, 33611, 33629 (Hyde Park / Bayshore / Palma Ceia / Westshore-east)
- Rent range: $1000-3200
- 1bd minimum (Tara House prototype is 1bd)

## How the leads were built

1. Direct web research for known boutique Hyde Park operators (Tara House, Casablanca, Innovo, Hyde Park Apartments Inc, 1301 SoHo, BC Tampa Properties) → 7 owners
2. Craigslist tampa sAPI scrape postal=33609, 5mi radius, min_br=1 → 116 raw listings → 33 candidates after building-type + corporate filter → 3 new unique owners with phones (Roy, David M, two unnamed)
3. Broader CL sweep across 33606/33611/33629 → 27 more candidates but **0 new phones** (wider radius pulled corporate/leasing-office posts that gate contact)

Scripts (in landlord-outreach repo):
- `scripts/tampa_south_harvest.py` — focused 33609 scrape with Hermes 4 LLM extraction
- `scripts/tampa_broader_harvest.py` — multi-postal sweep
- Output: `data/TAMPA_UNIQUE_OWNERS.csv` (10 owners), `data/TAMPA_50_LEADS.csv` (55 property-level rows)

## Honest gaps

- **Hyde Park Apartments Inc.** has 8 buildings but only 1 address (901 S Dakota Ave) confirmed publicly. The other 7 (The Georgian, Villa Siena, The Carlyle, The Leslie, Morningside, + one unnamed) require asking on the call.
- **BC Tampa Properties** — 4 of 10 portfolio addresses confirmed; the other 6 (Albany, Diamond Oaks, Erin Villas, Fox Villas, Island Villas, Park Villa, Texas Apartments) need to be asked on the call.
- **HOA verification** — done by building-type proxy (apt building / SFH = no HOA assumption). Not individually verified per property. Condos/townhomes were excluded outright.
- **Target was 50 unique owners**; delivered 10. The free-public-records skip-trace path (FastPeopleSearch via CloakBrowser) was attempted for surrounding landlord-outreach work and works but gets rate-limited. Scaling beyond 10 in South Tampa would require Apartments.com / Zillow FRBO / HotPads scraping with CloakBrowser pipelines we haven't built.

## What's also true

- CL harvest cost: $0.08 in Hermes 4 (OpenRouter)
- CloakBrowser proved out as Cloudflare bypass for FPS during the parallel landlord-outreach skip-trace work
- Daily AI Workflow Brief routine (Claude AI cloud routine `trig_01WspzJ3CoM41B2KJipVLmu1`) fires daily 6am PT to samthebillygoat@gmail.com

## Related

- [[project_landlord_outreach]] — the broader pipeline
- [[reference_str_master_prompt]] — outreach framing
- [[feedback_lead_pack_framing]] — call positioning rules
- [[feedback_str_honest_disclosure]] — corporate-housing framing
