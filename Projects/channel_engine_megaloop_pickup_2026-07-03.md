# Channel-Engine Megaloop — Pickup Memo (paused 2026-07-03 ~00:30 PT)

## Where it stands
- 16/16 niches rendered (12 reels + 4 carousels) at `~/projects/channel-engine/output/megaloop/` — see `gallery.html` (open in browser to view everything).
- Spend: **3.15 / 100 credit cap** (all video $0 — mixkit free clips via OpenMontage adapters + direct CDN pattern; 21 z_image stills @ 0.15).
- Vision-judged vs real TikTok search screenshots (`refs/<niche>/`): scoreboard in `judgment-round1.md`, adversarial panel directives in `evolution-round4.md`.
- channel.yaml v2 live: 72/28 viral/promo pillar mix, per-platform links block, scout RSS now includes real Tampa events/concerts/Ybor feeds. 204/204 tests pass.
- Real events wired in: tampa-weekend-events carousel re-rendered with actual July-4th-weekend inventory (Liberty by the Bay 250-drone show at Julian B. Lane, Busch Gardens drone+fireworks, Bad Boy Bill at Hyde Park Cafe, YDG + Un Verano Sin Ti Night at The Ritz Ybor, Mahaffey Pops, MOSI).

## Governance (Sam's rule, 2026-07-03)
All creative + judging goes through the **fusion panel (GLM+Kimi) with OPUS as fuse/vision judge — no Fable verdicts**. Fable/main session = mechanical plumbing only (renders, fetches, logging). Panel legs run via `askEach({judge:false})` in `~/projects/flux-fusion` (CLI judge ladder is fragile across session restarts); Opus judging via Agent tool `model: opus`.

## Exactly where it paused
Opus judge issued iteration-2 work order: **workation-remote-work** (FAIL → honest reframe, no owner assets needed):
- New creative: hook "No home office? A 1-bed still works." / beats: dining table desk by 9am → coffee counter, natural light → neighborhood walk → "Close the laptop. Tampa's right outside." / caption admits honest setup.
- Photos staged plan: 01__DSC1666 (dining hook), 01__DSC1727, 01__DSC1675, 01__DSC1700 from `channels/cityside-stays/assets/images`.
- Paused BEFORE applying creative.json update + re-render (Sam interrupted the tool call). Resume = run that step, re-render via `node output/megaloop/run-niche2.cjs workation-remote-work`, then Opus vision-judges frames vs `refs/workation-remote-work/`.

## Loop mechanics for resume
Each iteration: Opus agent reads judgment+evolution+creative → picks weakest + work order → main session executes (free assets first, z_image 0.15/img, "no text no letters" in every AI prompt, no people in clips, real venues/dates for events) → Opus vision-judge on frames vs refs → append verdict to `judgment-round1.md` + ledger. Panel critique round every ~4 iterations.

## Asks still open for Sam
1. 10–15s phone walkthrough clips per unit (unlocks true POV/tour motion — biggest quality ceiling).
2. Pre-staging/renovation photos (unlocks before-after niche, currently pivoted to "Why this 1-bed books out.").
3. Airbnb listing URLs ×2 → fill `links.airbnb_unit_28/18` in channel.yaml.
4. Postiz still unconnected — everything is review-mode only, nothing posts.
