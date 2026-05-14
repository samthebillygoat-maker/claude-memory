---
name: Operation Hail Mary
description: Brand-new SaaS — turns AirDNA Rentalizer screenshots into 20-page investor-grade STR arbitrage acquisition reports with built-in negotiation playbook. Separate codebase from DealScout/miami-arbitrage.
type: project
---

# Operation Hail Mary — v1 MVP

**Repo root:** `C:\Users\samth\hail-mary\`
**Spec:** `C:\Users\samth\Downloads\operation-hail-mary-prompt(4).md`
**Started:** 2026-04-29
**Owner:** Sam Lieberman / @Sam.lieberman1

## What it is
SaaS for STR arbitrage operators. User pastes a listing URL + uploads AirDNA screenshots → app extracts numbers via Claude vision → runs the acquisition formula → outputs a 20-page McKinsey-style PDF with verdict (GO/MAYBE/NO-GO), 3 scenarios (low/base/best), and a Voss/Ackerman negotiation playbook with calculated target rent + 4-offer sequence.

## Why
Target customer already pays for AirDNA but burns hours building deal analysis manually. This is the manual analyst replaced.

## Hard constraints (do NOT violate)
- **Separate codebase.** Do not pull from or modify `miami-arbitrage`. Fresh repo, fresh dir.
- **No AirDNA API integration.** Vision extraction from user screenshots only.
- **No market analytics / market browser / 3000-market expansion.** That's DealScout's territory.
- **No real-time auto-pipeline / "100 deals overnight."** v2 territory.
- **No team accounts, admin dashboard, mobile apps, Sentry/PostHog.** Post-launch.
- **No scrapers other than Apify Airbnb actor.** Other URLs fall back to manual entry form.
- **Vision is 95-98% accurate, not 100%** — always show editable confirmation step before report generation.

## Stack
Next.js (App Router) + TS + Tailwind • Clerk auth • Stripe (3 price IDs: $19 single, $97/mo founding, $147/mo standard w/ 7-day trial) • Supabase Postgres + Prisma + Storage • Apify (Airbnb actor) • Anthropic Claude vision (sonnet-4-5 or current) • React-PDF • Vercel deploy

## Pricing logic
- $19 single report (one-time, Stripe Checkout, no login required to buy → guest acct via magic link)
- $97/mo Founding Member — first 25 only, locked forever, hide once full
- $147/mo Standard — 7-day free trial, card required
- All subscriptions = unlimited reports
- DB tracks `founding_member_count`; homepage shows "X of 25 spots left" live

## Acquisition formula (constants for v1)
- OpEx 20% of revenue • Insurance $3k/yr • License $250/yr • Furnishing $500 startup • License/permit $250 startup
- `revToRentRatio = annualRevenue / (monthlyRent * 12)`
- Verdicts: ≥2.0x AND annualNet>0 = GO • ≥1.5x AND annualNet>0 = MAYBE • else NO-GO
- 3 scenarios per report: Low (-20% rev), Base (as-is), Best (+25% rev)
- Negotiation target rent = `annualRevenue / 24` (the 2.0x rent)
- Walk-away ceiling = `annualRevenue / 18` (the 1.5x rent)
- Ackerman sequence: 88% → 93% → 97% → 100% of target, non-round

## PDF spec — the centerpiece
20 pages, dark navy bg + purple accents (~`#9b87f5`) + white text, "looks like a McKinsey deck."
1. Cover (verdict + property) 2. Revenue projections + KPI tiles 3. Month-by-month 4-6. Low/Base/Best scenarios 7. Scenario comparison 8. Pro operator advantage (template) 9. Negotiation strategy + rent sensitivity 10-13. Negotiation guide (Voss tactics, mostly template) 14-15. Counter-offer playbook (Ackerman) 16. Deal at target rent 17. Profitability deep dive 18. P&L chart + seasonality 19. Regulation check (placeholder for v1) 20. Final recommendation
Header: "[USER] @[handle] · AI Airbnb Arbitrage" + section + page#. Footer: "Prepared by [User] · @handle · website"

## Build order
1. ✅ Next.js + TS + Tailwind + Prisma + Clerk + Stripe scaffold (commit `76cfc6d`, 2026-04-29)
2. ✅ DB schema (10 tables, Prisma client generates clean)
3. ⏳ Auth + 7-day trial Stripe flow + founding counter + single-report purchase
4. Apify (Airbnb) + scrape caching
5. Claude vision extraction + editable confirmation UI
6. Acquisition formula + scenarios
7. PDF report (React-PDF) — spend time here
8. Single deal flow E2E
9. Bulk flow (up to 30 URLs + grouped screenshots, parallel processing)
10. Leads pipeline
11. Homepage (How-It-Works fade-step infographic, sample report download, pricing w/ live founding counter, email capture)
12. Required pages + onboarding
13. Polish

## Tomorrow-morning setup checklist (real keys go here)
1. Clerk → publishable + secret
2. Stripe → 3 price IDs ($19 one-time, $97/mo, $147/mo w/ trial_period_days:7) + webhook → `/api/stripe/webhook` → signing secret
3. Supabase → `DATABASE_URL` + storage bucket
4. Apify → API token + confirm Airbnb actor ID
5. Anthropic API key
6. Drop into `.env`, run migrations, boot

## Cost-tracking rule
Log every Apify scrape, vision call, and PDF generation per user with timestamps — we'll set per-tier limits later.

## Next.js 16 quirks (gotchas for future sessions)
- **`middleware.ts` is renamed to `proxy.ts`** — file lives at `src/proxy.ts`. Docs: `node_modules/next/dist/docs/01-app/03-api-reference/03-file-conventions/proxy.md`. Currently inert; Clerk integration pending.
- **Prisma 7** — `url` and `directUrl` are no longer allowed inside `datasource db { }` in `schema.prisma`. They live in `prisma.config.ts` via `defineConfig({ datasource: { url } })`. Schema only declares `provider = "postgresql"`. The `directUrl` field isn't yet typed in Prisma 7's config type — set `DIRECT_URL` env separately if pgbouncer is used.
- **Tailwind v4** — CSS-first config. No `tailwind.config.ts`. Brand tokens defined via `@theme inline { ... }` in `src/app/globals.css`.

## Verification (as of commit 76cfc6d)
- `npx tsc --noEmit` → clean
- `npx prisma generate` → success
- `npm run dev` → ready in 799ms on http://localhost:3000
- Smoke test: `/`, `/dashboard`, `/buy/single` → 200; `/api/scrape` POST → 501 (correct, stub)
