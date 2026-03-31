---
name: Miami Arbitrage Tool — Technical Details
description: Architecture and feature details of the Miami Airbnb arbitrage Streamlit app
type: project
---

**Location:** `C:\Users\samth\miami-arbitrage\`

**Stack:** Python + Streamlit + Plotly + Pandas

**9 pages:**
1. `🏠 Property Analyzer` — combined property + furnishing calculator, full 12-month P&L, 3-scenario analysis, charts, save property
2. `🗺️ Neighborhood Guide` — compare all Miami neighborhoods, revenue heatmap, radar chart, search links
3. `🛋️ Furnishing Calculator` — standalone itemized furnishing (also embedded in Property Analyzer)
4. `📋 Saved Properties` — track properties with full contact info, status, click-to-expand detail view, comparison chart
5. `⚖️ Legal & Compliance` — STR rules by Miami jurisdiction, landlord questions, lease clause checklist
6. `✅ Checklist` — April 15 countdown, 3-phase task tracker, negotiation email/phone/text scripts
7. `📬 Outreach Manager` — paste listing text → auto-parse contact info → generate custom outreach email → send via SMTP or mailto → track responses with alerts
8. `🔍 Address Analyzer` — paste any Miami address → geocode → neighborhood detect → 2x rent analysis, AirDNA market data, regulation cross-check, sq ft/beds/baths ADR adjustment, real comps from Inside Airbnb, scenario + sensitivity analysis
9. `🏘️ Listing Scout` — connects to RentCast API (50 calls/month tracked) → auto-searches Miami rentals → runs every listing through 2x analyzer → ranks by score → regulation check per listing

**Key data files:**
- `data/neighborhoods.py` — 12 Miami neighborhoods with nightly rates, occupancy, feasibility scores
- `data/seasonal.py` — monthly demand factors (Miami peaks Dec-Apr, troughs Jun-Sep)
- `data/furnishing.py` — itemized furnishing items across Budget/Mid-Range/Premium tiers
- `data/regulations.py` — STR rules for City of Miami, Miami Beach, unincorporated MDC, Coral Gables, Hialeah
- `data/saved_data.json` — user's persistent saved properties, checklist state, outreach queue

**Financial model:**
- Revenue = nightly rate × nights × occupancy × seasonal factor
- Airbnb fee: 3%, Miami-Dade TOT: 6%, FL sales tax: 7%
- Expenses: rent, utilities (~$130-185), internet ($70), cleaning ($85-145/turn), supplies ($75), STR insurance ($85), platform tools ($55), misc (2% of rent)
- Concession: first N months rent = $0, full Airbnb revenue still collected
- ROI = annual net profit / (furnishing + deposit + license + launch supplies)

**Top neighborhoods for under $1,800:**
- Little Havana: $95/night, 62% occ, avg rent $1,500 — HIGH feasibility
- Airport/Doral: $90/night, 71% occ, avg rent $1,600 — HIGH feasibility (best consistency)
- Little Haiti/Upper NE: $85/night, 58% occ, avg rent $1,350 — HIGH feasibility (cheapest)
- Overtown: $90/night, 61% occ, avg rent $1,400 — HIGH feasibility (best transit)
- Miami Beach: AVOID — STR heavily restricted, fines up to $20k+
