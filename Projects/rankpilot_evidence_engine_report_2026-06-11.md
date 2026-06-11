# RankPilot weekly — listing 558584 — 2026-06-11

## SCORE: 88/100 — excellent (-1 vs last week)

### Category scores
- **title**: 100 (12%)
- **photos**: 84 (20%)
- **description**: 92 (12%)
- **amenities**: 79 (10%)
- **pricing**: 90 (18%)
- **availability**: 92 (13%)
- **policy**: 75 (10%)

### Performance
- Booked 8 stays in last 30d (+8 vs prior 30d). Not enough comp/booking data for percentile ranking yet.
- Booking pace 30d: 8 (+8 vs last week)
- ADR percentile vs market: 39

### Pricing signal
- Current base: $112 → suggested: $111 (pricelabs)
- PriceLabs recommends ~$111/night avg over the next 31 days (below market median $191).

### Search rank (clean session — personalized SERPs vary)
- "South Tampa 1BR": not in the first 5 pages
- "Tampa furnished apartment": not in the first 5 pages

### 🟡 IMPORTANT
1. [photos] 17 photos — below ideal 20 → Add detail + lifestyle shots to reach 20+.
   ↳ why: photos: 17 (ideal: 20) — p5-ranking-factors.md [high]
2. [photos] Only 1/17 photos captioned → Caption every photo with a keyword-rich benefit.
   ↳ why: captioned: 1/17 (6%) — threshold: 80% — p7-photo-algorithm.md [med]
3. [description] 2/4 key sections filled (Space/Access/Neighborhood/Transit) → Fill all four — they feed Airbnb search relevance.
   ↳ why: sections filled: 2/4 (Space, Access, Neighborhood overview, Transit) — p5-ranking-factors.md [med]
4. [amenities] Not listed: pool, hot tub, workspace → If you actually have these, add them — guests filter on them. Never list amenities you lack.
   ↳ why: missing key amenities: pool, hot tub, workspace (3 of 11 high-signal terms not found in listing) — p5-ranking-factors.md [med]
5. [pricing] Base $112 below market P25 ($119) — leaving money on table → Test raising toward market median.
   ↳ why: base price: $112; market P25: $119; P50: $191; n=18 comps — p5-ranking-factors.md [high]
6. [availability] 12 host-blocked nights in next 30d → Open the calendar — availability is a ranking + booking-velocity lever.
   ↳ why: blocked nights next 30d: 12 (threshold: 8; penalty: −8) — p5-ranking-factors.md [high]

### Review signals
- 1 published review — no repeated themes yet (early signal, need ≥2 reviews mentioning the same feature).

### Keyword gaps (used by winning comps, missing from you)
`retreat` `pool`

### Photo order — slot template (room-labeled)
> Pixel-stat ordering only: catches dark/blurry/flat photos. Composition and staging — most of what
> Airbnb's own model scores — are invisible here. Only the ORDER within this gallery is meaningful;
> raw scores are uncalibrated.
> 
> Within a room: lead wide, end detail — by eye; pixel stats can't see composition.

- Current cover ranks #1 of 17 by defect score (raw 46)
- Note: 16/17 photos have no captions — captions boost every raw score (max 85/100 uncaptioned) and are a quick win.

**First five (proposed order):**
#1 [living] 133556a8 — Living-room cover converts best: +35% booking rate in IJRM 2023 study (S14) vs bedroom negative. (brightness 0.683 (band 0.45–0.75); sharpness 0.031 ≥ 0.75× median 0.028 (gate: 0.021); room=living; score=46) [med]
#2 [kitchen] 1410fb44 — Secondary hero — different room from slot 1 to deliver gallery variety (first five = digital storefront). (slot 1 room=living; slot 2 room=kitchen; score=33; diversity is a first-party auto-rank objective (S1, S15); minDistinctRoomsFirstFive=4) [med]
#3 [bedroom] ac39facd — Bedroom answers "where will I sleep" — present in every found template (S5/S15/S17/S18). Only the COVER slot is bedroom-negative (S14). (room=bedroom; score=29; brightness=0.702) [med]
#4 [kitchen] 140a64dc — Kitchen/dining: functionality and cleanliness signal (S15); kitchen present in all first-five templates (S15/S16/S18). (room=kitchen; score=35; brightness=0.619) [med]
#5 [bathroom] 5e3819e7 — Slot 5 (bathroom): bathroom = trust signal for cleanliness (S15); unique feature if scores higher. Conflict on 5th subject resolved by score (p7b Q2). (room=bathroom; score=27; brightness=0.749; only bathroom available) [low]
tour (slots 6+): living×5, bedroom×2, dining×3, bathroom×2

**Near-duplicates flagged (flag only — review manually; full list in run JSON):**
- keep …133556a8 / drop …f52a030a — room=living; Δbrightness=0.031, Δsharpness=0.003, Δcolorfulness=0.003 (all < nearDupeMetricDelta 0.05); keep score=46 vs drop score=33
- keep …133556a8 / drop …fb876057 — room=living; Δbrightness=0.027, Δsharpness=0.008, Δcolorfulness=0.039 (all < nearDupeMetricDelta 0.05); keep score=46 vs drop score=34
- keep …eebda990 / drop …f52a030a — room=living; Δbrightness=0.004, Δsharpness=0.005, Δcolorfulness=0.047 (all < nearDupeMetricDelta 0.05); keep score=34 vs drop score=33
- (+10 more)

### Experiments (observational — what changed & what moved)
- 2026-06-11 summary: rankΔ n/a, paceΔ 0, scoreΔ 0

---
_Suggestions match patterns of higher-performing listings. No tool guarantees bookings, ADR, or placement._