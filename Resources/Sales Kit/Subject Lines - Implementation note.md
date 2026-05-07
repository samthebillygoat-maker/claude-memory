---
type: sales-section
parent: Subject Lines
tags:
  - #sales-kit
  - #sales/subject-lines
---

# Implementation note

## Context
From [[Subject Lines]].

## Content

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

## Links
- Parent: [[Subject Lines]]
- MOC: [[Sales Kit]]
