# CitySide Guest Handbook — 2026-06-03

A world-class guest handbook for the two CitySide Stays units at **3216 W De Leon St, Tampa FL 33609** (North Hyde Park / South Tampa). Built from deep research, reality-checked, and shipped in two forms: a **web handbook** on the booking site and a **printable in-unit welcome card**. Related: [[cityside_direct_booking_site_2026-06-03]], [[tara_house_west_apt18_furnishing_2026-05-22]].

## What was built
- **Web handbook** — live-ready at the `/handbook` route on the site. Content lives in `C:\Users\samth\cityside-stays\lib\handbook.ts` (edit values there; a `fill("…")` value renders as a dotted "to add" pill — no code needed). Rendered by `app\handbook\page.tsx` (server component, `noindex`, brand-consistent: olive hero + sticky contents nav + cream body). `next build` passes; render verified in-browser (10 sections, 26 fill-pills, no raw markers leaked).
- **Printable welcome card** — `C:\Users\samth\cityside-guest-handbook\CitySide-Welcome-Card.html`. Self-contained 4×6 card, brand-styled, QR inlined as vector. Print: Ctrl/Cmd-P → Paper 4×6 in, Margins None, Background graphics ON.
- **QR code** → `cityside-stays\public\handbook-qr.{png,svg}` points to `citysidestays.com/handbook` (works once the site is deployed).
- **Source + research** in `C:\Users\samth\cityside-guest-handbook\`: full markdown handbook, `HOST-FILL-IN-CHECKLIST.md`, and `research\` (handbook anatomy, South Tampa local guide, public records, reality-check report).

## Public facts researched (baked in)
Pulled live from official city/county tools — not guessed:
- **Trash:** garbage **Tuesday & Friday**, recycling **Friday**, yard waste **Friday** (City of Tampa lookup).
- **Hurricane Evacuation Zone C** (Hillsborough/Tampa lookup).
- **FEMA Flood Zone X** — minimal hazard, not a Special Flood Hazard Area (FEMA NFHL).
- **Nearest fire station:** Tampa Fire Station 14, 1325 S Church Ave (~1 mi).
- ER = Tampa General (Davis Islands); license **DWE3914138**; full South Tampa local guide (SoHo Sushi ~2 min walk, Bayshore, Hyde Park Village, Bern's, Cuban spots, beaches).

## Key decisions
- **Privacy:** live secrets (door code, Wi-Fi password) deliberately kept OFF the public web page — shown as "sent in your check-in message" / "on the welcome card" — to match the homepage's "address shared after booking" posture. Can be inlined or gated later.
- **Format:** digital-primary (QR → branded page on the site you already own) + a thin printed card as the battery-free arrival fallback. This was the research-backed recommendation over Touch Stay/print-only.

## Still to do (host-only)
- Fill the **26 blanks** in `lib\handbook.ts` (door codes, Wi-Fi, parking, host phone, check-in/out times, appliance how-tos, safety-equipment locations) — see the checklist.
- Site go-live: Resend key + domain verification, real photos, Vercel deploy + DNS. See [[cityside_direct_booking_site_2026-06-03]].
- The web QR is only functional once the site is deployed.
