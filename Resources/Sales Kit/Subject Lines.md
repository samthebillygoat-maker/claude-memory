---
type: sales-doc
source_file: sales\SUBJECT_LINES.md
tags:
  - #sales-kit
  - #sales/subject-lines
---

# Subject Lines

# Email Subject Line Variants

Data-driven from Belkins / Instantly 2026 benchmarks. Lowercase + short + specific wins.

## Currently shipped (suboptimal)
> A landing page mockup for {biz}

6 words, title-case, generic. Replace.

## Tier-A variants (test first)

1. `quick thing on {biz} site` — references them, casual, 4 words
2. `{first_name}` — just the name (54% open in tests, but stops working past 1-2 sends)
3. `mockup for {biz}` — direct, 3 words
4. `2-min thing for {biz}` — promises low time investment
5. `{first_name} — built you something` — pattern interrupt, personal

## Tier-B variants (rotate to avoid spam-folder pattern detection)

6. `noticed something about {biz} site`
7. `{biz} — quick design idea`
8. `worth 2 min, {first_name}?`
9. `{biz} {city} site → redesign`
10. `for {biz}'s next homepage`

## Question-format (46% open per Belkins)

11. `useful or skip, {first_name}?`
12. `worth a quick look?`
13. `{first_name}, made you a site — keep or trash?`

## Local hook (when we know city well)

14. `{city} contractor site — quick idea`
15. `for {biz} in {city}`

## Anti-patterns to AVOID

- ❌ "ASAP", "URGENT", "Limited Time", "FREE", "ACT NOW"
- ❌ All caps anywhere
- ❌ Multiple emojis in subject (one ✦ or → is fine, more = spam folder)
- ❌ Lying about a relationship ("RE: our conversation" when there wasn't one)
- ❌ "Hi" or "Hello" alone — looks like dictionary spam
- ❌ Subject longer than 50 chars on mobile (gets truncated mid-word)

## Implementation note

Subject line is set in `src/email_send/sender.py::build_message`. To A/B test, modify to pick by hash of license_num:

```python
SUBJECT_VARIANTS = [
    "quick thing on {biz} site",
    "{first_name} — built you something",
    "mockup for {biz}",
    "2-min thing for {biz}",
    "noticed something about {biz} site",
]
idx = int(license_num) % len(SUBJECT_VARIANTS)
subject = SUBJECT_VARIANTS[idx].format(biz=business_name, first_name=owner_first or business_name)
```

After 50 sends per variant, look at reply rate per subject (`src/stats.py` already has the schema). Pick the winner.

## Open-rate vs reply-rate tradeoff

A clickbait subject can lift opens but tank replies (recipient feels deceived). Optimize for REPLY rate, not opens. The 5 best-performing subjects on Lemlist data all averaged 35-45% open + 6-12% reply — much better than 60%-open / 2%-reply clickbait.


## Links
- MOC: [[Cold Outreach]]
- MOC: [[Sales Kit]]
