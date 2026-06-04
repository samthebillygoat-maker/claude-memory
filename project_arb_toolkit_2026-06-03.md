---
name: Arb Toolkit
description: Bundle of distributable Claude Skills sold as the perk of Sam's STR Skool; shared SKILL.md + references/ + examples/ + README template. Reply Guy (B2) shipped 2026-06-03.
type: project
---

# Arb Toolkit — distributable Claude Skills bundle

Productize Claude Skills as a bundle, distributed as the tangible perk of the STR-arbitrage Skool community (free tier = 1 lite skill lead magnet; paid tier = full vault + monthly new-skill drops + updated market data + community).

**Key insight:** static skill files can't be a true subscription (once downloaded, owned forever) — recurring value = monthly drops + updated comps/formulas + Skool community, NOT the files themselves. Free skill caps advanced features behind paid = natural upgrade.

## Template structure (every bundle skill mirrors this)

```
<skill>/
├── SKILL.md                 # frontmatter (name + description) + triggers, method, guardrails, output format
├── README.md                # dual-use install (skill folder + Claude.ai Project) + bundle note + honesty guarantees
├── references/*.md          # the deep logic, split by concern
└── examples/sample-run.md   # input → output
```
Dual-use: drop folder into `~/.claude/skills/` **or** paste SKILL.md + refs into a Claude.ai Project. Every skill ships zipped.

## Skills shipped (all at `C:\Users\samth\projects\<slug>\` + `.zip`)

| Slug | Audience | What it does |
|------|----------|--------------|
| **str-deal-screener** (flagship/A1) | STR arbitrage investors | GO/MAYBE/NO-GO via Double Rent Rule + full P&L + 4 Non-Negotiables + back-solved max rent + Ackerman ladder. Has LAUNCH.md (Gumroad + Skool + IG/X + Reddit). Overlaps internal [[triage-deal]] but this is the clean *distributable* version. |
| **str-room-stylist** | STR hosts | Room photo + market + budget → autonomous deep-research furnishing plan + Amazon affiliate cart. Never invents ASINs. |
| **job-app-tailor** (B1) | Job seekers / students | Tailors a resume/cover letter to a job post; ATS keyword match + rewrite rules. Built against A1 template. |
| **reply-guy** (B2) | Small biz / freelancers | Pastes a review/email/DM → drafts an on-brand reply in the owner's voice. |

## Reply Guy (B2) — shipped 2026-06-03

Built mirroring str-deal-screener exactly. Files: `SKILL.md`, `references/voice-profile.md` (3-question voice intake — tone/name, always-say, never-say — stored as a reusable block the user pastes back each session), `references/reply-playbooks.md` (5 scenarios + de-escalation ladder), `examples/sample-run.md`, `README.md`. Zipped to `reply-guy.zip` (~11 KB).

Handles 5 scenarios: positive review (gracious), negative review (de-escalate → take offline → recover), pricing/availability, refund request, cold sales email.

**Guardrails (the product's spine):**
- Never promises money the owner hasn't authorized — refunds/discounts/comps stay as `[bracketed placeholders]` for the owner to fill or delete.
- Never invents facts about the business (hours, policies, prices, ship dates) — unknowns → `[placeholder]`.
- Never argues in public on a bad review; acknowledge + move offline.
- Injury/illness/discrimination/legal-threat messages → neutral holding reply + tell owner to respond personally / loop counsel.

## Next candidates

Landlord Objection Coach, Airbnb Listing Doctor (note: AirCheck product already covers listing audit — keep distributable version distinct).
