---
title: Los Caporales — Hero Overlap Fix (CORRECTED 2026-08-25)
date: 2026-06-16
corrected: 2026-08-25
tags: [project, los-caporales, websites, bug, fix]
status: BUG STILL OPEN — but my original diagnosis was WRONG, see correction
---

# Los Caporales — Hero Button Overlap

## ⚠️ CORRECTION (2026-08-25) — read this before the section below

The first version of this note was written against **stale, ~2-month-old context**
and its "where the file lives" section was **wrong**. Do not act on it.

**What I originally assumed (WRONG):**
> single self-contained `index.html` with inline CSS at
> `builds-operator\data\mocks\los-caporales\index.html`

**What is actually true**, per the vault's own daily notes for 2026-08-17/18/19:
Los Caporales is now a **full Next.js application**, not a static mock. Evidence —
these files appear as created/edited in those notes:
- `page.tsx`, `layout.tsx`, `globals.css`, `next.config.ts`, `not-found.tsx`
- `site-header.tsx`, `hero-slideshow.tsx`, `menu-browser.tsx`, `chat-widget.tsx`
- `checkout-client.tsx`, `status-client.tsx`, `tablet-client.tsx`
- `hours.ts`, `i18n.ts`, `robots.ts`, `sitemap.ts`, `route.ts`

Plus a real backend: **Neon Postgres** (`DATABASE_URL`, `create_caporales_db.js`,
DB-backed menu), **Stripe checkout** (`STRIPE-GO-LIVE.md`), online ordering
(`project_caporales_ordering_build_2026-08-17.md`), deployed to **Vercel prod**,
with a vitest suite.

It started life as a builds-operator mock — slug
`los-caporales-taqueria-1st-street-livermore-ca`, one of the 12 Livermore downtown
walk-in builds — but it has since become a **paid client project**. Per the
2026-08-19 note: *"he payed me first half yesterday, i want it fully done today so
i can go in tmw and collect other half."*

**So the hero markup is almost certainly in `hero-slideshow.tsx` / `site-header.tsx`
/ `page.tsx`, styled via `globals.css` (+ likely Tailwind) — NOT an inline `<style>`
block in a static file.**

## Laptop docs that already exist — READ THESE FIRST

Created 2026-08-19, on the laptop, **not committed to this vault**:
- `DOMAIN-CUTOVER.md` ← **the new domain is documented here**
- `README-PRINT.md`, `panel-print-brief.md` ← **print/QR work may already be decided**
- `HANDOFF.md`, `OWNER-GUIDE.md`, `STRIPE-GO-LIVE.md`, `panel-site-review.md`

Do not re-decide anything these already settle.

## The bug (still real — screenshot 2026-06-16, mobile)

In the hero, the red **"CALL TO ORDER"** button overlaps the **"OPEN DAILY · 9:30PM"**
text and the **"★ 4.3 · 550+ REVIEWS"** / **address** lines beneath it. Confirmed
visually from a phone screenshot; not yet re-confirmed against the current
deployment.

**First step for whoever picks this up: re-check the live site.** Given ~2 months of
heavy work since the screenshot, this may already be fixed. Verify before fixing.

## Fix approach (if still present)

Principle is unchanged; the location is not. Get the CTA buttons and the
hours/rating/address into **one normal-flow vertical stack with gaps**, and remove
whatever is causing the collision — typically `position: absolute`, a negative
`margin-top`, or a fixed `height` on the hero container that overflows on mobile.

In a Tailwind/Next component that usually means:
- the CTA wrapper → `flex flex-col items-start gap-3.5` (drop any `absolute`)
- the button row → `flex flex-wrap gap-3`
- hero container → `min-h-*` instead of a fixed `h-*`
- mobile → buttons go full width and stack: `w-full sm:w-auto`

Target order at 390px width, no overlap:
headline → subtext → buttons → OPEN DAILY · hours → ★ rating → address.

## Separate issue — honesty check on "★ 4.3 · 550+ REVIEWS"

Builds Operator's hard rule is no fabricated ratings/reviews. If that figure is not
pulled from the real Google listing, it must go. **Unverified either way** — flag it
during the same pass. On a paying client's live ordering site this matters more than
it did on a spec mock.

## Why this wasn't fixed from the cloud session

Sandbox egress blocks `los-caporales.vercel.app` and the source is on the laptop.
Both the site fix and the QR code were also gated on the new domain, which is in
`DOMAIN-CUTOVER.md` — on the laptop, not in this vault.
