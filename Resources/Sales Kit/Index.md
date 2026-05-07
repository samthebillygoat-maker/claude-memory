---
type: sales-doc
source_file: sales\INDEX.md
tags:
  - #sales-kit
  - #sales/index
---

# Index

# Sales Kit — Index

Single grep-able reference for every document in this folder. When in doubt, read this first.

## When a contractor REPLIES

| Situation | File | What's in it |
|---|---|---|
| You need to write a reply right now | [REPLY_PLAYBOOK.md](REPLY_PLAYBOOK.md) | Copy-paste templates per category (INTERESTED / QUESTION / NEGATIVE / DELAY / REFERRAL / 5-day + 10-day follow-ups) |
| They asked for pricing | [PRICING.md](PRICING.md) | 3 flat tiers ($300 / $750 / $1500), payment terms, refund |
| They asked common questions | [FAQ.md](FAQ.md) | 14 pre-emptive answers (is this a scam, how did you get my info, why $300, will I be locked in, etc.) |
| They asked "have you done this before?" | [CASE_STUDIES.md](CASE_STUDIES.md) | Honest "be #1 with $50 off" framing — no fake testimonials |
| They want to book a call | [PHONE_SCRIPTS.md](PHONE_SCRIPTS.md) | Inbound + outbound + voicemail scripts, pre-call checklist |
| They challenged you on a call | [OBJECTIONS_LIVE.md](OBJECTIONS_LIVE.md) | 20 phone objections in scan-while-line-is-silent table format |
| They challenged "I'll just use Wix" | [COMPARISON.md](COMPARISON.md) | Year 1/5/10 cost comparison vs Wix/Squarespace/GoDaddy |

## When a contractor SAYS YES

| Step | File | What to do |
|---|---|---|
| 1. Send the agreement | [SERVICE_AGREEMENT.md](SERVICE_AGREEMENT.md) | Boilerplate contract, fill template variables |
| 2. Send the Stripe link | [STRIPE_SETUP.md](STRIPE_SETUP.md) | Setup walkthrough — Payment Links, fees, payouts, gotchas |
| 3. Send the intake form | [ONBOARDING_INTAKE.md](ONBOARDING_INTAKE.md) | Photos, services, brand colors, domain, contact form recipient |
| 4. Build the site | (you, with their inputs) | |
| 5. Deploy via Cloudflare Pages | `python deploy_package.py {license}` | Drag-drop ready folder |
| 6. Send the handoff doc | [HANDOFF_DOC_TEMPLATE.md](HANDOFF_DOC_TEMPLATE.md) | Login info, change instructions, warranty, what-if-Sam-disappears |

## When a LANDLORD replies (separate from contractor outreach)

| Situation | File | Strategy |
|---|---|---|
| Any landlord reply | [LANDLORD_REPLY_PLAYBOOK.md](LANDLORD_REPLY_PLAYBOOK.md) | Voss tactical empathy: mirror, label, calibrated questions, accusation audit, no-oriented questions |

## Outreach copy / tactics (test these)

| File | Purpose |
|---|---|
| [SUBJECT_LINES.md](SUBJECT_LINES.md) | 15 ranked email subject variants (data-driven) |
| [SMS_VARIANTS.md](SMS_VARIANTS.md) | 10 TCPA-compliant SMS bodies for when toll-free approves |
| [LOOM_PLAYBOOK.md](LOOM_PLAYBOOK.md) | 90-second video pitch template (4-22% reply rate per research) |
| [RESEARCH_INSIGHTS.md](RESEARCH_INSIGHTS.md) | Cited research: what actually converts for trade contractor cold outreach |

## Public-facing

| File | Purpose |
|---|---|
| [portfolio.html](portfolio.html) | Single-page portfolio site listing all built mockups. Open in browser to preview. |

## Frequently-asked questions Sam might have

**"Where do I keep client photos / files?"**
For now, Google Drive folder per client. Future: a `clients/{license}/` folder in the repo.

**"How do I track which subject line is winning?"**
Run `python send_outreach.py stats` — shows reply rate by send. (Subject A/B variation is wired in src/email_send/sender.py per license_num hash.)

**"How do I rotate to a different mockup variant?"**
Re-render with: `rm out/mockups/{license}.html out/screenshots/{license}.png && python send_outreach.py mockup --limit 1`

**"How do I handle a contractor who's pushy on price?"**
Read [OBJECTIONS_LIVE.md](OBJECTIONS_LIVE.md) row "Can you do it cheaper?" → offer $50 off in exchange for testimonial after launch.

**"What if I'm losing my voice on a call?"**
Read [PHONE_SCRIPTS.md](PHONE_SCRIPTS.md) "When they get aggressive" — stay calm, validate their concern, offer to remove them from list.

## Last-resort references

If you can't find what you need above:
- The full Python codebase is at `C:\Users\samth\projects\website-outreach\`
- The README has the runbook
- The dashboard has live numbers: `start out/dashboard.html`
- The Obsidian project memo: `C:\Users\samth\Documents\brain\claude-memory-main\project_website_outreach.md`


## Links
- MOC: [[Cold Outreach]]
- MOC: [[Sales Kit]]
