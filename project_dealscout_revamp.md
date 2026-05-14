---
name: DealScout UI Revamp
description: Full multi-section UI overhaul of the DealScout Streamlit app at miami-arbitrage, with agency-agents suite activated and accuracy preservation as a hard constraint
type: project
---

# DealScout — Full UI Revamp

**Project root:** `C:\Users\samth\miami-arbitrage\`
**Started:** 2026-04-29
**Effort mode:** xhigh (Opus 4.7)

## Why
The existing DealScout UI was hard to use and visually rough. User wants a complete, tab-by-tab revamp. **Hard rule: do not lose analysis accuracy** — only the presentation layer changes; underlying analyzer logic (`neighborhoods.py`, `regulations.py`, `revenue.py`, `seasonal.py`) must keep producing the same numbers.

## How to apply
- Treat this as a long-running, sectioned refactor — commit per section so progress is recoverable
- Always syntax-check the full project after edits before claiming a section done
- Theme/layout work goes through `theme.py` + `config.toml`; do not inline styles per-page
- Agency agents (extracted from `Downloads/agency-agents-main.zip`) are activated to work in parallel on tabs

## Status
- ✅ Section 1 committed — `app.py`, `config.toml`, `theme.py`, `pages/1_🏠_Property_Analyzer.py`, `pages/9_🏘️_Listing_Scout.py`, `pages/20_🏆_Lead_Ranker.py`, plus analyzer files (`neighborhoods.py`, `regulations.py`, `revenue.py`, `seasonal.py`) touched
- ✅ New files: `__init__.py`, `app.py`, `config.py`, `theme.py`
- ✅ `CLAUDE.md` updated with revamp context
- ⏳ Remaining tabs (Sections 2+) — not yet started

## Pages in scope (23 total)
Pages 1–23 of the DealScout app. Section 1 hit pages 1, 9, 20. Remaining pages still need the new theme + layout pass.

## Verification checklist (per section)
- [ ] Syntax check: `python -m py_compile` across edited files
- [ ] Full project syntax pass
- [ ] Spot-check that analyzer outputs match pre-revamp values for a known property
- [ ] Commit with section number in message
