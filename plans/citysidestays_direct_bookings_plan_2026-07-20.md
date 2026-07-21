# CitySide Stays — Direct Bookings Plan (2026-07-20)

**Goal:** Grow direct bookings on citysidestays.com to cut OTA fees (VRBO 5%, Airbnb ~15%) and own the guest relationship. Units: 558584 (Unit 28) + 558585 (Unit 18), Tampa, via Hostaway.

**Current live-site reality (verified):** citysidestays.com is a direct-booking *marketing* site, **inquiry-only** (form → email quote, "no payment now"). Gaps: no phone, no published prices, no reviews, no instant booking. Live source repo NOT yet located (the `~/projects/citysidestays-site` folder is a separate Twilio SMS opt-in page — do not edit that one).

**Chosen booking-engine approach: Option B — Hostaway API + Stripe, no monthly fee.** (Hostaway's native Booking Website is a paid Pro add-on — rejected.) Build real booking into the site via serverless functions calling Hostaway's public API + Stripe checkout. When building, route site work through the **FLUX FUSION panel** (Sam's directive). Rebuild vs enhance TBD once real source repo is found.

## Phase 1 — Fix conversion (prerequisite; do first)
- **Real booking engine (Option B):** serverless funcs `/api/availability`, `/api/quote`, `/api/book` → Hostaway API; Stripe Checkout for payment; keys server-side (Vercel env). Flow: pick dates → live quote → Stripe → Hostaway reservation created.
- **Trust stack:** import Airbnb/VRBO reviews + star ratings; real photos; **phone number**; "Licensed FL rental #DWE3914138"; secure-checkout badge.
- **Price-advantage banner:** "Book direct — same place, ~15% cheaper than Airbnb/VRBO." (Legit: no OTA fees.)
- Fill known gaps: phone, published price, reviews.

## Phase 2 — Convert guests already hosted (cheapest, highest ROI)
- Repeat-direct discount code (e.g. `CITYSIDE10`) in Hostaway **post-checkout** message + in-unit **QR welcome card / fridge magnet** → citysidestays.com.
- Post-stay email sequence via **Resend** (already wired): "Come back, skip the fees."
- Host the guidebook/house manual on citysidestays.com (drive guests to the domain during stay).
- Compliance: brand the stay + post-checkout contact only; never solicit off-platform before/during an OTA booking (delisting risk).

## Phase 3 — New traffic (scale once funnel converts)
- Google Vacation Rentals (already live) → confirm both units connect to the new booking engine so "book direct" transacts.
- Local SEO: "South Tampa furnished / short-term rental" page + Google Business Profile.
- Existing content/reels engine → CTAs to citysidestays.com (not the Airbnb link).
- Metasearch: Google free booking links via the direct rate.

**Build order:** Phase 1 → Phase 2 (parallel) → Phase 3. First build = Phase 1 booking engine + trust stack.

**Open item before build:** locate the live citysidestays.com source repo (or decide clean rebuild via FLUX FUSION panel).

See [[project_cityside_direct_booking_site_2026-06-03]], [[reference_vrbo_hostaway_setup_2026-07-20]].
