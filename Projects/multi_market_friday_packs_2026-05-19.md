# Multi-Market Friday Pack Pipeline — 2026-05-19 Final State

## Pipeline Overview
- **Script**: `C:\Users\samth\projects\landlord-outreach\scripts\multi_market_homeharvest.py` (scraper)
- **Script**: `C:\Users\samth\projects\landlord-outreach\scripts\build_market_packs.py` (pack builder)
- **Output**: `C:\Users\samth\projects\landlord-outreach\data\`
- **Format**: `homeharvest_{slug}_{date}.csv` → `friday_pack_{slug}_{date}.csv`
- **Python**: `.\.venv\Scripts\python.exe` (must use venv)

## Waves Completed Through Tonight (Waves 43–45)

### Wave 43
| Market | Phones | Pack | STRONG |
|--------|--------|------|--------|
| north_bergen_nj | 40 | 40 | 6 |
| west_new_york_nj | 38 | 38 | 0 |
| hoboken_nj | 31 | 31 | 4 |
| chelsea_ma | 28 | 28 | 2 |
| easton_pa | 24 | 24 | 5 |
| wilkes_barre_pa | 20 | 20 | 5 |
| conway_sc | 8 | 8 | 2 |
| secaucus_nj | 13 | 13 | 0 |
| Dead (0 phones) | roanoke_rapids_nc, tifton_ga, cordele_ga, sparta_tn, brownsville_tn, morgan_city_la, ponca_city_ok, hutchinson_ks, ottumwa_ia, palestine_tx |

### Wave 44
| Market | Phones | Pack | STRONG |
|--------|--------|------|--------|
| kissimmee_fl | 128 | 50 | 37 |
| cambridge_ma | 111 | 50 | 9 |
| brookline_ma | 83 | 50 | 6 |
| watertown_ma | 41 | 41 | 12 |
| asbury_park_nj | 35 | 35 | 8 |
| arlington_ma | 30 | 30 | 7 |
| white_plains_ny | 25 | 25 | 4 |
| montclair_nj | 22 | 22 | 1 |
| belmont_ma | 20 | 20 | 4 |
| belleville_nj | 20 | 20 | 1 |
| new_rochelle_ny | 17 | 17 | 0 |
| torrington_ct | 16 | 16 | 2 |
| harrison_nj | 15 | 15 | 0 |
| portsmouth_va | 14 | 14 | 1 |
| nutley_nj | 14 | 14 | 2 |
| maplewood_nj | 12 | 12 | 0 |
| bristol_ct | 15 | 15 | 0 |
| mount_vernon_ny | 11 | 11 | 1 |
| manchester_ct | 6 | 6 | 0 |
| rahway_nj | 5 | 5 | 0 |
| east_hartford_ct | 4 | 4 | 0 |
| Dead | port_huron_mi, mount_pleasant_mi, lewiston_me, auburn_me |

### Wave 45
| Market | Phones | Pack | STRONG |
|--------|--------|------|--------|
| baltimore_md | 77 | 50 | 8 |
| norwalk_ct | 35 | 35 | 8 |
| stratford_ct | 24 | 24 | 2 |
| towson_md | 18 | 18 | 1 |
| pawtucket_ri | 16 | 16 | 0 |
| red_bank_nj | 16 | 16 | 2 |
| neptune_nj | 12 | 12 | 4 |
| cranston_ri | 10 | 10 | 2 |
| edison_nj | 11 | 11 | 2 |
| freehold_nj | 11 | 11 | 1 |
| piscataway_nj | 9 | 9 | 1 |
| east_haven_ct | 8 | 8 | 1 |
| port_chester_ny | 8 | 8 | 0 |
| hempstead_ny | 5 | 5 | 0 |
| enfield_ct | 5 | 5 | 1 |
| sayreville_nj | 4 | 4 | 1 |
| woonsocket_ri | 4 | 4 | 1 |
| freeport_ny | 4 | 4 | 1 |
| southington_ct | 3 | 3 | 0 |
| bay_shore_ny | 3 | 3 | 0 |
| central_islip_ny | 3 | 3 | 1 |
| ossining_ny | 3 | 3 | 1 |
| patchogue_ny | 3 | 3 | 0 |
| peekskill_ny | 2 | 2 | 1 |
| lakewood_nj | 6 | 6 | 1 |
| brentwood_ny | 1 | 1 | 0 |
| Dead | altoona_pa, johnstown_pa |

## Wave 46 — Next Up
High-yield targets to add to both scripts:
- **Baltimore suburbs**: dundalk_md (21222), essex_md (21221), catonsville_md (21228), parkville_md (21234) — area code 410/443
- **RI**: east_providence_ri (02914), north_providence_ri (02904), johnston_ri (02919) — area code 401
- **NJ Union/Middlesex**: union_nj (07083), hillside_nj (07205), metuchen_nj (08840), carteret_nj (07008) — area code 908/732
- **Long Island**: amityville_ny (11701), copiague_ny (11726), medford_ny (11763), ronkonkoma_ny (11779) — area code 631
- **CT**: derby_ct (06418), seymour_ct (06483), putnam_ct (06260) — area code 203/475
- **MA North Shore**: winthrop_ma (02152), swampscott_ma (01907), gloucester_ma (01930) — area code 339/617/978
- **PA**: lebanon_pa (17042), hazleton_pa (18201) — area code 717/570

## Market Yield Patterns
- **Best**: NJ Hudson/Essex/Bergen/Passaic/Monmouth, MA inner Boston ring, FL Orlando/Kissimmee, MD Baltimore
- **Good**: CT Fairfield/Hartford/New Haven, RI Providence metro, NY Westchester/Long Island
- **Dead**: Rural Midwest, rural Appalachian TN/VA/WV, rural South

## How to Resume
```powershell
cd "C:\Users\samth\projects\landlord-outreach"
# Scrape one market
.\.venv\Scripts\python.exe scripts/multi_market_homeharvest.py --market {slug}
# Build pack
.\.venv\Scripts\python.exe scripts/build_market_packs.py --market {slug}
# Batch loop
$markets = @("m1","m2"); foreach ($m in $markets) { .\.venv\Scripts\python.exe scripts/multi_market_homeharvest.py --market $m }
```
