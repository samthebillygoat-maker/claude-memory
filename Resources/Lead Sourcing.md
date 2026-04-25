# 📋 Lead Sourcing — Landlord Phone Numbers

How to find real landlord phone numbers for cold calling campaigns.

---

## Source #1: RentCast API (Best — Use This First)

**What it returns:** Active rental listings with `listingAgent.phone` and `listingOffice.phone` fields  
**Quality:** Real, verified agent/property manager numbers  
**Cost:** Paid API — key stored in DealScout settings  
**API key:** `0e394cd1cacc42fab97b2246027802ea`

**How to run:**
```
cd C:\Users\samth\miami-arbitrage
python scripts/batch_national_scrape.py
```

**Markets where RentCast populates phone fields (confirmed):**

| Market | State | Notes |
|--------|-------|-------|
| Miami | FL | 79 phones per 100-listing pull |
| Jacksonville Beach | FL | 35 phones |
| Key West | FL | 25 phones |
| Destin | FL | 20 phones |
| Galveston | TX | 44 phones |
| Palm Springs | CA | 12+ phones |
| Marco Island | FL | 3 phones |
| Sedona | AZ | 1–2 phones |
| Fredericksburg | TX | 1–2 phones |
| Gatlinburg | TN | 2–3 phones |

**Markets where RentCast returns NO phones:**
- Tampa FL — 500 listings, zero phones
- Most inland/suburban markets

**API endpoint:**
```
GET https://api.rentcast.io/v1/listings/rental/long-term
  ?city={city}&state={state}&status=Active&limit=100
Header: X-Api-Key: 0e394cd1cacc42fab97b2246027802ea
```

---

## Source #2: Skip Tracing (For Markets With No Phone Data)

**When to use:** When RentCast returns listings but no phone fields (e.g., Tampa)

**Workflow:**
1. Pull addresses from RentCast (even without phones)
2. Export to CSV: `phone_number,city,number_of_units` → just `address,city,state,zip`
3. Upload to **batchskiptracing.com** (same company as BatchLeads)
   - New accounts get free credits — try before paying
   - Paid rate: ~$0.15–0.20/record
4. Download results → send to Claude → formatted for ElevenLabs

**Tampa skip trace file ready:** `C:\Users\samth\Downloads\tampa_addresses_skiptrace.csv` (500 addresses)

---

## Source #3: Craigslist Scraping (Mostly Useless — Documented for Reference)

**Why it doesn't work:**
- Phones hidden behind JS "reply" button — not in HTML
- Playwright can reveal them but most markets don't have phones in listing text
- Craigslist spam farms embed fake +1792 numbers in listing body text

**Tampa specifically:** Playwright confirmed 0/20 listings had any phone number.

**Markets that sometimes work:** Beach/vacation towns where individual landlords self-list (not property managers)

---

## ⚠️ The +1792 Fake Number Problem

**Area code 792 does not exist** in the North American Numbering Plan.

Any list with lots of +1792 numbers = from a Craigslist spam farm. Trash the list.

**How to spot:**
- Multiple numbers with same area code 792
- Numbers that resolve to invalid when dialed
- Common in CL scrapes for: Jackson WY, St. Augustine FL, Hilton Head SC, Cape Cod MA, Palm Springs CA (CL results only)

**Fix in scraper** — `normalize_phone()` in `batch_national_scrape.py` now blocks 792.

---

## Formatting for ElevenLabs

Once you have phone numbers, format as:

```csv
phone_number,city,number_of_units
+17863290972,Miami,5
```

Rules:
- E.164 format: `+1` + 10 digits, no spaces
- `city` and `number_of_units` must match your ElevenLabs agent's dynamic variable names exactly
- Do NOT add language/voice/prompt columns unless enabled in agent settings

---

## Results History

| Date | Count | Source | File | Notes |
|------|-------|--------|------|-------|
| Apr 23 | 18 valid | RentCast | `national_leads_elevenlabs.csv` | 82 CL numbers were +1792 spam |
| Apr 24 | 25 valid | RentCast | `miami_leads_elevenlabs_v2.csv` | From original 101-row Miami file |
| Apr 24 | **207 valid** | RentCast | `national_leads_elevenlabs_v2.csv` | 17 API calls, 532 markets searched |
