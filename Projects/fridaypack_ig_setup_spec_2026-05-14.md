# Friday Pack — Instagram Account Setup Spec

Everything you need to create `@thefridaypack` on Instagram in one sitting. Account creation itself has to happen on your phone or instagram.com — this doc is the copy/spec, ready to paste.

Created 2026-05-14. Pricing and product facts match live site.

---

## 1. Handle (pick one — check availability in order)

| Priority | Handle | Why |
|----------|--------|-----|
| 1 | `thefridaypack` | Exact brand match, mirrors thefridaypack.com |
| 2 | `friday.pack` | Clean, period-separator is on-brand IG style |
| 3 | `fridaypack.co` | If domain-style handle reads better |
| 4 | `getfridaypack` | "Get" prefix is a known fallback pattern |

**Avoid:** underscores (look spammy), numbers, `_official` suffix.

**Action:** open IG → tap your profile pic → Add Account → New Account → try `thefridaypack` first. If taken, work down the list.

---

## 2. Account Type

Set to **Business** (not Creator).

- Category: **Product/Service** (or "Business Service" if Product/Service isn't offered in your region)
- Why Business over Creator: gives you the contact button, the link-in-bio CTA button, IG Shopping eligibility later, and cleaner Insights.

---

## 3. Profile Fields — Paste Verbatim

**Name field (the bold line, 30 char max):**
```
The Friday Pack
```

**Username:** (whichever from §1 you locked)

**Pronouns:** leave blank.

**Bio (150 char max — current draft is 148):**
```
50 STR-friendly landlord leads. Every Friday morning.
Owner LLC + phone attached. Built by an operator, for operators.
$29 trial ↓
```

> Char count: 148. The ↓ arrow draws the eye down to the link. If your IG region strips the arrow, swap for `→`.

**Alternative bio (more conversion-focused, 142 char):**
```
Stop scraping Zillow at midnight.
50 STR-friendly leads every Friday.
Owner LLC + phone. Grouped by owner.
Trial $29 ↓
```

Pick whichever rolls off your tongue when you read it out loud.

---

## 4. Link in Bio

**Single link:** `https://thefridaypack.com` (or `https://thefridaypack.com/free-sample` if you want IG traffic to land on the lead-capture page rather than the homepage).

**Better — use a link aggregator** so you can A/B test landing pages and add a Stripe checkout button without redeploying the site:

- **Recommendation:** Stan.store or Beacons (creator-economy tools, faster than Linktree for selling)
- **Free fallback:** Linktree
- **Free + self-hosted:** add `/links` route on thefridaypack.com (1 hour of work, full control)

**Link block order:**
1. **Try the $29 Trial Pack** → `thefridaypack.com/?plan=trial`
2. **See a real sample (free)** → `thefridaypack.com/free-sample`
3. **How it works (60-sec)** → YouTube/Loom explainer URL (TBD — record this Monday)
4. **DM me on Twitter** → `x.com/[your handle]`

---

## 5. Profile Picture Spec

**Final size:** 320×320 px circle crop, but upload at **1080×1080 px** so it stays sharp on profile-tap zoom.

**Two safe options:**

**Option A — Wordmark (recommended for B2B service brands):**
- Background: ink-900 (`#0B0F14` or whatever your brand dark is — match the site)
- Text: "FP" in signal-500 (your brand green), bold, centered
- Font: same display font as the site (Inter Bold or whatever's loaded)
- Why: instantly readable at 32×32 px in the IG feed; doesn't get lost in DMs

**Option B — Calendar mark (more memorable):**
- A simple calendar icon with "FRI" highlighted in signal-500 on ink-900 background
- Riffs on the "Friday" half of the name; sticks in memory

**Avoid:** photos of you (this is the brand account, not your personal), stock house photos, generated AI art (looks low-effort), gradients that flatten at 32 px.

**Tool to generate:** Figma → 1080×1080 frame → export PNG. Or Canva → "Instagram Profile Picture" template. 15 minutes start to finish.

---

## 6. Highlight Covers — 5 Launch Highlights

Each highlight needs a 1080×1920 cover (IG crops to circle). Keep covers consistent: same background, same icon style, same color.

| Order | Highlight Label (max 15 char) | Icon | What goes inside |
|-------|-------------------------------|------|------------------|
| 1 | `WHAT IT IS` | Box/package | 3-4 stories explaining the product in 15 sec |
| 2 | `SAMPLE` | Magnifying glass | Screenshots of redacted lead data + free-sample CTA |
| 3 | `PRICING` | Tag | All 4 tiers as story slides — $29/$97/$197/$347 |
| 4 | `HOW TO USE` | Phone | Loom of opening pack → first call → first lease |
| 5 | `WINS` | Trophy | LEAVE EMPTY until you have real wins. Don't fabricate. |

**Highlight #5 caveat:** if you don't have signed-lease wins yet, don't create the Wins highlight at launch. Empty highlight slots scream "no traction." Add it after the first real customer signs a unit and gives permission to share.

---

## 7. Action Button (Business account)

After conversion to Business, add an **action button** on the profile:

- **Type:** "Book Now" or "Sign Up" (depends on what IG offers in your region)
- **Provider:** Stan.store, Calendly, or direct Stripe Payment Link to the $29 Trial
- **Why:** adds a second tappable CTA above the bio text — more conversion paths than just the link

---

## 8. Pre-Launch Checklist (before first post)

- [ ] Handle locked (one of §1)
- [ ] Switched to Business account
- [ ] Bio pasted (§3)
- [ ] Link in bio live and tested on mobile
- [ ] Profile pic uploaded, looks crisp at 32×32 in feed
- [ ] 5 highlight covers uploaded (skip Wins until real wins exist)
- [ ] Action button wired
- [ ] At least 3 grid posts queued so the profile doesn't look empty on first visit
- [ ] Settings → Privacy → Comments: turn on default filter for spam
- [ ] Settings → Business → connect to Facebook Page (required for ads later — do it now to avoid future friction)

---

## 9. First-Week Content Drop (from existing `A_instagram_bundle.md`)

Don't post-and-disappear. Schedule:

- **Monday:** Carousel — "Why PropStream leads are dead on arrival"
- **Wednesday:** Reel — 30-sec product walkthrough (record this; voiceover yourself)
- **Friday:** Carousel — "Inside this week's Friday Pack" (redacted preview of the live Miami pack)

Cross-post Reels to TikTok and YouTube Shorts the same day — zero extra production cost.

---

*Spec ready 2026-05-14. Replace handle in all docs once locked. Friday Pack pricing accurate as of this date.*
