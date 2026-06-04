# CitySide Stays — Brand System + 20-Reel Batch (2026-06-04)

Built a full editorial brand + a 20-reel content engine in `C:\Users\samth\reelstack-reels`.

## Brand decisions
- **Two-account structure (important):** `@citysidestays` = **guest booking brand ONLY** (units, neighborhood, reviews, "book direct"). Do **NOT** post arbitrage/tools/education there — it confuses guests and kills booking conversion. Arbitrage + the tool products live on a **separate personal/creator account** (Sam as operator) and/or each product's own handle.
- **Palette (from the live site `tailwind.config.ts`):** cream `#F3EEE3`, olive `#535A3E` / deep `#2B2F20`, terracotta `#BF6B43` / deep `#7E4225`, ink `#26241D`. Fonts: Cormorant Garamond (display), Marcellus (labels), Jost (body).
- **Logo system** (in `reelstack-reels/out/` + `Downloads/`): avatar = cream **arched-doorway + keyhole** mark on olive (`citysidestays-avatar.png`); header = arch mark over **CITYSIDE / STAYS** lockup (`citysidestays-logo.png`). 5 matching highlight covers in `out/highlights/`. Editorial, NO AI-mograph look (Sam rejected glow/iridescent/particle).

## Product handles (locked unless noted)
- CitySide Stays (STR guest) → **@citysidestays**
- FlipScout (house-flip finder) → **@flip.scout**
- Friday Pack (STR lead packs) → **@the.fridaypack**
- Reply tool → renamed **Replyflow** → **@replyflows** (replyguy/replyflow/replai were taken)
- Job-app tool → named **OfferBandit** → **@offerbandit**
- **Parent / family brand: UNDECIDED** — options floated: Scoutworks (rec), Bandit Labs, Prospect Labs, Sidequest.

## Reel engine
- `src/editorial/EditorialReel.tsx` — data-driven cream/olive engine. Scene types: title, stat, steps, list, quote, cta. Palette `E`, fonts via `designSystem.ts` (`ds.font.display` Cormorant, `ds.font.label` Marcellus, added via @remotion/google-fonts).
- `src/editorial/specs.ts` — `SPECS: ReelSpec[]` = **20 reels**. `Root.tsx` maps SPECS → Compositions. IDs must be hyphen/alnum only (no underscores — Remotion rejects).
- Render: `npx remotion render <id> out/<id>.mp4 --concurrency=2`; output buffers to end; first render re-bundles fonts. ffmpeg at `~/bin`. Batch copies to `C:\Users\samth\Downloads\citysidestays-batch\`.

## The 20 reels
- CitySide guest ×3: CS-StaySouthTampa, CS-BookDirect, CS-Neighborhood
- Arbitrage ×4: ARB-DontNeedToOwn, ARB-TheNumbers, ARB-Mistakes, ARB-IsItLegal — **currently tagged @citysidestays; move to personal handle + re-render once chosen**
- FlipScout ×3: FS-FindTheFlip, FS-SeventyRule, FS-StopGuessingARV
- Replyflow ×3: RG-RepliesBeatPosts, RG-WhatHits, RG-GrowFromZero
- OfferBandit ×3: JA-StopMassApplying, JA-SixSeconds, JA-FollowUp
- Friday Pack ×4: FP-WhatItIs, FP-StopScraping, FP-Quality, FP-FirstCall

## Bios
- **@citysidestays (guest):** "Furnished stays in South Tampa 🌿 / Walk to Bayshore · Hyde Park · MacDill / Book direct ↓ better rate than Airbnb" → citysidestays.com
- **Personal/creator:** "I rent apartments I don't own — and profit 🏠 / STR arbitrage operator · 2 units in Tampa / Comment LEASE for the playbook ↓" → links to the.fridaypack / flip.scout

## Open items
- [ ] Pick personal/creator handle → retag 4 arbitrage reels + re-render
- [ ] Pick parent family brand name
- [ ] Verify all handles available on IG; swap + re-render any taken
- [x] Reality-check pass — all 20 render clean; hooks + CTAs + handles verified via contact sheets (2026-06-04). All 20 MP4s in `Downloads/citysidestays-batch/`. (FS-FindTheFlip failed once in-batch on a mid-edit race, re-rendered fine.)
