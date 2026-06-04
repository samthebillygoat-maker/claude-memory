# Flip Scout — Skill + Launch Reel (2026-06-03)

## What it is
`/flip-scout "<city, ST>"` (or a zip) — a market-agnostic tool that finds distressed for-sale houses and scores each one **GO / MAYBE / NO-GO** for a flip. Built tonight, 30 passing tests. Lives at `C:\Users\samth\projects\flip-scout`.

## How it works (plain English)
1. **Finds** distressed inventory: foreclosures, bank-owned/REO, as-is, vacant, estate sales (via HomeHarvest MLS, any US market).
2. **Prices** the after-repair value (ARV) from recent sold comps.
3. **Scores** each house: max offer = (ARV × 65%) − rehab → GO / MAYBE / NO-GO vs the asking price.
4. **Reality-check** throws out junk: already-renovated (no spread), too few comps, no real margin.
5. Saves a ranked report to `data/flips_<market>_<date>.md`.

## First live run — Tampa
- 407 distressed listings scanned → 2 GO deals.
- Headline deal: **913 E 122nd Ave** — asking $179,900, ARV ~$484k (6 comps), est rehab ~$46k, max offer (70% rule) ~$268k.
- Rejected 10 others (already renovated / thin comps / no spread).
- ⚠️ ARVs skew optimistic (comp pool can include nicer homes) — always verify comps + get a real rehab bid before offering.

## The Instagram reel (built to advertise it)
- File: `C:\Users\samth\reelstack-reels\out\FlipScoutReel.mp4` (also copied to `Downloads\FlipScoutReel.mp4`).
- 20s, 1080×1920, Dark Cinematic (ReelStack), single terracotta accent, Geist type — premium/editorial, deliberately not "AI-looking."
- 5 beats: hook ("I built an AI that finds flip deals") → live terminal (`$ flip-scout tampa`) → the real deal card → "It threw out 10 others" (credibility) → **CTA: Comment "FLIP" / @citysidestays**.
- Rendered **silent on purpose** — add trending audio in the IG app (reach + licensing).

## Ties into
- [[project_arb_toolkit_2026-06-03|Arb Toolkit]] — flip-scout is a natural add to the distributable-skills bundle / Skool perk.
- Same HomeHarvest backbone as the STR lead pipeline.

## Caption posted with the reel
> Spent tonight building an AI that finds house-flip deals in any US market. You type a city — it scans every foreclosure, bank-owned, and as-is listing, pulls the comps, runs the 70% rule, and tells you GO or NO. First Tampa run: 2 real deals out of 407 — in under a minute. Comment **FLIP** 👇

## Open / next
- Tier B gov-REO scrapers (HUD/HomePath/HomeSteps) still stubbed — HUD is a reCAPTCHA-gated SPA needing browser automation.
- Tighten ARV comp quality (the top accuracy fix).
- flip-scout repo is local-only — push to GitHub if we want it backed up.
