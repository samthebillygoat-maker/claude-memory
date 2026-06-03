# CitySide Stays — Direct Booking Website (Build Handoff)

**Date:** 2026-06-03
**Status:** 🟡 Live preview deployed, paused for photo reshoot
**Project dir:** `C:\Users\samth\cityside-stays`
**Live preview:** https://cityside-stays.vercel.app (public, not on real domain yet)

---

## What this is
Lead-capture website for the 2 identical Tara House West STR units (Cityside Stays LLC, South Tampa). Guest submits a "Request to Book" inquiry → owner quotes/books manually. NOT a live booking engine (v1). Positioned nightly-to-monthly flexible.

## Stack
Next.js 14.2.35 (App Router) + Tailwind v3, deployed on Vercel (account `samthebillygoat-3560`, project `cityside-stays`). No database — email is the record. Spec at `docs/superpowers/specs/2026-06-03-cityside-direct-booking-design.md`.

## Design direction (locked + approved)
Boutique-hotel "Mediterranean editorial." Refs Sam gave: ritzcarlton.com, palisociety.com/hotels/tampa, hotelhaya.com.
- Fonts: **Cormorant Garamond** (display) + **Jost** (body) + **Marcellus** (Roman-caps labels/nav). Inter was removed — read as "AI."
- Signature motif: **arched image frames** (Hotel Haya doorway), `rounded-arch` token.
- Full-bleed alternating image/text bands, hairline rules, big airy serif headlines, generous whitespace.
- Understated CTAs: letter-spaced uppercase links w/ thin underline; ONE solid olive button (form submit only).
- Palette: olive #535A3E / cream #F3EEE3 / terracotta accent (used rarely). Film grain on dark bands.
- Footer shows FL DHR license #DWE3914138 (required).

## Units (both identical)
1BR / 1BA, sleeps 4 (queen + sofa bed), fully equipped kitchen (coffee bar, tea, knives, pots/pans, spices, soap). South Tampa, MacDill/Davis Islands adjacent. Address (private): 3216 W De Leon St, Tampa FL 33609.

## Verified working
Clean `next build`; homepage 200 (curl -i); inquiry API returns 400 (bad input) / 200 (bot honeypot) / 500 (graceful when no Resend key). Design + reality-check agents both run. Live URL public + rendering.

## Inquiry flow
Form → `POST /api/inquiry` → Resend sends (1) lead email to owner, (2) branded guest auto-reply. replyTo=guest, HTML-escaped, honeypot "company" field. Reads RESEND_API_KEY / OWNER_EMAIL / FROM_EMAIL from env.

---

## ⛔ RESUME HERE when photos arrive

### Photos (the blocker)
- Sam's photos come **GPS-stamped** by a map-camera app (burned-in date + "3216 W De Leon St, Tampa FL 33609" in a corner = the actual address, must be removed before public use).
- Files: 4032x3024, EXIF orientation=6 (browsers auto-upright). Bake with `PIL ImageOps.exif_transpose`.
- PIL wall-smear removes the stamp but leaves a faint seam (NOT pixel-perfect).
- **Best path: Sam reshoots with the GPS-stamp camera setting OFF** → clean originals, no editing. Else AI inpaint ("Remove the white timestamp/location text overlay; reconstruct the wall behind it; change nothing else").
- First batch: only **3 of 13** full-res arrived (bedroom/bathroom/livingroom). Living room cleaned + wired as hero (`public/images/hero.jpg`). Corrected originals in `incoming-photos/corrected/` (gitignored from Vercel via `.vercelignore`).
- **Shot list still needed:** each room wide (living/bed/bath/kitchen), styled kitchen+coffee bar, 2-3 detail vignettes, 1 exterior/entrance, 1 neighborhood. Both units. Landscape, daylight, lights on, decluttered.
- When they land: drop in `incoming-photos\`, then auto-rotate + crop to arched frames + color-grade + optimize WebP + swap `<Placeholder>` for real `<img>` in Hero/Units/Location/Gallery + content.ts.

### Email wiring (not done)
- Sam creates Resend API key named `cityside-stays` + adds domain `citysidestays.com` in Resend.
- Add to **Vercel → cityside-stays → Settings → Env Vars**: `RESEND_API_KEY`, `OWNER_EMAIL=samthebillygoat@gmail.com`, `FROM_EMAIL` (start `onboarding@resend.dev`, flip to `stay@citysidestays.com` after domain verifies). Do NOT paste key in chat.
- Then redeploy + send a real test inquiry to confirm inbox delivery.

### Domain go-live (not done)
- citysidestays.com registered at **Northwest Registered Agent / BusinessIdentity** (NS1/NS2.HOSTING.BUSINESSIDENTITY.LLC), reg to Cityside Stays LLC, exp 2027-04-06.
- DNS handoff: add `A @ 76.76.21.21` + `CNAME www cname.vercel-dns.com`, OR switch nameservers to Vercel. Batch Resend DKIM/SPF records in the same step. Then add domain in Vercel project + `vercel --prod`.

### Deferred to v2
SMS-to-owner via Quo/OpenPhone; live calendar + card payments; per-unit pages.

---
Related vault notes: tara_house_west_furnishing_decisions_2026-05-26, deleon_bathroom_analysis_2026-05-20. License: reference_fl_dhr_license_apt18_2026-05-25.
