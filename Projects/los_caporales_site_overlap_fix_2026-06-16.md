---
title: Los Caporales Site — Hero Overlap Fix (QUEUED for laptop)
date: 2026-06-16
tags: [project, builds-operator, websites, los-caporales, todo, fix]
status: PENDING — apply on laptop, then redeploy to Vercel
---

# Los Caporales Site — Hero Button Overlap (fix queued)

**Site:** https://los-caporales.vercel.app
**Business:** Los Caporales — Taqueria / Mexican Food, 1316 Railroad Ave, Livermore
**Source file (laptop):** `C:\Users\samth\projects\builds-operator\data\mocks\los-caporales\index.html`
(single self-contained HTML file — inline CSS/JS, no framework)

## The bug (seen 2026-06-16, mobile screenshot)
In the hero section, the red **"CALL TO ORDER"** button is overlapping the
**"OPEN DAILY · 9:30PM"** text and the **"★ 4.3 · 550+ REVIEWS"** / **address**
lines below it. The button and the hours/rating/address text are stacking on
top of each other instead of sitting in a clean vertical stack — clearly visible
on a phone-width viewport.

## Why it's almost certainly happening
Typical cause in these single-file hero layouts (one of these):
- The hours / rating / address line is **absolutely positioned** (or pulled up
  with a **negative margin**) and collides with the CTA button row on narrow screens.
- The hero content box has a **fixed height** and the content **overflows** on mobile.
- The CTA row is a flex row with **no `flex-wrap` / no `gap`**, so items pile up.

## The fix (for laptop-Claude — do this with the real file open)
1. Open the index.html for `los-caporales` and find the hero CTA block (the
   `CALL TO ORDER` / `VIEW THE MENU` buttons + the `OPEN DAILY`, reviews, and
   address lines).
2. Wrap the buttons + hours + rating + address in a **single vertical flex
   column** and let it flow naturally:
   ```css
   .hero-cta {            /* whatever the actual wrapper is */
     display: flex;
     flex-direction: column;
     align-items: flex-start;   /* or center, match the design */
     gap: 14px;
     position: static;          /* kill any absolute positioning */
   }
   .hero-cta .btn-row {
     display: flex;
     flex-wrap: wrap;           /* buttons wrap instead of overlapping */
     gap: 12px;
   }
   ```
3. Remove any `position: absolute` / negative `margin-top` on the hours,
   reviews, or address lines that pulls them up under the button.
4. Remove any fixed `height` on the hero content container — use `min-height`
   so it grows with content.
5. Add a mobile guard so it always stacks on small screens:
   ```css
   @media (max-width: 600px) {
     .hero-cta { width: 100%; }
     .hero-cta .btn-row { flex-direction: column; align-items: stretch; }
     .hero-cta .btn-row a { width: 100%; text-align: center; }
   }
   ```
6. Verify at 390px width (iPhone) — no overlap, clean vertical stack:
   headline → subtext → buttons → OPEN DAILY · hours → ★ rating → address.
7. Redeploy: `vercel deploy data/mocks --prod --yes` (or whatever the
   builds-operator deploy step is) so los-caporales.vercel.app updates.

## Note
Exact class names will differ in the real file — match the actual markup.
The principle: get the buttons and the hours/rating/address into one normal-flow
vertical stack with gaps, and kill any absolute positioning / negative margins /
fixed heights that are causing the collision.
