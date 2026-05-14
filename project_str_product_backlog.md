---
name: STR Product Idea Backlog
description: Ten brainstormed STR-adjacent SaaS ideas with consolidation strategy, pricing, target buyer, and shippability notes. Source for future product builds.
type: project
---

# STR Product Idea Backlog — 2026-04-29

> **2026-05-04 update:** Portfolio has expanded from the consolidated 5 to 11 scaffolds on ports 3001–3011. Current product map lives in `project_str_product_portfolio.md`. This file is preserved as the original brainstorm/consolidation history.


Ten ideas brainstormed in two batches, then consolidated to 5 products. Each is in Sam's STR/arbitrage adjacency, designed to reuse Hail Mary + DealScout infrastructure where possible.

## Tonight's build queue — ALL 5 SCAFFOLDED ✅
1. **Hail Mary DD Tier** ✅ commit `ea4ed35` (added inside hail-mary repo)
2. **DealMemo** ✅ commit `3189dc0` (`C:\Users\samth\dealmemo\`)
3. **Deal Engine** ✅ commit `21b0542` (`C:\Users\samth\deal-engine\`)
4. **SuperhostTracker** ✅ commit `20944d4` (`C:\Users\samth\superhost-tracker\`)
5. **AirCheck** ✅ commit `7cc9f99` (`C:\Users\samth\aircheck\`)

All 5 type-check clean, Prisma clients generate, ready for real keys tomorrow.

---

## The 10 raw ideas

### 1. RentVet
Paste any landlord's name/phone → returns a STR-friendliness score. Reddit/Google complaints scrape + Claude classification + ToS-scan of any listed properties.
- **Buyer:** operator about to spend $500 on furnishing
- **Price:** $9/lookup or $39/mo
- **Stack:** one Apify actor + one Claude call + thin Next page
- **Disposition:** rolled into Hail Mary DD tier (#1 above)

### 2. ClauseScout
Drop a lease PDF → 60-second STR risk report highlighting subletting clauses, Airbnb prohibitions, assignment language, suggested redlines.
- **Buyer:** same as Hail Mary
- **Price:** $29/lease or bundled
- **Stack:** PDF.js + Claude with fixed extraction prompt + React-PDF output
- **Disposition:** rolled into Hail Mary DD tier (#1 above)

### 3. PermitPing
Enter city + address → current STR regulatory status + watch alert if ordinance changes.
- **Buyer:** Hail Mary user, pre-close
- **Price:** $5/check, $19/mo unlimited + alerts
- **Stack:** scrape 10–20 top-market city sites; v1 covers ~80% demand
- **Disposition:** rolled into Hail Mary DD tier (#1 above)

### 4. Comp-Card
Paste an Airbnb URL → 1-page "should I list higher?" card showing 10 nearest comps' ADR/occupancy/title patterns.
- **Buyer:** existing Airbnb host (10× larger TAM than arbitrage operators)
- **Price:** $7/card, $29/mo
- **Stack:** Apify Airbnb actor + React-PDF template
- **Disposition:** rolled into AirCheck (saved for later)

### 5. Inbox-to-Lead
Connect Gmail → AI auto-extracts every "for rent" inquiry reply into a structured lead row (address, rent, landlord, response time).
- **Buyer:** anyone running outbound to landlords
- **Price:** $19/mo
- **Stack:** Gmail OAuth + Claude classification + Postgres + Hail Mary's Lead table
- **Disposition:** rolled into Deal Engine (#3 above)

### 6. AirCover Calc
Paste any active Airbnb URL → real take-home after Airbnb fees, cleaning costs, taxes, platform deductions.
- **Buyer:** existing host
- **Price:** $9/calc, $19/mo
- **Stack:** Airbnb scrape + 30-line math + one page
- **Disposition:** rolled into AirCheck (saved for later)

### 7. SuperhostTracker
Monitors Airbnb stats daily, alerts the moment a metric drops below Superhost threshold (response rate, rating, cancellations).
- **Buyer:** existing host who values Superhost badge
- **Price:** $9/mo per listing
- **Stack:** nightly cron + Apify scrape + Twilio SMS — 90% Hail Mary infra reuse
- **Disposition:** standalone, saved for focused build session

### 8. ListingDoctor
Paste your Airbnb listing URL → AI scores title, photo order, description, amenities, pricing strategy + prioritized fix list with 1-click rewrites.
- **Buyer:** every Airbnb host (largest TAM in this list)
- **Price:** $19 one-time scan, $49 with rewrites
- **Stack:** scrape + one big Claude prompt + Next page
- **Disposition:** rolled into AirCheck (saved for later)

### 9. RentRadar
Drop city + budget → app texts you the moment a Craigslist/Zillow/Apartments.com listing matches your STR criteria (rent, beds, sublet language).
- **Buyer:** active arbitrage hunter
- **Price:** $29/mo
- **Stack:** DealScout's existing Craigslist monitor + scrapers, productized for non-technical users
- **Disposition:** rolled into Deal Engine (#3 above)

### 10. DealMemo
Twilio inbound number. Text any deal description → 60-second AI reply with verdict + 3-bullet rationale + walk-away rent. No app, no login.
- **Buyer:** any operator who lives on their phone
- **Price:** $19/mo unlimited
- **Stack:** Twilio inbound webhook + 1 Claude call + reuse `src/lib/acquisition.ts` from Hail Mary
- **Disposition:** standalone, scaffolding tonight (#2 above)
- **Distribution:** screenshot a real text exchange on Twitter → "text DEAL to (xxx) xxx-xxxx, free trial." The demo IS the product.

---

## The consolidated 5 (sales-optimized)

### 1. Hail Mary DD Tier — bundle of #1 + #2 + #3
$29/mo upsell tier on top of Hail Mary. Same login, same Stripe customer, same buyer journey. ARPU jumps $147 → $176, ~80% margin. **Highest-leverage action; not a new SaaS.**

### 2. AirCheck — bundle of #4 + #6 + #8
Existing-host optimizer. One Airbnb URL → comps + real take-home + listing audit. $29/mo or $99 one-time. **TAM is every Airbnb host, not just arbitrage operators.** Different buyer = no Hail Mary cannibalization.

### 3. Deal Engine — bundle of #5 + #9
Top-of-funnel companion to Hail Mary. Monitor scrapers + SMS alerts + Gmail-to-CRM. $29/mo. **Pairs naturally: "Deal Engine finds them, Hail Mary analyzes them."** DealScout scraper code is the foundation.

### 4. SuperhostTracker — standalone
Daily monitoring + SMS alerts. $9/mo per listing. **Sticky: cancellation rate near zero because the value is "we caught it before Airbnb did."**

### 5. DealMemo — standalone
Text-message-as-app. $19/mo. **Zero UI to build. Distribution gimmick is the entire moat.**

---

## Strategic notes

- **Hail Mary** = pre-close acquisition analysis (analyze)
- **DealScout** = personal multi-page analyst tool (already built, separate)
- **The 5 consolidated products** map to a full STR operator funnel:
  - Top: Deal Engine (find)
  - Mid: Hail Mary (analyze deeply) + DealMemo (analyze fast on phone)
  - Pre-close: Hail Mary DD Tier (clear contingencies)
  - Post-close: AirCheck (optimize listing) + SuperhostTracker (maintain status)
- **Cross-sell paths:** Deal Engine → Hail Mary → DD Tier → (after lease signs) AirCheck → SuperhostTracker. Average customer LTV bumps significantly if even 2 of 5 attach.
- **Don't build all 5 in parallel.** Hail Mary itself has 11 build-order steps left. Treat the others as project memos until Hail Mary v1 is shipping revenue.
