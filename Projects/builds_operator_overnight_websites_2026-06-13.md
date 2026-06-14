---
title: Builds Operator — Overnight Bespoke-Website Factory
date: 2026-06-13
tags: [project, lead-gen, websites, builds-operator, automation]
---

# Builds Operator — Overnight Bespoke-Website Factory

Autonomous, self-healing pipeline that builds **bespoke premium mock homepages** for real
no-website local businesses, then deploys them to Vercel as a lead-gen pitch
("I built you a free preview — want it live?"). Runs unattended in waves of ~10 concurrent
agents, chaining batch after batch of 150 until I check in.

## Where it lives
- Project: `C:\Users\samth\projects\builds-operator` (TypeScript/tsx, filesystem-as-DB, JSON manifests)
- Mock sites: `data/mocks/<slug>/index.html` (one self-contained file each: inline CSS/JS, no frameworks)
- Live preview base: **https://builds-previews.vercel.app/<slug>/**
- Lead source: Google Places API (New) Text Search, `website===null` = no-site signal (key in `.env`, gitignored)

## How a site is built
Each site is a hand-built-looking ($500–1000) single-page design with:
- Real business **name / phone / address** + a live **OpenStreetMap iframe** (exact coords)
- Per-niche × 5-variant **aesthetic matrix** (rotating Google-font pairs, palettes, layouts) so no two look alike
- **Frozen local images** in `data/mocks/_img/<prefix>-NN.jpg` (20 niche pools) — a finalizer swaps ALL
  LoremFlickr `src`s to verified local files, killing CDN drift/outage risk
- A **reveal-safety-net** script (forces scroll-reveal content visible → no blank sections)
- Footer: **"Proposed design · samliebermanbuilds"**

## Honesty guardrails (hard rules)
NO fabricated reviews / ratings / testimonials / years-in-business / job counts / awards /
"#1 / top-rated / trusted by N". NO "licensed / insured / bonded / certified / warranty / guarantee".
"Free estimate/quote" is allowed. A final-pass **honesty grep** (licensed|insured|bonded|certified|
warranty|guarantee) is the backstop; flagged phrases get reworded (e.g. "Licensed-grade" → "Clean, careful work").

## The loop (per cycle, ~15 min)
1. `node scripts/overnight-status.mjs status`
2. Finalize completed builds: `inject-reveal-safety.mjs $U` + `finalize-all.mjs $U`
3. Deploy: `vercel deploy data/mocks --prod --yes` → aliased to builds-previews.vercel.app
4. Dispatch next 10 todo slugs as background general-purpose agents; `ScheduleWakeup 900s`
5. On batch complete → final pass + honesty grep + write `TRI-VALLEY-OVERNITE-CALL-SHEET-<n>.md`
   + **auto-chain** `start-next-150.mjs` (archives finished batch into `overnight-done.json`,
   finds+curates+spec-gens a fresh 150 with zero overlap), reschedule.

## Key scripts
- `find-overnight.mjs` — 22 cities × ~20 trades Places search; filters no-site + phone + in-target-city
  + not-chain (BLOCK regex) + deduped vs all prior batches
- `curate-overnight.mjs` — round-robins niches/cities, assigns variant, writes `build-manifest-overnight.json`
- `finalize-all.mjs` — swaps every image to local frozen pool by niche prefix
- `inject-reveal-safety.mjs` — idempotent visibility net
- `gen-spec-overnight.mjs` — writes `BUILD-SPEC-OVERNIGHT.md` (shared rules + 20-niche × 5-variant matrix)
- `overnight-status.mjs` — status / todo N / unproc / todocount
- `start-next-150.mjs` — the auto-chain

## Area expanded (vs. original Tri-Valley)
Livermore, Pleasanton, Dublin, San Ramon, Danville, Tracy, Mountain House, Manteca, Lathrop,
Brentwood, Oakley, Antioch, Pittsburg, Walnut Creek, Concord, Pleasant Hill, Martinez,
Castro Valley, Hayward, Union City, Newark, Fremont.

## Status (2026-06-13, ~11:30 PDT)
- **Batch 1: COMPLETE — 149 sites live + honesty-clean.** Call sheet `TRI-VALLEY-OVERNITE-CALL-SHEET-1.md` (149 leads, 21 cities).
- **Batch 2: in progress — 144 fresh leads, ~50 built so far.** Auto-chains to batch 3 on completion.
- Running total in flight: **~200 live sites**, growing each cycle until I check in.

## Mislabel / edge-case handling (watch list)
Places mis-tags some leads; caught + corrected so far:
- "A and A Billiards" tagged pool service → **dropped** (batch 1)
- "Aquatic Pool Service & Repair LLC" tagged **garage door** → fixed niche to pool service, deleted wrong file, **rebuilt** (batch 2)
- "VentPure Cleaners" (vent/duct) tagged window cleaning → kept (content still cleaning-themed)
- "La Canada Tree Service and certified arborist" → "certified arborist" kept ONLY in verbatim business name, no extra cert claims
- "Sherman Robert M" (personal-name sole-prop concrete) → reframed as "Robert M. Sherman — Concrete"
- No-number street addresses (e.g. "D St") → **city-only framing**, no street printed

## Fav 7 (showcase)
1. LV Hand Wash & Detailing — editorial Prata, IG-feed gallery
2. Delta Bay Concrete Cutting — cobalt+lime glow, diamond mark
3. Ace Auto Details — oxblood+mustard, story-ring IG grid
4. Jefferson Painting — Saira Condensed, sage dark+glow
5. Trees By Irish — bright airy, floating blobs, slate-blue/gold
6. All Volts (electrician) — cobalt+lime cursor-follow glow
7. Austin's Detailing — oxblood+mustard, 8-cell IG grid

## Legacy cleanup TODO (non-blocking)
Two older-template sites (Inter font, config-object, fabricated-review scaffold) still have honesty
violations and are out of the current manifest: `kirkpatricks-handyman-service-livermore-ca`,
`ryans-automotive-services-livermore-ca` (ASE-certified/warranty/bonded&insured). Plus demo
`joes-plumbing-tampa-fl` / `lux-hair-salon-tampa-fl`. Fix in a dedicated pass if these get pitched.
