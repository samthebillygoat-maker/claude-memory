---
type: moc
tags: ["#moc"]
---

# Active Pipeline

What's actually moving this week.

## Sent emails (last 7 days)
```dataview
TABLE to, status, sent_at FROM "Email Threads" WHERE date(sent_at) >= date(today) - dur(7 days)
```

## Recent calls
```dataview
TABLE from, summary FROM "Calls"
```

## Hot landlord threads
```dataview
LIST FROM #landlord AND #cold-thread
```
