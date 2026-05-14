---
name: STR Landlord Outreach Pipeline
description: Automated pipeline to find and contact STR-friendly landlords across Sevierville, Gatlinburg, Tampa, Miami — Craigslist + Apartments.com leads, SQLite, Python 3.12
type: project
---

# STR Landlord Outreach Pipeline

_created 2026-05-06_

**Repo**: `C:\Users\samth\projects\landlord-outreach`
**Status**: Plan B COMPLETE 2026-05-06 ~10:30pm PDT. Plan C next.

**Why:** DealScout and the lead trackers surface market data, but none of it closes a deal without actually contacting landlords at scale. This pipeline automates the top-of-funnel: find rental listings, qualify them against STR comp data, and queue them for VA outreach.

## What it does

Scrapes rental listings from Craigslist and Apartments.com in STR target markets, stores leads in SQLite, qualifies against AirDNA comps (Plan B, bulk export + cache), and surfaces a prioritized queue for the VA to work from the cold call SOP.

## Markets (markets.yaml)

- Sevierville, TN
- Gatlinburg, TN
- Tampa, FL
- Miami, FL

## Stack

- Python 3.12
- scrapling (scraping)
- SQLite (lead store + AirDNA comps cache)
- uv (dependency management)
- markets.yaml config (add/remove markets without code changes)

## Lead Sources

- **Craigslist** — housing listings, free, no proxies needed
- **Apartments.com** — free, no proxies needed
- AirDNA comps qualifier via bulk export + SQLite cache (Plan B)

## Key docs

- Design spec: `docs/superpowers/specs/2026-05-06-landlord-outreach-design.md`
- Plan A (foundation): `docs/superpowers/plans/2026-05-06-landlord-outreach-plan-a-foundation.md`

## Companion assets

- VA cold call SOP: `C:\Users\samth\CitySide_Stays_VA_Cold_Call_SOP.txt`
- VA follow-up email templates: `C:\Users\samth\CitySide_Stays_Followup_Email.txt`
- VA meeting: 2026-05-07 (SOP review + walkthrough)

## VA SOP highlights

- Sam's exact script: corporate housing provider framing, "20 units by end of month," 5-20 unit pitch
- Chris Voss label-first objection handling throughout
- Objections covered: damage, no track record, non-payment, turnovers, vacancy cost, HOA, minimum stay, parties
- Section 7 (Ackerman rent): VA never quotes rent — routes to Sam
- CRM logging: 9 outcome codes
- 30-day listing rule: flag, don't reject
- Airbnb transparency hard rule: always disclose upfront, never hide
- Both voicemail scripts included

## Plan A — COMPLETE (2026-05-06)

All 7 tasks built and committed. 17/17 pytest passing in 0.49s.

Entry point: `python -m landlord_outreach.scrape <market>`

Git log:
- `e945293` feat: scrape CLI with dedup-on-insert
- `75f1b7e` feat: craigslist source with apa search + posting parser
- `0bc1165` feat: apartments.com source with schema.org parser
- `9f006f3` feat: Lead dataclass + Source protocol
- `e2f6868` feat: sqlite schema with leads table + dedup constraint
- `0f014d0` feat: market config loader with by-slug lookup
- `0a2e93d` chore: scaffold landlord-outreach project

## Plan B — COMPLETE (2026-05-06 ~10:30pm PDT)

77/77 tests passing (up from 17 in Plan A). 10 tasks built TDD.

Entry point: `python -m landlord_outreach.qualify <market>` — runs all 4 filters in sequence (heuristics → zoning → owner enrichment → AirDNA comps) and updates leads in SQLite.

Git log:
- `0948960` chore: Plan B qualify pipeline complete — all tests green
- `b9b0dc4` chore: gitignore data/airdna exports, keep zoning GeoJSON tracked
- `39c2e2a` feat: qualify CLI — heuristics, zoning, owner enrichment, AirDNA in sequence
- `10a9345` feat: AirDNA comp qualifier with haversine, 5-comp radius, 30-day cache
- `891802a` feat: owner enrichment with county assessor lookup (Sevier TN, Hillsborough FL, Miami-Dade FL)
- `0a46085` feat: zoning filter with shapely point-in-polygon + stub GeoJSON fixtures for all 4 markets
- `561fca3` feat: heuristic prefilter with BR, rent-band, blocked-keyword rules
- `570d549` feat: add Plan B qualification fields to Lead dataclass
- `659a85a` feat: db schema migration for Plan B qualify columns + airdna_listings table
- `4b3d9b5` chore: add shapely/httpx deps and heuristic fields to markets.yaml

## Plan C — NEXT

Scope:
- Outreach email generator (Claude personalization, 2-step sequence)
- Send mode toggle (auto vs approval queue via Resend)
- Reply loop (IMAP + Resend webhook, Claude classifier, Slack push on positive)
- Streamlit dashboard (Queue, Pipeline funnel, Threads, Settings)

## Open

- [ ] Plan C build
- [ ] Sam to fill in track record blanks in SOP Section 5 (sister company markets + years)
- [ ] Sam to add Calendly link to SOP before 2026-05-07 VA meeting

_updated 2026-05-06_
