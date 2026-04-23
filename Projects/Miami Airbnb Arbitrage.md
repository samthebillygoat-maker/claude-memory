# 🏠 CitySide Stays — STR Arbitrage (National)

**Status:** Active — scaling nationally  
**Goal:** Sign long-term leases with sublease rights → furnish → list on Airbnb/Furnished Finder → keep the spread  
**Scope:** All 50 states — not just Miami anymore

---

## Deal Criteria

| | |
|--|--|
| Min ratio | 2.0x (STR monthly revenue ÷ rent) |
| Target ratio | 3.0x+ |
| Sweet spot | 4x+ ratio, rent under $1,000/mo |
| Lease requirement | Written sublease/STR permission |

---

## DealScout Tool

**Location:** `C:\Users\samth\miami-arbitrage\`  
**Stack:** Python · Streamlit · Plotly · Pandas · Flask · Twilio · ElevenLabs · Playwright

**Run it:**
```
cd C:\Users\samth\miami-arbitrage
streamlit run app.py
```
Opens at http://localhost:8501

**Data persists** to `data\saved_data.json` — survives restarts.

### Pages (as of April 2026)
1. **Property Analyzer** — full 12-month P&L, 3-scenario analysis
2. **Neighborhood Guide** — compare markets, revenue heatmap
3. **Furnishing Calculator** — Budget/Mid/Premium tiers
4. **Saved Properties** — track leads with contact info, status
5. **Legal & Compliance** — STR rules by jurisdiction
6. **Checklist** — 3-phase task tracker, outreach scripts
7. **Outreach Manager** — parse listings → generate emails → track responses
8. **Address Analyzer** — paste any address → full analysis + comps
9. **Listing Scout** — multi-source lead finder + auto cold caller ← MAIN PAGE
10. **Acquisitions Report** — PDF report generator
11. **Contact Finder** — owner lookup + skip trace
12. **Email Monitor** — Gmail IMAP scanner + AI drafts + SMS alerts

### Key Data Files
```
data/scraper.py         — 266 national markets (MARKET dict) — single source of truth
data/neighborhoods.py   — Miami neighborhood rates/occupancy
data/seasonal.py        — monthly demand factors
data/furnishing.py      — furnishing items by tier
data/regulations.py     — STR rules by jurisdiction
data/saved_data.json    — saved properties, pipeline, outreach queue
data/scout_cache.json   — Listing Scout search results cache
data/airdna_cache.json  — AirDNA Rentalizer cache (7-day TTL)
```

---

## Automated Cold Caller

**Stack:** Twilio + ElevenLabs Conversational AI + Flask (`server.py`)

**ElevenLabs Agent ID:** `agent_4801kpp6506efqhv1n4v62w555bs`  
**Agent name:** Outbound Dialer with Voicemail Handling  
**Voice:** Greg from CitySideStays LLC

### How to Run Every Session
```
# Terminal 1 — Flask server (cold caller backend)
cd C:\Users\samth\miami-arbitrage
set ELEVENLABS_API_KEY=[from ElevenLabs dashboard]
set TWILIO_ACCOUNT_SID=[from Twilio dashboard]
set TWILIO_AUTH_TOKEN=[from Twilio dashboard]
set TWILIO_FROM_NUMBER=+17753695206
set SERVER_URL=https://[ngrok-url-changes-each-session]
python server.py

# Terminal 2 — expose Flask to internet (Twilio needs public URL)
C:\Users\samth\miami-arbitrage\ngrok.exe http 5001

# Terminal 3 — DealScout UI
cd C:\Users\samth\miami-arbitrage
streamlit run app.py
```
> ⚠️ ngrok URL changes every session — always update SERVER_URL before starting Flask

### Server Endpoints
| Endpoint | Purpose |
|---|---|
| `POST /make-call` | Dials landlord via Twilio, starts ElevenLabs AI |
| `GET /audio-stream` | Live call audio stream — open in browser to listen in |
| `GET /call-status/<sid>` | Returns call status + recording URL |
| `WS /audio-fork` | Twilio forks call audio here (internal) |
| `POST /outbound-call` | Twilio webhook — returns ElevenLabs TwiML |

### Features
- **Auto Call button** in every Listing Scout lead card
- **🎧 Listen In** — open `http://localhost:5001/audio-stream` in browser during call
- **📼 Recording** — auto-records every call, playback inline after call ends
- **Auto-marks lead** as `📞 Called` in pipeline after dialing

### Known Issue (as of April 22, 2026)
ElevenLabs workflow has broken `voicemail_detection` tool reference in **Leave Voicemail** node → causes "Documents with ids not found" error mid-call.  
**Fix:** Go to ElevenLabs → Agent → Workflow → click Leave Voicemail node → remove broken tool reference

### ElevenLabs Agent Variables
- `{{city}}` — target city name
- `{{callback_number}}` — 9254098490
- `{{number_of_units}}` — fill in before calling (e.g. 3)

---

## Phone Number Sourcing

**RentCast** returns `listingAgent.phone` and `listingOffice.phone` — these are the agent/property manager numbers.  
**Craigslist** — phones hidden behind login wall; Playwright scraper tries to extract from body text  
**Manual entry** — enter phone per listing in Listing Scout, saved to pipeline

**RentCast API key:** stored in DealScout → Listing Scout → API Keys section

---

## Top Target Markets (National)

| Market | State | Ratio | Net/mo | Why |
|--------|-------|-------|--------|-----|
| Columbus | GA | 3.7x | $1,900 | Fort Moore military, near-zero STR competition |
| Blue Ridge | GA | 6.6x | $3,900 | Mountain cabins, demand > supply |
| Tuscaloosa | AL | 6.0x | $3,485 | Alabama football, 366 total listings |
| Red River Gorge | KY | 5.2x | $2,959 | Climbing/NP, only 695 listings |
| Pigeon Forge | TN | 5.5x | $3,568 | Dollywood, rent ~$800 |
| Jackson | WY | 12.1x | $13,320 | Extreme ADR, seasonal |
| Waco | TX | 4.9x | $3,150 | Magnolia Market, Baylor, low supply |

### Military Town Playbook
Columbus GA confirmed: Fort Moore drives PCS/TDY/family demand, almost no STR competition.  
Same model: San Antonio TX · Fayetteville NC · Killeen TX · Clarksville TN

---

## Financial Model

```
Revenue = nightly rate × nights × occupancy × seasonal factor
Airbnb fee: 15.5% (host-only, changed Dec 1 2025)
Miami-Dade TOT: 6% (monthly remittance now)
FL sales tax: 7%

Expenses: rent · utilities $130–185 · internet $70 · cleaning $85–145/turn
          supplies $75 · STR insurance $85 · platform tools $55 · misc 2% rent

ROI = annual net profit / (furnishing + deposit + license + launch supplies)
```

---

## Miami STR Regulations (for reference)

- DBPR Vacation Rental License: ~$170/yr + $50 one-time
- Miami-Dade Certificate of Use required
- City BTR required if >$25k/yr
- Tourist tax: monthly remittance (25% penalty for late)
- **Miami Beach: AVOID** — fines start $20k, grandfathering cutoff Jan 1, 2026

---

## World Cup 2026 — Miami Opportunity

Match dates at Hard Rock Stadium: Jun 21, 24, 27 · Jul 3, 11, 18  
- ADR up 30% YoY · 80% demand increase · avg host earns ~$5,000 for full tournament
- $750 Airbnb bonus for new hosts live by Jul 31, 2026

---

## Related
- [[Resources/Miami STR Intelligence]] — market research & regulatory updates
- [[Resources/Tech Notes]] — API changes, Streamlit updates
