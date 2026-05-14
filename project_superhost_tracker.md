---
name: SuperhostTracker
description: Daily monitoring of Airbnb host metrics with SMS alerts before Airbnb demotes. $9/mo per listing. Sticky retention.
type: project
---

# SuperhostTracker

**Repo:** `C:\Users\samth\superhost-tracker\`
**Initial commit:** `20944d4` (2026-04-29)

## What it is
Daily Apify scrape of every active Airbnb listing → check against Superhost thresholds → SMS alert when a metric trends toward demotion. Hosts currently find out 3 months later when Airbnb removes the badge — by then it's a 90-day rebuild.

## Why it works
**Sticky retention.** "We caught it before Airbnb did" is a value claim that's verifiable monthly. Cancellation rate stays near zero.

## Stack
Next.js 16 + TS + Tailwind v4 (red accent — alert color) • Clerk auth • Stripe per-listing $9/mo (per-seat or metered billing) • Postgres via Prisma 7 • Apify Airbnb host stats actor • Twilio SMS • Vercel Cron daily 6am UTC

## Schema (5 tables)
User • Subscription (with `listingQuantity` for per-seat) • AirbnbListing • DailySnapshot (unique [listingId, capturedAt]) • Alert (severity warning/critical, `smsSentAt`, `resolvedAt`)

## Working in commit 20944d4
- `src/lib/thresholds.ts` — Airbnb's Superhost criteria codified as pure functions:
  - Response rate ≥ 90% (warning < 93%)
  - Overall rating ≥ 4.8 (warning < 4.85)
  - Cancellation rate < 1% (warning > 0.5%)
  - Trips/year ≥ 10 (or 100 nights / 3 trips)
- `/api/cron/daily-scrape` 501 stub with full TODO spec, gated by `x-cron-secret`
- `/api/listings` POST/GET stubs with quantity-enforcement TODO
- `vercel.json` cron at `0 6 * * *`
- Dashboard nav: Listings / Alerts / Settings

## Critical operational rules
- **Reverify Superhost thresholds quarterly.** Airbnb has changed them before. Source: airbnb.com/help/article/829.
- One DailySnapshot per listing per day (enforced by `@@unique`)
- Don't double-SMS: check unresolved Alert rows of same type before raising new one
- On subscription quantity decrease, deactivate oldest excess listings

## Tomorrow morning
1. Clerk keys
2. Stripe per-listing $9/mo (use per-seat pricing) + webhook
3. Supabase Postgres
4. Apify token + Airbnb host stats actor ID
5. Twilio SID + auth + number
6. Generate random `CRON_SECRET`
7. Deploy to Vercel (cron needs Vercel cron, not local dev)
