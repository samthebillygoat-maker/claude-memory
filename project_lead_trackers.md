---
name: Lead-Gen Trackers
description: 5 HTML/localStorage call-tracker apps in C:\Users\samth\call-tracker\, ~270 leads across nationwide/Tampa/multi-city/beach-mountain
type: project
---

# Lead-Gen Tracker Suite

Built across 2026-04-29 → 2026-05-04. All in `C:\Users\samth\call-tracker\`. Vanilla HTML + localStorage — no backend, no deploy, just open in browser.

**Why:** Sam needs to dial leads from a single pane and persist call notes/dispositions across browser sessions without standing up a CRM.

**How to apply:** when Sam asks "where are my [city] leads" or "did I call X already," open the matching tracker; localStorage key tells you which one is fresh.

## The 5 trackers

| File | Scope | Lead count | localStorage key |
|---|---|---|---|
| `index.html` | nationwide | 424 | `call_tracker_2026_05_04` |
| `bayshore.html` | Tampa Bayshore / Hyde Park SFH | 21 | `bayshore_tracker_2026_05_04` |
| `apartments.html` | Tampa apartments | 27 | `apt_tracker_2026_05_04` |
| `all-cities.html` | Tampa 88 / Austin 25 / Miami 25 | 138 | `multi_city_tracker_2026_05_04` |
| `beach-mountain.html` | PCB 33 / Smoky Mtns 29 | 62 | `beach_mtn_tracker_2026_05_04` |

Total: **~270 leads with phone numbers extracted** (nationwide index counts include some without phones).

## Build scripts (Python, in same folder)

- `bayshore-build.py`
- `apartments-build.py`
- `multi-city-build.py`
- `beach-mountain-build.py`

Each pulls from a source CSV/MD in `~/Downloads` and emits the corresponding HTML.

## Source data files (`C:\Users\samth\Downloads\`)

- `leads-RANKED-2026-05-04.csv` — 424 nationwide, scored
- `leads-RANKED-ENRICHED-2026-05-04.csv` — 308 viable / 76 banned / 37 MTR-only after regulatory enrichment
- `pcb-gatlinburg-leads-2026-05-04.md` — Zumper scrape
- `offmarket-pcb-gatlinburg-2026-05-04.md` — Craigslist FRBO
- `tampa-apartments-batch3.md` — USF + suburbs, 38 leads
- `OVERNIGHT_BRIEF_2026-05-04.md` — canonical wake-up brief

Updated 2026-05-04.
