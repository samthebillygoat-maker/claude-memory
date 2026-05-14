# ðŸ  CitySide Stays â€” STR Arbitrage (National)

[[Home|ðŸ  Home]] | [[Areas/Goals|ðŸŽ¯ Goals]] | [[Daily Notes/_Hub|ðŸ“… Daily Notes]]

**Status:** Active â€” scaling nationally  
**Goal:** Sign long-term leases with sublease rights â†’ furnish â†’ list on Airbnb/Furnished Finder â†’ keep the spread  
**Scope:** All 50 states â€” not just Miami anymore

---

## Deal Criteria

| | |
|--|--|
| Min ratio | 2.0x (STR monthly revenue Ã· rent) |
| Target ratio | 3.0x+ |
| Sweet spot | 4x+ ratio, rent under $1,000/mo |
| Lease requirement | Written sublease/STR permission |

---

## DealScout Tool

**Location:** `C:\Users\samth\miami-arbitrage\`  
**Stack:** Python Â· Streamlit Â· Plotly Â· Pandas Â· Flask Â· Twilio Â· ElevenLabs Â· Playwright

**Run it:**
```
cd C:\Users\samth\miami-arbitrage
streamlit run app.py
```
Opens at http://localhost:8501

**Data persists** to `data\saved_data.json` â€” survives restarts.

### Pages (as of April 2026)
1. **Property Analyzer** â€” full 12-month P&L, 3-scenario analysis
2. **Neighborhood Guide** â€” compare markets, revenue heatmap
3. **Furnishing Calculator** â€” Budget/Mid/Premium tiers
4. **Saved Properties** â€” track leads with contact info, status
5. **Legal & Compliance** â€” STR rules by jurisdiction
6. **Checklist** â€” 3-phase task tracker, outreach scripts
7. **Outreach Manager** â€” parse listings â†’ generate emails â†’ track responses
8. **Address Analyzer** â€” paste any address â†’ full analysis + comps
9. **Listing Scout** â€” multi-source lead finder + auto cold caller â† MAIN PAGE
10. **Acquisitions Report** â€” PDF report generator
11. **Contact Finder** â€” owner lookup + skip trace
12. **Email Monitor** â€” Gmail IMAP scanner + AI drafts + SMS alerts

### Key Data Files
```
data/scraper.py         â€” 532 national markets (MARKET dict) â€” single source of truth
data/neighborhoods.py   â€” Miami neighborhood rates/occupancy
data/seasonal.py        â€” monthly demand factors
data/furnishing.py      â€” furnishing items by tier
data/regulations.py     â€” STR rules by jurisdiction
data/saved_data.json    â€” saved properties, pipeline, outreach queue
data/scout_cache.json   â€” Listing Scout search results cache
data/airdna_cache.json  â€” AirDNA Rentalizer cache (7-day TTL)
```

---

## Automated Cold Caller

**Stack:** Twilio + ElevenLabs Conversational AI + Flask (`server.py`)

**ElevenLabs Agent ID:** `agent_4801kpp6506efqhv1n4v62w555bs`  
**Agent name:** Outbound Dialer with Voicemail Handling  
**Voice:** Greg from CitySideStays LLC

### How to Run Every Session
```
# Terminal 1 â€” Flask server (cold caller backend)
cd C:\Users\samth\miami-arbitrage
set ELEVENLABS_API_KEY=[from ElevenLabs dashboard]
set TWILIO_ACCOUNT_SID=[from Twilio dashboard]
set TWILIO_AUTH_TOKEN=[from Twilio dashboard]
set TWILIO_FROM_NUMBER=+17753695206
set SERVER_URL=https://[ngrok-url-changes-each-session]
python server.py

# Terminal 2 â€” expose Flask to internet (Twilio needs public URL)
C:\Users\samth\miami-arbitrage\ngrok.exe http 5001

# Terminal 3 â€” DealScout UI
cd C:\Users\samth\miami-arbitrage
streamlit run app.py
```
> âš ï¸ ngrok URL changes every session â€” always update SERVER_URL before starting Flask

### Server Endpoints
| Endpoint | Purpose |
|---|---|
| `POST /make-call` | Dials landlord via Twilio, starts ElevenLabs AI |
| `GET /audio-stream` | Live call audio stream â€” open in browser to listen in |
| `GET /call-status/<sid>` | Returns call status + recording URL |
| `WS /audio-fork` | Twilio forks call audio here (internal) |
| `POST /outbound-call` | Twilio webhook â€” returns ElevenLabs TwiML |

### Features
- **Auto Call button** in every Listing Scout lead card
- **ðŸŽ§ Listen In** â€” open `http://localhost:5001/audio-stream` in browser during call
- **ðŸ“¼ Recording** â€” auto-records every call, playback inline after call ends
- **Auto-marks lead** as `ðŸ“ž Called` in pipeline after dialing

### Known Issue (as of April 24, 2026 â€” still unresolved)
ElevenLabs workflow has broken `voicemail_detection` tool reference in **Leave Voicemail** node â†’ causes "Documents with ids not found" error mid-call.  
**Fix:** ElevenLabs â†’ agent `agent_4801kpp6506efqhv1n4v62w555bs` â†’ Workflow â†’ Leave Voicemail node â†’ remove broken tool reference

### ElevenLabs Agent Variables
- `{{city}}` â€” target city name (populated from CSV per row)
- `{{callback_number}}` â€” 9254098490 (hardcoded in agent)
- `{{number_of_units}}` â€” 5 (set in CSV column)

---

## Phone Number Sourcing

**Best source:** RentCast API â†’ `listingAgent.phone` + `listingOffice.phone`  
**Skip trace:** batchskiptracing.com (free credits for new accounts) â€” for markets where RentCast has no phones  
**Craigslist:** mostly useless â€” phones hidden behind JS, spam farms embed fake +1792 numbers  
**Manual entry:** enter phone per listing in Listing Scout, saved to pipeline

**âš ï¸ +1792 area code = fake** â€” not a real US area code. Any list with lots of 792 numbers is Craigslist spam. Trash it.

See [[Resources/Lead Sourcing]] for full sourcing guide and results history.

**RentCast API key:** `[REDACTED-RentCast-key]` (also stored in DealScout settings)

## Batch Cold Calling

207 real landlord numbers collected April 24 â€” ready to call via ElevenLabs batch.  
See [[Projects/ElevenLabs Batch Calling]] for full workflow, CSV format, and known issues.

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
Same model: San Antonio TX Â· Fayetteville NC Â· Killeen TX Â· Clarksville TN

---

## Financial Model

```
Revenue = nightly rate Ã— nights Ã— occupancy Ã— seasonal factor
Airbnb fee: 15.5% (host-only, changed Dec 1 2025)
Miami-Dade TOT: 6% (monthly remittance now)
FL sales tax: 7%

Expenses: rent Â· utilities $130â€“185 Â· internet $70 Â· cleaning $85â€“145/turn
          supplies $75 Â· STR insurance $85 Â· platform tools $55 Â· misc 2% rent

ROI = annual net profit / (furnishing + deposit + license + launch supplies)
```

---

## Miami STR Regulations (for reference)

- DBPR Vacation Rental License: ~$170/yr + $50 one-time
- Miami-Dade Certificate of Use required
- City BTR required if >$25k/yr
- Tourist tax: monthly remittance (25% penalty for late)
- **Miami Beach: AVOID** â€” fines start $20k, grandfathering cutoff Jan 1, 2026

---

## World Cup 2026 â€” Miami Opportunity

Match dates at Hard Rock Stadium: Jun 21, 24, 27 Â· Jul 3, 11, 18  
- ADR up 30% YoY Â· 80% demand increase Â· avg host earns ~$5,000 for full tournament
- $750 Airbnb bonus for new hosts live by Jul 31, 2026

---

## Related
- [[Resources/Miami STR Intelligence]] â€” market research & regulatory updates
- [[Resources/Tech Notes]] â€” API changes, Streamlit updates
- [[Resources/Miami STR Zoning per ZIP]] — verified per-zip STR posture (2026-05-14), pack-shipping filter rules
- [[Resources/Apify Apartments Scraper Field Notes]] — actor gotchas, Prosumer detection, PM filter heuristics, cost model

---

## The Friday Pack — Fresh Lead Pipeline (added 2026-05-14)

A second product layered on top of CitySide: weekly lead-pack delivery
to other STR operators. Lives in two repos:

- `C:\Users\samth\hail-mary\` — Next.js app at thefridaypack.com
- `C:\Users\samth\miami-arbitrage\` — Python scraper + formatter

**Pipeline:**
1. `miami-arbitrage/scripts/scrape_apartments_apify.py --markets <slugs> --pages N --details`
2. `miami-arbitrage/scripts/format_as_friday_pack.py --date YYYY-MM-DD --markets <slugs>`
   - Dedupes by (address, phone), drops phones with >5 listings (PM filter)
   - Scores: +15/extra building, +10 rent in band ($950-$3500), +10 phone valid, +5 owner tag
   - Writes `data/friday_pack_leads_<DATE>.json` keyed by market slug
3. Copy to `hail-mary/src/data/friday-pack-fresh.json`
4. `hail-mary/scripts/send-friday-sample.mjs --send` blasts 3 GREEN leads/week to Free Sample subscribers

**Free Sample funnel:** `/free-sample` route + FAB widget on every page →
`EmailSignup` Prisma model (source='free-sample-friday-pack') → Friday
9am ET blast script.

**Paid pack pricing (canonical):** $29 trial / $97 starter / $197/mo
weekly / $347/mo pro. **Always 50 leads per pack, never 25.**

**Apify budget:** Free tier $5/mo (currently exhausted, resets June 1).
Starter $49/mo covers ~25k listings/mo. Don't upgrade until a customer
is waiting on a market not in `friday-pack-fresh.json`.
