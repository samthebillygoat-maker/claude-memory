---
name: DealScout — Technical Details
description: Architecture, pages, data files, and financial model for the DealScout STR arbitrage Streamlit app
type: project
---

## Location

`C:\Users\samth\miami-arbitrage\` (folder name is legacy — tool is fully national)

**Run:** double-click `run.bat` or `streamlit run app.py` → http://localhost:8501

## Stack

Python + Streamlit + Plotly + Pandas + ReportLab + Matplotlib + Twilio + Anthropic

## Pages

| # | Page | Purpose |
|---|------|---------|
| 1 | 🏠 Property Analyzer | Full 12-month P&L, 3-scenario analysis, charts, save property |
| 2 | 🗺️ Neighborhood Guide | Compare markets, revenue heatmap, radar chart |
| 3 | 🛋️ Furnishing Calculator | Itemized furnishing across Budget/Mid/Premium tiers |
| 4 | 📋 Saved Properties | CRM — track properties, contact info, pipeline status |
| 5 | ⚖️ Legal & Compliance | STR rules by market, landlord questions, lease clause checklist |
| 6 | ✅ Checklist | Phase tracker, negotiation scripts |
| 7 | 📬 Outreach Manager | Paste listing → parse contact → generate outreach → track responses |
| 8 | 🔍 Address Analyzer | Any address → neighborhood → 2x analysis → AirDNA data → regulation check |
| 9 | 🏘️ Listing Scout | 35+ national markets, manual lead research, byBedroom ADR breakdowns |
| 10 | 📊 Acquisitions Report | Kash Wason 15-page PDF generator (AirDNA data → full deal report) |
| 11 | 🗺️ National Leads | Live Craigslist scraper — 70 markets, 3-gate filter, CRM pipeline |
| 12 | 📧 Email Monitor | Gmail scanner for both accounts — AI summaries, draft replies, SMS alerts |

## Key Data Files

- `data/scraper.py` — 70-market MARKET dict (national), gate filter logic, Craigslist RSS scraper
- `data/national_leads.json` — saved leads from last scrape
- `data/saved_data.json` — saved properties, pipeline state, checklist, outreach queue
- `data/email_drafts.json` — pending email drafts awaiting approval
- `data/email_config.json` — Gmail app passwords, Twilio credentials, Anthropic key
- `data/email_log.json` — seen email IDs (prevents duplicate alerts)
- `data/seasonal.py` — monthly demand factors (currently Miami-tuned, expand as needed)
- `data/neighborhoods.py` — neighborhood-level STR data
- `scripts/kash_report.py` — `generate_pdf(data) -> bytes` — 15-page acquisition PDF
- `scripts/email_scanner.py` — Gmail IMAP scanner + Claude classifier + Twilio SMS
- `scripts/email_scheduler.py` — auto-scan every 15 min (run in separate terminal)

## Financial Model

- Revenue = ADR × days × occupancy × seasonal factor
- Airbnb fee: 3%
- Operating expenses: configurable % (default 20%)
- 2x rule: projected monthly STR revenue must be ≥ 2× monthly rent to pass gate
- Ratio = monthly_rev / rent — higher = better arbitrage margin

## Scraper Gate System

Every scraped listing passes 3 gates before saving:
1. **Gate 1** — Rent ≤ market maxRent
2. **Gate 2** — Not in STR-restricted zone (blacklist/whitelist per market)
3. **Gate 3** — Projected monthly revenue ≥ 2× rent

## Email Monitor Setup (needs credentials)

1. Gmail App Passwords for both accounts → DealScout → Email Monitor → Setup
2. Twilio (free): Account SID + Auth Token + phone number
3. Anthropic API key (console.anthropic.com)
4. Run `python scripts/email_scheduler.py` to auto-scan every 15 min
