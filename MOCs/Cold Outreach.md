---
type: moc
tags: ["#moc"]
---

# Cold Outreach

MOC for the contractor cold-email pipeline.

## Active leads
```dataview
LIST FROM #active-lead
```

## All contractors
```dataview
TABLE city, trade, status FROM #contractor LIMIT 100
```

## Email threads
```dataview
TABLE to, status, sent_at FROM "Email Threads"
```

## Sales kit
```dataview
LIST FROM #sales-kit
```
