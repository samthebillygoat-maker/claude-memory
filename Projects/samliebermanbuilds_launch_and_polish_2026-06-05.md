# samliebermanbuilds — Launched + Big Polish Pass (2026-06-05)

**🟢 LIVE: https://samliebermanbuilds.com** — Sam's personal builder-for-hire / lead-gen site. Pitch: *"custom websites, tools & automations for local businesses."* One-person shop, flat quote, shipped in days. Continuation of [[builder_portfolio_and_scholarship_pack_2026-06-04]] (the positioning pivot) — this is the site, built and shipped.

**Repo / stack:** `C:\Users\samth\projects\samliebermanbuilds` (renamed from `axion-studio` on 6/5). React 19 + Vite 8 + Tailwind 3.4 + framer-motion + lucide-react 1.17. Now multi-file: `src/App.tsx` + `src/sections.tsx` + `src/components/*` (MagicUI). Deploy: `vercel --prod` (CLI installed + authed as `samthebillygoat-3560`, Vercel project `samliebermanbuilds`).

## What shipped today (in order)
1. **Renamed** axion-studio → samliebermanbuilds, **deployed to Vercel prod**.
2. **Custom domain** `samliebermanbuilds.com` wired (registrar = **Porkbun**). Method: KEPT Porkbun nameservers, added `A @ 76.76.21.21` + `CNAME www cname.vercel-dns.com` (NOT nameserver swap — because Porkbun email forwarding needs Porkbun DNS). **SSL gotcha: Vercel didn't auto-issue — forced it with `vercel certs issue`.** HTTPS + http→https 308 all working.
3. **Email**: `sam@samliebermanbuilds.com` → forwards to samthebillygoat@gmail.com (Porkbun free forward; MX fwd1/fwd2.porkbun.com). Replaced the personal Gmail everywhere on the site.
4. **Pricing** section — "from $X" cards, anchors pushed LOW: Website $400 · Tool/automation $400 · Lead-gen $300 · Full product $1,500 · support $100/mo.
5. **Formspree** contact form (id `mnjynolp`) — replaced the broken `mailto`. Verified delivering to Gmail (checked via Gmail MCP).
6. Removed the Tampa live clock; added **Instagram @sam.lieberman1** + **Google Voice (925) 315-7268** (tap-to-call) in nav/footer/contact.
7. **Giant-wordmark footer** redesign (big "Sam Lieberman." + email/phone/IG row).

## The 5-agent audit → big polish pass
Ran 5 review agents in parallel (Reality Checker, UX Researcher, UI Designer, Accessibility Auditor, Growth Hacker/launch research), read-only. Sam's decisions, then implemented:
- **Hero = BLEND** (plain outcome lead-line added above the clever "pays for itself" H1).
- **Products section REFRAMED** → "What I can build for you" services menu (5 services). Dropped the 9 techy product modals a local owner couldn't relate to; kept ProjectModal only for the 3 real Featured builds + footer "this site".
- **Fonts** swapped system → **General Sans (display) + Inter (body)**, biggest de-template lever.
- **Launch additions:** FoundingBar (**first 3 BAY AREA clients, 30% off + free first month support**), named **guarantee** ("you see it working before you pay the balance — or you walk owing nothing"), **FAQ** (7 Qs in his voice). NO teardown lead magnet (skipped).
- **Favicon fixed** (was leftover Axion purple lightning bolt → SL mark). **OG/Twitter meta + 1200×630 /og.png** generated. Removed dead files (public/mock, sam.jpg, icons.svg, liquid-glass CSS).
- **Accessibility:** `<main>` + skip link, modal focus-trap + dialog semantics, cards `role=button` + keyboard, mobile-menu Esc/focus, global focus-visible ring, reduced-motion gate, contrast `#c2410c → #9A3412` everywhere, form aria-live + autocomplete + phone field + "what happens next".
- **Mobile** (Sam's repeated concern): sticky-stacking Featured cards now PLAIN STACK on phones; hero shortened + blockquote hidden; work-wall paused < 640px; footer wordmark wraps (no clip) + breathing orange period; dark Contact→Footer seam fixed. A dedicated mobile-audit agent verified at 390/320px = **SHARE-READY**; fixed founding-bar × overlap + footer tap targets.

## ⚠️ Sam is BAY AREA, not Tampa
His 925 area code + "first 3 Bay Area clients" → the builder business targets the **Bay Area**. All "Tampa" copy on the site → Bay Area. (His STR/CitySide work is still Tampa — separate thing.)

## Honesty guardrail
Only **The Friday Pack** (thefridaypack.com) + **CitySide Stays** (citysidestays.com) are truly-live client-style products. Everything else = his own builds, framed honestly. Still **ZERO real testimonials** — Growth agent's #1 remaining lever; Sam should land 1 named quote.

## In progress (as of end of session)
Sam is wiring **MagicUI components** into the site (installed `src/components/`: BorderBeam, MagicCard, DotPattern, AnimatedShinyText, Lens, ScrollProgress, StatsBand, NumberTicker; deps `canvas-confetti` + `tailwindcss-animate`). MagicCard already in the Services cards. App.tsx had unused-import build errors mid-integration — that's his live editing, not a regression to "fix."

## Follow-ups
- Land 1 real **testimonial** (draft-the-quote ask written this session).
- **Launch post** copy (IG caption + DM version, leading with founding offer) written this session — ready to paste.
- Optional www→apex primary redirect (Vercel dashboard).
- Rename Formspree form ("A New Form" → samliebermanbuilds).
- Tighten the hero paragraph (stops re-listing "websites/tools/automations" 3×) — queued, not yet applied.
- Porkbun free-trial email hosting auto-removes ~2026-06-20 (ignore).

Source-of-truth content/voice: `C:\Users\samth\projects\portfolio\POSITIONING-BRIEF.md`.
