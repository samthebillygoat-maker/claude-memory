---
title: Claude Code Setup — Plugins & Tools
date: 2026-04-24
tags: [setup, claude-code, mcp, plugins, tools]
type: reference
status: active
---

# Claude Code Setup — Plugins & Tools

*Last updated: 2026-04-24*

## Plugins (in ~/.claude/settings.json)

### 1. Karpathy Guidelines ✅
- **Source**: Local → `C:\Users\samth\Downloads\andrej-karpathy-skills\andrej-karpathy-skills-main`
- **Plugin ID**: `andrej-karpathy-skills@karpathy-skills`
- Think Before Coding · Simplicity First · Surgical Changes · Goal-Driven Execution

### 2. Superpowers ✅
- **Source**: Official Claude marketplace
- **Plugin ID**: `superpowers@claude-plugins-official`
- Full dev methodology: brainstorm → spec → plan → subagent execution → TDD → review → merge

### 3. claude-mem ✅
- **Source**: Local → `C:\Users\samth\Downloads\claude-mem\claude-mem-main`
- **Plugin ID**: `claude-mem@thedotmack`
- Persistent memory across sessions. Web viewer: `http://localhost:37777`

### 4. Playwright MCP ✅ (installed April 2026)
- Full browser control — navigate, click, fill forms, extract data, screenshot
- Available as plugin from Claude Plugins Marketplace
- Gives Claude a real Chromium browser to automate any website

---

## MCP Servers (in ~/.claude.json)

### Filesystem ✅
- Access to entire `C:\Users\samth` directory
- `claude mcp add filesystem --scope user -- npx -y @modelcontextprotocol/server-filesystem "C:/Users/samth"`

### Context7 ✅
- Pulls live, version-specific docs into Claude's context while coding
- `claude mcp add context7 --scope user -- npx -y @upstash/context7-mcp`

### GitHub ✅
- Full GitHub API — repos, PRs, issues, code review
- **⚠️ Regenerate token** — old token was exposed in chat
- `claude mcp add github --scope user -e GITHUB_PERSONAL_ACCESS_TOKEN=<new_token> -- npx -y @modelcontextprotocol/server-github`

---

## Pending Setup

### Auto Browser 🔄
- MCP-native browser control via Docker
- **Blocked**: Docker Desktop won't install (Windows permissions — "deny only" Administrators group)
- **Fix**: Restart PC → run Docker installer as admin on fresh boot
- **Files**: `C:\Users\samth\Downloads\auto-browser-main-extracted\auto-browser-main`
- See [[Setup/Auto Browser Setup]] for full details

### Brave Search MCP ⏳
- Real-time web search inside sessions
- Free API key: brave.com/search/api (10k searches/month)
- `claude mcp add brave-search --scope user -e BRAVE_API_KEY=<key> -- npx -y @modelcontextprotocol/server-brave-search`

---

## Saved Project Zips

| Tool | Location | How to Run |
|------|----------|-----------|
| Hermes Agent | `C:\Users\samth\Downloads\hermes-agent\hermes-agent-main` | Python — 15 messaging integrations |
| Pascal Editor | `C:\Users\samth\Downloads\editor\editor-main` | `bun install && bun dev` → localhost:3000 |
| Claude Official Plugins | `C:\Users\samth\Downloads\claude-plugins-official\claude-plugins-official-main` | playwright, github, context7, linear, telegram, etc. |

---

## Notes

- After any plugin/MCP change → **restart Claude Code** to activate
- Playwright MCP preferred over Docker auto-browser — simpler setup, no Docker needed
