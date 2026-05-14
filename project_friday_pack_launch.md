---
name: The Friday Pack — Launch Plan
description: Hail Mary renamed to The Friday Pack (thefridaypack.com); ship Product A only Monday 2026-05-11, defer SaaS dashboard
type: project
---

# The Friday Pack — Launch Plan

Created 2026-05-08. Supersedes the launch portion of `project_hail_mary.md`.

## Brand

- **Name:** The Friday Pack (was "Hail Mary"). "Hail Mary" connoted desperation/long-shot — undercut a premium intel product. "The Friday Pack" creates a publication/ritual brand (Morning Brew model); customers anticipate a weekly Friday drop.
- **Domain:** `thefridaypack.com` purchased on Porkbun 2026-05-08. DNS not yet wired (Saturday task).

**Why:** premium positioning + ritual cadence beats lottery-ticket framing for a $97–$397 intel subscription.

## Stack

- Next.js 16 + Prisma 7 (driver-adapter `@prisma/adapter-pg`) + Clerk + Supabase (Postgres) + Stripe + Anthropic SDK + Apify
- Hosted on Vercel
- Repo: `C:\Users\samth\hail-mary\` (rename pending)

## Two products in one repo

- **Product A — Landing → Checkout → Manual Fulfillment.** Ship Monday 2026-05-11.
- **Product B — Full SaaS Dashboard** (`/dashboard/*`). Defer 2–3 weeks. Every dashboard route is currently a 4-line TODO stub, Clerk not wired (publicly accessible), no charts. Hide from prod for launch.

## Final pricing (locked 2026-05-08)

| Tier | Price | Bundle |
|------|-------|--------|
| Starter Pack | $97 one-time | unchanged |
| Weekly Pack | $147/mo | leads + **Call Script Playbook PDF** (LAIRC + Ackerman + objection rebuttals) — feels like a membership, not a bulk discount. Was $197; dropped under $150 mental cliff for conversion. |
| Pro | $397/mo | 100 leads/wk across **2 markets** + **Landlord Pitch Deck PDF** + monthly 30-min strategy call + direct Slack access. Stays at 2 markets; +1 market = $97/mo add-on. |

**Why Pro stays at 2 markets:** adding markets dilutes the "premium intangibles" positioning and worsens per-lead anchor. Top tier wins on intangibles, not volume. See `feedback_pricing_ladder_psychology.md`.

## Tonight's build fixes (2026-05-08 evening)

- Fixed broken `parseManualCsv` import in `src/lib/llm/extract.ts`.
- Deleted dangerous Stripe webhook stub at `src/app/api/stripe/`.
- Installed `@prisma/adapter-pg`, `pg`, `@types/pg`; rewrote `src/lib/prisma.ts` to driver-adapter pattern (lazy connection — build now passes with placeholder DATABASE_URL).
- Stripe account created tonight; `.env.local` template at `C:\Users\samth\hail-mary\.env.local` with all required keys.
- Stripe CLI download in progress (`stripe_1.40.9_windows_x86_64.zip`); installs to `C:\Users\samth\bin\` (created and added to user PATH tonight).
- **Stripe fully wired (2026-05-08 ~11:51 PM):** CLI installed + authenticated via `~/.config/stripe/config.toml`; 3 products created in test mode (Starter `price_1TV3xe…Eje7` $97 one-off, Weekly `price_1TV3z9…TUeo` $147/mo, Pro `price_1TV40X…DqBj` $397/mo); persistent webhook secret `whsec_11f789…2f3c` in `.env.local`; Customer Portal active (`bpc_1TV4cKKLrBV6fxlk4Ntpi030`) with cancel + payment-method update enabled. End-to-end smoke test passed: $97 Starter charged via `4242…4242`, webhook → `[NEW ORDER]` log → `/checkout/success` render.
- Dev server runs on **port 3001** (start with `npm run dev -- -p 3001`); `NEXT_PUBLIC_APP_URL` and webhook listener both wired to 3001.

## Saturday plan (2026-05-09)

**How to apply:** work this list top-down before any other Friday Pack work.

1. Provision Supabase project, paste real `DATABASE_URL`/`DIRECT_URL` into `.env.local`.
2. Wire Stripe webhook → Prisma (replace deleted stub with real handler).
3. Replace `window.prompt()` email capture with proper form.
4. Wire Resend for transactional email (receipt + Friday delivery).
5. Hide `/dashboard/*` routes from prod (middleware redirect or feature flag).
6. Fix `/order` checkout submit handler.
7. Rename "Hail Mary" → "The Friday Pack" across codebase (copy, metadata, package.json, README).
8. Deploy to Vercel.
9. Wire DNS at Porkbun → Vercel.
10. Customer Portal — enable **"Allow customers to update subscriptions"** (blocked tonight, retry in test mode portal settings).

## Sunday (2026-05-10)

- 24-hr soak + smoke test (real card $1 test purchase, webhook fires, email arrives, manual fulfillment sequence).

## Monday (2026-05-11)

- Ship Product A only. Announce.

## 2026-05-13 — post-launch fixes shipped

10-task punchlist run via subagent-driven-development (implementer → Playwright reviewer → fix loop). 18 commits + 1 follow-up (`a4e36fd`). All verified live at https://www.thefridaypack.com.

1. **Mobile lead-row collapse** — `grid-cols-12` now stacks to flex column <sm.
2. **Focus indicators** — `focus-visible` amber outline replaces blanket `focus:outline-none`.
3. **Lead-row legibility** — italic opener and meta line sizes/opacity bumped.
4. **Tap targets** — footer links hit 44px exact.
5. **Overflow** — `overflow-x: clip` on body, 1px scroller hunted.
6. **Pricing** — $97/$147/$397 everywhere; all $197 instances purged.
7. **Tampa top-5** — contiguous 01-05 (was 01,02,03,05,26).
8. **Hydration** — React #418 cleared; zero warnings in console.
9. **Opener variety** — PCB + Smokies top-5 rewritten signal-specific.
10. **Push** — production deploy + Playwright re-verify at 375px and 1280px.

### Launch promo LIVE (added 2026-05-13)

"First 10 Weekly subscribers get a free Starter pack delivered same week." Visible as top promo bar + Weekly tier badge on homepage. Tracked manually via Stripe Dashboard — when 10 Weekly subs land, remove the bar. State memo: `state_friday_pack_active_promo.md`.

### Stripe Customer Portal configured (live mode)

Plan switching enabled. "No proration" on downgrades + shorter intervals. Stripe Checkout as payment integration.

### Other artifacts

- `C:\Users\samth\Downloads\friday-pack-ig-story.png` — 1080×1920 IG Story asset (Fraunces, signal-amber, real Tampa lead). Pending post.

### Deferred (not blocking)

- Delete duplicate Vercel projects `the-friday-pack-e9sl`, `the-friday-pack-1vs4`.
- Real-card E2E test once card is funded.
- Next workstream Sam is transitioning to: social media + paid ads.

## Updated 2026-05-13
