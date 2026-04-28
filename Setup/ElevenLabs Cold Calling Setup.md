---
title: ElevenLabs Cold Calling Setup
date: 2026-04-27
tags: [elevenlabs, twilio, cold-calling, miami-arbitrage, setup]
type: reference
status: active
---

# ElevenLabs Cold Calling — 500 Calls/Day Setup

Full copy-paste guide: `C:\Users\samth\miami-arbitrage\data\elevenlabs_agent_config.md`

---

## Step 1 — Create Agent at elevenlabs.io

Go to → **Conversational AI → Create Agent**

**Agent Name:** `Miami Rental Outreach`  
**Voice:** Jessica (American, professional) · Speed: 1.0 · Stability: 0.5 · Similarity: 0.75

**First Message:**
```
Hi, is [landlord_name] available? This is Jessica calling about the rental property at [address].
```

**System Prompt:** Agent is "Jessica," a friendly rental inquirer. Goal: 12-month lease + subletting permission for occasional short-term stays. Never mentions "Airbnb arbitrage." If interested → "My investor Sam will call you right back at [callback_number]."

**Dynamic Variables:**
| Variable | Example |
|----------|---------|
| `landlord_name` | Maria |
| `address` | 411 NW 37th St, Miami |
| `rent` | 1800 |
| `callback_number` | 925-409-8490 |

**Call Settings:** Silence timeout: 20s · Max duration: 3 min · End phrases: `not interested`, `stop calling`, `remove me`

---

## Step 2 — Connect Twilio

ElevenLabs → **Settings → Phone Numbers → Add via Twilio**:
- Account SID: `ACadfec5b845985ca53d66630c8da6b941`
- Auth Token: (from `data/email_config.json`)
- Phone: `+17753695206`

Copy the **Phone Number ID** — needed in page 23.

---

## Step 3 — Get Agent ID

After saving → URL bar shows agent ID. Also in DealScout: `agent_4801kpp6506efqhv1n4v62w555bs`

---

## Step 4 — Enter in Streamlit App

Page 23 (AI Caller) → **Setup tab** → paste ElevenLabs API key + Agent ID + Phone Number ID

---

## Launch 500 Calls

**Streamlit:** Page 23 → Call Queue → Select All Pending → Launch

**CLI:**
```
python C:\Users\samth\miami-arbitrage\scripts\launch_calls.py --limit 500 --concurrent 5
```

**Dry run first:**
```
python scripts\launch_calls.py --limit 10 --dry-run
```

---

## How the Stack Works

1. Streamlit → Flask `server.py` triggers call
2. Twilio dials landlord via REST API
3. On answer: Twilio webhook returns TwiML with `<Connect><Stream>` to ElevenLabs
4. ElevenLabs WebSocket handles AI conversation
5. Second `<Stream>` forks audio to Flask for live monitoring

**Critical:** ElevenLabs API key must be in WebSocket URL as query param (`?xi-api-key=...`) — Twilio doesn't support custom WebSocket headers.

**ngrok** required (Twilio needs public URL). ngrok exe: `C:\Users\samth\miami-arbitrage\ngrok.exe`

---

## Run Every Session

```
# Terminal 1 — Flask server
cd C:\Users\samth\miami-arbitrage
set ELEVENLABS_API_KEY=[from dashboard]
set TWILIO_ACCOUNT_SID=ACadfec5b845985ca53d66630c8da6b941
set TWILIO_AUTH_TOKEN=[from email_config.json]
set TWILIO_FROM_NUMBER=+17753695206
set SERVER_URL=https://[ngrok-url-changes-each-session]
python server.py

# Terminal 2 — expose to internet
C:\Users\samth\miami-arbitrage\ngrok.exe http 5001

# Terminal 3 — DealScout UI
streamlit run app.py
```

⚠️ ngrok URL changes every session — always update SERVER_URL before starting Flask.

---

## Known Issue

ElevenLabs workflow has broken `voicemail_detection` tool reference in **Leave Voicemail** node → causes "Documents with ids not found" error mid-call.

**Fix:** ElevenLabs → agent `agent_4801kpp6506efqhv1n4v62w555bs` → Workflow → Leave Voicemail node → remove broken tool reference

---

## Checklist Before First Call

- [ ] Agent created with system prompt
- [ ] Voice: Jessica, speed 1.0
- [ ] Twilio number connected → Phone Number ID copied
- [ ] Agent ID + Phone Number ID pasted into page 23 Setup tab
- [ ] ElevenLabs API key entered
- [ ] Test call made to own number (925-409-8490)
- [ ] `data/api_keys_local.json` has `elevenlabs` key filled in

---

## See Also

- [[Projects/Miami Airbnb Arbitrage]]
- Full config: `C:\Users\samth\miami-arbitrage\data\elevenlabs_agent_config.md`
