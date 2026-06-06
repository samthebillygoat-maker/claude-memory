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

## Sam's next steps (priority order)
1. **Deploy citysidestays.com to Vercel + domain** (unblocks everything; submit sitemap in GSC).
2. **List on Furnished Finder** (goldmine for travel nurses; ranks on Google where Airbnb listing never will).
3. **Max Airbnb internal ranking**: fill every field, Instant Book after 2-3 stays, <1hr response, low launch pricing to win first reviews.
4. Service-area GBP (not property-address — borderline ineligible for STR).
5. Build per-audience landing pages (travel-nurse, MacDill, monthly).

Related: [[airbnb_listing_tara_house_west_2026-06-06]], [[project_cityside_direct_booking_site_2026-06-03]].
