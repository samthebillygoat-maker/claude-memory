---
name: launch-superhost-tracker-2026-05-13
description: SuperhostTracker launch run — Phases 1-4 complete, awaiting Sam for Phase 3 finish + 5 + 6 + 7
type: project
---

# SuperhostTracker Launch Log — 2026-05-13

## Status: 4 of 7 phases complete; awaiting Sam-side actions

## Phase status

| # | Phase    | Status | Notes                                                        |
|---|----------|--------|--------------------------------------------------------------|
| 1 | SCAFFOLD | ✅     | Audit complete, gaps documented and addressed in P3/P4       |
| 2 | INFRA    | ✅     | Supabase live, schema pushed, Clerk test keys, CRON_SECRET   |
| 3 | PAYMENTS | 🟡     | Schema + webhook + cron CODE done; live Stripe prices pending |
| 4 | CONTENT  | ✅     | Homepage 2-tier, 4 legal pages, emails, SMS — review-gated   |
| 5 | EMAIL    | ⏸️     | Awaits Resend domain add + Namecheap DNS                    |
| 6 | DEPLOY   | ⏸️     | Awaits vercel link + env var paste                          |
| 7 | VERIFY   | ⏸️     | Awaits deploy                                                |

## Commits this run (local, not pushed)
- `2b7b4fd` Fix homepage: remove fantasy data-storage claim + stale per-listing FAQ
- `0af28be` Fix webhook idempotency race + speculative-write guard for sub.updated
- `85829bf` Fix Prisma 7 client constructor — add pg driver adapter
- `5fe00ac` Fix Prisma 7 config typecheck
- `703c12d` Phase 3: two-tier pricing schema + webhook + cron implementation
- (Phase 4 commit prior) two-tier pricing + legal pages + email/SMS templates

## Review gate outcomes
- **Phase 3+4 Code Reviewer:** FAIL → retry #1 PASS (3 critical issues fixed)
- **Phase 3+4 Reality Checker:** PASS (Playwright screenshots verified homepage, 4 legal pages, 404 on invalid slug, .legal-prose styling)

## Anti-patterns avoided (verified by review)
1. Speculative-write guard in webhook (both checkout.session.completed AND customer.subscription.updated re-fetch from Stripe)
2. Idempotency via insert-first + P2002 catch (race-safe)
3. Named skip counters in cron (not aggregate skipCount)
4. Per-listing incremental save in cron
5. `smsSentAt` only set after Twilio success
6. Twilio import hoisted to module scope (not per-alert)
7. Diagnostic admin endpoint at /api/admin/scrape-status

## Outstanding decisions / actions for Sam

### Phase 3 finish (Stripe live prices)
1. Log into Stripe live mode (top-right toggle, no orange test banner)
2. Create Product "SuperhostTracker Single" → recurring $9/mo → copy price_xxx
3. Create Product "SuperhostTracker Unlimited" → recurring $19/mo → copy price_xxx
4. Paste both into `.env` as:
   - `STRIPE_PRICE_ID_SINGLE=price_xxx`
   - `STRIPE_PRICE_ID_UNLIMITED=price_xxx`
5. Get live Stripe keys (from Friday Pack, same account):
   - `STRIPE_SECRET_KEY=sk_live_...`
   - `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...`
6. After deploy: register webhook at `https://<vercel-url>/api/stripe/webhook` for events `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.payment_failed`
7. Copy webhook signing secret → `STRIPE_WEBHOOK_SECRET=whsec_xxx`

### Also still needed
- **Apify token** — still PLACEHOLDER in .env (Sam started earlier)
- **Vercel project create + link** — `vercel link` from repo root
- **Resend domain add** — add `send.superhosttracker.com` in Resend dashboard, paste DNS records into Namecheap Advanced DNS

## Resume command
After above, run: `/launch-saas superhost-tracker --resume`
