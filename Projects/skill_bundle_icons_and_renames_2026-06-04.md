# Skill Bundle — New Skills, Icon Set & Renames (2026-06-04)

Work session extending the distributable Claude Skills bundle ([[project_arb_toolkit_2026-06-03|Arb Toolkit]]). Built two skills, gave all four a matching icon set, and locked final product names.

## Final product names (renamed this session)
| Name | Slug / folder | Was | What it does |
|------|---------------|-----|--------------|
| **Flip Scout** | `flip-scout` | (unchanged) | Finds + scores distressed flip houses, GO/MAYBE/NO-GO |
| **Offer Bandit** | `offer-bandit` | job-app-tailor | Resume + job posting → tailored resume, cover letter, ATS keyword-gap report, 3 interview Qs |
| **Reply Flow** | `reply-flow` | reply-guy | Drafts on-brand replies to reviews/emails/DMs in the owner's voice |
| **Parent Admin Brief** | `parent-admin-brief` | (new) | Aging-parent bills/statements → monthly family brief (what's due / changed / needs a decision / who's on point) |

All live under `C:\Users\samth\projects\<slug>\` with the template: `SKILL.md` + `references/` + `examples/sample-run.md` + `README.md` + `icon.svg`/`icon.png` + `<slug>.zip`.

## New skill: Parent Admin Brief
- Came out of a "what would my whole family pay for" brainstorm. Answer: **older parents + adult kids**, pain = **coordination + money/bills**. That intersection is a fundable space (Carefull/Onist exist).
- Deliberately **paste-in / brief-out, nothing linked, nothing stored** — no account access, no credentials, never moves money. That trust boundary is what makes it usable by a non-technical parent/sibling.
- Hard guardrail: **never guesses an amount/date** — missing data becomes `[needs confirming]`. Not financial/medical/legal/tax advice; it surfaces decisions, names who should make them.
- Road-test plan: run it on one real parent bill for 2 months; if the family actually uses the group-chat summary, build the real shared hub (logins + billing).

## Offer Bandit (was job-app-tailor)
- Built earlier today, renamed tonight. Guardrail: never fabricate experience/credentials/metrics; flag gaps honestly; inferences tagged `[confirm?]`.

## Icon set (all 4)
Matching squircle / cream foreground / one accent color each + shared gold detail — reads as a bundle in a grid.
- Flip Scout — emerald, house-in-magnifier + gold flip arc
- Offer Bandit — indigo, **bandit domino mask over an offer letter** + gold star seal (redrawn from the earlier resume-needle version to be on-theme)
- Reply Flow — coral, two chat bubbles (message + reply)
- Parent Admin Brief — teal, checklist clipboard + heart clip
- Rendered SVG→PNG @1024 via `sharp` (no ImageMagick on this box; Windows `convert` is the disk tool).
- Drag-to-email copies collected at `C:\Users\samth\projects\skill-icons\` (`flip-scout.png`, `offer-bandit.png`, `reply-flow.png`, `parent-admin-brief.png`).

## Ties into
- [[project_arb_toolkit_2026-06-03|Arb Toolkit]] — Flip Scout, Offer Bandit, Reply Flow are the bundle; Parent Admin Brief is a **new audience** (families, not STR investors) — may deserve its own bundle/line.
- Same SKILL.md template as the flagship STR Deal Screener.

## Open / next
- Decide whether Parent Admin Brief ships inside the Arb Toolkit or as a separate "family tools" product (different audience).
- Optional: smaller icon sizes (512/256 favicons, Skool thumbnails) + transparent-bg variants.
- Refresh `parent-admin-brief.zip` / `reply-flow.zip` if icons change again (offer-bandit zip already rebuilt with new icon).
