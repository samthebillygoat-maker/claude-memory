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

## Host fill-ins (captured 2026-06-21)
Sam provided the live values. Drop these into `lib\handbook.ts`. Two units: **#18** and **#28** at 3216 W De Leon St.

**Access & arrival**
- **Door code:** changes after every stay; delivered to guest the **morning of check-in** (keep OFF public web page — show as "sent the morning of your arrival").
- **Wi-Fi #18:** network `citysidestays18` / password `Citysidestays18` (capital C).
- **Wi-Fi #28:** network `citysidestays#28` / password `Citysidestays28` (capital C).
- **Parking:** spot = the unit number (#18 → spot 18, #28 → spot 28).
- **Host contact:** Sam's Google Voice number — ⚠️ **NOT on file in the vault, still needed.**

**In-unit how-tos**
- **Thermostat/AC:** nothing quirky — one **wall remote controls both AC units**.
- **TV:** smart TV + Fire TV, fully set up; guests sign in with their **own** streaming logins.
- **Laundry:** coin machines in **back-left of building** — **washer $2.75, dryer $1.75**.
- **Trash:** leave it in the unit (cleaner handles it). Guests *may* take it to the **dumpster in the back-right of the parking lot** but aren't required to.
- **Appliances:** no quirks, all self-explanatory.

**Safety**
- **Fire extinguisher:** under the kitchen sink (both units).
- **Smoke + CO detectors:** on the ceiling (both units).
- **Breaker panel:** to the **left of the fridge**.
- **Water shut-off:** to the **right of the stove** (water heater location).
- **First-aid kit:** under the sink.

**House rules**
- Quiet hours **10 PM – 8 AM**.
- **No smoking** anywhere on the property.
- **Pets:** case-by-case.
- **Occupancy:** max **4 guests overnight**; up to **6 in the unit** during the day but extras must leave by quiet hours.
- No pool / amenity rules.

## Still to do (host-only)
- ⚠️ **Need from Sam: Google Voice number** (the only remaining blank — everything else captured above).
- Apply the captured values to the **26 blanks** in `lib\handbook.ts` (on Sam's Windows machine — not in this repo).
- Site go-live: Resend key + domain verification, real photos, Vercel deploy + DNS. See [[cityside_direct_booking_site_2026-06-03]].
- The web QR is only functional once the site is deployed.
