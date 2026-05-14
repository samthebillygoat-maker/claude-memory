# CitySide Stays — Master Dashboard

_Last updated: 2026-05-07_

---

## Section 0: CitySide Stays Pipeline Status (2026-05-07)

| Metric | Value |
|--------|-------|
| Total deduped leads | 1,052 |
| At 3.0x+ ratio | 252 |
| At 2.5x+ ratio | 350 |
| Phone-verified | 164 |
| Source files | 79 |
| VA status | Onboarded 2026-05-07, OpenPhone going live this week |
| Phone system | OpenPhone $15/mo |
| First deal in negotiation | Tampa 4207 S Dale Mabry Hwy — $1,675/mo counter pending owner reply |
| Compliance site | `C:\Users\samth\projects\citysidestays-site\` (ready, not yet deployed) |
| Master leads file | `C:\Users\samth\projects\landlord-outreach\data\leads_master_2026-05-07.md` |
| VA HTML call list | `C:\Users\samth\projects\landlord-outreach\data\VA_CALL_LIST.html` |
| VA daily call plan | `C:\Users\samth\projects\landlord-outreach\data\VA_DAILY_CALL_PLAN_2026-05-07.md` |

**Methodology rules locked in 2026-05-07:** 12-month min lease, $1,200+ rent floor, premium destinations only, 2BR+ minimum, 30-day post date, STR-permissive zoning. Full memo: [[project_cityside_stays]].

---

## Section 1: How to Start Each Product

### Hail Mary
**What:** AirDNA screenshots → 20-page investor-grade STR arbitrage acquisition PDF with GO/MAYBE/NO-GO verdict + Ackerman negotiation playbook
**Repo:** `C:\Users\samth\hail-mary\`
**Start:** `cd C:\Users\samth\hail-mary && npm run dev`
**URL:** http://localhost:3000
**Key files:**
- `src/proxy.ts` — middleware (renamed from middleware.ts in Next 16)
- `src/lib/` — acquisition formula + scenario math
- `prisma/schema.prisma` — 10-table schema

---

### DealMemo
**What:** SMS-only STR deal screener — text any deal, get GO/MAYBE/NO-GO verdict in <4 lines, no app required
**Repo:** `C:\Users\samth\dealmemo\`
**Start:** `cd C:\Users\samth\dealmemo && npm run dev`
**URL:** http://localhost:3000
**Key files:**
- `src/app/api/sms/route.ts` — Twilio webhook handler + quickVerdict logic
- `src/app/page.tsx` — landing page with example text exchange

---

### Deal Engine
**What:** RentRadar (saved search → SMS on match) + Inbox-to-Lead (Gmail AI parser). Top-of-funnel for Hail Mary. $29/mo
**Repo:** `C:\Users\samth\deal-engine\`
**Start:** `cd C:\Users\samth\deal-engine && npm run dev`
**URL:** http://localhost:3000
**Key files:**
- `src/lib/matching.ts` — pure listing-match function
- `src/app/api/cron/` — rent-radar + gmail-pull cron stubs
- `vercel.json` — cron schedule (needs Vercel to run, not local dev)

---

### SuperhostTracker
**What:** Daily Apify scrape of Airbnb listings → SMS alert before Superhost demotion. $9/mo per listing
**Repo:** `C:\Users\samth\superhost-tracker\`
**Start:** `cd C:\Users\samth\superhost-tracker && npm run dev`
**URL:** http://localhost:3000
**Key files:**
- `src/lib/thresholds.ts` — Superhost criteria as pure functions
- `src/app/api/cron/daily-scrape/route.ts` — cron stub (needs Vercel to run)
- `vercel.json` — cron at 6am UTC daily

---

### AirCheck
**What:** Paste Airbnb URL → Comp-Card + AirCover take-home calc + ListingDoctor AI audit. $29/mo or $99 one-time
**Repo:** `C:\Users\samth\aircheck\`
**Start:** `cd C:\Users\samth\aircheck && npm run dev`
**URL:** http://localhost:3000
**Key files:**
- `src/lib/comps.ts` — comp analysis (pure, testable)
- `src/lib/aircover.ts` — take-home calculator (pure, testable)
- `src/app/api/audits/route.ts` — main audit flow stub

---

### Website Outreach (CA Contractor Cold Engine)
**What:** Python cold-outreach engine targeting CA C-39 roofers. Scrapes CSLB + contractor sites, sends personalized emails with inline mockups
**Repo:** `C:\Users\samth\projects\website-outreach`
**Branch:** `feat/cold-outreach`
**Start:** `cd C:\Users\samth\projects\website-outreach && python nightly.py`
**Dashboard:** `out/dashboard.html` (open in browser)
**Key files:**
- `nightly.py` — main cron entrypoint
- `NEXT_ACTIONS.md` — morning checklist
- `sales/` — 14 sales kit docs (pricing, reply playbook, objection scripts)

---

### Landlord Outreach Pipeline
**What:** Python + scrapling + SQLite pipeline to find STR-friendly landlords in Sevierville/Gatlinburg/Tampa/Miami from Craigslist + Apartments.com
**Repo:** `C:\Users\samth\projects\landlord-outreach`
**Start:** `cd C:\Users\samth\projects\landlord-outreach && python -m landlord_outreach.scrape <market>`
**Markets:** `sevierville-tn` | `gatlinburg-tn` | `tampa-fl` | `miami-fl` | `gulf-shores-al` | `branson-mo` | `chattanooga-tn`
**Lead scout command:** `/str-lead-scout` — run any time for fresh leads with post-dates
**Key files:**
- `markets.yaml` — add/remove markets without code changes
- `docs/superpowers/specs/2026-05-06-landlord-outreach-design.md` — full spec
- `docs/superpowers/plans/2026-05-06-landlord-outreach-plan-a-foundation.md` — Plan A build log

---

## Section 2: STR Operations Quick Reference

### Double Rent Rule
```
Monthly Rent × 12 × 2 = Minimum Target Annual STR Revenue
Example: $2,500/mo × 12 = $30,000 annual rent → need $60,000+ STR revenue
```
- Negotiation target rent = Annual Projected Revenue / 24
- Walk-away ceiling = Annual Projected Revenue / 18

### Active Markets
| Market | Ratio | Notes |
|--------|-------|-------|
| Sevierville, TN | — | Smokies gateway, high seasonal demand |
| Gatlinburg, TN | — | Tourist core, cabin-heavy |
| Tampa, FL | — | USF MTR stack, STR-permissive zones (FS 509.032) |
| Miami, FL | — | High ADR, stricter zoning — verify per neighborhood |
| Gulf Shores, AL | 2.1–3.1x | $45/yr permit only, no NOO ban. Beach seasonal — use MTR in off-season. Added 2026-05-07 |
| Branson, MO | 2.7–4.0x | $250 permits, widest margins. Jan-Mar slow, plan reserves. Added 2026-05-07 |
| Chattanooga, TN | 1.9–2.2x | Year-round demand. NOO restricted to C-2/C-3/C-4/UGC — verify zoning before signing. Added 2026-05-07 |

### Lead Sources
- **Craigslist** — `housing > apts/housing for rent` — free, no proxies
- **Apartments.com** — free, no proxies
- **FRBO** (For Rent By Owner) — direct landlord contacts
- **Zillow** — comps and listing lookup

### VA Outreach Assets
- Cold call SOP: `C:\Users\samth\CitySide_Stays_VA_Cold_Call_SOP.txt`
- Follow-up email template: `C:\Users\samth\CitySide_Stays_Followup_Email.txt`
- VA meeting scheduled: 2026-05-07

### Value Positioning (use on every landlord call)
- Guaranteed rent paid 2 weeks in advance
- Professional cleaning after every stay
- Noise monitors + Ring cameras + smart locks
- $1M insurance per unit
- One point of contact, one lease
- Always disclose Airbnb upfront — never hide it

---

## Section 3: Memory & Claude Quick Reference

### How claude-mem works
- Claude reads `MEMORY.md` at session start as the index
- Each entry points to a detailed memo file (project/feedback/user)
- Claude updates files during sessions — always append, never overwrite daily notes

### Vault location
`C:\Users\samth\Documents\brain\claude-memory-main\`

### What MEMORY.md is for
One-line index of every memo. Claude uses it to know what context exists before reading any file. If it's not in MEMORY.md, Claude won't find it.

### How to resume a Claude session with context
1. Open a new Claude Code session
2. Say: "Read my vault at `C:\Users\samth\Documents\brain\claude-memory-main\MEMORY.md` and load context for [project name]"
3. Claude will read MEMORY.md, find the relevant memo, and load it
4. For STR sessions, also paste the master prompt from `reference_str_master_prompt.md`

### STR Master Prompt
Full advisor prompt lives at: `C:\Users\samth\Documents\brain\claude-memory-main\reference_str_master_prompt.md`
Paste into any Claude session for full STR context (underwriting, negotiation, operations, scaling).

---

## Section 4: Open Loops

See today's daily note: [[Daily Notes/2026-05-07]]

Current open items (as of 2026-05-07):
- [ ] Tampa 4207 S Dale Mabry — send $1,675 counter email (drafted), await owner response
- [ ] Deploy citysidestays-site to Netlify (5 min) → submit Twilio toll-free verification
- [ ] VA go-live — OpenPhone signup → Google Sheet → first 5 practice calls
- [ ] Verify top 10 leads in AirDNA Rentalizer manually
- [ ] CitySide Stays one-pager PDF + STR permission addendum template
- [ ] LLC formation, $1M GL insurance quote, buy citysidestays.com
- [ ] Website Outreach — Twilio toll-free IN_REVIEW, ETA 2026-05-10 to 2026-05-13
- [ ] Hail Mary — Step 3 (Auth + Stripe flow + founding counter) pending
- [ ] Deal Engine, SuperhostTracker, AirCheck — all need real API keys before launch
