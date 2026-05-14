---
name: Deal Engine
description: Top-of-funnel companion to Hail Mary. RentRadar (scrape + SMS) + Inbox-to-Lead (Gmail + AI extraction). $29/mo.
type: project
---

# Deal Engine

**Repo:** `C:\Users\samth\deal-engine\`
**Initial commit:** `21b0542` (2026-04-29)

## What it is
Two products under one $29/mo subscription:
1. **RentRadar** — saved searches scrape Craigslist / Zillow / Apartments.com every 5 min via Apify, SMS you on match (criteria: city, min beds, max rent, keywords like "sublet ok" or "airbnb friendly")
2. **Inbox-to-Lead** — Gmail OAuth → AI parses every "for rent" reply into structured Lead row (address, rent, beds, sublettable y/n, response time)

## Why it works
"Deal Engine finds them, Hail Mary analyzes them." Cross-sell: every Hail Mary user who runs out of deals to analyze becomes a Deal Engine prospect. Reuses 80% of DealScout's existing scraper logic.

## Stack
Next.js 16 + TS + Tailwind v4 (amber accent) • Clerk auth • Stripe $29/mo • Postgres via Prisma 7 • Apify (3 actors) • Twilio SMS • googleapis (Gmail) • Anthropic Claude • Vercel Cron

## Schema (6 tables)
User • Subscription • RentRadarSearch (saved criteria) • RentRadarMatch (unique by [searchId, url]) • GmailIntegration (OAuth tokens + historyId for incremental pull) • ExtractedLead (kanban: New/Contacted/Negotiating/Closed/Dead)

## What's working in commit 21b0542
- Cron route stubs at `/api/cron/{rent-radar,gmail-pull}` with header-based auth (`x-cron-secret`)
- `vercel.json` configures both crons (5 min + 10 min)
- Pure `src/lib/matching.ts` — testable listing-match function
- Gmail OAuth step 1 (`/api/gmail/connect`) is functional — builds Google consent URL with right scopes
- Gmail OAuth step 2 (`/api/gmail/callback`) is a 501 stub
- Dashboard layout with 4-tab nav (RentRadar / Leads / Inbox / Settings)

## Tomorrow morning
1. Clerk keys
2. Stripe $29/mo price + webhook
3. Supabase Postgres
4. Apify token + 3 actor IDs (Craigslist, Zillow, Apartments.com)
5. Twilio SID + auth + number
6. Google Cloud: enable Gmail API, OAuth web client, redirect URI `/api/gmail/callback`
7. Anthropic key
8. Generate random `CRON_SECRET`
9. Deploy to Vercel (crons need Vercel cron, not just `npm run dev`)

## Hard constraints
- All `/api/cron/*` routes MUST reject requests without `x-cron-secret` matching `CRON_SECRET` (already wired)
- Gmail tokens are sensitive — never log them, encrypt at rest if possible
- Don't scrape Airbnb here — that's Hail Mary's job. Deal Engine finds rentals to sublet, not existing STR listings.
- SMS budget: ~$0.008/msg via Twilio. At 1,000 matches/user/month worst case = $8 — rate-limit per search if needed
