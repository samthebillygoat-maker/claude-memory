---
name: STR SaaS Product Portfolio
description: 11 SaaS scaffolds on ports 3001-3011 with launch infra (launchpad, viewer, launch-all.bat); pivot/kill log
type: project
---

# STR SaaS Product Portfolio — 11 scaffolds on ports 3001–3011

Updated 2026-05-04. Supersedes the "5 consolidated" picture in `project_str_product_backlog.md` (which is now historical).

## Port map

| Port | Product | Status | Notes |
|---|---|---|---|
| 3001 | Hail Mary | live scaffold | landlord-acquisition cold-call SaaS |
| 3002 | AirCheck | live scaffold | listing audit (Comp-Card + AirCover + ListingDoctor) |
| 3003 | DealMemo | live scaffold | SMS deal memo generator |
| 3004 | Deal Engine | live scaffold | RentRadar + Inbox-to-Lead orchestrator |
| 3005 | SuperhostTracker | live scaffold | host metrics + SMS alerts |
| 3006 | ClaimDesk | new (pivot) | damage-claim workflow tool. Pivoted from ClaimWin after Airbnb Apr 20 2026 ToS update banned AI-generated evidence. Blocked: Anthropic API credit |
| 3007 | OrdinanceRadar | new | STR regulation monitoring. **Blocked: ordinanceradar.com domain not yet registered — blocking YC app** |
| 3008 | TrueComps | new | true Airbnb comp engine using Bianchi rule (271+ days available + 20+ reviews) |
| 3009 | AssessGuard | new | property-tax assessment monitor. Blocked: Anthropic API credit |
| 3010 | Damage Letter Tool | new | automated damage-letter generator. Blocked: Anthropic API credit |
| 3011 | str-vote | new | comparison tool |

## Launch infrastructure (`C:\Users\samth\call-tracker\`)

- `launch-all.bat` — starts all 11 dev servers
- `product-viewer.html` — iframe grid showing all 11 simultaneously
- `launchpad.html` — product index with copy-to-clipboard dev commands

**Why:** running 11 ports manually was slowing iteration. The launchpad is now the single entry point.

**How to apply:** when Sam says "spin up the portfolio" or names a port number, look here first.

## Pivots / kills log

- **2026-04-20 — ClaimWin → ClaimDesk.** Airbnb ToS update banned AI-generated evidence. Original product dead; repositioned as workflow/case-management tool, no AI evidence generation.
- **EU Reg ID — KILLED.** Spike showed government portals in Spain/Italy/Portugal/Greece are free or €27. Chekin already owns the lane. Don't reopen.
- **Verdict Terminal → Verdict Inbox** (re-pivoted; current shape).

## Action items blocking launch

- [ ] Buy `ordinanceradar.com` domain (blocks YC app)
- [ ] Top up Anthropic API credit (blocks ClaimDesk + AssessGuard + Damage Letter Tool)
- [ ] Mom-email task: clarifying question about her role still unanswered
