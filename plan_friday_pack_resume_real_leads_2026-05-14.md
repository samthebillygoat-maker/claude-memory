---
name: plan-friday-pack-resume-real-leads-2026-05-14
description: Cold-pickup plan to resume real-lead pipeline work after session reset 2026-05-14. Covers surgery state, real scraper inventory, exact CLI for Gulf Shores/Branson/Chattanooga/Smokies, and reality-check gates.
metadata:
  type: project
---

# Friday Pack — Resume Plan (2026-05-14, post-context-reset)

**Session ended:** late 2026-05-14 — context was getting heavy, Sam asked for a clean save before pushing further.
**Next session goal:** generate 50 real signal-flagged leads for Gulf Shores AL / Branson MO / Chattanooga TN / Smokies TN using the existing scraper infrastructure, then build the Free Friday Sample page on top.

---

## Read these first (cold-start order)

1. This file
2. `plan_friday_pack_deep_dive_2026-05-14.md` (canonical product strategy, $97/$197/$347 pricing decided)
3. `plan_friday_pack_first_week_sales.md` (distribution playbook)
4. `project_friday_pack_launch.md` (rebrand state)
5. `feedback_friday_pack_launch_lessons.md` (9 mistakes to avoid)
6. `feedback_review_every_task.md` (use agents on every task)

---

## What was done this session (file changes — all persisted to disk)

### Launch-kit surgery (`C:\Users\samth\Downloads\friday-pack-launch-kit\`)
Fabricated stats stripped + pricing reconciled to canonical $97/$197/$347 across:
- `week-1-outbound-plays.md` — killed "11% conversion", "2% graveyard", "30-50% vs 5-10%" benchmarks, fabricated Gulf Shores lead row, wrong-state Branson ZIP (76616 → noted MO ZIPs are 65616/65672/65737), marked all X handles UNVERIFIED, replaced fake $500-900 week-1 forecast with measurable signals
- `growth-deep-dive.md` — stripped 9 invented percentage lifts (+15-20pp, +10-15pp, "25-40% openers", "K-factor 0.2-0.4", etc.)
- `starter-pack-value-stack.md` — pricing fixed; **drafted addendum replaced with real CitySide Stays Addendum A (2026-05-12)** — 10 clauses extracted from `CitySideStays_AddendumA_PlatformHosting_2026-05-12.docx`, with state-localization buyer instructions added
- `A_instagram_bundle.md`, `B_linkedin_x_posts.md`, `C_reddit_drafts.md`, `D_welcome_email_sequence.md`, `H_claude_design_prompts.md`, `organic-week-1.md`, `paid-meta-test-plan.md`, `TOMORROW_ACTION_PLAN.md`, `instagram-renders/post-02/carousel.html` — pricing batch-fixed

### Hail-mary repo pricing aligned to canonical
- `src/app/page.tsx` — pricing UI cards + intake header
- `public/legal/sla.md` — customer-facing SLA pricing
- `samples/sample-pack-{pcb,smokies,tampa}.html` — footer line
- `samples/_build.py` + `samples/_brand_patch.py` — generator scripts
- `samples/README.md` — sample doc
- `STRIPE_SETUP.md` — Stripe SKU setup instructions (SKU 2 + SKU 3)
- `legal/terms.md`, `legal/RISK_SUMMARY.md` — $97-$397 → $97-$347 range
- `playbook/05-retention.md` — re-engagement offer reference
- `.env.example` — PRO comment

**Left alone (different product):** AirCheck/Hail Mary single-report tiers ($19 single / $97 founding / $147 standard) in README.md and .env.example — those are AirCheck, not Friday Pack.

---

## ⚠️ Outstanding Sam-only tasks (claude can't do these)

1. **Update Stripe LIVE prices**: Weekly $197/mo, Pro $347/mo. Copy new price IDs into `NEXT_PUBLIC_STRIPE_PRICE_WEEKLY` and `NEXT_PUBLIC_STRIPE_PRICE_PRO` in Vercel env vars.
2. **Attorney pass on the addendum** before bundling in any paid Starter delivery. Florida-statute references need localization for AL/MO/TN customers.
3. **Verify the live site** at thefridaypack.com shows $97/$197/$347 after deploy. (Vercel will auto-rebuild from the git push if Sam pushes the hail-mary changes.)

---

## Reality-confirmed inventory (scrapers — what actually works)

Previous audit dismissed too quickly. The **real working scraper stack lives in `C:\Users\samth\miami-arbitrage\`**, NOT in hail-mary.

**Working today (real credentials, tested):**
| Script | What it does | Source | Status |
|---|---|---|---|
| `scripts/scrape_apartments_apify.py` | Apify actor `pro100chok~apartments-scraper-usage`, ~$0.002/listing | Apartments.com | ✅ Active |
| `scripts/scrape_new_cities.py` | Free Craigslist scraper | Craigslist | ✅ Active |
| `scripts/craigslist_monitor.py` | 5-min polling loop (Miami only currently) | Craigslist | ✅ Active |
| `scripts/batch_national_scrape.py` | 4-phase: RentCast → Apartments → Zillow (letscrape) → Craigslist | Multi | ✅ Active |
| `scripts/group_by_owner.py` | Ranks + dedupes raw output → top-50 CSV/MD | — | ✅ Active |
| `scripts/enrich_phones.py` / `auto_skip_trace.py` | Phone enrichment | — | ✅ Active |
| `scripts/airdna_scraper.py` | Playwright login to AirDNA Rentalizer | AirDNA | ✅ Active |
| `audit_leads.py` | NANP validation of output CSV | — | ✅ Active |
| `automations/run_{daily,weekly,monthly}.py` | Cron entry points wrapped with `safely()` | — | ✅ Active |

**Credentials confirmed REAL in `miami-arbitrage/.env`:** APIFY_API_TOKEN, RENTCAST_API_KEY, ZILLOW56 (via api_keys_local.json), ANTHROPIC_API_KEY, OPENAI_API_KEY, AIRDNA_EMAIL/PASSWORD, Twilio, Gmail, Reddit. NOT placeholders.

**Apify actor ID hardcoded:** `pro100chok~apartments-scraper-usage` (Apartments.com only — Sam needs to confirm subscribed in Apify console).

---

## The two surgical gaps blocking real Gulf Shores leads

### Gap 1 — Target markets not seeded
`scrape_apartments_apify.py` MARKET_URLS only contains miami / tampa / scottsdale / nashville. The 4 Friday Pack target markets need adding:

```python
"gulf-shores": "https://www.apartments.com/condos/gulf-shores-al/",
"branson":     "https://www.apartments.com/branson-mo/",          # VERIFY URL SLUG
"chattanooga": "https://www.apartments.com/chattanooga-tn/",      # VERIFY URL SLUG
"smokies":     "https://www.apartments.com/gatlinburg-tn/",       # VERIFY URL SLUG (or pigeon-forge-tn)
```

**Action for next session:** open the Apartments.com URL for each in a browser FIRST, verify the slug, then patch the dict. Don't trust my guesses above blindly.

### Gap 2 — No Friday-Pack-shaped output writer
`group_by_owner.py` outputs a ranked CSV but it's not formatted to match the existing `sample-leads.json` schema (which has `rank`, `address`, `city`, `state`, `zip`, `rent`, `beds`, `type`, `ownerName`, `phone`, `tier`, `verdict`, `signal`, `opener`, `url`).

**Action for next session:** write `scripts/format_as_friday_pack.py` — takes `data/leads_by_owner_<DATE>.csv` → outputs JSON matching `sample-leads.json` schema. The `signal` field can be derived from existing rank logic + add days-on-market / vacancy / price-drop heuristics. The `opener` field probably needs a small Claude call per row to generate (template + listing data → Voss-style opener).

---

## ⚠️ Honest market-yield expectations

Apartments.com has uneven coverage by market type:
- **Tampa**: rich data (urban, large stock) — 50+ leads achievable
- **Miami**: rich data — 50+ achievable
- **Chattanooga**: probably 30-50 (mid-size city, mixed)
- **Gulf Shores AL**: small market (~pop 15k), Apartments.com may have only 10-25 condo listings
- **Branson MO**: vacation market, Vrbo/Airbnb-dominated, Apartments.com sparse
- **Smokies (Gatlinburg/Pigeon Forge)**: same — vacation, sparse on Apartments.com

**To hit 50/market in vacation markets, we need supplementary sources**: the existing Craigslist scripts (`scrape_new_cities.py`) for FRBO/owner-direct listings, plus possibly Zumper (not currently wired but could be added). Realistic Week-1 yield from Apartments.com alone in Gulf Shores: 10-25 leads, not 50. Plan accordingly.

---

## Existing assets we can use TODAY (zero new scraping)

`C:\Users\samth\hail-mary\src\data\sample-leads.json` contains **150 real, hand-curated leads** dated **4 May 2026** (10 days old as of session end):
- Tampa: 50 leads (real names, phones, signal reasons, personalized openers)
- PCB: 50 leads
- Smokies: 50 leads

**Freshness check:** at 10 days old these are *within* Sam's 30-day freshness rule for paid packs, and definitely fine for the Free Friday Sample (the sample exists to prove data quality, not be hot off the press).

**Strategy:** use these 150 existing leads as the Free Friday Sample source while the fresh-scrape pipeline is being built. Each weekly sample email = 3 leads pulled from this corpus (rotate markets). Buy ~3 weeks of cover while building the scraper extensions.

---

## Resume plan (do these in order, ONE per agent or me per task)

### Phase 0 — Sanity reset
- [ ] Read this file + the 5 vault files listed at top
- [ ] Run `git status` in both `hail-mary` and `miami-arbitrage` — see what's uncommitted from this session's edits
- [ ] Confirm with Sam: should we git-commit the surgery before pushing further?

### Phase 1 — Reality-check the surgery (BEFORE building anything new)
Dispatch the Reality Checker on `C:\Users\samth\Downloads\friday-pack-launch-kit\` AND on the hail-mary pricing changes:
- [ ] Verify zero `$147` / `$397` references in launch-kit (excluding intentional context like AirCheck mentions)
- [ ] Verify no surviving fabricated statistics in the 3 main docs
- [ ] Verify the swapped CitySide addendum text matches the docx source exactly
- [ ] If Reality Checker flags anything → fix before Phase 2

### Phase 2 — Market URL verification (Sam + me, parallel)
- [ ] Sam: open Apartments.com in browser for each of Gulf Shores AL, Branson MO, Chattanooga TN, Gatlinburg TN — confirm the URL slug each one uses, paste back to me
- [ ] Me: while Sam verifies, read `C:\Users\samth\miami-arbitrage\scripts\scrape_apartments_apify.py` end-to-end so I understand the MARKET_URLS dict shape and any expected CLI flags

### Phase 3 — Seed the new markets + test small
- [ ] Add the 4 verified market URLs to `MARKET_URLS` in `scrape_apartments_apify.py`
- [ ] Run a **single-market test** first: `python scripts/scrape_apartments_apify.py --markets gulf-shores --pages 1 --details` (~$0.02 cost, validates output shape)
- [ ] Inspect output: yield count, field completeness, phone presence
- [ ] If yield <20: enable Craigslist supplementary source via `scrape_new_cities.py` (will need a similar MARKET_URLS addition there)

### Phase 4 — Full 4-market pull
- [ ] `python scripts/scrape_apartments_apify.py --markets gulf-shores,branson,chattanooga,smokies --pages 3 --details`
- [ ] `python scripts/group_by_owner.py` → ranked leads_by_owner CSV
- [ ] `python scripts/audit_leads.py` if CSV path matches; otherwise inspect manually
- [ ] (If phones <80% complete) `python scripts/enrich_phones.py` or `auto_skip_trace.py`

### Phase 5 — Friday-Pack-shape output writer
- [ ] Write `C:\Users\samth\miami-arbitrage\scripts\format_as_friday_pack.py`:
  - Input: `data/leads_by_owner_<DATE>.csv`
  - Output: JSON matching `hail-mary/src/data/sample-leads.json` schema, keyed by market slug
  - Signal-reason: derived from rank fields + DOM/price-drop heuristics
  - Opener: per-row Claude call (anthropic SDK is in stack, use the same Voss-style prompts from `playbook/`)
- [ ] Reality-check the output before declaring done

### Phase 6 — Free Friday Sample page (hail-mary)
- [ ] Add `/free-sample` route to `hail-mary/src/app/`
  - GET: landing page with email opt-in
  - POST `/api/free-sample/signup`: stores email in DB (`FreeSampleSubscriber` model — add to Prisma schema), confirms with Resend email
- [ ] Add a Friday cron at `/api/cron/free-sample-blast`:
  - Pulls 3 leads from sample-leads.json (or the new fresh pipeline once Phase 5 is done)
  - Renders one branded HTML email per subscriber
  - Sends via Resend with utm-tagged links back to checkout
- [ ] Test end-to-end with Sam's own email as the test subscriber

### Phase 7 — Reality-check everything before delivery
- [ ] Reality Checker on Phases 4-6 output: zero fabricated leads, zero phone numbers without real source, zero claims that can't be backed
- [ ] Verify the Free Friday Sample email matches Friday Pack public framing rules ("STR-friendly decision-makers", "corporate housing for traveling professionals" — never "Airbnb arbitrage")

### Phase 8 — Save state + close out
- [ ] Update this plan file with what was actually done vs. planned
- [ ] Add a memory entry for the new pipeline scripts
- [ ] If Phase 6 shipped: schedule the first Friday Sample blast

---

## Tasks still PENDING in the task list (sticky across sessions)

These tasks were created in the live task list this session. New session can re-check via TaskList:

1-8. Postiz deploy on Fly.io (PAUSED — Sam will resume later)
10. Build Free Friday Sample landing page + email opt-in (Phase 6 above)
12. ✅ Surgery on launch-kit docs (DONE)
13. ✅ Replace drafted addendum with real CitySide addendum (DONE)
14. Build real 50-lead pipeline → REDEFINED as Phases 2-5 above
15. Reality-check all artifacts → covered by Phases 1, 7

---

## Critical reminders for fresh session

- **Use agents on every task.** Sam explicitly asked. Dispatch the Reality Checker on every artifact before declaring done. Use apify-scraper-specialist for scraper work. Use Content Creator for any new copy.
- **NEVER fabricate stats.** Every percentage, conversion rate, or benchmark needs a verified source. If you don't have one, say "not measured yet" — do NOT invent.
- **NEVER fabricate handles, ZIP codes, addresses, or contact info.** The session before this one inserted a fake Branson ZIP (76616) and an entirely fabricated Gulf Shores lead row into the FB value-drop post. Both were caught by the Reality Checker. Same standard applies forever.
- **Pricing canonical: $97 / $197 / $347.** If you see $147 or $397 anywhere, it's either AirCheck (different product, leave alone) or stale (fix it).
- **Public framing rule:** "STR-friendly decision-makers" / "corporate housing for traveling professionals." NEVER "Airbnb arbitrage" or "sublease" in any prospect-facing asset.
- **Lead freshness:** reject anything >30 days. The 150 existing curated leads in sample-leads.json are dated 4 May 2026 — still valid through ~3 June 2026.

---

## Related memory

- [[plan-friday-pack-deep-dive-2026-05-14]] — full strategy + canonical pricing decision
- [[plan-friday-pack-first-week-sales]] — distribution playbook
- [[project-friday-pack-launch]] — rebrand + live state
- [[feedback-friday-pack-launch-lessons]] — past mistakes to avoid
- [[feedback-review-every-task]] — agent-driven review per task
- [[feedback-no-comp-advantage]] — uncomped > comped lead scoring
- [[reference-friday-pack-lead-criteria]] — $950+, 12mo, signal-required
- [[feedback-secret-handling]] — never echo credentials when patching env files
