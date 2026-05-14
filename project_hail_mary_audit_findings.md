---
name: Hail Mary / Friday Pack — 3-Specialist Launch Audit (2026-05-08)
description: Reality Checker + Trend Researcher + PM audit synthesis; verdict = ship Product A only Monday, defer dashboard 2-3 weeks
type: project
---

# Hail Mary / Friday Pack — Launch Audit Findings

Audit run 2026-05-08 evening on `C:\Users\samth\hail-mary\` ahead of the Monday 2026-05-11 launch. Three specialist agents: Reality Checker, Trend Researcher, Product Manager.

**Verdict:** NOT READY for Monday as a full SaaS. Ship Product A (landing → checkout → manual fulfillment) only. Defer Product B (SaaS dashboard) 2–3 weeks.

## Headline finding

**Product pivot already happened — README is stale.** README/CLAUDE.md describe the old AirDNA-screenshots → 20-page-PDF analyzer. Actual shipped product on `src/app/page.tsx` is a **done-for-you weekly STR landlord lead-pack subscription** (originally $97 / $197/mo / $397/mo). Reconcile docs as part of the rename.

## Hard blockers (cannot ship Product B Monday)

- Every `/dashboard/*` route is a 4-line TODO stub.
- Clerk auth not wired — every dashboard page is publicly accessible.
- No charts — Apr 30 chart-rendering bugs were "fixed" by deleting the components.
- No real Stripe webhook (the unsafe stub at `src/app/api/stripe/` was deleted tonight).
- DATABASE_URL still placeholder; Supabase not provisioned.

## Soft blockers (Product A can ship around these, but fix Saturday)

- `window.prompt()` for email capture on landing.
- `/order` submit handler not wired.
- No transactional email (Resend not wired).
- Codebase still says "Hail Mary" everywhere.
- DNS not wired at Porkbun.

## Saturday do-today checklist (2026-05-09)

1. Provision Supabase, paste real DB URLs into `.env.local`.
2. Wire Stripe webhook → Prisma.
3. Replace `window.prompt()` with a real form.
4. Wire Resend transactional email.
5. Hide `/dashboard/*` from prod.
6. Fix `/order` checkout submit.
7. Rename "Hail Mary" → "The Friday Pack" across codebase.
8. Deploy to Vercel.
9. Wire DNS at Porkbun.

## Tonight's completed fixes (2026-05-08)

- `parseManualCsv` import in `src/lib/llm/extract.ts` — fixed.
- Stub Stripe webhook at `src/app/api/stripe/` — deleted.
- Prisma 7 client constructor — installed `@prisma/adapter-pg`, `pg`, `@types/pg`; rewrote `src/lib/prisma.ts` to driver-adapter pattern with lazy connection; build passes with placeholder DATABASE_URL.
- Stripe account created; `.env.local` template populated; Stripe CLI download in progress to `C:\Users\samth\bin\` (PATH updated).

## Cross-references

- Launch plan + pricing: `project_friday_pack_launch.md`
- Pricing rule learned tonight: `feedback_pricing_ladder_psychology.md`
- Original product memo (now partially stale, keep for history): `project_hail_mary.md`

## Updated 2026-05-08
