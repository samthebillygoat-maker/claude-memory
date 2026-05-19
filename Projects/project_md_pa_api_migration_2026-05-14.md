---
name: md-pa-api-migration-2026-05-14
description: Miami-Dade Property Appraiser API endpoint migrated to apps.miamidadepa.gov + new param shape (drop myCity/folio, add from/to); folio detail requires no-dash 13-digit folio
metadata:
  type: project
---

# Miami-Dade Property Appraiser API — Post-Migration Format (2026-05-14)

**Endpoint moved.** The legacy `www.miamidade.gov/Apps/PA/PApublicServiceProxy/PaServicesProxy.ashx` 301-redirects to the new host but the OLD param shape gets a `400 Bad Request` from the upstream WCF service.

**Working base URL:**
```
https://apps.miamidadepa.gov/PApublicServiceProxy/PaServicesProxy.ashx
```
Requires `Referer: https://apps.miamidadepa.gov/PropertySearch/`.

## The breaking change

Old param set (now 400s):
```
Operation=GetAddress&clientAppName=PropertySearch&myAddress=...&myCity=Miami&folio=&myUnit=
```

New param set (works):
```
Operation=GetAddress&clientAppName=PropertySearch&myUnit=&from=1&myAddress=...&to=200
```
**Drop `myCity` and `folio`. Add `from=1` and `to=200`.** The 400 was the upstream rejecting the legacy fields.

## All three working operations

| Operation | Required params |
|---|---|
| `GetAddress` | `clientAppName=PropertySearch&myUnit=&from=1&myAddress=...&to=200` |
| `GetPropertySearchByFolio` | `clientAppName=PropertySearch&folioNumber=3122110690010` (**13 digits, no dashes**) |
| `GetOwners` | `clientAppName=PropertySearch&from=1&ownerName=...&to=200` |

## Folio gotcha

Address-search results return `Strap` field with dashes: `"31-2211-069-0010"`. The folio-detail endpoint **rejects the dashed form silently** — returns 200 with empty `AssessmentInfos`/`PropertyInfo`. Strip dashes before calling `GetPropertySearchByFolio` (`re.sub(r"\D", "", folio)`).

## Response schema quirks

- Address search → flat: `MinimumPropertyInfos[].Owner1`, `.Strap`, `.SiteAddress`, `.SiteUnit`, `.Municipality`
- Folio detail → nested: `data["Assessment"]["AssessmentInfos"][0]["AssessedValue"]`, `data["PropertyInfo"]["DORDescription"]`
- "Master" / common-element parcels can return empty `AssessmentInfos` — loop through up to ~10 address matches to find one with real numbers.
- Upstream errors come back as `text/html` (auto-POST to `MessagePages/Messages.aspx`) with HTTP 200 — check `Content-Type` not just status.

## Verified live (2026-05-14)

- `lookup_by_address("18001 Collins Avenue", "Sunny Isles Beach")` → owner `SUNNY ISLES LUXURY VENTURES INC`, folio `31-2202-003-0281`, assessed `$8.7M`, use `HOTEL OR MOTEL : COMMERCIAL`
- `lookup_parcels_by_owner("SUNNY ISLES LUXURY VENTURES INC")` → 71 parcels

## Discovery method

Fetched `https://apps.miamidadepa.gov/PropertySearch/main.b29be37fb946b6ef.js` (5.5MB Angular bundle) and grepped for `Operation:"`. The service builders are inline:
```
Operation:"GetAddress",clientAppName:"PropertySearch",myUnit:..,from:1,myAddress:..,to:200
Operation:"GetOwners",clientAppName:"PropertySearch",from:1,ownerName:..,to:200
Operation:"GetPropertySearchByFolio",clientAppName:"PropertySearch",folioNumber:..
```
Base URL is built from `GetWebServer()` which now switches `apps.miamidadepa.gov` → `https://apps.miamidadepa.gov`.

## Reference script

`C:\Users\samth\Desktop\md_pa_api_test.py` — drop-in client with `lookup_by_address()` and `lookup_parcels_by_owner()` using httpx + follow_redirects=True.

Pre-migration code in `C:\Users\samth\miami-arbitrage\scripts\auto_skip_trace.py` is now broken — `query_miami_dade_pa()` needs to be updated to the new param shape.

**Why:** Sam's Friday Pack / Miami enrichment pipeline depends on this API for owner-name lookup before the TruePeopleSearch skip-trace step. Without the param fix, every Miami-Dade lead silently loses owner enrichment.

**How to apply:** When updating any Miami enrichment script (auto_skip_trace.py, broader_harvest, Friday Pack pipeline), use the new base URL, new param shape, and strip folio dashes before detail calls. Related: [[project-zumper-harvest-2026-05-14]].
