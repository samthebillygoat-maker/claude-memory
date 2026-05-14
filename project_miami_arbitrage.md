---
name: CitySide Stays — STR Arbitrage Business
description: Sam's national Airbnb arbitrage business. Signs leases, furnishes, lists on Airbnb. No geographic limits.
type: project
date: 2026-04-22
---

## Business Overview

**Brand:** CitySide Stays  
**Model:** Sign long-term leases → furnish → list on Airbnb/Furnished Finder → keep the spread  
**Scope:** All 50 states — no geographic limits  
**Goal:** Build a portfolio of STR units generating consistent monthly net income

## The Numbers That Matter

- **Minimum ratio:** 2.0x (monthly STR revenue ÷ rent) to even consider a deal
- **Target ratio:** 3.0x+ for a strong deal
- **Sweet spot markets:** ratio 4x+ with rent under $1,000/mo

## Active Markets Being Targeted (Top Priority)

| Market | State | Ratio | Net/mo | Why |
|--------|-------|-------|--------|-----|
| Columbus | GA | 3.7x | $1,900 | Fort Moore military, almost zero STR competition |
| Blue Ridge | GA | 6.6x | $3,900 | Mountain cabins, demand > supply |
| Tuscaloosa | AL | 6.0x | $3,485 | Alabama football, 366 listings for whole city |
| Red River Gorge | KY | 5.2x | $2,959 | Climbing/NP, only 695 listings |
| Pigeon Forge | TN | 5.5x | $3,568 | Dollywood, $800 rent |
| Jackson | WY | 12.1x | $13,320 | Extreme ADR, extreme seasonality |
| Waco | TX | 4.9x | $3,150 | Magnolia Market, Baylor, low supply |

## Strategy Priorities

### Military Town Arbitrage (Proven Model)
Columbus GA confirmed: Fort Moore drives PCS/TDY/family demand, almost no STR hosts serving it.

Same playbook applies to:
- San Antonio, TX — Lackland AFB + Fort Sam Houston
- Fayetteville, NC — Fort Liberty (formerly Bragg)
- Killeen, TX — Fort Cavazos (formerly Hood)
- Clarksville, TN — Fort Campbell

All share: 60%+ occupancy, rent under $900, minimal STR competition.

### High Demand / Low Supply Entry Points
Best arbitrage comes from markets where supply is constrained:
- **Permit caps:** Santa Fe NM (hard 1,000 cap), Telluride CO (just voted to cap)
- **Geography:** Jackson WY, Moab UT, Bar Harbor ME, Estes Park CO
- **Under-awareness:** Missoula MT (281 listings), Eureka Springs AR, Branson MO
- **Regulations removed supply:** Las Vegas NV and Honolulu HI are dead — do not target

## DealScout Tool

Full Streamlit app: `C:\Users\samth\miami-arbitrage\`  
Run: `streamlit run app.py` → http://localhost:8501

- 70 national markets in scraper
- 12 pages including national leads, email monitor, PDF report generator
- See `project_miami_tool_details.md` for full technical reference

## AirDNA Batch Scraper

- Script: `miami-arbitrage/scripts/airdna_batch.py`
- Use `--use-profile` to skip login (uses saved Chrome session)
- Chrome profile: `C:\Users\samth\AppData\Local\Google\Chrome\User Data`
- 18 addresses queued as of Apr 27, 2026

## Outreach Stack

- **Afroman** = ElevenLabs conversational AI agent for landlord calls
- Agent ID: `agent_4801kpp6506efqhv1n4v62w555bs`
- 207 phone numbers ready as of Apr 27, 2026
- Twilio for SMS / phone routing

## Business Status (Apr 28, 2026)

- Pre-revenue
- Deadline: **Jul 31, 2026**
- Tampa leads have data quality issues (duplicates, vague descriptors)

## Accounts & Contacts

- **Personal email:** samthebillygoat@gmail.com
- **Business email:** info@citysidestays.com
- **SMS alerts:** 925-409-8490
- **Obsidian vault:** `C:\Users\samth\Documents\brain\claude-memory-main\`
