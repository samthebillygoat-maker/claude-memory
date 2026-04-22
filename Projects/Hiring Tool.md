# 📋 Hiring Tool — Resume Screener

**Status:** Paused — planning stage, no code written yet
**Approach:** Gmail API monitors inbox → auto-parses resumes → scores candidates → Streamlit dashboard

---

## How It Works

1. Post job on Indeed
2. Indeed delivers applications to a dedicated hiring Gmail
3. Tool monitors inbox via Gmail API (OAuth 2.0)
4. Auto-parses resumes (PDF/Word)
5. Scores and ranks candidates via Claude API
6. Dashboard shows ranked list with reasoning + auto-generated interview questions

---

## Setup Steps (Still To Do)

- [ ] Create dedicated hiring Gmail (e.g. `hiring@yourbusiness.com`)
- [ ] Set Indeed → Application delivery → that email
- [ ] Go to console.cloud.google.com → create project → enable Gmail API → OAuth 2.0 credentials → download `credentials.json`
- [ ] Complete Google restricted-scope security assessment (takes several weeks — required for mail read/send access)
- [ ] Enable 2FA on the Gmail account (mandatory from May 2026)

> ⚠️ Gmail restricted-scope API (mail read/send) now requires annual independent security assessment from a Google-approved third-party assessor before production approval. Plan several weeks for this.

> ⚠️ Gmail POP mail fetching removed January 2026. Gmail API (OAuth 2.0) is the only correct approach.

> ⚠️ Google enforcing mandatory 2FA for ALL Gmail accounts starting May 2026. The hiring Gmail must have 2FA or OAuth tokens will be revoked.

---

## Screening Criteria (To Confirm)

- Years of experience
- Certifications / licenses (customs broker license likely key)
- Education
- Keywords / standout factors
- Cover letter quality
- Custom screening questions

> ⚠️ Legal note: Age filtering is illegal (ADEA). Use experience level, graduation year ranges, or career stage instead.

---

## Resume Parser Options

| Option | Notes |
|---|---|
| **pyresume** (github.com/wespiper/pyresume) | Claude API integration, per-section confidence scores, batch CSV/JSON export, <2s per resume — preferred if using Claude API |
| **OmkarPathak/ResumeParser** | Local Qwen2.5-1.5B model, ~1GB, no API keys, 100% local |

---

## Tech Stack (Planned)

```
Gmail API (OAuth 2.0) — inbox monitor
pyresume — PDF/DOCX/TXT parser
Claude API — scoring + interview question generation
Streamlit (+ st.App ASGI) — dashboard
FastAPI — backend for Gmail API + Claude API
```

> Streamlit v1.53 added `st.App` ASGI entry point — can mount Streamlit inside FastAPI as single process (no separate deployment)

---

## Still Need From You

- [ ] Folder/location for the project
- [ ] Roles you're hiring for
- [ ] Top 5 screening criteria
- [ ] `credentials.json` from Google Cloud

---

## Related

- [[Areas/Customs Business]] — why you need to hire
- [[Projects/Customs Consulting Assistant]] — the other tool being built
