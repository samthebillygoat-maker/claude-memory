---
name: plan-friday-pack-deep-dive-2026-05-14
description: Multi-agent deep dive into The Friday Pack — reality audit, pain/feature/competitive/pricing/cost/channel analysis, retention design, and prioritized 90-day gameplan
metadata:
  type: project
---

# The Friday Pack — Deep-Dive Gameplan (2026-05-14)

Five specialist agents ran in parallel: codebase audit, customer pain + feature gap (PM), competitive teardown (research), pricing + cost (finance), acquisition channels (growth). This document synthesizes their findings into a single prioritized plan.

---

## EXECUTIVE SUMMARY (1 page)

**What the product is, stripped of marketing.** Manually-fulfilled weekly delivery of 50 STR-friendly landlord leads in 3-5 vacation markets. Built on Next.js 16 + Stripe + Apify + BatchSkipTracing. Live homepage, working checkout, manual fulfillment pipeline (Sam runs scripts). Dashboard, intake form, call-script playbook, DD tier, and Clerk auth are scaffolded but not built. Marketing promises features that don't exist yet (call-script PDF, weekly market intel).

**Where it stands competitively.** Defensible market position: market depth over national breadth + per-lead signal reasons + pre-vetted regulatory layer. Real artifact value is $3-10/lead = $150-500/pack. Current price ($197/wk Weekly) implies $0.99/lead — under-priced for the layer of judgment delivered, but only IF those layers are visible to the buyer.

**The structural problem.** Success kills demand. Operators need 2-3 STR-friendly units, then they're done. Without an expansion path (more markets, more services, a community to belong to), every closed deal accelerates churn. **The whole retention strategy must counter this.**

**The single highest-leverage move.** Ship a **per-lead AI cold-DM/voicemail/script generator (Voss-loaded)** behind the Weekly tier. It attacks the bottleneck *after* "I can't find landlords" — which is "I can't close." It's a +30-50% landing-page conversion lift, ~40% month-1→2 churn cut, demoable in a 90-second Loom, and ~2 weeks of build. Anthropic SDK is already in the stack.

**The single channel bet for 30 days.** **Partner emails / affiliate program**, starting with Kash Wason (existing warm relationship). One Kash send can exceed 30 days of cold DMs. Kill Google Ads (search volume too thin). Reclassify Twitter from "sales channel" to "credibility moat."

**The pricing change.** Add a $29 / 15-lead trial pack as the funnel front door. Keep Weekly $197 and Pro $347 (canonical per playbook, NOT the stale STRIPE_SETUP.md $147/$397). Negotiate bulk skip-trace at $0.07/lead once 200 subs in, replace human QA with Claude Haiku verification. GM moves 38% → 67%.

**Week-1 actions.** Reconcile pricing tier names (DB ↔ homepage). Fix Stripe live mode. Build per-lead AI script generator. Pitch Kash on affiliate deal. Launch $29 trial tier. Everything else waits.

---

## PASS 1 — CODEBASE REALITY AUDIT

**Stack:** Next.js 16, TypeScript, Tailwind v4, Clerk auth, Stripe, Supabase + Prisma 7, Apify (Airbnb scraper), Claude (Sonnet 4.5 + extended thinking), Resend, BatchSkipTracing.

**Live & shipping:**
- Homepage (`src/app/page.tsx`, 740+ lines) — hero, how-it-works, pricing, FAQ, market picker with GREEN/YELLOW/RED badges, embedded sample preview, launch promo bar
- `/api/checkout` → Stripe Checkout; `/api/webhooks/stripe` → consumes session.completed + subscription.* + invoice.paid
- `/api/scrape` (Apify), `/api/extract` (Claude vision over AirDNA screenshots)
- Brand system (forest green / amber / ink, Inter / IBM Plex Serif / JetBrains Mono)

**Scaffolded, not built:** `/dashboard/*` (new, bulk, reports, leads, settings, dd/*) — 19 TODOs. Clerk auth gate on dashboard layout: TODO. Sign-in/sign-up: TODO. Intake form: spec only. Sample report PDF: stub.

**Manual today:** Sam runs `scripts/scrape-market.ts → filter.ts → skiptrace.ts → rank.ts → render-pack.ts`, uploads to Supabase, sends email. Automation triggers after customer #10 + 3 weeks stable.

**Pipeline (6-factor rank):** owner type / STR-rev-to-rent / building competition density / lease flexibility / absentee signal / TOP-MID-SKIP tier. 30-day max source freshness. 180-day suppression to prevent re-delivering same owner.

**Cost in code:** Skip-trace ~$14/pack. LLM cost logger exists (`src/lib/llm/cost.ts`) but not wired into responses.

**CRITICAL MISMATCHES:**
1. **Tier name drift.** Homepage: Starter / Weekly / Pro. DB schema (`Subscription.tier`): single / founding / standard. STRIPE_SETUP.md says $97/$147/$397. `.env.example` + playbook/05-retention say $97/$197/$347. **Playbook is canonical.** Reconcile before next launch push.
2. **Promised but not built:** Call-script playbook PDF (Weekly tier feature). Weekly Market Intel report (Pro tier feature). DD tier ($29/mo upsell). Sample report PDF anonymizer. `/buy/single` checkout flow.
3. **Stripe live prices still PLACEHOLDER** in env. Test mode only.

**Docs that exist & matter:** `playbook/02-fulfillment-sla.md` (SLA + manual workflow), `playbook/05-retention.md` (canonical pricing + retention tactics), `playbook/06-first-10.md` (Sam's runbook), `brand/BRAND.md` (full token system). `AGENTS.md` is a 3-line stub.

---

## PASS 2 — CUSTOMER PAIN AUDIT

**Top 5 operator pains (frequency × severity, 1→10 unit scaling):**

| # | Pain | Friday Pack solves (0-10) |
|---|---|---|
| 1 | "I can't find landlords who'll say yes to STR/arbitrage." | **8** — direct hit, the entire product |
| 2 | "I get to humans, then fumble the close." | **3** — static playbook PDF only, not per-lead |
| 3 | "I don't know if a unit will cashflow." | **1** — no deal-analyzer in product |
| 4 | "10+ hrs/wk sourcing instead of operating." | **9** — explicit JTBD |
| 5 | "Leads rot in my notes app — no pipeline." | **0** — delivery-only today |

**The pain to OWN: #1 — STR-friendly landlord discovery.** Pain #4 (time savings) is the mechanism; #1 is the outcome.

**Positioning lock:**
> The Friday Pack is the only product that delivers a fresh weekly batch of pre-qualified, STR-friendly landlord decision-makers in vacation-rental markets — for arbitrage operators scaling from 1 to 10 units who refuse to spend their weekends scraping Zillow.

---

## PASS 3 — COMPETITIVE TEARDOWN

**Direct competitors (sells landlord/lead lists to STR operators):**
- **BNB Depot** — closest analog. Course-bundled "10,000+ Airbnb-friendly owners" list. Stale, over-shared, claims "partnered with Airbnb" (dubious).
- **Course-bundled lists** (BNB Formula, Rakidzich, Preston Seo) — bonus inside $500-$5k courses. Stale, national, shared.

**Adjacent (NOT direct):**
- **Rabbu** — sells *buyer* leads to *agents* at $150/lead, $3k+ bundles. Different ICP.
- **AirDNA** — market data, no contacts. Upstream tool.
- **Awning** — full-service mgmt at 10% rev share. Not a list product.

**DIY substitutes:**

| Path | Cost/wk | Quality |
|---|---|---|
| VA scraping Zillow/CL/FB | $80 cash + 4hr QA = $280 all-in | Mostly PM-listed, gatekept |
| PropStream | $99/mo (~$0.01/raw record) | No STR-intent filter |
| BatchLeads | $0.10-$0.14/record | No STR-intent filter |
| Facebook STR groups | Free | Same leads everyone calls |

**Operator DIY total: ~$300-350/wk in time + tools** to produce 50 leads, with 1-2 week VA ramp.

**Defensible advantages (3):**
1. **Market depth over national breadth.** Re-walking 3-5 markets weekly catches new listings in 48hr, builds "we already know this building" institutional memory no national list replicates.
2. **Signal-reason per lead.** The "why this landlord" judgment is the moat — competitors who automate lose judgment, competitors who hire it can't match unit economics in small markets.
3. **Pre-vetted regulatory layer.** Pairing each lead with "this address is in zone X allowing 30+ day stays" requires 2+ hrs of muni-code per market. No competitor publishes this.

**Pricing benchmark:** raw skip-trace ($0.10/lead) ↔ buyer-intent leads ($150). Friday Pack's defensible artifact value is **$3-10/lead = $150-500/pack.** Sub-$150 undersells. Above $500 invites VA DIY.

---

## PASS 4 — PRICING TEARDOWN

**Canonical pricing (playbook):** $97 Starter one-time / $197 Weekly / $347 Pro. (STRIPE_SETUP.md $147/$397 is stale.)

**Value math (Weekly subscriber, base case):**

| Funnel stage | Conversion | Count |
|---|---|---|
| Leads | 100% | 50 |
| Reachable phone | 70% | 35 |
| Conversation held | 30% | 10.5 |
| Open to STR | 25% | 2.6 |
| Signed lease | 40% | **1.05** |

**~1 closed unit per pack of 50.** At $1,200-$2,500/mo net profit per unit × 12mo = **$14k-$30k annualized value per close**. Midpoint: **$22,200/yr**.

**Value-to-price ratio at $197/mo:** ~9.4x. Strong, not absurd — "obvious yes" but not "raise prices now."

**The structural problem:** operators need 2-3 units, then they're done. Success kills demand. Churn is structurally high. **This is the actual pricing problem, not the price level.**

**Three alternative structures:**

1. **$29 / 15-lead trial pack.** Drives **2.5-4x** visitor→buyer at 76% GM. **Net more paying subs** if top-of-funnel doubles. Lead-magnet quality, not revenue.
2. **$5/lead usage-based, min 25.** Avg buyer takes 120/mo = $600/mo (3x current Weekly). 92% GM. Cuts churn ~40% (self-throttle). LP conversion drops 20-30%. **Best as power-user tier post-trial, not headline.**
3. **8% of first-month rent on closed deal.** 5-8x LP conversion ("free until you close") but 40-60% attribution leakage → effective take ~4%. **Use as partnership tier for vetted operators, not retail.**

**Price ceiling.** Serious 20+ unit/yr operators would pay **$2k-$5k/mo** with proof points:
1. Verified landlord intent (recorded screening call)
2. Exclusive ZIP territory lock
3. Done-for-you outreach (first 3 calls)
4. Closed-deal SLA refund
5. Zoning pre-clearance

$500/mo tier needs items 1 + 5. $2k+ tier needs 2 + 3 + 4.

---

## PASS 5 — FEATURE GAP (5 highest-leverage of 20)

| Rank | Feature | Effort | LP lift | M1→M2 churn cut |
|---|---|---|---|---|
| 1 | **Per-lead AI cold-DM/script generator (Voss-loaded)** | M (2wk) | **+30-50%** | **~40%** |
| 2 | In-pack red flags + per-lead market score (Double Rent Rule + AirDNA pull) | M (1.5wk) | +20-30% | ~20% |
| 3 | Landlord pipeline CRM-lite + cross-pack de-dupe | L (3wk) | +10% | **~50% (switching cost)** |
| 4 | Lead replacement guarantee (form + SLA) | S (3d) | +15-25% | ~15% |
| 5 | Weekly Market Intel 1-pager (already promised) | S (1wk recurring) | +10% | ~20% |

**Ship next: #1 — Per-lead AI script generator.**

Why this one:
- Attacks the next bottleneck after Friday Pack solves pain #1.
- Compounds existing Call Script Playbook IP into per-lead dynamic output.
- Highest demoable upgrade on landing page (`/samples/tampa` with "see the script for lead #3").
- Anthropic SDK already in stack.

Dev-ready spec: add `outreach_kit` JSON to Lead model; one Claude prompt taking `{name, role, signal_reason, market, property_type}` → outputs `{instagram_dm, sms_opener, voicemail_30s, top_3_objection_rebuttals}`; render in web view + PDF; gate to Weekly/Pro tier (drives Starter→Weekly upgrades).

---

## PASS 6 — COST STRUCTURE

**Per 50-lead pack:**

| Cost line | $/pack |
|---|---|
| Apify scraping | $3.00 |
| Skip-trace (BatchSkipTracing @ $0.25) | $12.50 |
| Phone validation | $1.50 |
| Public records / GIS | $1.00 |
| Resend email | $0.10 |
| Hosting allocation | $0.30 |
| Stripe fees (on $197 sub) | $6.01 |
| Human QA (15min @ $25/hr) | $6.25 |
| **Total** | **$30.66** |

**Revenue/pack (Weekly $197 / 4 packs):** $49.25. **GM: 38%.**

**Two biggest cost levers:** skip-trace (41% of cost), human QA (20%).

**Cost-down moves:**
1. **Bulk skip-trace** at $0.07/lead (BatchSkipTracing 10k/mo tier) saves $9/pack. Unlocks at ~200 active subs.
2. **LLM QA via Claude Haiku** (phone format, name-address match, zoning lookup) at $0.02/lead replaces $6.25 human QA. Validate via 5% shadow QA.

**Combined: $30.66 → $16.41/pack. GM 38% → 67%.**

**Cost-up moves that unlock higher pricing:**
1. **Pre-call verification** ($4/lead VA) → 50× = $200/pack cost added → justifies $497/mo Weekly tier (close rate 2% → 10%). **Net +$100/pack contribution.**
2. **Zoning pre-clearance API** (~$1.50/lead) → $75/pack cost → justifies $150/mo add-on. **Net +$75/pack.**

---

## PASS 7 — ACQUISITION CHANNELS

**Reality check on each channel:**

| Channel | CAC reality | Verdict |
|---|---|---|
| Cold DM (IG/LinkedIn) | $0 cash + 30-50 min/sale. Caps ~500 DMs before rate-limit; reachable arbitrage pool in 3 markets ≈ 2,000. **Works wk 1-4, not 90-day.** | Use, don't scale |
| Reddit value posts | 45-60 hrs/sale. Operators consume free sample, never pay. **Good for backlinks/credibility, bad for direct conversion.** | Defer |
| Twitter BIP | Zero week-1 ROI. Pays at month 3 if account grows. **Reclassify as credibility moat, not sales channel.** | Keep posting, drop expectations |
| Partner emails / affiliates | One Kash Wason send (5k STR list) at 25% open / 2% CTR / 5% close = **~12 sales from one send**. Trade 4 wks free per partnership = **$24 CAC**. | **THE BET** |
| Google Search Ads | Keywords "rental arbitrage leads" / "STR leads" have <50 combined searches/mo. $280 spend → ~1-2 sales = **$167 CAC**. | **KILL** |

**The 30-day bet: Partner emails / affiliate program.**

Math: 3 signed partners → 3 dedicated sends → ~40 paying subs at $197 blended × 8wk LTV = **$32k ceiling. Realistic mid-case $8-12k.**

30-day plan:
- Wk 1: Pitch Kash + 4 warm intros (Bill Faeth, Avery Carl, Jeremy Werden, James Svetec)
- Wk 2: Co-branded landing page `/p/[partner-slug]` live
- Wk 3: First send
- Wk 4: Second send + recruit affiliate #2

**Kill list:** Google Ads (defer until $5k MRR + can afford $500 test). Twitter reclassified (not killed).

**Missing channels to add:**
- **Affiliate program (formalized at 30% recurring)** — operationalizes partner channel as self-serve. Build dashboard by 2026-06-01.
- **Skool community presence** in Kash's group specifically. $0, 30 min/day, warm audience. Test 14 days.
- **SEO long-tail** ("STR-friendly landlords Gulf Shores") — start month 2. 50 markets × 1 page/wk = 1,000+ visits/mo at zero CAC.
- **Podcast sponsorship** (STR Unfiltered, Get Paid for Your Pad) — after first $3k MRR. $50-150 CAC expected. Better than Google Ads.

**Skip:** YouTube, AppSumo/LTD (wrong product shape — buyers will arbitrage one pack and quit), SaaS cross-sells (too early).

---

## PASS 8 — RETENTION & EXPANSION

**The core retention problem: success kills demand.** An operator who closes 2-3 deals will cancel. Without an expansion path, every win accelerates churn.

**Churn-risk save flow (operator closed 0 deals in week 1):**
- Day 5: Coaching email — "the 5 leads from your pack most likely to close based on signal_reason." Loom of Sam dialing one.
- Day 8: 15-min call offer — Sam reviews their call log, picks the next 3 to pursue.
- Day 12: Free 1-market extension of pack — "we'll add Branson on top of Gulf Shores."
- Day 25 (pre-renewal): "Pause for 30 days" option (cheaper than cancel).

**Expansion paths for power users (operator closed 2+):**

1. **Market expansion** — Pro tier at $347/mo unlocks 2nd market (already in pricing). Trigger: 1 close detected → email upsell.
2. **Done-for-you outreach add-on** — $200-$500/mo. Friday Pack team makes first 3 calls per lead, warm-transfers to operator. Highest LTV unlock.
3. **DD tier** ($29/mo) — landlord vetting, lease scan, permit check. Already scaffolded in `/dashboard/dd/*`. Builds switching cost.
4. **CRM-lite + cross-pack de-dupe** (feature gap #3) — once pipeline lives in Friday Pack, leaving = losing pipeline. Strongest structural retention play.
5. **Community / Discord** — gated to paying subs. Weekly office hour with Sam. Builds belonging — operators stay subscribed to stay in the room, not for the leads.

**Predicted retention impact stack:**
- Per-lead AI script (Feature 1): M1→M2 -40% churn
- CRM-lite + de-dupe (Feature 3): structural switching cost -50%
- Community: belonging-driven -20-30%
- Combined: targeting M3 retention from ~30% → ~70%

---

## PASS 9 — THE GAMEPLAN

### Week 1 (now → 2026-05-21)

| # | Action | Owner | Success metric | Kill criteria |
|---|---|---|---|---|
| 1 | Reconcile pricing: DB schema rename (single→starter, founding→weekly, standard→pro). Fix STRIPE_SETUP.md to $97/$197/$347. Push live Stripe price IDs. | Sam | All three sources agree; Stripe live mode tested with $0.50 charge | n/a — blocker |
| 2 | Build & ship `/api/outreach-kit` — per-lead AI script generator (DM, SMS, VM, 3 rebuttals). Gate to Weekly/Pro tier. | Sam | Visible in next Friday pack delivery; one operator quotes a script back in reply | Defer 1 wk if Pass 1 reveals deeper auth blockers |
| 3 | Pitch Kash Wason on affiliate deal: 30% recurring + first send to his list. Co-branded landing page wireframe attached. | Sam | Verbal yes by 2026-05-20 | If no reply by 2026-05-19, send to Bill Faeth in parallel |
| 4 | Add $29 / 15-lead trial pack as new SKU. Single-market, 48hr delivery. New homepage CTA. | Sam | $29 SKU live in Stripe; LP CTR on trial vs. Weekly tracked | Pull if trial→Weekly conversion <10% after 20 trial buyers |
| 5 | Daily 30 cold DMs to STR arbitrage operators (in parallel to partner pitches). | Sam | 6%+ reply rate by day 5; 3 paid by day 10 | Reply rate <3% by day 5 = pause and retool angle |

### Weeks 2-4 (2026-05-22 → 2026-06-11)

1. **Launch first Kash send** to his list (or whichever partner signed Wk 1).
2. **Build CRM-lite + cross-pack de-dupe** (Pass 5 Feature #3) — strongest structural retention. 3-week build.
3. **Replace human QA with Claude Haiku verification** + 5% shadow QA. Watch quality metric for 2 wks. Saves $5.25/pack.
4. **Ship Weekly Market Intel 1-pager** (already promised on homepage). Sam writes first 4; templatize after.
5. **Lead replacement guarantee** form + 7-day SLA. Build is 3 days, conversion lift 15-25%.
6. **Recruit affiliate #2** in parallel to running affiliate #1.
7. **Skool presence** — daily value post in Kash's Skool group.

**Build/market/talk-to-customers ratio:** 40% build / 40% market (partner + DMs + Skool) / 20% customer interviews (validate pain ranking against first 5 paid users).

### Days 30-90 (the bet)

**Bet: become the must-have second tool in the STR operator stack** (after AirDNA, before PMS). Concretely:

1. **Path to $5k MRR:** 25 Weekly subs ($4,925) + 1 Pro ($347) ≈ $5,272/mo by day 60.
2. **Path to $10k MRR by day 90:** Second partner send + SEO long-tail traffic + 1 podcast sponsorship + affiliate program self-serve.
3. **Once at $5k MRR:** negotiate bulk skip-trace ($0.07/lead), unlocking 29% cost reduction. GM rises to 67%.
4. **Once at $10k MRR:** test podcast sponsorship #2 + pre-call verification add-on at $497/mo Weekly tier.

### What we are explicitly NOT doing

- ❌ Google Ads — search volume too thin (<50/mo combined). Defer indefinitely.
- ❌ YouTube / short-form video — wrong audience search behavior.
- ❌ AppSumo / lifetime deals — wrong product shape; LTD buyers arbitrage one pack and quit.
- ❌ Twitter as a sales expectation — keep posting for credibility, drop the conversion target.
- ❌ Building the DD tier UI yet — promised but not blocking revenue. Defer to Wk 5+.
- ❌ Outcome-based pricing as headline — 40-60% attribution leakage. Use only as partnership-tier deal.
- ❌ Reddit value posts as a primary channel — keep monthly for backlinks, not as a paid-conversion play.
- ❌ Expanding to a 4th market until current 3 are saturated (Gulf Shores, Branson, Chattanooga).

---

## OPEN QUESTIONS (require customer interviews, not analysis)

1. Is pain #1 ("can't find STR-friendly landlords") actually ranked higher than pain #2 ("can't close") by paying operators? — Confidence on ranking: 60%. Validate with first 5 paid users by 2026-05-25.
2. Will operators pay $497/mo Weekly if pre-call verification adds 10% close rate? — Model says yes; need 3 customer-development calls to confirm.
3. Does success actually kill demand at 2-3 units, or do operators want to scale to 10+? — Determines whether retention play is community/expansion (yes) or "graduation" upsells like coaching (no).

## CONFIDENCE FLAGS

- LTV (~$600 / 8wk): **guess** — no churn data yet. Firm up at customer #20.
- DM conversion rates: **directional** from analogous niches.
- Feature-impact %: **analogous-product based** (Morning Brew, Apollo, Hustle Premium).
- Skip-trace bulk pricing: **public tier doc**, confirmed.
- Competitor pricing on BNB Depot: **not exposed publicly** — guess based on category norms.

---

**Files referenced:**
- `C:\Users\samth\hail-mary\` (full repo)
- `C:\Users\samth\hail-mary\STRIPE_SETUP.md` (stale prices — fix)
- `C:\Users\samth\hail-mary\playbook\05-retention.md` (canonical prices)
- `C:\Users\samth\Documents\brain\claude-memory-main\plan_friday_pack_first_week_sales.md`
- `C:\Users\samth\Documents\brain\claude-memory-main\project_friday_pack_launch.md`
- `C:\Users\samth\Documents\brain\claude-memory-main\state_friday_pack_active_promo.md`

Related: [[plan-friday-pack-first-week-sales]], [[project-friday-pack-launch]], [[feedback-friday-pack-launch-lessons]]
