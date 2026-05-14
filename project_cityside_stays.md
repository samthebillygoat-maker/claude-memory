---
name: CitySide Stays — Operating Memo
description: National STR arbitrage operation — 1,052 deduped leads, 252 at 3x+, VA onboarded 2026-05-07 on OpenPhone, first deal in negotiation Tampa $1,675 counter, premium-tier methodology locked
type: project
---

# CitySide Stays — Operating Memo

_created 2026-05-07_

**Brand:** CitySide Stays (LLC pending — tenant of record on all leases)
**Repos:**
- Lead pipeline: `C:\Users\samth\projects\landlord-outreach`
- Compliance site: `C:\Users\samth\projects\citysidestays-site`

**Status (2026-05-07):** 1,052 leads in master file. 252 at 3.0x+. 164 phone-verified. VA onboarded today, going live this week on OpenPhone. First deal in negotiation: Tampa, awaiting owner response.

## The rule (state first)

CitySide Stays only signs leases that meet **all** of these:

1. **12-month minimum lease** — no 6-month, no seasonal. Auto-detected and rejected by polish_v2.
2. **$1,200+ monthly rent floor** for premium tier — avoid sub-$1,000 ultra-rural markets.
3. **Real tourist destinations only** — no coal country, no trailer-park ratios. Sam's words: "i dont want cheap inbreds at my place."
4. **2BR+ minimum**, listing posted within last 30 days, STR-permissive zoning, ratio gate cleared.

**Why:** Cheap-rural ratios look great on paper but the STR demand isn't there year-round, the comp data is thin, and the property condition / tenant pool / regulatory enforcement are unpredictable. Premium tier (real destinations + serious rent) is where guaranteed rent + professional ops actually clears margin.

**How to apply:** The "Premium" filter button in `data\VA_CALL_LIST.html` enforces all three rules — VA defaults to that view. Anything below the floor stays out of the daily call plan.

## Pipeline numbers (as of 2026-05-07)

| Metric | Count |
|--------|-------|
| Unique deduped leads | 1,052 |
| At 3.0x+ ratio | 252 |
| At 2.5x+ ratio | 350 |
| Phone-verified | 164 |
| Source files | 79 |

Master file: `C:\Users\samth\projects\landlord-outreach\data\leads_master_2026-05-07.md`

## Tools shipped

### Lead pipeline (3-script chain)
- `compile_master.py` — merges 79 source files
- `polish_v2.py` — auto-detects short leases, normalizes rent/BR, dedupes
- `export_html_csv.py` — emits VA HTML + CSV
- Outputs:
  - `data\leads_master_2026-05-07.md`
  - `data\VA_CALL_LIST.html` (click-to-call, sortable, Premium filter, YES/MAYBE/VM/NO buttons → localStorage)
  - `data\VA_CALL_LIST.csv`
  - `data\VA_DAILY_CALL_PLAN_2026-05-07.md` (top 25 with hooks)

### AirDNA modules (built, not yet live)
- `src\landlord_outreach\airdna\bulk_export.py` — Playwright/patchright stealth, 8 markets, weekly gate, ban detection. **Verdict: probably blocked by AirDNA Pro tier.** Sam said "its not a option."
- `src\landlord_outreach\airdna\rentalizer.py` — hardened anti-detection: headed mode, session warm-up, 18-25 per batch with 4-7min rests, max 3 batches/day, mouse jitter, XHR capture. **NOT YET RUN** — needs `.env` creds + one selector verification pass before live use.

### Compliance landing site
- `C:\Users\samth\projects\citysidestays-site\` — 3 pages (index.html, privacy.html, terms.html)
- TCPA-compliant SMS consent checkbox
- Ready for Netlify drag-and-drop deploy
- Required to unblock Twilio toll-free verification

## VA workflow

- **Phone:** OpenPhone, $15/mo, 7-day free trial. Chosen over Google Voice (spam-flagged) and JustCall/Kixie (overkill day 1).
- **Daily quota:** 80 dials.
- **Source list:** `data\VA_CALL_LIST.html` (Premium filter on by default).
- **Status tracking:** YES / MAYBE / VM / NO buttons in the HTML save to localStorage. End-of-day, VA logs to a Google Sheet (one row per dial).
- **Cold call SOP:** `C:\Users\samth\CitySide_Stays_VA_Cold_Call_SOP.txt`
- **Follow-up email template:** `C:\Users\samth\CitySide_Stays_Followup_Email.txt`
- **TCPA hard rules:** never call before 8am or after 9pm local, always disclose Airbnb upfront, never hide it.
- **Rent quoting:** VA never quotes rent — routes to Sam (Ackerman sequence).

## Active deals

### Tampa — 4207 S Dale Mabry Hwy, Tampa FL 33611
- Grand Key apartment unit
- Owner asking $1,850/mo, 3-year lease
- Sam had phone call 2026-05-07; owner asked for written info
- Counter sent: **$1,675/mo + 4 weeks free + COI in lieu of deposit**
- Status: **AWAITING OWNER RESPONSE**
- Risks: Grand Key is managed apartment complex (HOA STR risk), Tampa STR restrictions in residential zones (Fairoaks neighborhood may not qualify) — needs HOA permission addendum before signing.

## Top 5 highest-conviction call targets (2026-05-07 verified)

1. 147 Weaver Creek Rd, Blue Ridge GA — $1,900/2BR, 4.30x, (706) 455-8800 — mtn view + furnished
2. 2147 Henrietta Fulford Pl, Gulf Shores AL — $1,450/3BR, 4.14x, (251) 210-6667 — 12mo confirmed
3. 1375 Lion Mtn Dr, Whitefish MT — $3,200/2BR, 3.90x, (406) 862-5994
4. 1001 Beach Hollow Ct, Sevierville TN — $1,800/2BR, 3.78x, (865) 436-2849 — hot tub + Smokey view
5. 133 Yellowbird Trl, Blue Ridge GA — $2,350/2BR, 3.75x, (706) 258-8105

## Active premium markets

- Premium Smokies cabins (Sevierville, Gatlinburg, Pigeon Forge)
- Premium beach: Gulf Shores AL, Destin, PCB, AMI, HHI, Myrtle
- Premium ski: Park City, Whitefish, Big Bear, Stowe
- Premium lakes: LOZ, Geneva, Door County, Tahoe NV side
- Branson MO + LOZ fresh
- Catskills + Hudson Valley
- Hudson, ADK, East PA (Jim Thorpe)
- Blue Ridge GA, Chattanooga TN
- Tampa FL (USF MTR stack, FS 509.032 zones only)

## Markets explicitly rejected (don't re-research)

Saratoga Springs city, Ithaca city, Marquette MI, Truckee, Telluride town residential, Leavenworth city, Lincoln City OR R1, Jackson WY outside Lodging Overlay, Hill City/Custer/Deadwood SD, Moab residential, Wrightsville Beach town, Saugatuck, Austin Type 2 (cap closed), Hawaii Maui & Oahu, MS Gulf Coast inland, FL Atlantic premium (math doesn't work), Mid-Atlantic premium (Cape May/Lewes math fails).

## Pending this week

- [ ] Send Tampa $1,675 counter email (drafted, ready)
- [ ] Deploy citysidestays-site to Netlify (5 min)
- [ ] Submit Twilio toll-free verification with deployed URL + screenshot
- [ ] VA goes live — OpenPhone signup → Google Sheet → first 5 practice calls
- [ ] Verify top 10 leads in AirDNA Rentalizer manually
- [x] CitySide Stays one-pager PDF — `Downloads\CitySideStays_Overview_2026-05-08.pdf` (v2 honest)
- [x] STR permission addendum template — `Downloads\CitySideStays_LeaseAddendum_2026-05-08.pdf` (v2)
- [x] LLC formation — completed 2026-04-03 (FL formation doc in Downloads)
- [ ] Get $1M GL policy quote from Proper Insurance / Steadily (sample COI built; need real quotes — Sat task)
- [ ] Buy `citysidestays.com` ($12 on Cloudflare) → point at Netlify

## Owner outreach collateral (built 2026-05-08 / -11)

**How to apply:** attach as a pack to every PM/owner cold email or follow-up. Use the SAMPLE COI + AirCover summary to address "but what if a guest trashes the place / sues me?" objections in writing.

- `Downloads\CitySideStays_Overview_2026-05-08.pdf` — one-page company overview (v2 honest mixed-use)
- `Downloads\CitySideStays_LeaseAddendum_2026-05-08.pdf` — platform-hosting addendum (12 clauses, STR indemnity, adaptive termination)
- `Downloads\CitySideStays_Lease_Amending_Agreement_2026.pdf` — alternate short-form amendment (built 2026-05-11 from Expedition Sunset template; simpler 2-pager when full addendum is overkill)
- `Downloads\CitySideStays_SampleCOI_2026-05-11.pdf` — **SAMPLE** ACORD 25-style COI showing the $1M/$2M GL structure with [LANDLORD NAME] as Additional Insured. Clearly watermarked SAMPLE / NOT IN FORCE — pre-binding reference only. Real COI issued by broker at lease signing.
- `Downloads\AirCover_Summary_2026-05-11.pdf` — plain-English summary of Airbnb's AirCover for Hosts ($3M damage + $1M liability per booking) showing the 3-layer stack (AirCover → CGL → addendum indemnity)

**Why this matters:** owners' #1 objection is liability/property damage risk. The collateral pack converts that objection into "I see exactly how I'm protected" before they even ask.

## Related memos

- `project_landlord_outreach.md` — the underlying scraping pipeline (Plan A/B/C build)
- `project_miami_arbitrage.md` — broader CitySide Stays business memo (markets, military strategy)
- `reference_str_master_prompt.md` — STR session system prompt
- `reference_str_deal_criteria.md` — Double Rent Rule, regs checklist
- `feedback_lead_freshness.md` — 30-day post date rule
- `feedback_lead_signals.md` — short-lease = negative signal

_updated 2026-05-11 — Stripe fully wired for The Friday Pack; CitySide collateral pack complete (overview + addendum + amending agreement + sample COI + AirCover summary)._
