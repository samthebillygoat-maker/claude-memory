---
type: project
date: 2026-06-17
tags: [claude-code, hooks, settings, prospect-site, prettier, vercel]
---

# Claude Code Guardrails + Prettier Adoption — 2026-06-17

Hardened the Claude Code setup and made code-formatting automatic for new prospect sites. Triggered by a "top 3 actions" morning brief — only 1 of the 3 was real after reality-check.

## Morning-brief reality-check (don't act on briefs blindly)
- **Update to v2.1.179** → already on **2.1.181**, no-op.
- **`.env` write-validator hook** → live-key writes were ALREADY guarded (`stripe-live-key-write-guard.py` PreToolUse + `.env.production` read-denies). Real gap = trailing-whitespace contamination. Built that.
- **`chmod 444` + distrust PreToolUse** → `chmod` is a Linux no-op on Windows; protection already existed.
- Skim items (Fable 5 Commerce Dept, etc.) = unverifiable noise, ignored.

## Hooks added (`~/.claude/hooks/`, wired in `~/.claude/settings.json`)
1. **`env-whitespace-guard.py`** — PostToolUse `Write|Edit`. On `.env*` files, blocks (exit 1) values with trailing whitespace or whitespace inside quotes. Catches Sam's documented piped-echo `.env` bug.
2. **`lockfile-guard.py`** — PreToolUse `Write|Edit`. `*.lock.md` → **deny** (protects `business-pulse/GUARDRAILS.lock.md`); dep locks (package-lock.json/yarn.lock/pnpm-lock.yaml/uv.lock/etc) → **ask**.
3. **`autoformat-on-edit.py`** — PostToolUse `Write|Edit`. Formats the touched file ONLY if the owning project is configured: prettier (`.prettierrc`/dep) for JS/TS/JSON/CSS/MD/HTML, `ruff format` for `.py` with `[tool.ruff]`. Always exits 0.
   - ⚠️ **Windows gotcha fixed:** `subprocess(["npx",...], shell=False)` silently fails — `npx` is `npx.cmd`. Hook now calls the local binary directly via `node_modules/.bin/prettier.cmd` (walks up to find it). Same spawn-npx footgun as the reelstack note.
   - Only fires after `npm install` in a project (deliberately no auto-install).

Final `Write|Edit` stack: Pre = stripe-live-key-write-guard → lockfile-guard. Post = env-whitespace-guard → autoformat-on-edit.

## Prettier adoption — prospect sites
- **Template seeded:** `~/projects/build-kit/` now carries `.prettierrc.json` (printWidth 100, double quotes, semi, 2-space) + `.prettierignore`.
- **Skill updated:** `~/.claude/skills/prospect-site/SKILL.md` — new sites must add `prettier` devDep + `format` script, copy the two configs from build-kit, and `npm install` once.
- **Pilot:** `caratti-jewelers-livermore` fully retrofitted (prettier 3.8.4 installed, configs in place). Verified the hook formats real HTML/JS edits end-to-end (collapsed one-line AI output → clean multi-line).
- **Existing live sites NOT retrofitted** (amazing-day-spa, other Livermore builds) — applies going forward; batch-retrofit is optional follow-up.

## Vercel deploy gotcha (re-confirmed)
- Deployed caratti pilot: https://caratti-jewelers-livermore-b1qo9volo.vercel.app (READY).
- Anonymous = **401** because Deployment Protection ("Vercel Authentication") defaults ON. Owner CAN view while logged in.
- Tried disabling via REST API with the CLI token → **403 `invalidToken`**. Confirms prior memory: CLI OAuth token works for `vercel deploy` but is rejected for settings writes. **Must toggle OFF in dashboard** (Settings → Deployment Protection) to make public.

## Not done (by Sam's call)
- **No pruning** of the 86 agents / 102 skills (Sam said don't, despite saturation).
- Supabase/Postgres MCP still the one genuine integration gap — needs live DB creds + decision on which of the 5 SaaS DBs are running.
