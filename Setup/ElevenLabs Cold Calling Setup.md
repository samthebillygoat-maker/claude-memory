---
title: ElevenLabs Cold Calling Setup
date: 2026-04-27
tags: [elevenlabs, twilio, cold-calling, miami-arbitrage, setup]
type: reference
status: active
---

# ElevenLabs Cold Calling â€” 500 Calls/Day Setup

Full copy-paste guide: `C:\Users\samth\miami-arbitrage\data\elevenlabs_agent_config.md`

---

## Step 1 â€” Create Agent at elevenlabs.io

Go to â†’ **Conversational AI â†’ Create Agent**

**Agent Name:** `Miami Rental Outreach`  
**Voice:** Jessica (American, professional) Â· Speed: 1.0 Â· Stability: 0.5 Â· Similarity: 0.75

**First Message:**
```
Hi, is [landlord_name] available? This is Jessica calling about the rental property at [address].
```

**System Prompt:** Agent is "Jessica," a friendly rental inquirer. Goal: 12-month lease + subletting permission for occasional short-term stays. Never mentions "Airbnb arbitrage." If interested â†’ "My investor Sam will call you right back at [callback_number]."

**Dynamic Variables:**
| Variable | Example |
|----------|---------|
| `landlord_name` | Maria |
| `address` | 411 NW 37th St, Miami |
| `rent` | 1800 |
| `callback_number` | 925-409-8490 |

**Call Settings:** Silence timeout: 20s Â· Max duration: 3 min Â· End phrases: `not interested`, `stop calling`, `remove me`

---

## Step 2 â€” Connect Twilio

ElevenLabs â†’ **Settings â†’ Phone Numbers â†’ Add via Twilio**:
- Account SID: `[REDACTED-Twilio-SID]`
- Auth Token: (from `data/email_config.json`)
- Phone: `+17753695206`

Copy the **Phone Number ID** â€” needed in page 23.

---

## Step 3 â€” Get Agent ID

After saving â†’ URL bar shows agent ID. Also in DealScout: `agent_4801kpp6506efqhv1n4v62w555bs`

---

## Step 4 â€” Enter in Streamlit App

Page 23 (AI Caller) â†’ **Setup tab** â†’ paste ElevenLabs API key + Agent ID + Phone Number ID

---

## Launch 500 Calls

**Streamlit:** Page 23 â†’ Call Queue â†’ Select All Pending â†’ Launch

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

1. Streamlit â†’ Flask `server.py` triggers call
2. Twilio dials landlord via REST API
3. On answer: Twilio webhook returns TwiML with `<Connect><Stream>` to ElevenLabs
4. ElevenLabs WebSocket handles AI conversation
5. Second `<Stream>` forks audio to Flask for live monitoring

**Critical:** ElevenLabs API key must be in WebSocket URL as query param (`?xi-api-key=...`) â€” Twilio doesn't support custom WebSocket headers.

**ngrok** required (Twilio needs public URL). ngrok exe: `C:\Users\samth\miami-arbitrage\ngrok.exe`

---

## Run Every Session

```
# Terminal 1 â€” Flask server
cd C:\Users\samth\miami-arbitrage
set ELEVENLABS_API_KEY=[from dashboard]
set TWILIO_ACCOUNT_SID=[REDACTED-Twilio-SID]
set TWILIO_AUTH_TOKEN=[from email_config.json]
set TWILIO_FROM_NUMBER=+17753695206
set SERVER_URL=https://[ngrok-url-changes-each-session]
python server.py

# Terminal 2 â€” expose to internet
C:\Users\samth\miami-arbitrage\ngrok.exe http 5001

# Terminal 3 â€” DealScout UI
streamlit run app.py
```

âš ï¸ ngrok URL changes every session â€” always update SERVER_URL before starting Flask.

---

## Known Issue

ElevenLabs workflow has broken `voicemail_detection` tool reference in **Leave Voicemail** node â†’ causes "Documents with ids not found" error mid-call.

**Fix:** ElevenLabs â†’ agent `agent_4801kpp6506efqhv1n4v62w555bs` â†’ Workflow â†’ Leave Voicemail node â†’ remove broken tool reference

---

## Checklist Before First Call

- [ ] Agent created with system prompt
- [ ] Voice: Jessica, speed 1.0
- [ ] Twilio number connected â†’ Phone Number ID copied
- [ ] Agent ID + Phone Number ID pasted into page 23 Setup tab
- [ ] ElevenLabs API key entered
- [ ] Test call made to own number (925-409-8490)
- [ ] `data/api_keys_local.json` has `elevenlabs` key filled in

---

## See Also

- [[Projects/Miami Airbnb Arbitrage]]
- Full config: `C:\Users\samth\miami-arbitrage\data\elevenlabs_agent_config.md`
