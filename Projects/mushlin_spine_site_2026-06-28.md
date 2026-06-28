# Mushlin Spine — Website (2026-06-28)

Client: **Dr. Harry M. Mushlin, MD, FAANS** — Long Island academic spine neurosurgeon (Stony Brook).
Contact: **hmushlin@gmail.com** (the address he uses; NOT the @stonybrookmedicine.edu one).

## Where it lives
- Code: `C:\Users\samth\projects\mushlin-spine` (static HTML/CSS/JS, no build step). Pages: index, conditions, research, about, contact + privacy/terms/accessibility.
- Live: **https://mushlin-spine.vercel.app** (Vercel project `mushlin-spine`, CLI deploy: `vercel --prod --yes`).
- FLUX FUSION review scripts: `~/projects/flux-fusion/review-mushlin.cjs` (correctness/a11y) + `review-mushlin-ux.cjs` (UI/UX). Outputs saved as `flux-fusion-review-*.md` in the project.

## Design system — "Clinical Ivory + Surgical Steel"
paper #F6F4EF, ink #1C2024, steel #3E5C5A, clay CTA #A8623F. Newsreader serif + Spline Sans. Signature motif = the **spine**, rendered anatomically in 3 places: ambient background flow-spine (`#spineBg`, fills on scroll), the dark "Why Academic" section spine, and the interactive lateral-spine **explorer** (`#anatomySpine` + WAI-ARIA tablist).

## Work done this session
- Ran a FLUX FUSION UI/UX-elevation round (GLM+Kimi+DeepSeek → Opus judge). Applied: tabular stat figures, hero H1 widow/tracking fix, hanging blockquote, spacing/shadow/radius tokens, clay creds top-rule, ::selection, designed focus ring, staggered creds reveal.
- **Spine motif rework**: kept + upgraded the ambient background spine (more visible, with discs); replaced the ugly crosshair-glyph spines (rail + dark section) with real anatomical spines (curved bodies, gradient discs, sacrum). Explorer rebuilt with concave-endplate bodies, sheen/shade for depth, nuclei, facet nubs, region landmarks (7 cervical uncinate, 12 thoracic costal), thicker spinous blades.
- Fixed hero "Jump to" buttons (whole row clickable, not just the glyph).
- **Testimonials section** added (real reviews only): featured Healthgrades "mother's last hope" quote + cards (Rich Iannuzzi, Lauren Contino, a longer Healthgrades review) + a dark **Nev Schulman** (Catfish host) "notable patient" callout.
- Responsive QA (390/768/1024/1440): fixed credential strip not stacking on mobile/tablet, long-email word-wrap; added then later REMOVED the hero headshot (Sam: "looks bad" — face now only on About page + quote byline).
- New 400×500 headshot saved as `dr-mushlin.jpg` (About + byline); original tight crop kept as `dr-mushlin-sm.jpg` (byline circle).

## Facts corrected (verified)
- Title: **Director of Spine Surgery, Stony Brook Spine Institute · Associate Professor of Neurosurgery** — per Harry's own email. (I had wrongly "corrected" it to Director of Complex Spine and Deformity / Assistant Professor from US News/Healthgrades; reverted. Lesson: client's words > web directories.)
- Phone fixed site-wide **631-444-7328 → 631-444-1213** (the patient line on his SB provider page, all 3 offices).
- Offices confirmed correct as-is: **Riverhead · Lake Grove · Commack** (East Setauket worry was wrong).

## Sent to Harry (2026-06-28)
Emailed hmushlin@gmail.com the live link + asked him to confirm: phone, the title discrepancy (SB directory says "Clinical Assistant Professor"), the "4.9/177 Google reviews" figure, where form submissions should route + a public contact email, and a better photo — plus any UI/design tweaks. (Had to temporarily lift the `business-pulse/NO_SEND.flag` kill-switch to send, then restored it.)

## Still open (waiting on Harry)
- "4.9 / 177 Google reviews" figure UNVERIFIED (third-party shows lower/mixed) — confirm or remove.
- Where appointment-form submissions go (form currently falls back to "call the office", not wired to an inbox).
- Public contact email (JSON-LD currently uses harry.mushlin@stonybrookmedicine.edu — unconfirmed).
- His design/copy tweaks + possible better headshot.
- Custom domain (canonical/og currently point at the .vercel.app host).
