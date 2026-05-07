---
type: sales-section
parent: Sms Variants
tags:
  - #sales-kit
  - #sales/sms-variants
---

# A/B test plan

## Context
From [[Sms Variants]].

## Content

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
- Parent: [[Sms Variants]]
- MOC: [[Sales Kit]]
