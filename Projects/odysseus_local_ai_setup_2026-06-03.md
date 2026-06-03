# Odysseus — Local AI Workspace (no Docker) — 2026-06-03

Self-hosted ChatGPT/Claude-style AI workspace running **natively on the laptop, fully free/local**. Repo `pewdiepie-archdaemon/odysseus` cloned to `C:\Users\samth\odysseus`. Vetted before running (docker-compose/Dockerfile/requirements/setup.py all clean — localhost-only ports, no docker.sock, no curl|bash, standard PyPI deps).

## How to run it
- **Start server:** `cd C:\Users\samth\odysseus` then `.\venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 7000` (or `powershell -ExecutionPolicy Bypass -File .\launch-windows.ps1`).
- **Open:** http://localhost:7000
- **Login:** user `admin`. Password = the setup-generated temp password (stored in `odysseus/data/auth.json`); change it in Settings → Account.

## LLM = fully local & free (Ollama)
- Ollama already installed (v0.24). Model pulled: **qwen2.5:7b** (~4.6 GB, runs CPU-only — Intel Arc not accelerated by mainline Ollama).
- Endpoint registered in Odysseus: **Ollama (local)** → `http://localhost:11434/v1` (inserted directly into `data/app.db` `model_endpoints` table; Settings UI "Test" deadlocks because Odysseus runs its own Playwright browser that collides).
- **Critical fix:** set `OLLAMA_KEEP_ALIVE=-1` (User env var) + restarted Ollama so the model stays warm. Without it, cold-load is ~21 s and Odysseus's model probe times out ("probe failed after 1 attempt"). Warm call ≈ 1.6 s. `ollama ps` should show UNTIL = Forever. Costs ~4.6 GB RAM held resident (fine on 16 GB).

## Without Docker — what's missing
- **SearXNG** (bundled web search) is Docker-only → not running. For the **Deep Research** agent, set Search engine = **duckduckgo** (free, no key, no Docker). Other options (searxng/tavily/brave/google/serper) need Docker or API keys.
- **ChromaDB** vector store falls back to keyword matching; local embeddings still work via fastembed (all-MiniLM, auto-downloaded).

## Reality check on capability
Local 7B + DuckDuckGo is a generalist — slow (multi-round research = minutes) and weak at scraping listing sites (Zillow/Apartments.com block bots). Good for "does it work," NOT a replacement for the [[furnished_str_call_sheet_2026-06-03]] MLS pipeline. Always tell it "do not invent" + require source URLs so output is fact-checkable.

## Hardware
16 GB RAM, Intel Core Ultra 5 226V (Lunar Lake), Intel Arc 130V iGPU, Windows 11 Home.

Related: [[furnished_str_call_sheet_2026-06-03]]
