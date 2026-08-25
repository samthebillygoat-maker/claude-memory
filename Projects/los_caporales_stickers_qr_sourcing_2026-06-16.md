---
title: Los Caporales — Stickers & QR Codes: Sourcing, Cost, Lead Time
date: 2026-06-16
corrected: 2026-08-25
tags: [project, los-caporales, stickers, qr-codes, sourcing]
status: VENDOR RESEARCH VALID — but check laptop print docs first, they may already decide this
---

# Stickers & QR Codes — Where, How Long, How Much

## ⚠️ CHECK FIRST (added 2026-08-25)

This research was done against ~2-month-stale context. Per the vault's 2026-08-19
daily note, these files already exist **on the laptop** and may already settle the
print decisions below:

- `README-PRINT.md`
- `panel-print-brief.md`
- `DOMAIN-CUTOVER.md` ← **the new domain is in here**
- plus `brand.py`, `gen_menu.py`, `pieces.py`, `compact.py` (look like print/menu generators)

**Read those before ordering anything.** The vendor prices and lead times below are
still good reference, but do not re-litigate choices already made there.

Also relevant precedent: builds-operator already produced **QR leave-behind cards**
for the Livermore field kit (`Livermore-leave-behind-cards.html`, QR generated via
`api.qrserver.com`, script `scripts/livermore-fieldkit.mjs`). There is an existing
QR pipeline to reuse rather than invent.

Note: Los Caporales is now a **paying client** (first half paid ~2026-08-18), not a
spec mock — so print quality and correctness carry real reputational weight.

## ⚠️ Do NOT print until the domain is locked

A static QR code has the URL **baked into the pattern**. Print stickers pointing at
`los-caporales.vercel.app`, then cut over to the new domain, and **every sticker is
dead plastic** — reprint cost, plus customers scanning a broken code at the table.

Given `DOMAIN-CUTOVER.md` exists, a cutover is actively planned. That makes this a
live risk, not a hypothetical.

**Two ways to be safe:**

1. **Point the QR at our own domain (best — free, permanent, no subscription).**
   Encode `newdomain.com/m`, then control where `/m` redirects ourselves. The site
   is Next.js, so this is trivial — a redirect in `next.config.ts` or a route
   handler. Destination changeable forever, no third party, nothing to lapse.
2. **Dynamic QR service (fast, but a dependency).**
   - qrcode.ing — dynamic by default, editing + basic scan analytics free
   - TQRCG — 2 free dynamic codes that never expire
   - QRKIT — changing destination / renaming / folders free; advanced controls paid
   - Pageloot / QR Code Generator — dynamic requires a paid plan
   **Risk:** free tier changes or account lapses → QR dies. Option 1 avoids this.

**Option 1 is clearly right here** — we control the domain *and* the app.

## Sequencing (the order that avoids wasted money)

1. Lock the new domain (see `DOMAIN-CUTOVER.md`) ← blocking everything below
2. Fix the hero overlap; ship on that domain
3. Generate the QR against the final URL, **scan-test on a real phone**
4. Proof one sample sticker, scan-test the printed proof
5. Only then order the full run

## Stickers — vendors & real numbers

Vinyl QR stickers, waterproof + UV laminate (mandatory — restaurant tables get wiped
constantly; paper stickers will not survive):

| | What the sources say |
|---|---|
| Entry price | QR code stickers **from $35** |
| Bulk per-unit | as low as **$0.59 each** at volume |
| Standard turnaround | **5–7 business days** |
| Rush | **3–4 days** |
| Express | **1–2 days**; some vendors **1 business day**; 48HourPrint does 2-day w/ free shipping |

Vendors seen: Sticker Mule, StickerGiant, UPrinting, 48HourPrint, PrintPlace,
MakeStickers, PrintRunner, Sticky Brand, Vinyl Status, Stickerine.
- **Sticker Mule** — higher per-unit, low minimums (from 10 pcs), frequent promos →
  **best for the first proof run**
- **StickerGiant** — geared to US repeat business runs, rush options → **best for the real run**

## Table stands / tents

- Reusable acrylic QR standees **from ~$2.50/each** at volume
- Tiered example: 6 @ $12 ea · 12 @ $11 ea · 18 @ $10 ea · 24 @ $9 ea · 30+ = quote
- Range **$6.05–$46.20** each depending on customization
- Custom colors (non-black) often carry a **40-piece minimum**
- Amazon generic 12-packs of 4x6 table tents w/ QR insert = cheapest path if we just
  slide in a printed card

**Take:** flat vinyl stickers on tables + one acrylic stand at the register. Stands
are reusable — if the URL changes you swap the insert card, not the whole thing.

## ❗ Honest gaps — NOT fabricating these

Vendor sites are **blocked by this sandbox's network egress**, so no live quote pages
were pulled. Unknown, **not estimated**:
- Exact per-unit price at our real quantity (how many tables does the place have?)
- Real shipping cost + delivered-by date to Livermore
- Current promos

## Open questions

1. **New domain?** — likely already answered in `DOMAIN-CUTOVER.md`
2. **How many stickers?** tables + windows/register
3. **Who pays** — us as part of the deal, or the restaurant?
4. QR destination — homepage, or straight to the ordering/menu page?

## Sources
- https://www.namebadge.com/stickers/qr-code-stickers
- https://www.48hourprint.com/qr-code-stickers.html
- https://www.printplace.com/products/qr-code-stickers
- https://www.uprinting.com/qr-code-stickers.html
- https://www.makestickers.com/products/qr-code-stickers
- https://printreviewer.com/best-sticker-companies-of-2026-ranked-and-reviewed/
- https://www.stickerine.com/best-sticker-companies
- https://qrcode.ing/free-dynamic-qr-code
- https://useqrkit.com/edit-qr-code
- https://outweave.com/product/standees/reusable-acrylic-qr-code-table-top-standee-with-design/
- https://menushopworkshop.com/shop/45279848/acrylic-qr-table-stand
- https://www.amazon.com/Risch-Double-Sided-Hardback-Table-Tents/dp/B08QTCDGLN
