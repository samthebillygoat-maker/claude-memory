---
name: project_cityside_googlevr_northwest_2026-06-30
description: "CitySide Stays — Google Vacation Rentals is LIVE via Hostaway booking engine; the citysidestays.com redesign SOURCE lives in the \"Northwest\" platform, not a local repo."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1f2c4af5-05a9-4bc1-9d93-e85a520f10fd
---

**Google Vacation Rentals — DONE (2026-06-30).** Both units (Hostaway 558584/558585) are `googleExportStatus: exported`. Achieved by publishing the Hostaway **booking engine "Cityside Stays" (id 26034)** — it was DRAFT; Google VR activation failed with "listing not linked to a published booking engine" until the engine was published. Engine: `isPublished:1`, `isActiveForGoogleVR:1`, `listingMapIds:[558584,558585]`, Stripe connected (`acct_1TV2zzKLrBV6fxlk`), default subdomain `200456-001.holidayfuture.com` (no custom domain — Sam said not needed for Google). `googleVrListingUrl` still null = Google still ingesting (days–2wk). A duplicate draft engine "citysidestays.com" exists — ignore/delete it.

**Still TODO in Hostaway (need stable Playwright dashboard):** brand engine 26034 with the new logo + olive/cream colors; set the Google channel company name="Cityside Stays" + logo (Google brand approval ~2wk); connect **Vrbo** (Channel Manager→Vrbo→Configure, then Vrbo approves over days — content already staged); Booking.com/Expedia need their own OTA onboarding. Only Airbnb + Google are connected.

**WHERE THE SITE SOURCE LIVES (the thing I kept hunting for):** the live citysidestays.com **Next.js redesign is built/stored in an external platform Sam calls "Northwest"** (agents/website builder). It is NOT on this machine, NOT in GitHub `samthebillygoat-maker`, and NOT in the visible Vercel project (`citysidestays-site` prj_ubfZdDrc2ACEVFAviXjTpx2k4t7H only serves the OLD static landlord page on *.vercel.app). The domain/DNS for citysidestays.com is managed in Northwest's control panel. To edit the site, get the source out of Northwest (export to a repo) or apply changes there.

**Brand palette (from live site):** olive `#2B2F20`/`#3A3F2B`, cream `#F3EEE3`, ink `#26241D`, terracotta `#BF6B43`. **Logo made** → `~/Downloads/cityside-logo/`. **Site change-spec** (FLUX + agents) ready → `~/Downloads/citysidestays-site-changes.md`. See [[feedback_tara_units_short_stay_not_nurse]] and [[project_cityside_direct_booking_site_2026-06-03]].
