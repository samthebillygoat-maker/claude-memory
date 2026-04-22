# ⚖️ Customs Consulting Assistant

**Status:** Paused — planning stage, no code written yet
**Goal:** AI-powered customs compliance tool that uses real-time official data, not hallucinated answers

---

## The Problem

- AI gives incorrect or outdated customs info
- Regulations change fast (tariffs, import alerts, agency rules)
- Hard to keep up with all partner agency data simultaneously
- Errors cost clients money (wrong duties, detained shipments, penalties)

---

## Planned Approach

- Real-time API/data lookups from official sources
- Multi-agent cross-check: one agent pulls → second verifies → third flags conflicts
- Always cite primary source + show last-updated timestamp
- Refuse to answer when confidence is low rather than guess
- HTS code lookup, admissibility checks, partner agency requirements

---

## Agencies to Integrate

| Agency | Coverage |
|---|---|
| CBP | Entry, duties, tariffs, WROs, UFLPA |
| FDA | Food safety, import alerts, FSMA |
| USDA / APHIS | Plant/animal, ag products, equine |
| NOAA | Seafood, MMPA prohibitions |
| FWS | Fish & Wildlife |

---

## Critical Current Intel (2025–2026)

### Tariffs
- **Section 122:** 15% global surcharge (NOT 10% — raised Feb 22 before Feb 24 effective date) · expires Jul 24, 2026 unless Congress extends · court challenge active (CIT hearing Apr 10 — judges skeptical) · USMCA Canada/Mexico exempt · Section 232-covered goods exempt
- **Section 232 metals (effective Apr 6, 2026):** 50% on primary aluminum/steel/copper (full customs value) · 25% on derivative articles · 15% transitional for metal-intensive industrial equipment through Dec 2027 · 10% if made entirely from US metal
- **Section 232 semiconductors:** 25% effective Jan 15, 2026 · multiple exemptions (US data centers, R&D, consumer electronics, public sector)
- **Section 232 pharma (signed Apr 2, 2026):** 100% on imported patented pharma/APIs effective Jul 31/Sep 29 2026 · generics/biosimilars exempt · EU/JP/KR/CH: 15%
- **Section 301 investigations:** USTR investigating 16 economies for overcapacity (20+ sectors) + 60 economies for forced labor — no statutory expiration if imposed; July 24 remedy target
- **Ecuador:** Exempt from Section 122 and reciprocal tariffs (US-Ecuador agreement Mar 13, 2026)
- **Section 122 sunset note:** July 24, 2026 · Section 232-covered goods don't stack with 122

### CBP Systems
- **CAPE System (launched Apr 20, 2026):** IEEPA tariff refunds via ACE Portal CSV upload
  - Only original Importer of Record or filing broker can submit Phase 1
  - Refund ACH must be separately enrolled (not same as duty-payment ACH)
  - Each Declaration capped at 9,999 entries · cannot be amended once accepted
  - Processing time: 60–90 days after acceptance
  - Phase 2 (finalized liquidations): no announced timeline
  - Launched with technical glitches Apr 20 · CBP support calls Apr 21
- **Forced Labor Portal (mandatory Jan 21, 2026):** cbp.gov/trade/forced-labor — all WRO/UFLPA/CAATSA reviews must go through portal (Login.gov required)
- **CBP ACH refunds only** starting Feb 6, 2026 — no more checks
- **ACE Portal modernized** (Apr 1, 2026) — new web form for first-time ACE account applications

### De Minimis
- **Suspended globally** (EO 14324, effective Aug 29, 2025) — all low-value shipments now pay full duties · after Feb 28, 2026 only ad valorem duty method for postal shipments

### FDA
- **TouristExpress** (Miami-Dade): mandatory monthly remittance since Oct 2025
- **FISP / SERIO+**: centralized national import review with real-time cross-port alerts
- **Import Alert 45-02**: consolidated all illegal/undeclared food color additive alerts
- **IA 99-08 updated Apr 14, 2026**: pesticide residues in processed food/animal food
- **FSMA certification (effective Oct 31, 2025)**: Indonesian shrimp (Java/Lampung) require MFQAA cert; spices require BPOM cert
- **April 2026 enforcement sweep**: Salmonella, pesticide residues, heavy metals, cheeses, seafood, cilantro
- **IA 99-48**: 8 Chinese firms added for PFAS-contaminated clams in early 2026

### NOAA / Seafood
- **MMPA import prohibitions (effective Jan 1, 2026)**: 240 fisheries in 46 nations banned without comparability finding — ~$3.6B in US seafood trade affected; tuna and mahi-mahi most impacted
- **Swimming crab STAYED**: Vietnam, Philippines, Indonesia, Sri Lanka import ban stayed by CIT pending NOAA reconsideration (these are still importable during stay)
- **Settlement**: NFI and NOAA settled suit; NOAA must reconsider within 60 days of gov't reopening; new determinations within 180 days

### USDA APHIS
- **Part 330 revised (Feb 2026)**: removes obsolete requirements, streamlines permits for low-risk organisms, updates foreign soil import rules
- **Equine import (effective May 11, 2026)**: 48-hour pre-export vet exam removed · new consolidated health certificate mandatory from Jun 15, 2026

### Forced Labor / WROs
- **CBP WRO (2026)**: Finca Monte Grande (Chiapas, Mexico) coffee — 6 ILO indicators
- **40% penalty tariff** on confirmed transshipment — no mitigation; CBP using AI isotopic/chemical analysis to detect
- **Section 301 forced labor investigation**: 60 economies including Canada (comment deadline Apr 15)

---

## Still Need From You

- [ ] What commodities you import most (food, wildlife, ag, pharma?) — determines which agencies matter most
- [ ] Preferred format: Streamlit app or something else?

---

## Related

- [[Areas/Customs Business]] — your business context
- [[Projects/Hiring Tool]] — the other tool being built
- [[Resources/Customs Regulations Intel]] — ongoing regulatory research
