---
title: Builds Operator — Livermore Field-Sales Day
date: 2026-06-14
tags: [project, builds-operator, lead-gen, websites, livermore, sales]
---

# Builds Operator — Livermore Field-Sales Day (2026-06-14)

Shifted from overnight site-factory mode (see [[builds_operator_overnight_websites_2026-06-13]])
to **actively selling** the mock sites to Livermore businesses — by phone, in person, and email.
Built a pile of new bespoke sites for walk-in/lodging verticals + the full pitching toolkit.

Project root: `C:\Users\samth\projects\builds-operator`. Live preview base: **https://builds-previews.vercel.app/<slug>/**

## 🔥 Hot lead: STUDIO INN (interested!)
- Real budget motel: **1321 Portola Ave, Livermore · (925) 447-1515 · studioinnli@gmail.com** · no website (3.5★/65).
- Built a **full legit hotel site** (took time): **builds-previews.vercel.app/studio-inn-livermore-ca/**
  - Real Google photos (pulled via Places Photo API), working **two-month date-range BOOKING CALENDAR** (vanilla JS, range select → "call to confirm"), rooms, amenities, gallery, map, forest+brass boutique palette.
  - Honesty: omitted the 3.5★, "call for rates", footer "Proposed design".
- **Email DRAFTED in Sam's Gmail** (to studioinnli@gmail.com) — Sam clicks send. Covers site link, features, caveats (confirm amenities/rates), and **the big upsell**.
- **THE BIG UPSELL (reusable):** site's calendar is a UI mock → upsell = wire up **real 24/7 online booking + payments** (Cloudbeds/Lodgify). "Stop losing 2am bookings." Recurring-revenue angle.
- Pricing pitch: **$400 one-time** on own domain + booking integration as premium add-on.

## New Livermore sites built + deployed (all live)
**Downtown walk-in (12):** Los Caporales Taqueria, The Local Bar, Polomoni's Bar & Lounge, Railroad Saloon, Loard's Ice Cream, Temptation Nails & Spa, Eliambrose's Cut (barber), Old First Tattoo, JAKWEAR (streetwear consignment), Mimosa Nails, Pampered Poodle (grooming), Discount Cigarettes. Each a distinct per-niche aesthetic (manifest `data/build-manifest-livdt.json`, slugs like `los-caporales-taqueria-1st-street-livermore-ca`).

**Lodging + storefront (5):** Sands Motel (3787 First St) & Del Valle Lodge (3979 First St) — **hotel builds w/ booking calendar + real Google photos**, modeled on the Studio Inn file; Valley Furniture (2193 First St), Classical Clocks & Antiques (1082 E Stanley Blvd), East Ave. Cleaners (4074 East Ave) — bespoke storefront sites w/ real photos. Manifest `data/build-manifest-livshops.json`.

## Pitching toolkit (all in builds-operator)
- **Clickable call sheet:** `CALL-SHEET.html` (259 leads, tap-to-call `tel:` + tap-to-text `sms:` prefilled w/ pitch + preview link, notes col). Deployed private at **builds-previews.vercel.app/sam-callsheet-9f3kx/** (open on phone). Gen: `scripts/gen-callsheet.mjs`.
- **Google Voice:** import leads as Google Contacts → call/text through GV (925)315-7268. CSVs: `builds-leads-google-contacts.csv` (258) + `builds-leads-livermore.csv`. Gen: `scripts/gen-gvoice-csv.mjs`. ⚠️ GV rate-limits heavy outbound.
- **In-person field kit:** Google Maps walk-in route + printable **QR leave-behind cards** (`Livermore-leave-behind-cards.html`, QR via api.qrserver.com → each shop's preview). Gen: `scripts/livermore-fieldkit.mjs`.
- Ranking/filter scripts: `hot-leads.mjs`, `city-leads.mjs`, `real-vs-dispatcher.mjs`.

## ⚠️ KEY LEARNINGS (reuse these)
1. **Dispatcher / lead-gen filter (huge).** Many "no-website" Google listings for trades are **call-center fronts**, not real owners — calling them hits a dispatcher. Tells: generic geo+trade names ("Tree Service Livermore", "Edison Electricians of Livermore"), the repeated **"___ Door's Repair Service"** network across many cities, and **out-of-state area codes** on a local shop. Filter them OUT (`scripts/real-vs-dispatcher.mjs`). Prioritize **personal/family names + local area code (925/510/209) + physical storefront**. Auto shops, detailers, salons, restaurants, motels = real.
2. **Email-finding reality.** Small no-website businesses **rarely publish a verifiable email**. Google Places returns NONE. Web search **fabricates** them — Sands Motel repeatedly "resolved" to `reservations@sandsmotel.com` which is a **different motel in San Simeon**. NEVER send to an AI-summarized/guessed email. Get real emails by: **asking on the call/visit**, or their **Facebook "About" tab**. Email works best as *follow-up after* they've seen the site; phone/walk-in is the primary channel.
3. **Hotel-site recipe (reusable).** Pull real Google photos via Places Photo API (`scripts/fetch-studio-inn.mjs`, `scripts/fetch-shop-photos.mjs` → saves to `data/mocks/_<prefix>/`). Use `data/mocks/studio-inn-livermore-ca/index.html` as the **hotel template** (working date-range calendar). Look at photos before labeling rooms (don't call a parking lot a suite).
4. **Walk-in script:** "Are you the owner? I'm Sam, local — I build websites and noticed you don't have one, so I already built you a sample. Can I show you?" → pull up live link → "$400 to make it live on your own domain, it's yours either way."

## Open / next
- Send the Studio Inn Gmail draft; follow up by phone.
- Get emails by asking; then I draft Studio-Inn-style outreach instantly.
- Optional: QR leave-behind cards for the 5 lodging/storefront sites.
- Bigger play: build the **online-booking integration** offer as a real premium tier.
