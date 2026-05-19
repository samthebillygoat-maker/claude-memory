---
name: friday-pack-tracker-v2-2026-05-15
description: Dark editorial tracker redesign matching thefridaypack.com — shipped CSS patch + A/B/C prioritizer (deferred wiring); 38-lead Miami preview
type: project
---

# Friday Pack Tracker — v2 Visual Redesign (2026-05-15)

The customer-facing weekly tracker HTML got a full visual overhaul so it stops looking like a generic developer-terminal output and starts looking like an editorial product worth the affiliate price.

## Why

- The v1 tracker (gradient navy banner, neon green pills, monospace everywhere) was indistinguishable from a debug dashboard. Sam's been running it himself, fine. But Tabare's affiliate launch (TABARE50, 1000+ students inbound — see `tabare_promo_swipe_kit_v3_2026-05-14.md` and `coach_intel_tabare_2026-05-14.md`) makes the tracker customer-facing for the first time. Every student opening it judges Friday Pack on what they see.
- The marketing site at `thefridaypack.com/samples/tampa` already nailed the brand: dark page, Fraunces serif headlines, deep-green CTAs, amber accent, hairline rules. The tracker was off-brand from the product it ships to deliver.
- Goal: tracker = same visual world as the landing page, so the affiliate funnel feels like one coherent thing from sign-up to first call.

## What changed

**Theme pulled from the live site via Playwright, not guessed.** Inspected computed styles on thefridaypack.com/samples/tampa to lock these tokens:

- Page `#0A0A0A`, surface `#121212`, inset `#1C1C1A`
- Primary CTA green `#1C3F2E` (hover `#26553E`)
- Amber accent `#E8A33D` for "WHY" highlights, links, focus rings
- Ivory text `#FAF9F6`, muted `#B0B0AA`, dim `#9A9A95`
- Hairline rules at 8% / 16% ivory alpha — never solid borders

**Typography:** Fraunces serif (300–500 weight, opsz 9..144) for H1 + owner names + rank numerals; Inter for body and labels; JetBrains Mono for phone digits and the "Score 95" tag. One Google Fonts request, preconnected.

**Layout:** CSS Grid named areas (`rank | head/owner/tags/addr | phone` with why/script/actions/notes spanning) replaced the flexbox stack. Rank is now a 60px Fraunces numeral in its own column instead of a pill.

**Components rebuilt:**
- Banner: bottom-rule only (no card), 68px Fraunces H1, wordmark with amber accent dot.
- Phone CTA: solid `#1C3F2E` squared rectangle, ivory mono digits, 44px min-height.
- Action buttons: ghost (transparent + 1px hairline), no color-coded variants — hover/focus = ivory border. (Final polish pass — see below.)
- `<details>` script block: inset surface with `+ / −` amber marker, uppercase summary.
- `.why` panel: inline text with amber `b` label instead of a tinted box.
- Squared corners everywhere (border-radius:0) — matches site's squared CTAs.

## Three parallel reviews (a11y / UI Designer / Reality Checker)

Spun three review agents in parallel after the first pass. Each caught real defects, all shipped fixes before final render.

1. **a11y reviewer** — caught:
   - Missing `:focus-visible` styles on every interactive (added 2px amber ring).
   - `.why` body text at 13.5px on `.amber-soft` failed WCAG AA contrast — bumped to ivory on transparent with amber-only label.
   - Phone CTA wasn't 44px min-height for touch target compliance — fixed.
   - Mobile action buttons too small for thumb hit area — `min-height:44px` at `<=820px`.

2. **UI Designer reviewer** — caught:
   - Phone CTA at 24px was so loud it competed with the H1; dialed to 16px (with mobile bumping back to 20px on stacked layout).
   - `.why` panel as a gold tinted box was the second-loudest element on the card after the phone — way too much. Reduced to inline text with amber label.
   - Score tag was using `.ok-soft` green which fought the primary green CTA. Switched to muted mono with bullet prefix.
   - Mono-font overuse was reading as "developer tool." Pulled mono back to phone digits + score tag only.

3. **Reality Checker reviewer** — caught:
   - **CSV export data-loss bug**: the v2 redesign had stripped the `data-rank`, `data-haspack` attributes from the card markup in an earlier iteration. JS exporter relies on these. Restored.
   - Status localStorage key would change format if we renamed any status string — preserved exact `setStatus` argument strings.
   - `<details>` open-state was being reset by a CSS animation. Disabled the animation on `[open]`.
   - "Loading polish hint" in `.controls::after` was rendering on print — added to `@media print` hide list.

## Final polish pass (after the three reviews)

- **Ghost-button conversion**: action buttons originally had color-coded variants (green=interested, blue=pitch sent, red=pass, vm=amber). On the dark theme this looked like Christmas. Collapsed all variants to a single ghost style — border becomes ivory on hover. The emoji prefix carries the semantic meaning.
- **Nav-strip removal**: an earlier draft had a top utility nav strip (Export | Reset | Help). Redundant with the controls row below; deleted.
- **Mono dial-back**: pulled JetBrains Mono off `.props`, `.status`, `.controls button` — kept it only on phone digits and the "Score NN" tag where the tabular feel is earned.

## Three artifacts in vault

- `friday_pack_tracker_v2_PREVIEW.html` — **NOT copied into vault** due to file size (~1962 lines / 53k tokens). Canonical render lives at `C:\Users\samth\Desktop\friday_pack_tracker_v2_PREVIEW.html`. To mirror into the vault, run from PowerShell:
  ```powershell
  Copy-Item C:\Users\samth\Desktop\friday_pack_tracker_v2_PREVIEW.html `
            C:\Users\samth\Documents\brain\claude-memory-main\friday_pack_tracker_v2_PREVIEW_2026-05-15.html
  ```
- [build_friday_pack_delivery_v2_2026-05-15.patch.md](build_friday_pack_delivery_v2_2026-05-15.patch.md) — patch instructions for `scripts/build_friday_pack_delivery.py` (CSS swap + 5 micro-tweaks).
- [prioritize_pack_2026-05-15.py](prioritize_pack_2026-05-15.py) — A/B/C priority ranker; signals: portfolio (max CL listings vs county parcels, capped 10, ×6pts), LLC/entity (12pts), absentee phone area code (10pts), multi-phone (4pts), county-confirmed (3pts). Tier cutoffs A>=30, B>=15, C<15.

## DEFERRED — next session

1. **Wire `prioritize_pack.py` into `build_friday_pack_delivery.py`**:
   - Replace the existing `rows.sort(...)` call with `sort_by_priority(rows, enrichment)` from the new module.
   - Call `rekey_enrichment(before, after, enrichment)` so enrichment lookups still match the new rank order.
   - Swap the rendered `<span class="score-tag">Score NN</span>` for `<span class="score-tag tier-{tier}">{tier_label(tier)}</span>` (CALL FIRST / STRONG / OPPORTUNISTIC).
   - Add CSS for `.score-tag.tier-A` (amber), `.tier-B` (ivory), `.tier-C` (dim) so tier reads at a glance.
2. **66-lead merged pack not yet rendered**: `broader_harvest` (38 Miami) + `zumper_harvest` (28 Miami, 17 with phones — see `project_zumper_harvest_2026-05-14.md`) need merge-dedupe-render through the v2 pipeline. Owner-collapse logic must dedupe across both sources.

## Source-of-truth files

- Build script: `C:\Users\samth\projects\landlord-outreach\scripts\build_friday_pack_delivery.py`
- Zumper scraper: `C:\Users\samth\projects\landlord-outreach\scripts\zumper_harvest.py`
- Broader scraper: `C:\Users\samth\projects\landlord-outreach\scripts\broader_harvest.py`
- Live design reference: `https://thefridaypack.com/samples/tampa`
