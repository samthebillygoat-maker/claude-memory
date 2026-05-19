---
name: manual-zumper-miami-leads-2026-05-14
description: 25-lead manual Friday-Pack-style harvest from Zumper covering Miami/Sunny Isles/Wynwood/Hollywood/Wilton Manors/Lauderdale-by-the-Sea/Brickell; methodology, prime targets, and what the automated [[zumper-harvest-2026-05-14]] scraper would have missed
metadata:
  type: project
---

# Manual Zumper Miami Lead Harvest — 2026-05-14

Output: `C:\Users\samth\Desktop\manual_zumper_apartments_miami_2026-05-14.csv` (25 rows).

**Why:** Friday Pack needed real owner-direct leads pulled by hand because apartments.com was bot-walled and the [[zumper-harvest-2026-05-14]] scraper wasn't yet wired into the workflow for these specific zips. WebFetch-via-LLM was used as a human-grade browser substitute.

**How to apply:** Use these contacts for the first cold-outreach pass. For future runs of similar manual harvests, follow the [[reference-zumper-phone-pattern]] heuristics — they cut wasted fetches in half.

## Prime call-first targets (multi-unit, fresh, clean target zip)

| Rank | Owner | Phone | Address | Zip | Signal |
|------|-------|-------|---------|-----|--------|
| 1 | Tamara Sabbagh | (954) 471-8904 | 4144 El Mar Dr | 33308 | 6-unit building, 3 available |
| 2 | Lorraine Llobet | (305) 851-2820 | 70 NW 31st St | 33127 | 2-unit furnished Wynwood multifamily (STR-ready) |
| 3 | Claudio Nieto | (786) 252-4552 | 17375 Collins Ave | 33160 | 2 units same building Sunny Isles |
| 4 | George Rodriguez | (786) 267-2291 | 3701 NE 170th St | 33160 | 6-unit Eastern Shores |
| 5 | Lauder Management | (754) 354-8386 | 817 NE 19th Ave | 33304 | 4-unit Victoria Park |
| 6 | Larisa | (305) 975-4132 | 1715 N 16th Ave | 33020 | On-site mgr, multi-unit Hollywood |
| 7 | Ziprent | (786) 313-5471 | 2532 Garfield + 1250 Miami Rd | 33020 / 33316 | Small tech-PM, 2 cities |
| 8 | Gina Villanell | (954) 243-5580 | 1433 NE 22nd St #1 | 33305 | Front of duplex |

## Discovery worth keeping: Miami condotel buildings

Two Downtown Miami / Brickell condotel addresses surfaced where Zumper exposes individual-investor direct dials at scale:

- **121 NE 5th St ("501 First Residences"), 33132** — 19 distinct landlord phones in the listing table. 6 added to CSV; 13 more available. Classic STR-arbitrage condotel pattern.
- **111 E Flagler St, 33131** — 4 distinct landlord phones, 3 fresh.
- **1155 Brickell Bay Dr, 33131** — 6 landlords surfaced; 1 fresh in budget.

These are zips **NOT on the existing Friday Pack target list** (33131 / 33132). Worth a Sam-level zoning decision: condotels in T-6 downtown Miami zoning historically permit STR via condo association rules. If 33131/33132 are confirmed STR-friendly via the condo association (not city ordinance), these become a high-density pocket that broader_harvest currently ignores.

## What the automated scraper would have missed

Per [[zumper-harvest-2026-05-14]] the scraper deliberately skips `/address/` paths because the JSON-LD blocks there are `ImageObject` only. But the LLM-based WebFetch found real direct-dial owner phones on those same `/address/` pages — Zumper renders them in the visible "Contact" UI block even when the JSON-LD is missing.

**Implication for the scraper:** `/address/` pages are scrapeable for phones via a non-JSON-LD path. The contact phone lives in a `<div data-testid="contact-phone">` or similar UI element (need to confirm exact selector). A second extraction strategy on `/address/` pages would roughly **double yield** of multi-unit-condo discoveries. This contradicts gotcha #2 in [[zumper-harvest-2026-05-14]] — the warning about "silent pollution from Zumper's own number" is real for regex on raw HTML, but the actual rendered contact block is owner-direct and worth scraping with a DOM-aware selector.

## Methodology learned (apply next manual harvest)

1. **Start at neighborhood pages, not zip URLs.** Per the harvest gotcha. Zip-search URLs 301 to homepage.
2. **Page 1 of any neighborhood is mostly 844-relay listings from syndicated agents** (Charles Rein / Jon Fiorentino / Frederic Achotegui / Bradley Minto). The owner-direct leads start showing up on page 2+, especially under $2,500/mo.
3. **/address/ building pages are gold** — they often list every available unit with a per-unit phone. One fetch can yield 5+ owners (e.g. 17375 Collins, 121 NE 5th St, 111 E Flagler).
4. **Skip Blueground, Landing, Sonder, Mint House** — these are corporate STR competitors, not landlords.
5. **Skip Invitation Homes, Progress Residential, FirstKey Homes, Tricon** — institutional SFR, won't sublease.
6. **844 / 888 numbers with `ext. NNNN` are Zumper's call-tracking relay** — not a direct line. Reject regardless of the named "agent" attached.

## Bot-wall status as of 2026-05-14

| Source | Status |
|--------|--------|
| zumper.com | ✅ Friendly to WebFetch, no rate limits hit in 70+ sequential requests |
| apartments.com | ❌ HTTP 403 on every `/houses/{city}-fl/` and `/condos/...` URL |
| realtor.com | Skipped per prior session — confirmed not useful for FRBO |

## Files

- CSV output: `C:\Users\samth\Desktop\manual_zumper_apartments_miami_2026-05-14.csv`
- Phone-pattern reference: `[[reference-zumper-phone-pattern]]`
- Related scraper project: `[[zumper-harvest-2026-05-14]]`
