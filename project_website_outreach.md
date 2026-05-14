---
name: Website Outreach — CA Contractor Cold Engine
description: Cold-outreach SaaS targeting CA-licensed contractors (C-39 roofers first). Python+Scrapling+Cerebras+Twilio. 5 verified emails sent 2026-05-05/06; toll-free SMS IN_REVIEW.
type: project
---

# Website Outreach — CA Contractor Cold Engine

_updated 2026-05-06 (overnight build + May 6 evening status check)_

**Repo**: `C:\Users\samth\projects\website-outreach`
**Branch**: `feat/cold-outreach` (11+ commits)
**Status**: First batch of 5 cold emails sent overnight 2026-05-05 → 2026-05-06. Twilio toll-free verification `HHb0fe77fd2232b8c7116708f9149d6999` IN_REVIEW (4-7 days from 2026-05-06 0:17 UTC).

## What it is

Cold-outreach tool that sends polished, personalized emails (and TCPA-safe SMS once Twilio approves) to **CA-licensed trade contractors** offering them a website build. Differentiator: scrapes the contractor's own photos and licensing data, ships an inline mockup preview in the email so they see their business in the new design before replying.

**Why this niche:** small-market CA roofers / HVAC / plumbers / painters mostly run 2010-era WordPress or Wix sites with no mobile, no schema, no Google Business sync. License # + city + phone are public via CSLB → high-confidence verification possible.

## The Why (lead with this)

Most cold outreach fails because it's generic. The trade niche works because:
1. CSLB license # gives a free identity-verification handle (rejects evil-acmeroofs.com clones).
2. Contractors' existing sites are visibly bad, so a mockup-in-email is *self-evidently* an upgrade.
3. Small markets (High Desert, Coachella Valley, Central Valley, Far North) have low SEO competition — a $300-tier site can actually rank #1.

**How to apply:** Anytime Sam wants to test cold outreach for a new vertical, the pattern is `verify lead identity from a public registry → scrape their own assets → personalize first line → human-gate any inbound replies`.

## Stack

- Python 3.12 + Scrapling 0.4.7 + Playwright + Jinja2
- Cerebras LLM rotation for personalization
- Twilio (SMS, pending verification) + IMAP for replies
- 4 polished trade templates: roofer / HVAC / plumber / painter
- Static dashboard: `out/dashboard.html` (inline mockup previews)
- 62/62 pytest passing; `nightly.py` for cron

## What was built overnight

- **Photo scraper** — pulls contractor's own photos from their site
- **Reply classifier** — STOP / NEGATIVE / INTERESTED / QUESTION / AUTO_REPLY
- **Voss-tactical landlord drafter** (gated to human review, never auto-sends)
- **Hot-prospects scorer**
- **TCPA-compliant SMS sender** with quiet-hours guard (9am-6pm PT only)
- **Bounce monitor + suppression DB**
- **Deploy package generator** (drag-and-drop ready for Cloudflare Pages)
- **14 sales kit docs** in `sales/`: PRICING, REPLY_PLAYBOOK, FAQ, PHONE_SCRIPTS, OBJECTIONS_LIVE, HANDOFF_DOC_TEMPLATE, LANDLORD_REPLY_PLAYBOOK (Voss), RESEARCH_INSIGHTS (cited), STRIPE_SETUP, COMPARISON, SUBJECT_LINES, SMS_VARIANTS, LOOM_PLAYBOOK, ONBOARDING_INTAKE, CASE_STUDIES (rewritten as honest "Sample Build Patterns" with be-#1 discount offer)

## First batch sent (2026-05-05 → 2026-05-06)

5 verified C-39 roofers:
1. C&G New Generation Roofing — Victorville
2. Desert Roof Concepts — Palm Springs
3. Desert Roofing Solutions — Indio
4. Towers Waterproofing — Patterson
5. McLain's Roofing — Modesto

9 initial leads → 6 failed verification (wrong-state name collisions) → 5 sent.

## Critical bugs caught + fixed in agent QA pass

- TCPA timezone hardcoded to LA (real legal exposure for non-CA recipients)
- Dashboard XSS via `business_name` interpolation → `html.escape` applied
- Domain host check used `lstrip('www.')` → security flaw, let `evil-acmeroofs.com` through
- Reply classifier matched "no problem" as NEGATIVE → regression test added
- IMAP fetch marked unread as SEEN on crash → switched to `BODY.PEEK[]`
- Inbox classifier firing on 50+ school newsletters / Discord bots as "landlord" → strict NEVER_RESPOND list + 2-keyword + subject-signal requirement
- Sales: $300 deposit / $300-on-launch math bug (Tier 1 is $300 *total*)
- Sales: 7-day refund window inconsistent across PRICING / SERVICE_AGREEMENT / FAQ
- Sales: case studies were fake testimonials → rewritten as honest patterns + be-#1 discount

## Research consumed (cited in `sales/RESEARCH_INSIGHTS.md`)

- Personalized first line: 3.4% → 18% reply rate (Instantly / Belkins / Lemlist)
- Loom video personalization: 4% → 22%
- Tue/Wed/Thu 6:30-7:30am PT optimal for trade contractors
- TCPA / CCPA: $500-$1,500 per non-compliant SMS, mandatory STOP+HELP+sender-ID, quiet hours 8am-9pm
- Stripe sole prop: Payment Links is right product, $9 fee on $300 refund (eat or buffer), 1099-K threshold $2,500 in 2026

## Decisions / tradeoffs

- **Target:** C-39 roofers, small-market CA cities first
- **Verification gate:** city + phone + zip + state + license # signals on candidate site, score ≥50 required
- **Skip own-photo scraping for C-39:** roofers' best hero is a finished home, not a worker close-up
- **Don't auto-send Voss drafts:** always gate to human review

## 6 feedback memories saved to `memory/` in project repo

1. Curate, don't auto-search, for visual assets
2. Verify lead identity before cold sends
3. Always offer to do it (don't hand Sam manual checklists)
4. Research → build → test → iterate
5. Make Sam proud but conserve tokens
6. Test classifiers on real data first

## Open / pending

- [ ] Twilio toll-free verification IN_REVIEW — ETA 2026-05-10 to 2026-05-13
- [ ] Real PHYSICAL_ADDRESS still placeholder (`1400 W 3rd St, Chico, CA` — confirm real?)
- [ ] Inbox triage agent running as of 2026-05-06 evening — check for replies
- [ ] Decide: auto-render mockups for unverified leads?
- [ ] Plan next outreach batch (HVAC? More roofers?)
- [ ] Decide whether to keep auto-rendering mockups for unverified leads
- [ ] Replies should start arriving by 9am PT 2026-05-06 — triage flow ready

## Morning checklist

`NEXT_ACTIONS.md` at repo root: open dashboard, run triage, check Twilio status, decide on next outreach batch.

## Cross-references to other Sam projects

The cold-outreach pattern here is portable:
- **[Deal Engine](project_deal_engine.md)** — RentRadar's outbound DM-to-landlord flow could reuse the Voss drafter + reply classifier verbatim.
- **[Hail Mary](project_hail_mary.md)** — same Stripe Payment Links + 7-day refund pattern; same sole-prop 1099-K math applies.
- **[DealMemo](project_dealmemo.md)** — same Twilio toll-free verification path; once HHb0fe77... approves, that A2P 10DLC playbook ports over.
- **[Lead Trackers](project_lead_trackers.md)** — the verification-before-send gate (`feedback_no_fabricated_leads.md`) is the same hard rule.
