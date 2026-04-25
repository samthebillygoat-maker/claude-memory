# 📞 ElevenLabs Batch Calling

**Purpose:** Automatically call hundreds of landlords using ElevenLabs Conversational AI + Twilio. AI pitches the STR arbitrage deal, detects voicemail, leaves message if no answer.

**Agent ID:** `agent_4801kpp6506efqhv1n4v62w555bs`  
**Agent name:** Outbound Dialer with Voicemail Handling  
**Voice:** Greg from CitySideStays LLC

---

## How to Launch a Batch Campaign

1. Prepare your CSV (see format below)
2. Go to **ElevenLabs → Conversational AI → [your agent] → Batch Calling**
3. Click **Upload CSV**
4. Map columns if prompted
5. Click **Start Batch**

---

## CSV Format (Confirmed Working)

```csv
phone_number,city,number_of_units
+17863290972,Miami,5
+17867669388,Miami,5
```

**Rules:**
- `phone_number`: E.164 format — `+1` followed by 10 digits, no spaces, no dashes
  - ✅ `+17863290972`
  - ❌ `+1 786 329 0972`
  - ❌ `786-329-0972`
- `city` and `number_of_units` must match the exact dynamic variable names in your agent's system prompt
- **Do NOT include** `language`, `voice_id`, `first_message`, or `prompt` columns unless you've enabled those overrides in agent settings → they will cause an error

---

## Agent Dynamic Variables

| Variable | Value | Notes |
|---|---|---|
| `{{city}}` | city name | populated per row from CSV |
| `{{number_of_units}}` | 5 | fixed value — how many units you want to take |
| `{{callback_number}}` | 9254098490 | hardcoded in agent settings |

---

## Known Issue — Leave Voicemail Node

**Status: UNRESOLVED as of April 24, 2026**

ElevenLabs workflow has a broken `voicemail_detection` tool reference in the **Leave Voicemail** node → causes "Documents with ids not found" error mid-call.

**Fix (manual, ~2 min):**
1. Go to ElevenLabs → Conversational AI → agent `agent_4801kpp6506efqhv1n4v62w555bs`
2. Click **Workflow** tab
3. Click **Leave Voicemail** node
4. Find and remove the broken `voicemail_detection` tool reference
5. Save

---

## Phone Number Sourcing

### What Works
- **RentCast API** → `listingAgent.phone` + `listingOffice.phone` — best source, real agent numbers
  - Not all markets populate these fields
  - Best markets: tourist/vacation areas with licensed property managers
  - Confirmed working: Miami FL, Key West FL, Jacksonville Beach FL, Destin FL, Gatlinburg TN, Galveston TX, Sedona AZ, Marco Island FL, Palm Springs CA, Fredericksburg TX

### What Doesn't Work
- **Craigslist** → phones not in HTML; hidden behind reply button; Playwright reveals them but most Tampa/generic markets don't post phones in listing text
- **Fake +1792 numbers** → area code 792 does not exist; Craigslist spam farms embed these; blocked in scraper

### Skip Tracing (for markets with no phone data)
- Upload addresses to **batchskiptracing.com** (free trial credits for new accounts)
- Same company as BatchLeads
- Tampa: 500 addresses exported to `Downloads/tampa_addresses_skiptrace.csv` — ready to upload

---

## Scraping Script

**File:** `C:\Users\samth\miami-arbitrage\scripts\batch_national_scrape.py`

**Run:**
```
cd C:\Users\samth\miami-arbitrage
python scripts/batch_national_scrape.py
```

**Outputs:**
- `Downloads/national_leads_phones.csv` — full data (address, market, rent, ratio, source)
- `Downloads/national_leads_elevenlabs.csv` — ElevenLabs-ready (phone, city, number_of_units)

**Current settings:**
- `TARGET = 200`
- `MIN_RATIO = 1.8`
- Searches top 120 markets by revenue spread
- Blocked area codes: 800, 888, 877, 866, 855, 900, **792**
- Phases: RentCast → Apartments.com → Craigslist

---

## Results Log

| Date | File | Count | Markets | Notes |
|------|------|-------|---------|-------|
| Apr 23, 2026 | `national_leads_elevenlabs.csv` | 18 valid | Gatlinburg, Sedona, Marco Island, Palm Springs, Fredericksburg | 82 CL numbers were +1792 spam — do not use |
| Apr 24, 2026 | `national_leads_elevenlabs_v2.csv` | **207 valid** | Miami, Jax Beach, Galveston, Key West, Destin, Gatlinburg, Fort Lauderdale | All RentCast, all real |

---

## Related
- [[Projects/Miami Airbnb Arbitrage]] — the business these calls support
- [[Resources/Lead Sourcing]] — all phone/lead sourcing methods documented
