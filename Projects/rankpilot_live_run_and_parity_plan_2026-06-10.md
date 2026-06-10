---
type: project
project: RankPilot
date: 2026-06-10
tags: [rankpilot, airbnb, str, autorank, hostaway, pricelabs, plan]
---

# RankPilot — First Live Run + Final AutoRank-Parity Plan (2026-06-10)

Self-hosted replica of **AutoRank by Otamiser** ($850/mo Airbnb listing-optimization
tool). Repo: `C:\Users\samth\projects\rankpilot` (TypeScript, `npx tsx`).

## What happened this session

1. **Audited Sam's live Airbnb listing** (Boutique South Tampa 1BR · full kitchen,
   Airbnb `1701923259294423968`, 3216 W De Leon St) via Playwright. Real score ≈ **84/100**:
   strong copy + 17 pro photos + 48 amenities, and it already has a **booking (Jun 16–18)
   before any review** = strong early signal. Top fix: convert that first stay into a review.
   Audit saved at `C:\Users\samth\Documents\brain\claude-memory-main\listing_audits\2026-06-08_1701923259294423968.md`.

2. **Wired RankPilot to live keys.** `.env` now has Hostaway acct+key (token cached ~24mo)
   + PriceLabs key. AirROI SKIPPED (use Airbnb scrape for comps instead — Sam's call).
   - Hostaway IDs: **558584** ↔ Airbnb `1701923259294423968` (audited unit);
     **558585** ↔ Airbnb `1702759145847957725` (twin).
   - PriceLabs works: base **$112 → recommended ~$105**.

3. **🔴 Found the core bug.** First `run` scored a false **56/100**. Cause: Hostaway's
   record for an **Airbnb-natively-built** listing is a near-empty mirror —
   `listingImages:[]`, `listingAmenities:[]`. Only the 3398-char description blob (with
   "The space / Guest access / Other things to note" markers) + price sync through. So the
   engine scored an empty mirror, not what guests see.
   - **Fix = flip the READ source:** parse description sections from the Hostaway blob
     (no network) + scrape photos/amenities from the live Airbnb PDP; keep Hostaway for
     WRITE + reservations + price; PriceLabs for pricing. (Sam's instinct: Playwright, not paid AirROI.)

## Deliverable: the final parity plan (ready to hand to "Fable" = Claude's new model)

**Plan file:** `C:\Users\samth\projects\rankpilot\docs\superpowers\plans\2026-06-10-rankpilot-autorank-parity.md`

Self-contained, TDD, exact paths, real code, commit points, STOP-for-review checkpoints.
Built from a full read of the existing codebase. **9 phases:**

- **P0** git init + Playwright + fixtures
- **P1** trustworthy read source (description-section parser + Airbnb photo/amenity scraper + gather merge) — THE unblock, 56→~84
- **P2** comps + keyword gaps from Airbnb search (replaces AirROI)
- **P3** search-rank tracking over a query set, with history
- **P4** experiment log — correlates applied changes w/ rank/booking deltas (the validation loop)
- **P5** complete the 10-factor score: calendar hygiene, cancellation policy, instant-book, compliance
- **P6** weekly auto-refresh (AutoRank's freshness mechanic) with anti-thrash guard
- **P7** photo quality scoring + cover/reorder via `sharp`
- **P8** review mining (loved features + accuracy flags)
- **P9** scrape hardening (cache + rate-limit + proxy hook)

**Research-gated design (the key bit):** Phases 5–8 each OPEN with a mandatory RESEARCH task —
specific web searches → cross-check ≥2 sources → sourced findings doc in `docs/research/` →
encode every algorithm assumption as a named, tunable constant in `src/engine/weights.ts`
(no magic numbers). The Phase-4 experiment log then proves what actually moves rank, so the
weights self-correct toward Airbnb's real (unpublished) algorithm instead of freezing a guess.

**Handoff prompt:** "Execute the plan at docs/superpowers/plans/2026-06-10-rankpilot-autorank-parity.md
in C:\Users\samth\projects\rankpilot. Use superpowers:subagent-driven-development. Do Phase 0→9
in order, TDD. For Phases 5–8 complete the RESEARCH task + findings doc BEFORE coding. STOP at each
phase checkpoint. Dashboard out of scope."

## Status / next

- Plan is **ready to hand over as-is** (Sam chose: hand it over, let Fable capture its own fixture).
- RankPilot repo NOT yet git-init'd (Plan P0 does it first; `.env` is gitignored — verified).
- Known risks flagged in plan: Airbnb bot walls (has fallback+fixture+headless escape),
  Hostaway `getCalendar` field names (validate on first call), markup drift (pure-fn parsers + fixtures).
- Honest caveat: can match AutoRank mechanics, not the human revenue manager — Sam is that person.
- Dashboard (Next.js) still deferred to a later plan.

Related: [[project_airbnb_listing_tara_house_2026-06-06]] · [[cityside_seo_overnight_2026-06-06]]
