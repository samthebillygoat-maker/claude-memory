---
title: Auto Browser Setup
date: 2026-04-24
tags: [setup, docker, browser, automation, mcp]
type: reference
status: superseded
---

# Auto Browser Setup

> **Note:** Playwright MCP (installed April 2026) gives Claude full browser control without Docker. Use that instead. This doc kept for reference on the Docker auto-browser project.

---

## What It Is

Docker-based MCP browser control plane — gives Claude a real Playwright/Chromium browser.  
Files: `C:\Users\samth\Downloads\auto-browser-main-extracted\auto-browser-main`

---

## Docker Desktop Install — BLOCKED

**Error:** *"For security reasons C:\ProgramData\DockerDesktop must be owned by an elevated account"*

Root cause: User account (`samth`) has Administrators group set to **"deny only"** — common on Windows 11 local accounts.

**Fixes tried:**
- Run installer as admin → same error
- `takeown` + `icacls` → folder doesn't exist yet, not the issue
- `runas /user:Administrator` → blank password blocked by policy
- Set temp password + runas → installer window doesn't accept input

**If you still want Docker:**
1. Restart PC → run Docker Desktop installer as admin on fresh boot (before opening other apps)
2. Alternative: WSL2 + Docker inside Linux layer

---

## Once Docker Works

```bash
cd C:\Users\samth\Downloads\auto-browser-main-extracted\auto-browser-main
cp .env.example .env
docker compose up --build
```

Opens:
- Dashboard: http://127.0.0.1:8000/dashboard
- Browser view: http://127.0.0.1:6080/vnc.html?autoconnect=true&resize=scale
- API docs: http://127.0.0.1:8000/docs
