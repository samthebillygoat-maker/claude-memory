---
name: Do work inline, do not spawn subagents by default
description: User prefers inline tool use over Agent/subagent calls — their subagent setup is unverified
type: feedback
---

Do not spawn subagents (Agent tool, Backend Architect, etc.) by default. Do work inline using direct tools (Bash, Read, Write, Edit, Grep).

**Why:** User said "I don't know if I have them setup well" — they don't trust the subagent runtime to actually execute. Spawning agents risks silent failure or context loss.

**How to apply:** Default to handling tasks inline, even multi-step ones. Only suggest a subagent if the user explicitly asks for one or names an agent type. If a task is genuinely too large for one turn, break it into sequential inline steps and report progress between them.
