---
name: AirCheck
description: Existing-host listing optimizer. One Airbnb URL → 3 reports (comp-card, take-home calc, listing audit). $29/mo or $99 one-time. TAM ~10x arbitrage.
type: project
---

# AirCheck

**Repo:** `C:\Users\samth\aircheck\`
**Initial commit:** `7cc9f99` (2026-04-29)

## What it is
Paste your Airbnb URL → 60 seconds later you get three reports:
1. **Comp-Card** — 10 nearest comps, average ADR + occupancy, price-position verdict (underpriced / on-market / overpriced)
2. **AirCover Calc** — real monthly take-home after Airbnb 3% fee, cleaning, fixed costs, taxes
3. **ListingDoctor** — AI score 0-100 across title/photos/description/amenities/pricing + prioritized fix list with one-click rewrites

## Why it works
- TAM is **every Airbnb host**, not just arbitrage operators (~10× larger than Hail Mary's audience)
- One Apify scrape powers all 3 reports — fetch cost is the same whether selling 1 or 3
- Different buyer than Hail Mary — no cannibalization

## Pricing
- $29/mo unlimited audits
- $99 one-time per audit (`OneTimeCredit` row consumed by next audit)

## Stack
Next.js 16 + TS + Tailwind v4 (sky-blue accent `#38bdf8`) • Clerk auth • Stripe (2 prices) • Postgres via Prisma 7 • Apify Airbnb actor • Anthropic Claude

## Schema (4 tables)
User • Subscription • OneTimeCredit (for $99 buyers, `used` flag) • ListingAudit (single fat row: `scrapedJson` + comps fields + aircover fields + doctor fields, status enum pending → scraping → analyzing → complete)

## Working in commit 7cc9f99
- `src/lib/comps.ts` — `analyze(yourAdr, comps[])` returns price position + averages. Pure, testable.
- `src/lib/aircover.ts` — `takeHome(input)` computes monthly net after Airbnb 3% + cleaning per stay + fixed costs + taxes. Pure.
- `/api/audits` POST/GET stubs with full TODO flow spec
- `/api/audits/[id]` GET poll stub
- Dashboard with audit detail page showing 3 collapsible sections
- `/buy/single` $99 one-time entry page

## Hard constraints
- **One Apify fetch per audit.** Don't re-scrape per report — pass `scrapedJson` through to all three analyzers.
- ListingDoctor rewrites are AI-generated — mark as suggestions, not facts. User accept/reject each one.
- AirCover assumptions (3% Airbnb fee, occupancy, cleaning fee, tax rate) must be user-overridable in settings.
- Don't compete with Hail Mary's audience. AirCheck = **existing host optimizer**. Hail Mary = **arbitrage acquisition**.

## Tomorrow morning
1. Clerk keys
2. Stripe → `STRIPE_PRICE_ID_UNLIMITED` ($29/mo) + `STRIPE_PRICE_ID_ONE_TIME` ($99) + webhook
3. Supabase Postgres
4. Apify token + Airbnb actor ID
5. Anthropic key
6. `npx prisma migrate dev --name init`, `npm run dev`
