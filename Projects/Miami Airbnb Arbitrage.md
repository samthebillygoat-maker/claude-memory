# 🏠 Miami Airbnb Arbitrage

**Status:** Active — sign lease ASAP
**Goal:** 1BR/1BA under $1,800/mo with sublease permission → Airbnb → positive cash flow

---

## Deal Targets

| | |
|--|--|
| Max rent | $1,800/mo |
| Unit type | 1 bed / 1 bath |
| Concession | 2 free months from landlord |
| Lease requirement | Written sublease/Airbnb permission |

---

## The Tool

**Location:** `C:\Users\samth\miami-arbitrage\`
**Stack:** Python · Streamlit · Plotly · Pandas

**Run it:**
- Double-click `run.bat`, OR
- `cd C:\Users\samth\miami-arbitrage` → `streamlit run app.py`
- Opens at http://localhost:8501

**Data persists** to `data\saved_data.json` — survives restarts.

### 9 Pages

1. **Property Analyzer** — full 12-month P&L, 3-scenario analysis, save property
2. **Neighborhood Guide** — compare all Miami hoods, revenue heatmap, radar chart
3. **Furnishing Calculator** — itemized furnishing across Budget/Mid/Premium tiers
4. **Saved Properties** — track with contact info, status, comparison chart
5. **Legal & Compliance** — STR rules by jurisdiction, lease checklist
6. **Checklist** — 3-phase task tracker, negotiation email/phone/text scripts
7. **Outreach Manager** — parse listings → generate emails → track responses
8. **Address Analyzer** — paste any Miami address → full analysis + real comps
9. **Listing Scout** — RentCast API → auto-searches Miami → ranks by score

---

## Financial Model

```
Revenue = nightly rate × nights × occupancy × seasonal factor
Airbnb fee: 15.5% (host-only, standardized Dec 1 2025)
Miami-Dade TOT: 6% (TouristExpress, now MONTHLY remittance)
FL sales tax: 7%

Expenses: rent · utilities $130–185 · internet $70 · cleaning $85–145/turn
          supplies $75 · STR insurance $85 · platform tools $55 · misc 2% rent

Concession: first N months rent = $0, full Airbnb revenue collected
ROI = annual net profit / (furnishing + deposit + license + launch supplies)
```

> ⚠️ Airbnb fee in tool may show 3% — update to 15.5% (changed Dec 2025)

---

## Top Neighborhoods (Under $1,800/mo)

| Neighborhood | ADR (2026) | Occupancy | Avg Rent | Notes |
|---|---|---|---|---|
| Little Havana | ~$178–186/night | 56–63% | $1,500 | HIGH — tool shows $95 (outdated) |
| Airport/Doral | $90/night | 71% | $1,600 | HIGH — best consistency |
| Little Haiti/Upper NE | $85/night | 58% | $1,350 | HIGH — cheapest |
| Overtown | $90/night | 61% | $1,400 | HIGH — best transit |
| Miami Beach | AVOID | — | — | Fines start $20k, repeat up to $100k |

**Above $1,800 but high ROI:**
- Wynwood: $185–240/night · rents $2,200–2,800 (2BR)
- Edgewater: $183–232/night · ~$30k–36.5k/yr · World Cup demand zone

---

## STR Regulations

**City of Miami / Miami-Dade:**
- DBPR Vacation Rental License: ~$170/yr + $50 one-time
- FL Dept of Revenue sales tax registration: free
- Miami-Dade Certificate of Use: fees vary
- City of Miami Business Tax Receipt required
- Business Tax Receipt (BTR) required if >$25k/yr rental income
- Total initial licensing: ~$500–800 · annual renewal ~$300
- Occupancy cap: 2 per bedroom + 2 additional, max 12 persons
- Tourist tax: monthly remittance (was quarterly) — 25% penalty for late

**STR-Friendly Condo Buildings (rare):**
- LOFTY Brickell (99 SW 7th St) — purpose-built STR, T6 zoning, no rate cap
- The Standard Brickell (1034 SW 2nd Ave) — fully STR-certified

**Miami Beach: AVOID**
- 500-foot minimum distance between STR properties in residential zones
- Grandfathering cutoff Jan 1, 2026 — new applications much harder
- Automated compliance platform being built to auto-detect unlicensed listings

---

## World Cup 2026 — Massive Opportunity

**Match dates at Hard Rock Stadium:** Jun 21, 24, 27 · Jul 3, 11, 18
- ADR already up 30% vs same period last year
- 80% demand increase YoY · 128% occupancy spike post-draw
- Airbnb projects ~$255/night · Deloitte: avg host earns ~$5,000 for full tournament
- $123M total Airbnb guest spending projected in South Florida
- $750 Airbnb bonus for new hosts who go live by Jul 31, 2026

**Pricing strategy (PriceLabs):**
- Near Hard Rock: 7-night minimums on match dates
- Broader market: 2–3 night minimums for visibility
- Set rates at 90th percentile with 20% buffer
- Highlight transit/stadium proximity

---

## Airbnb ToS — April 20, 2026 Changes

> All accounts created before Feb 5, 2026 had to accept on April 20.

- **Payout freeze:** Airbnb can freeze payouts indefinitely with no explanation or timeline
- **AI evidence ban:** No AI-generated/enhanced photos in AirCover damage claims
- **Consumables excluded:** Toiletries, cleaning supplies ineligible for AirCover
- **Host cancellation penalties:** Now 10–50% of reservation (was flat $50/$100)
- **Dispute resolution:** Switched to AAA (filing fee ~$225, recoverable on win)
- **24-hr free cancellation:** Now applies to ALL listings regardless of policy

---

## Key Data Files

```
data/neighborhoods.py   — 12 neighborhoods with rates/occupancy/scores
data/seasonal.py        — monthly demand factors (peaks Dec–Apr, troughs Jun–Sep)
data/furnishing.py      — Budget/Mid/Premium furnishing items
data/regulations.py     — STR rules by jurisdiction
data/saved_data.json    — saved properties, checklist, outreach queue
```

---

## Related

- [[Resources/Miami STR Intelligence]] — ongoing market research & regulatory updates
- [[Areas/About Me]] — your profile and how you work
