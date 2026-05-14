# Apify Apartments.com Scraper — Field Notes

**Actor:** `pro100chok~apartments-scraper-usage`
**Used in:** `C:\Users\samth\miami-arbitrage\scripts\scrape_apartments_apify.py`
**Last verified:** 14 May 2026 against Gulf Shores + 4-market 3-page pull.

## What the actor returns (relevant fields per listing)

- `url`, `listingId`, `name`, `propertyType` (e.g. "Condo",
  "ApartmentUnitForRent")
- `address` (street/city/state/zip), `location` (lat/lng)
- `pricing.min` / `pricing.max`, `rentals[0]` (Beds, Baths, SquareFeet, Rent)
- `contact.phone` (formatted `+1-NNN-NNN-NNNN`)
- `meta.profileType` — one of **`Basic`** / **`Paid`** / **`Prosumer`**
- `meta.listingTypeId` — integer, 1/2/3/6/7 observed

## Owner-direct detection (the rules that work)

`profileType` is the more reliable signal than `listingTypeId`:

| profileType | listingTypeId | What it usually is |
|---|---|---|
| `Basic` | 1 | Cheap listing, often small landlord OR small PM |
| `Paid` | 2 | Paid PM placement — gatekeeper |
| `Paid` | 3 | Paid feature listing — PM |
| `Prosumer` | 6 | Small landlord, classic FRBO |
| `Prosumer` | 7 | Small landlord, newer-style listing |

**Use as `is_owner_direct`:**

```python
is_frbo = (
    meta.get("listingTypeId") in (5, 6, 7)
    or meta.get("profileType") in ("FRBO", "Prosumer")
)
```

Combined with the **>5-listings-per-phone PM filter**, this catches most
PMs that slip past the profileType check (some PMs use `Basic` profiles).

## Critical gotchas

- **NO CONCURRENT RUNS** on this actor. Firing a second scrape while the
  first is running causes the second's DETAILS action to `ABORTED`.
  Always wait for the previous job to finish.
- **/condos/ path filters out big PMs** — use
  `https://www.apartments.com/condos/<city>-<state>/` instead of bare
  `/<city>-<state>/`. The condos path returns mostly individual owners
  on the Apartments.com classification.
- **City bucketing is fuzzy.** A scrape of `/condos/chattanooga-tn/`
  returns listings whose `address.city` field includes neighbouring
  suburbs (Hixson, Rossville, East Ridge). Use a MARKET_CLUSTERS dict
  in the formatter to fold suburbs back into the parent market.
- **HTML entities in fields.** Addresses come back with `&#x27;`,
  `&amp;`, etc. — run `html.unescape()` before display.
- **Phone format is `+1-NNN-NNN-NNNN`.** Strip non-digits, validate
  NANP (area 200-999, exchange 200-999).

## Cost / budget (Apify pricing as of May 2026)

- **Free tier:** $5/mo platform credit, hard cap. Hits 403
  `platform-feature-disabled: Monthly usage hard limit exceeded` when
  exhausted. Resets monthly on the 1st.
- **Starter $49/mo:** $49 platform credit included (~24,500 listings
  at $0.002/listing). Residential proxy traffic ~$13/GB on top.
- **Friday Pack realistic pattern** (weekly 5-market 3-page pull):
  ~1,000-1,500 listings/wk = $8-12/mo in actor compute (well within
  Starter's $49 credit), plus ~$5-10 proxy. Net out-of-pocket = $49/mo
  flat.

**Break-even:** 1 Starter pack sale ($97) covers 2 months of Apify
Starter. 1 Weekly subscription month ($197) covers 4 months.

## Per-page yield expectations

From the 5-market 3-page pull (2026-05-14):

| Market (slug) | 3-page raw | After dedupe + PM filter | GREEN |
|---|---|---|---|
| gulf-shores | 13 | 12 | 12 |
| branson (+ Hollister, Rockaway, Merriam-Woods) | 45 | 19 | 9 |
| chattanooga (+ Hixson, Rossville, East Ridge) | 111 | 103 | 83 |
| smokies (Gatlinburg + Pigeon Forge + Sevierville + Cosby + Pittman Center + Newport) | 31 | 17 | 8 |

Big city / 5-page expected yield: Tampa, Miami each ~200 listings
(before dedupe + PM filter).

## Related

- [[Miami Airbnb Arbitrage]] — DealScout / CitySide hub
- [[Miami STR Zoning per ZIP]] — pre-delivery filter
