---
type: sales-doc
source_file: sales\SMS_VARIANTS.md
tags:
  - #sales-kit
  - #sales/sms-variants
---

# Sms Variants

# SMS / MMS Copy Variants

10 message bodies ready for when toll-free verification approves. Pick by ear or A/B test.

All include the legally-required STOP opt-out. All under 480 chars (≤2 SMS segments / 1 MMS segment with image).

Variables to fill in: `{{first_name}}`, `{{biz}}`, `{{city}}`.
If first_name unknown, drop the greeting and start with "Hey —".

---

## V1 — The "I made you something" version (recommended)

> Hey {{first_name}} - it's Sam, 19 in college teaching myself web design. I made a quick site mockup for {{biz}} in {{city}} - photo attached. If you want it built for cheap, reply YES. Not interested? Reply NO and I'll delete it. Reply STOP to opt out.

(437 chars, 1 segment with MMS)

---

## V2 — The shorter, punchier version

> Sam here, 19, teaching myself web design. Built a sample site for {{biz}} - see image. Want it real? Reply YES. Not for you? Reply NO. Reply STOP to opt out.

(165 chars, fits in 1 SMS segment)

---

## V3 — The "honest student" version (vulnerable, builds trust)

> Hey {{first_name}}, I'm Sam, 19, in college. I made a free sample homepage for {{biz}} so I can practice my web design skills. If you like it, $300 and it goes live. If not, reply NO and I'm gone. Reply STOP to opt out.

(229 chars)

---

## V4 — The "specific value" version

> Hi {{first_name}}, Sam here. Made a sample site for {{biz}} - mobile-friendly, contact form, your reviews pulled in. $300 to go live in 5 days. Reply YES for the agreement. Reply NO or STOP to skip.

(202 chars)

---

## V5 — The "one job" version (no fluff)

> {{first_name}} - I built a website mockup for {{biz}}. Photo attached. Want it real? $300, 5 days. Reply YES / NO. STOP to opt out. - Sam

(141 chars, 1 segment SMS)

---

## V6 — The "personalized signal" version

> Hey {{first_name}}, noticed {{biz}} is licensed in {{city}}. Built a quick site mockup just for you - take a look. If you like it: $300 to go live. Don't? Reply NO. Reply STOP to opt out. - Sam, 19, web designer

(214 chars)

---

## V7 — The "challenge" version

> {{first_name}} - I'll bet you $300 your business looks better with this site. Built one for {{biz}} - image attached. Want it live? Reply YES. Not interested? NO. STOP to opt out. - Sam

(187 chars)

---

## V8 — The "nephew rate" version (quirky, cheap)

> Hey {{first_name}}, Sam here. I'm 19 and in college so I work at the rate your nephew would charge - $300 for a real website. Sample for {{biz}} attached. YES / NO / STOP. Thanks.

(187 chars)

---

## V9 — The "saw your trade" version

> {{first_name}} - heard {{city}} contractors are slammed this season. Built {{biz}} a quick sample site so you don't have to think about it. Image attached. $300 if you want it. NO to skip, STOP to opt out. - Sam

(216 chars)

---

## V10 — The "two-step" version (just opens conversation)

> Hey {{first_name}}, Sam here. I make websites for trade contractors. Designed a sample for {{biz}}. OK to send the image? Reply YES, NO, or STOP.

(149 chars — note: image goes in second message after they reply yes — preserves SMS segment cost when most don't reply)

---

## Compliance footer (already baked into all of the above)

Every message must contain one of:
- `Reply STOP to opt out`
- `Reply STOP to unsubscribe`
- `Text STOP to end`

Twilio also handles STOP automatically via their carrier filter — but include the text anyway, both for legal safety and for recipient clarity.

## A/B test plan

When toll-free approves, send 30/day for first week using V1, V2, V3, V5 in rotation. Track reply rate per variant in `replies` table. After 50 sends per variant, pick the winner.

```sql
SELECT
  substr(body, 1, 30) as variant,
  COUNT(*) as sent,
  SUM(CASE WHEN replied THEN 1 ELSE 0 END) as replies,
  ROUND(100.0 * SUM(CASE WHEN replied THEN 1 ELSE 0 END) / COUNT(*), 1) as reply_pct
FROM sends_with_replies
GROUP BY substr(body, 1, 30);
```


## Links
- MOC: [[Cold Outreach]]
- MOC: [[Sales Kit]]
