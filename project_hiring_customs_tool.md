---
name: Hiring & Customs Consulting Tool
description: Two new tools planned — automated hiring/resume screener and customs compliance consulting assistant
type: project
---

## Status: PAUSED — planning stage only, no code written yet

---

## Tool 1 — Hiring / Resume Screener

**Approach chosen:** Email route (Gmail API)
- Indeed delivers applications to a dedicated hiring email
- Tool monitors inbox via Gmail API, auto-parses resumes, scores and ranks candidates

**Setup steps user still needs to do:**
1. Create dedicated hiring Gmail (e.g. hiring@yourbusiness.com)
2. Set Indeed employer → Application delivery → that email
3. Go to console.cloud.google.com → create project → enable Gmail API → OAuth 2.0 credentials → download credentials.json

**Screening criteria (user to confirm):**
- Years of experience
- Certifications / licenses (customs broker license likely key)
- Education
- Keywords / standout factors
- Cover letter quality
- Custom screening questions

**Legal note:** Age filtering is illegal (ADEA). Use experience level, graduation year ranges, career stage instead.

**Planned features:**
- Inbox monitor (Gmail API)
- Resume parser (PDF/Word)
- Auto-scorer via Claude API
- Ranked candidate dashboard (Streamlit)
- Per-candidate score with reasoning + auto-generated interview questions

**Still need from user:**
- Folder/location for the project
- Roles they're hiring for
- Top 5 screening criteria
- credentials.json from Google Cloud

**Why:** Customs business needs to hire; want to automate screening to save time

---

## Tool 2 — Customs Consulting Assistant

**Business:** User runs a customs brokerage/consulting business

**Core problem:** AI gives incorrect or outdated customs info; regulations change fast; hard to keep up with all partner agency data

**Planned approach:**
- Real-time API lookups from official sources: CBP, FDA, USDA, NOAA, FWS, APHIS
- Multi-agent cross-check: one agent pulls data, second verifies against another source, third flags conflicts
- Always cite primary source + show last-updated timestamp
- Refuse to answer when confidence is low rather than guess
- HTS code lookup, admissibility checks, partner agency requirements

**Key agencies to integrate:**
- CBP (Customs & Border Protection)
- FDA
- USDA / APHIS
- NOAA
- FWS (Fish & Wildlife Service)

**Still need from user:**
- What commodities they import most (food, wildlife, ag products, etc.) — determines which agencies matter most
- Whether they want this as a Streamlit app or something else

**Why:** Saves consulting time, reduces errors, keeps up with fast-changing regs
