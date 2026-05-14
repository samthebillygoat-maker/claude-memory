# JARVIS — Voice Assistant for Personal Dashboard

**Repo:** `C:\Users\samth\dashboard\`
**Live:** `http://localhost:5173` (frontend), `http://localhost:8000` (backend)
**Stack:** FastAPI + SQLite (backend), React + Vite + TypeScript (frontend)

## What It Is
A real-time voice + text assistant overlaid on the personal command-center dashboard. Iron Man HUD aesthetic. Conversational, can act on the dashboard via tool calls, has long-term memory.

## Core Files
- **Backend:** `backend/main.py` (everything in one file: chat endpoint, tools executor, weather, ElevenLabs proxy, memories CRUD)
- **Frontend:** `frontend/src/Futuristic.tsx` (~2000 lines — single file, multi-component, all FX + JARVIS in one place)
- **Styles:** `frontend/src/App.css` (neon overlay + JARVIS HUD CSS appended at bottom)
- **DB:** `dashboard.db` SQLite, tables `jarvis_memories` + `jarvis_chat` for persistence

## Key Architectural Decisions
- **Single FuturisticLayer component** wraps everything; mounted with one line in App.tsx, easy to disable
- **Error boundary** around the FX layer so any crash there can't blank the dashboard
- **All FX gated on `body:not(.theme-light)`** — light theme stays clean
- **LLM = Groq Llama 3.3 70B Versatile** (primary) — fast (~700ms), free tier 14.4k req/day, conversational
- **TTS = ElevenLabs `eleven_turbo_v2_5`** with George voice (deep British, ID `JBFqnCBsd6RMkjVDRZzb`)
- **Browser TTS fallback** if ElevenLabs returns non-200
- **Speech-to-text = Web Speech API** (Chrome/Edge); typed-input fallback for unsupported browsers
- **Tool calling format = OpenAI standard** via Groq; with regex fallback for Llama's legacy `<function=name{...}</function>` format

## Endpoints (all under `/api/jarvis/`)
| Endpoint | Method | Purpose |
|---|---|---|
| `/chat` | POST | Tool-using conversation; body `{message, reset?}`; returns `{reply, model, actions, history_len}` |
| `/speak?text=` | GET | Returns mp3 audio from ElevenLabs, cached on disk by SHA-1 of `(voice|model|text)` in `storage/jarvis_tts/` |
| `/weather?location=` | GET | Open-Meteo + ipapi.co; smart geocoding; 10-min cache |
| `/memories` | GET | List remembered facts |
| `/memories/{id}` | DELETE | Remove a fact |
| `/config` | GET | `{elevenlabs: bool, voice_id}` — frontend uses to decide TTS path |

## Tool Inventory (LLM function calls)
| Tool | Side | Persistence |
|---|---|---|
| `switch_theme` | frontend action | localStorage |
| `navigate_to` | frontend action | — |
| `get_weather` | backend fetch | 10-min cache |
| `save_note` | backend file write | Obsidian vault `Inbox/` |
| `set_reminder` | frontend timer + UI | runtime only |
| `remember_fact` | backend SQLite | persistent |
| `forget_fact` | backend SQLite | persistent |
| `clear_conversation` | backend + frontend toast | wipes DB + memory |
| `suggest_command` | backend lookup | reads agents/commands tables |
| `play_music` | stub toast | not implemented |

## Wake Word + VAD
- Continuous passive listener when `WAKE` toggle is ON
- Patterns: `(hey|okay|ok|yo )?jarvis[,.! ]+(.*)` (case-insensitive)
- If captured-with-command: runs immediately. If wake-word alone: opens active HUD for follow-up.
- Auto-restarts on Chrome's 60s idle timeout
- **True VAD** (not naive timeouts): adaptive thresholds from rolling noise floor (25th percentile)
- Auto-submit after 1.1s of silence post-speech (configurable `TRAILING_SILENCE_MS`)
- Backup 2.5s text-finalization timer in case mic analyser fails

## Barge-in
- Mic stays open during speaking phase
- Sustained 280ms above raised threshold (0.18, vs 0.04 for normal listen) interrupts JARVIS mid-sentence
- Threshold raised to ignore his own voice bleeding into mic (best-effort echo handling)

## Speaking-Orb Sync
- ElevenLabs Audio element routed through `MediaElementAudioSourceNode` → `AnalyserNode` → speakers
- Tick loop reads frequency data, drives orb amplitude during `state === 'speaking'`
- Falls back to mic-driven pulse if `createMediaElementSource` unavailable

## Persistent State
- **Long-term memories:** `jarvis_memories` table; injected into every system prompt as `REMEMBERED FACTS ABOUT SAM:`
- **Chat history:** `jarvis_chat` table; loaded at startup; capped at 200 rows; rolling window of last 14 turns sent to LLM
- **Time-of-day classification:** late night / morning / afternoon / evening / late evening — injected into every system prompt
- **Live dashboard state:** `_dashboard_summary()` calls `insights_mod.hero()` and injects today's spend, sessions, projects, todos, notes into every system prompt

## Performance Cache (insights)
- `_WALK_CACHE` keyed by `(days, max_turns)` → `(timestamp, list[dict])`
- 5-minute TTL
- **Threading lock** so concurrent callers serialize; only one file walk runs at a time
- **Cache fallback:** asking for `(30, 20_000)` returns slice of cached `(30, 50_000)` — same data, wider window
- **Startup primer:** daemon thread warms `(30, 50_000)` immediately on boot

## Environment Variables (gitignored in `~/dashboard/.env`)
```
ELEVENLABS_API_KEY=sk_...
ELEVENLABS_VOICE_ID=JBFqnCBsd6RMkjVDRZzb   # George, British male
ELEVENLABS_MODEL=eleven_turbo_v2_5         # default; override-able
GROQ_API_KEY=gsk_...
GROQ_MODEL=llama-3.3-70b-versatile         # default
ANTHROPIC_API_KEY=...                      # fallback only; currently $0 balance
JARVIS_MODEL=claude-haiku-4-5              # used by Anthropic fallback
OBSIDIAN_VAULT=...                         # optional; defaults to ~/Documents/brain/claude-memory-main
```

## Keyboard Shortcuts
| Key | Action |
|---|---|
| **V** | Toggle JARVIS listen/stop |
| **Esc** | Close JARVIS HUD |
| **Cmd/Ctrl+K** | Command palette |
| **M** | Mute toggle |
| **T** | Cycle theme (neon → tron → matrix → synthwave) |
| **/** | Focus search bar |
| **?** | Open shortcuts modal |
| **Konami code** (↑↑↓↓←→←→BA) | 12-second Matrix rain easter egg |
| **Double-click any card** | Focus mode (fullscreen + backdrop blur) |

## Open Issues / Deferred
1. **Spotify** — `play_music` tool is a stub. Need: Spotify dev app registration → Client ID → PKCE OAuth flow → token storage → API calls. ~30 min build, blocked on user creating dev app.
2. **Slash command execution** — `suggest_command` looks up matching commands but doesn't actually run them. Would need subprocess to invoke Claude Code CLI from FastAPI; deferred.
3. **Streaming Groq responses** — would feel snappier; complicated by tool-call loop. Deferred.
4. **Voice cloning** — could clone Sam's voice via ElevenLabs Instant Voice Clone for personalized JARVIS. Not done.
5. **Anthropic fallback unusable** — $0 balance. Top up if needed.
6. **Llama 3.3 inline tool format quirks** — handled via regex fallback but model occasionally still leaks `</function>` text into final reply (stripped post-hoc).
7. **Voice-not-supported in Firefox** — only Chromium-based browsers support Web Speech API. Typed input works everywhere.

## Workflow / How to Use
1. Open `http://localhost:5173` in Chrome/Edge
2. Click the glowing JARVIS arc-reactor button (bottom-right) or press **V**
3. (Optional) Click `WAKE · OFF` to arm wake word — say *"Hey JARVIS, ..."* anytime
4. (Optional) Click `PROX · OFF` to enable proactive announcements (notifies you of new warn/danger events)
5. Speak naturally — JARVIS handles routing (action vs. conversation) automatically

## Things to Try First
- *"JARVIS, who are you?"* (gets the identity reply)
- *"Switch to matrix theme and tell me how many TODOs I have"* (chained tools + dashboard awareness)
- *"What's the weather in Chico California"* (smart geocoding, US-state filtered)
- *"Remember that I prefer short responses"* (persists across restarts)
- *"Set a 5 minute reminder to drink water"* (visible countdown card)
- *"Save a note: standup is 9am tomorrow"* (writes to Obsidian Inbox)
- *"I want to evaluate an STR deal"* (suggest_command → recommends `/triage-deal`)
