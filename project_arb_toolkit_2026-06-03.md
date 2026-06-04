---
name: Arb Toolkit
description: Bundle of distributable Claude Skills sold as the perk of Sam's STR Skool; shared SKILL.md + references/ + examples/ + README template. 4 skills shipped 2026-06-03 (deal-screener, room-stylist w/ photo→render, job-app-tailor, reply-guy).
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
| **str-room-stylist** | STR hosts | Room photo + market + budget → autonomous deep-research furnishing plan + Amazon affiliate cart + "after" render of their actual room. Never invents ASINs. See detailed section below. |
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

## STR Room Stylist — advanced 2026-06-03 (Sam's favorite idea so far)

Sam's refined vision: user sends a room **photo** + market + budget → agent runs an **autonomous deep-research pass ("works ~20 min")** → personalized furnishing plan → shopping list w/ Amazon affiliate links → **one-click add-to-cart** → **"after" render of their actual room**. Best in Claude Code (can loop minutes); claude.ai Project = shorter draft.

**SKILL.md = 7-phase workflow:** 0 intake (read photo + 4 Qs) · 1 infer location context (climate, guest profile that market draws, price tier from nightly rate, local aesthetic) · 2 plan (furnishing template) · 3 research real products live (the long part — Amazon-first, cache as you go) · 4 optimize to budget · 5 output · 6 cart link · 7 **visualize**.

**Files:** `SKILL.md`, `references/furnishing-templates.md` (per-room M/S/N checklist + budget allocation %), `references/amazon-cart-and-affiliate.md` (affiliate setup + `/gp/aws/cart/add.html` multi-ASIN URL format), `references/render-visualization.md` (image-to-image method), `catalog/seed-catalog.json` (**growing cache**, NOT hand-fill — agent appends verified finds; seeded w/ Sam's Tara House picks), `scripts/build_cart_url.py`, `scripts/render_room.py`, `examples/sample-run.md`. Zip ~19 KB.

**Monetization unlock:** Amazon Associates affiliate links → tool is FREE to user, Sam earns ~$180–300 commission per unit furnished on the buyer's money.

**Two tested scripts:**
- `build_cart_url.py` — builds Amazon add-to-cart deep link from ASINs+qty w/ AssociateTag; **skips null ASINs, never builds on a fake/missing ASIN** (tested 3 paths).
- `render_room.py` — **image-to-image edit** of the REAL room photo via Nano Banana (Gemini 2.5 Flash Image, model `gemini-2.5-flash-image`), steered by product ref images → "after" PNG. Reads `GEMINI_API_KEY` from env or `.env` (**never chat**). `google-genai` installed; failure paths tested. Model-agnostic fallback = paste-ready edit prompt for ChatGPT/Gemini (no key needed). Always labeled **mockup**.

**Render method (references/render-visualization.md):** EDIT don't generate (base = real photo, never a from-scratch room). 5-part prompt: anchor what stays → list edits → tie to product ref images → style/quality → negative constraints. ≤3 items = single fused edit; more = iterative.

**PROVEN REAL RUN — 3216 W De Leon St, South Tampa 33609** (already-furnished unit → ran as **upgrade pass**, not scratch build). Headline insight = Tampa **30+ day MTR** model + Westshore **business/medical travelers** → biggest gap is **no workspace** → add desk + chair. 5 real ASINs found via WebSearch (cached): `B08Z7BP5L3` Armocity oak corner desk · `B0F9F3HFX9` Rowill boucle chair no-wheels · `B0CQWZSFDK` 5x7 washable rug · `B0C3QJSS56` OCWHT rattan flush mount (wood base, ties to oak) · `B07RV55RX3` Home Zone slim dual trash/recycle. Cart link built (~$395). Saved as `examples/sample-run.md`. ⚠️ Amazon blocks WebFetch price reads → prices search-estimated, **confirmed at cart, never fabricated**.

## TOMORROW'S DROP — pending / pickup
- **Set `GEMINI_API_KEY`** (`setx GEMINI_API_KEY "..."`, key from aistudio.google.com/apikey) → then `render_room.py` produces the De Leon "after" image. Mechanism fully built; only the key is missing (Sam-only, billing-tied).
- **Amazon Associates tag** — sign up, replace `citysidestays-20` placeholder in cart links. This is the money layer.
- **Fill 3 De Leon gaps** (kitchen runner, coffee-station tray + canisters, faux plant) + lock live prices via browser.
- Bundle distribution: free lite skill (lead magnet) → paid Skool tier (full vault + monthly drops). Deal Screener has LAUNCH.md copy ready (Gumroad/Skool/IG/Reddit); Room Stylist needs its own launch copy ("send me a photo of your room").

## Next candidates

Landlord Objection Coach, Airbnb Listing Doctor (note: AirCheck product already covers listing audit — keep distributable version distinct).
