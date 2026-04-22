# 🛠️ Tech Notes

Updates on tools and APIs used across all projects.

---

## Streamlit

### Removed APIs (breaking — update before upgrading)
- `st.experimental_get_query_params` → use `st.query_params`
- `st.experimental_set_query_params` → use `st.query_params`
- `st.experimental_user` → use `st.user`

### New Features (2025–2026)

**v1.46.0 (Jun 18, 2025):**
- `st.navigation` supports `position="top"` for horizontal top nav bar
- `st.context.theme` detects light/dark mode at runtime
- Columns, expanders, popovers, chat containers can now be **freely nested** (nesting restriction removed)

**v1.53 (Jan 14, 2026):**
- `st.App` ASGI entry point — mount Streamlit inside FastAPI/Starlette as single process
- Supports middleware (auth, logging), lifecycle hooks, custom HTTP routes, shared event loop
- Useful for hiring tool: FastAPI (Gmail API + Claude API backend) + Streamlit dashboard in one process

**v1.56.0 (Mar 31, 2026):**
- `st.iframe` — embed iframes directly
- `st.menu_button` widget
- `AudioColumn` + `VideoColumn` for `st.column_config`
- `hide_index` + `hide_header` params for `st.table`
- `autoscroll` param for `st.container`
- State persistence + CSS key classes for `st.tabs` / `st.expander` / `st.popover`
- `required` param for `st.pills` + `st.segmented_control`
- `filter_mode` for `st.selectbox` and `st.multiselect` — users can search/filter options by typing
- `st.multiselect` "select all" button
- `st.navigation` has `expanded` param
- `st.file_uploader` and `st.chat_input` accept type shortcuts: `"image"`, `"audio"`, `"video"`, `"document"`
- `st.info/warning/error/success` auto-extract leading Material icon from message body
- Pandas 3.x support — **test Miami tool compatibility**

**Other 2026 additions:**
- `theme.chartDivergingColors` config — sets default diverging color palette for all charts app-wide
- `st.user.tokens` exposes OIDC ID/access tokens · `st.logout` for full OAuth sign-out
- `st.tabs` / `st.popover` / `st.expander` now have `on_change` parameter
- `st.Page` has `visibility` parameter to hide pages from nav while keeping them routable
- `st.metric` has `delta_description` param · `st.image` has `link` param
- Most non-trigger widgets have `bind` parameter for direct query param syncing

---

## RentCast API

**Breaking change (Aug 2025):**
- Top-level `latitude` and `longitude` fields are **DEPRECATED**
- Use `subjectProperty.latitude` and `subjectProperty.longitude` instead
- Miami tool Listing Scout page needs this update

**Expanded search (recent):**
- `properties/listings` endpoints now support: property type, beds, baths, sq footage, year built, listed price (min/max ranges)
- AVM endpoints now auto-look up subject property attributes in single call
- `stateFips` / `countyFips` fields added to all address responses
- `suppressLogging` boolean param added

**MCP Server:** RentCast launched official MCP server at developers.rentcast.io/mcp — Claude, Cursor, VS Code, Windsurf can connect directly. Community implementation also at github.com/robcerda/rentcast-mcp-server. Requires active API subscription.

---

## Gmail API

**Mandatory 2FA (May 2026):** Google enforcing 2FA for ALL Gmail accounts — hiring Gmail must have 2FA or OAuth tokens will be revoked.

**Restricted-scope security assessment:** Gmail mail read/send scope now requires annual independent security assessment from Google-approved third-party assessor. Takes several weeks. Required before production approval — plan for this in hiring tool timeline.

**POP mail fetching removed (January 2026):** Gmailify also removed. Gmail API (OAuth 2.0) is the only correct approach.

---

## Resume Parsers

| Library | Notes |
|---|---|
| **pyresume** (github.com/wespiper/pyresume) | Claude API integration, per-section confidence scores, batch CSV/JSON export, <2s/resume, Lever ATS-compatible — preferred if using Claude API |
| **OmkarPathak/ResumeParser** | Local Qwen2.5-1.5B (GGUF, ~1GB), 100% local, no API keys, JSON output — use if no API key |

---

*Last updated from research-scout: April 21, 2026*
