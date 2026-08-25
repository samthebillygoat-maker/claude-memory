---
title: Los Caporales — Stickers & QR Codes: Sourcing, Cost, Lead Time
date: 2026-06-16
tags: [project, los-caporales, stickers, qr-codes, sourcing, builds-operator]
status: RESEARCH DONE — blocked on final domain before anything gets printed
---

# Stickers & QR Codes — Where, How Long, How Much

## ⚠️ Read this first: do NOT print until the domain is locked

Sam said 2026-06-16 that Los Caporales is moving to **a new domain** (name not yet
captured — see Open Questions).

A normal ("static") QR code has the URL **baked into the pattern**. If we print
stickers pointing at `los-caporales.vercel.app` and then move to the new domain,
**every sticker becomes dead plastic.** Reprint cost + the restaurant looks broken
to customers scanning a table.

**Two ways to be safe:**

1. **Point the QR at our own domain (best — free, permanent, no subscription).**
   Encode something like `newdomain.com/m`, then control where `/m` redirects
   ourselves. Destination changes forever, no third party, nothing to lapse.
2. **Dynamic QR service (fast, but a dependency).** The code points at the
   service's short link; you edit the destination in their dashboard.
   - qrcode.ing — all codes dynamic by default, editing + basic scan analytics free
   - TQRCG — 2 free dynamic codes that never expire
   - QRKIT — changing destination / renaming / folders free; advanced controls paid
   - Pageloot / QR Code Generator — dynamic requires a paid plan
   **Risk:** if the free tier changes or the account lapses, the QR dies. Option 1
   avoids this entirely. Prefer option 1 since we already own a domain.

**Bonus of both:** scan analytics = proof for the client that the site is working.

## Sequencing (the order that avoids wasted money)

1. Lock the new domain ← **blocking everything below**
2. Fix the hero overlap + ship the site on that domain
3. Generate the QR against the final URL, **scan-test it on a real phone**
4. Proof one sample sticker, scan-test the printed proof
5. Only then order the full run

## Stickers — vendors & real numbers

Vinyl QR stickers, waterproof + UV laminate (needed — restaurant tables get wiped
constantly; plain paper stickers will not survive):

| | What the sources say |
|---|---|
| Entry price | QR code stickers **from $35** (namebadge) |
| Bulk per-unit | as low as **$0.59 each** at volume |
| Standard turnaround | **5–7 business days** |
| Rush | **3–4 days** |
| Express | **1–2 days**; some vendors **1 business day**; 48HourPrint does 2-day w/ free shipping |

Vendors seen: Sticker Mule, StickerGiant, UPrinting, 48HourPrint, PrintPlace,
MakeStickers, PrintRunner, Sticky Brand, Vinyl Status, Stickerine.
- **Sticker Mule** — higher per-unit, but low minimums (from 10 pcs) and frequent
  promo deals → **best for the first proof/sample run**
- **StickerGiant** — geared to US repeat business runs, rush options → **best for the real run**
- Both start as low as 10 pieces, so a cheap proof before committing is easy

## Table stands / tents (if we want more than a flat sticker)

- Reusable acrylic QR standees **from ~$2.50/each** at volume (Outweave)
- Tiered example: 6 @ $12 ea · 12 @ $11 ea · 18 @ $10 ea · 24 @ $9 ea · 30+ = call for quote
- Range **$6.05–$46.20** each depending on customization
- Custom colors (non-black) often carry a **40-piece minimum**
- Amazon has generic 12-packs of 4x6 table tents w/ QR insert — cheapest path if we
  just slide in a printed card instead of custom-printing the stand

**Take:** flat vinyl stickers on the tables are cheapest and fastest. Acrylic stands
look more premium and are reusable — if the URL ever changes you swap the insert
card, not the whole thing. For a taqueria, stickers on tables + one stand at the
register is probably the right mix.

## ❗ Honest gaps — NOT fabricating these

Direct vendor sites are **blocked by this sandbox's network egress**, so I could not
pull live quote pages. The following are **unknown, not estimated**:
- Exact per-unit price at our real quantity (how many tables does Los Caporales have?)
- Real shipping cost + delivered-by date to Livermore
- Whether any current promo applies

To close these: open the vendor sites and run the real quote configurator, or
allowlist the hosts so I can pull them.

## Open questions for Sam

1. **What is the new domain?** Blocking the site fix AND the QR code.
2. **How many stickers?** i.e. how many tables + windows/register. Drives all pricing.
3. **Whose spend is this** — are we eating the cost as part of the pitch, or is the
   restaurant paying? Changes how premium we go.
4. Where does the QR point — homepage, or straight to the menu?

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
