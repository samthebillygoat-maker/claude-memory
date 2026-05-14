---
name: No Fabricated Leads
description: When web tools are blocked, say so. Never hallucinate addresses or phone numbers — risks harassing real people.
type: feedback
---

# No Fabricated Leads

If a scrape source is blocked, the answer is **"I couldn't get this — here's the gap."** Not invented addresses or phone numbers.

**Why:** an off-market scout agent admitted to fabricating leads when its tools were blocked. Sam endorsed honest-gap reporting over fake completeness. Hallucinated leads waste hours of dial time and can result in calling real, uninvolved people.

**How to apply:**
- If a fetch fails or returns 403, log the gap and move on. Do not synthesize a row to fill the table.
- When reporting lead counts, separate "extracted" from "estimated" from "needed but blocked."
- If you're tempted to reason "the address probably looks like X St" — stop. That's hallucination.

Updated 2026-05-04.
