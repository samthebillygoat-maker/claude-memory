# CitySide / South Tampa STR — SEO Work — 2026-06-06 (overnight, autonomous)

Sam asked to "get the Airbnb listing to #1 on Google for South Tampa stays," using agents + reality-checker, done solo overnight.

## Honest reframe (the core finding)
You CANNOT SEO an individual Airbnb listing URL to Google #1 — Airbnb owns that domain; SERPs are won by Airbnb category pages, Booking, Vrbo, Furnished Finder, hotels. The real levers:
1. **Airbnb internal search ranking** (conversion, Instant Book +15-25%, 100% field completeness, <1hr response, review velocity, calendar fullness, Guest Favorites path).
2. **citysidestays.com** — the only asset Sam can directly rank on Google.
3. **Furnished Finder + Google Business Profile** — high-intent channels that DO rank for the medical/monthly audience.

**Day-0 blocker:** citysidestays.com is NOT deployed (pending Resend key, DNS, Vercel). Zero ranking until live + indexed; then weeks-to-months. Deploy = highest leverage.

## Work done on `C:\Users\samth\cityside-stays` (build-verified, NOT a git repo — changes in working tree)
- Added metadata routes: `app/robots.ts`, `app/sitemap.ts`, `app/manifest.ts`
- `components/JsonLd.tsx` — JSON-LD: LodgingBusiness + FAQPage + Organization. No fake reviews, address city-level only, NO geo coords (privacy). FL license #DWE3914138 surfaced as PropertyValue.
- `app/layout.tsx` — keyword-optimized title ("Furnished South Tampa Rentals Near Tampa General & MacDill"), keywords array, canonical, robots meta, renders <JsonLd/>.
- `public/llms.txt` — AI-search summary.
- Honesty copy fixes: "full sofa bed"→"twin-size sofa bed"; "Fast Wi-Fi"/"Fast fiber"→"Wi-Fi throughout".
- `npm run build` passes clean; verified live robots.txt/sitemap.xml/9 schema types render.

## Deliverables in project
- `SEO-STRATEGY.md` (SEO Specialist agent) — keyword map (travel-nurse/medical = strongest moat via 5-min HCA walk), on-page plan, landing pages to build, Airbnb internal-ranking playbook, Furnished Finder + GBP, 30/60/90 checklist.
- `MORNING-REPORT-SEO-2026-06-06.md` — Sam-facing summary.
- `SEO-WORK-2026-06-06.md` — work log.

## Reality Checker agent (caught + FIXED 2 must-fix items)
1. 🔴 geo coord sat ~377m from real unit but comment claimed "neighborhood centroid" → removed geo entirely.
2. 🔴 "Fast Wi-Fi" edit half-applied (still on homepage) → fixed everywhere.
Confirmed: build passes, ZERO fabricated reviews/ratings, license real, strategy doc hype-free + honest on timelines.

## Round 2 (continued overnight) — landing pages + assets
- Built 3 SEO landing pages (build-verified, in working tree): `app/travel-nurse-housing-tampa/`, `app/macdill-tdy-lodging/`, `app/monthly-rentals/` via reusable `components/LandingPage.tsx`. Each: keyword title/meta, 1 H1, H2 sections, FAQ + BreadcrumbList JSON-LD. Honest guardrails held (on-site laundry, real drive times incl Moffitt ~20-25min, 2nd-floor walk-up, no "luxury", no invented price).
- Added all 3 to `app/sitemap.ts`; **linked them site-wide from `components/Footer.tsx`** (were orphaned).
- Split FAQPage out of global `JsonLd.tsx` → moved to `components/Faq.tsx` (homepage) so each page has exactly ONE FAQPage matching visible content (Google requirement). Verified clean on fresh build (a stale background `next start` briefly faked a dup during testing — cygwin pkill doesn't kill Windows node; kill port 3000 via PowerShell Get-NetTCPConnection/Stop-Process).
- Deliverable `LISTING-ASSETS-2026-06-06.md`: Airbnb photo captions (per real photos) + Furnished Finder listing copy (title/description/fields).
- Built `/south-tampa-guide` (link-magnet hub, honest local content, BreadcrumbList schema, internal-links all 3 audience pages) → sitemap + footer. Made LandingPage `included`/`faqs` optional + added `relatedLinks`. Build-verified (guide has NO FAQPage, correct). Deliberately SKIPPED `/the-apartment` (would cannibalize homepage intent).
- ⚠️ FLAG for Sam: `lib/handbook.ts` overclaims "steps from the SoHo strip / North Hyde Park" — unit is west South Tampa, SoHo is a short DRIVE. Soften (noindex page, but accuracy risk). Same walkability trap removed from Airbnb listing.

## Final Reality-Checker sweep — SHIP-READY
2nd RC agent audited all 4 new pages + LandingPage + listing-assets vs verified facts + ran build. ZERO must-fix. Walk-vs-drive correct everywhere, sleeps-4 qualified, MacDill disclaims GSA, no invented prices, no fake reviews, FAQ schema gated to visible FAQ. 5 confirm-items resolved via unit photos + conservative defaults: dishwasher TRUE (photo), tub-shower TRUE (photo), coffee=Keurig pods (fixed content.ts "grounds"→"pods"), "blackout curtains"→"soft linen curtains" (unverified), Bayshore superlative removed. Rebuilt green (15/15 static). All cityside-stays changes remain in WORKING TREE (not a git repo) — Sam reviews via MORNING-REPORT-SEO-2026-06-06.md.

## Sam's next steps (priority order)
1. **Deploy citysidestays.com to Vercel + domain** (unblocks everything; submit sitemap in GSC).
2. **List on Furnished Finder** (goldmine for travel nurses; ranks on Google where Airbnb listing never will).
3. **Max Airbnb internal ranking**: fill every field, Instant Book after 2-3 stays, <1hr response, low launch pricing to win first reviews.
4. Service-area GBP (not property-address — borderline ineligible for STR).
5. Build per-audience landing pages (travel-nurse, MacDill, monthly).

Related: [[airbnb_listing_tara_house_west_2026-06-06]], [[project_cityside_direct_booking_site_2026-06-03]].
