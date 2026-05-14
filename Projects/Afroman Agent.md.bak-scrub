---
title: Afroman Agent — CitySide Stays Cold Caller
date: 2026-04-27
tags: [project, elevenlabs, cold-calling, citysidestays, agent]
type: project
status: in-progress
---

# Afroman Agent — CitySide Stays LLC

**ElevenLabs Agent ID:** `agent_4801kpp6506efqhv1n4v62w555bs`
**Full config file:** `C:\Users\samth\miami-arbitrage\data\afroman_agent_config.md`

---

## What This Agent Does

Outbound cold caller for CitySide Stays LLC. Calls landlords/property managers and pitches corporate housing leases. Transparent about the model — lists on Airbnb, VRBO, Furnished Finder, Booking.com, Travelnurses.com.

**Pitch:** "We lease 5-20 units, pay 2 weeks in advance, handle all guests, background checks on everyone, cameras/smart locks/noise monitors installed."

---

## What Was Set Up (April 27, 2026)

- ✅ System prompt — full corporate housing script with all branches
- ✅ First message set
- ✅ Dynamic variables: city, address, callback_number, units_interested, landlord_name, sam_email
- ✅ Voice settings: Speed 0.95, Similarity Boost 0.80
- ✅ Turn settings: Patient, 15s timeout
- ✅ Guardrails added to system prompt

## What Still Needs To Be Done (pick up here after restart)

- ❌ **Workflow tab** — needs to be built (Playwright browser required)
- ❌ **Data collection fields** — not configured yet
- ❌ **Knowledge base** — not attached yet

### Workflow Nodes to Build
1. Start → Wait for Human (silent until they say hello)
2. Human detected → Live Pitch (main conversation node)
3. Voicemail detected → Voicemail node (leave message, end)
4. Live Pitch → End (don't hang up abruptly — let conversation finish naturally)
5. Voicemail → End immediately after message

### Data Collection Fields to Add
- Contact name and role
- Phone and email
- Number of vacant units and configurations
- Move-in timeline
- Corporate leasing: yes/no
- Third-party platforms: approved/not approved
- Tour scheduled: yes/no
- Specials or concessions offered
- Call outcome: reached/voicemail/no answer
- Interest level: hot/warm/cold
- Next action: follow up/DNC/qualified/send email

### Knowledge Base Doc to Create + Attach
See full KB content in: `C:\Users\samth\miami-arbitrage\data\afroman_agent_config.md` → "Knowledge Base" section

---

## Script Summary (Sam's Real Script)

**Opening:** Corporate housing provider, looking to lease 5-20 units in [city] by end of month. Saw listing at [address]. "Do you allow corporate leases?"

**If YES:** Explain model → clarify 3rd party platforms (Airbnb, VRBO, Furnished Finder, Booking.com, Travelnurses.com) → qualify units → collect email → schedule tour

**If CONFUSED:** Explain "we lease FROM you, you get rent, we house our guests" → re-ask

**If NO:** Ask why → pitch: background checks, cameras, smart locks, noise monitors, professional cleaning, never leave, multi-year lease → still try to collect email

**If MINIMUM STAY concern:** "We sign 12-36 month lease WITH YOU. Your lease is long-term. Our guests vary."

**Voicemail:** "Hi, this is Alex from CitySide Stays. We're a corporate housing provider looking to lease units in [city]. Call Sam back at [callback_number]."

**Always:** Try to get email even if they say no.

---

## API Access Issue

ElevenLabs key `sk_f8d2329a91584c52b9be16be8d43ee2825b904a484bf8b7e` has zero ConvAI permissions — can't push config via API. Need either:
- New key with ConvAI read/write permissions
- OR use Playwright browser to configure directly

---

## AirDNA — Still Pending

Need to run these addresses through AirDNA Rentalizer after restart:

**Miami (12 addresses):**
1. 8000 NE Bayshore Ct Apt 115
2. 411 NW 37th St (Wynwood)
3. 53 NE 49th St Apt 7
4. 1536 NW 15th Ave Apt 302
5. 1450 SW 6th St Apt 2
6. 14735 NW 9th Ave Unit B
7. 771 NE 177th St Unit 1
8. 10495 SW 14th Ter
9. 2652 SW 23rd Ave Unit Back
10. 8000 NE Bayshore Ct Apt 211
11. 1035 SW 4th St Apt 2
12. 245 NE 33rd St Apt 207

**Tampa (6 addresses):**
- 785 117th Terrace N, St. Petersburg
- 411 Danube Ave (near Chesapeake)
- 1410 Candlelight Blvd (near Cortez Blvd)
- 324 30th Ave N
- 712 51st Ave Plz W
- 15215 Livingston Avenue

**Goal:** ADR, occupancy rate, monthly revenue estimate, comparable listings for each address.

---

## Session Hook Issue

The Stop hook at `~/.claude/obsidian_session_sync.py` is running too frequently — appending duplicate entries to the daily note on every minor stop event. Needs to be fixed to deduplicate or only run once per session.
