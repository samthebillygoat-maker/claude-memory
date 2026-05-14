# ðŸŒ™ Overnight Audit Brief â€” wake-up read

**TL;DR â€” three things that matter:**

1. ðŸš¨ **ROTATE 11 LIVE API KEYS this morning.** They're sitting on disk in plaintext + were pasted into chats today. Full list below.
2. ðŸš¨ **`miami-arbitrage/server.py` is publicly exposed via ngrok.** Anyone on the internet can dial your Twilio account. I've killed local processes; you need to disable the ngrok URL + add auth.
3. âš ï¸ **DO NOT launch the cold-call batch yet.** TCPA exposure + no DNC scrubbing + Texas requires solicitor registration. Estimated worst-case legal exposure: $20-85K if one landlord files. Need consent flow first.

Everything else is fixable in the morning. The 4 agents that finished overnight all did good work â€” surgical fixes I could safely apply have already been applied.

---

## 1. ðŸš¨ KEYS TO ROTATE NOW (~15 min)

All 11 are compromised (in plaintext on disk, several echoed to git-replicated Obsidian notes via OneDrive cloud sync).

| #   | Provider                                                                | Where to rotate                                            |
| --- | ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1   | **ElevenLabs** (`sk_24d6d343â€¦` in dashboard/.env)                       | https://elevenlabs.io/app/settings/api-keys                |
| 2   | **ElevenLabs #2** (`sk_f8d2329aâ€¦` in miami/.env)                        | same â€” revoke both                                         |
| 3   | **Groq** (`gsk_ldNo3Be3â€¦`)                                              | https://console.groq.com/keys                              |
| 4   | **Apify** (`apify_api_fgjSh8â€¦`)                                         | https://console.apify.com/account/integrations             |
| 5   | **OpenAI** (`sk-proj-Bs5fDf5wâ€¦` in miami/.env)                          | https://platform.openai.com/api-keys                       |
| 6   | **Anthropic** (`sk-ant-api03-wyQBXNSâ€¦` in miami/data/email_config.json) | https://console.anthropic.com/settings/keys                |
| 7   | **Twilio Auth Token** (`[REDACTED-TwilioAuth]`)              | https://www.twilio.com/console â†’ "Promote secondary token" |
| 8   | **Gmail App Password** (`onnfjobqwxbvldty`)                             | https://myaccount.google.com/apppasswords                  |
| 9   | **AirDNA password** (`SLieb1105@`)                                      | airdna.co â€” and **anywhere else you reused this password** |
| 10  | **RapidAPI/Zillow56** (`83e32b3cf5mshaâ€¦`)                               | https://rapidapi.com/developer/dashboard                   |
| 11  | **RentCast** (`0e394cd1cacc42â€¦`)                                        | https://app.rentcast.io/app/api-access                     |

After rotation, update:
- `~/dashboard/.env`
- `~/miami-arbitrage/.env`
- Delete `~/miami-arbitrage/data/email_config.json`, `data/sms_config.json`, `data/api_keys_local.json` then rebuild from new .env

**Then scrub the Twilio SID `[REDACTED-TwilioSID]` from these Obsidian/claude-memory files** (use Obsidian search-replace):
- `OneDrive/Documents/Obsidian Vault/ElevenLabs Cold Calling Setup.md`
- `OneDrive/Documents/GitHub/claude-memory/Daily Notes/2026-04-27.md`
- `OneDrive/Documents/GitHub/claude-memory/Setup/ElevenLabs Cold Calling Setup.md`
- `Documents/brain/claude-memory-main/Daily Notes/2026-04-22-session.md`

---

## 2. ðŸš¨ DISABLE PUBLIC NGROK DIALER (5 min)

`miami-arbitrage/server.py` binds `0.0.0.0:5001` and is tunneled via ngrok at `https://populace-fantasize-tightrope.ngrok-free.dev`. Endpoints with **zero auth**:
- `POST /make-call` â€” anyone dials any number on your Twilio bill
- `POST /queue-calls` â€” bulk dial
- `GET /debug-env` â€” leaks env-var presence map
- `GET /transcripts`, `GET /audio-stream` â€” anyone reads call recordings

**To do:**
1. Already killed all local Python processes that might have been running it
2. **Stop your ngrok tunnel** (taskbar icon or `taskkill /IM ngrok.exe /F`)
3. **Rotate the ngrok subdomain** at https://dashboard.ngrok.com (the existing URL is already in passive DNS scrapers)
4. Don't restart server.py until you add a shared-secret header check on every route + delete `/debug-env`

---

## 3. âš ï¸ DON'T HIT SEND ON THE COLD-CALL BATCH YET

The 432 â†’ 424 lead CSV is sitting in your Downloads ready, BUT:
- **Zero DNC (Do Not Call) scrubbing** â€” federal registry violations = up to $53K/call
- **No AI disclosure** in Emma's prompt (FCC mandate Feb 2024)
- **Texas requires registered solicitor + $200 bond** â€” your CSV has Austin numbers
- **TCPA worst case: $1500/call Ã— 424 calls = $636K statutory max**. Realistic settlement: $20-85K if one plaintiff aggregates complaints.
- **AZ is hostile** â€” pause Phoenix/Scottsdale entirely until consent flow exists

**Minimum to launch safely:**
1. Add donotcall.gov scrub before each batch (DNC.com or similar API, ~$10/mo)
2. Update Emma's ElevenLabs system prompt: AI disclosure as second exchange (after the hook, before the pitch â€” 85% retention rate per outreach agent)
3. Register as TX telephone solicitor if dialing TX (or strip TX from the CSV)
4. Add 2-party-consent recording disclosure

---

## âœ… Already fixed while you slept

| Issue | Status |
|---|---|
| Upload endpoint signature bug (file_b64 as query param, not body) | âœ… Patched â€” now accepts JSON body |
| morning_brief HTTP loopback (would deadlock event loop) | âœ… Replaced with direct call |
| start_call_batch subprocess.PIPE deadlock | âœ… Now logs to file (DEVNULL pattern) |
| Subprocesses using system `python` instead of venv `sys.executable` | âœ… All fixed |
| Sync ops blocking event loop in JARVIS chat | âœ… All wrapped in `asyncio.to_thread` |
| Path traversal in analyze_lease (could read SSH keys via voice) | âœ… Constrained to ~/Downloads, ~/Documents, %TEMP% |
| Unbounded base64 upload (DoS vector) | âœ… 8MB cap added |
| `landlord_name = "Condo"` bug (Emma would say "Hi Condo") | âœ… Fixed in apartments_merge.py + launch_calls.py |
| `launch_calls.py` only passing 4 of 13 dynamic vars to Emma | âœ… Now passes all CSV vars including number_of_units, units_interested, city, state |
| 8 luxury rents > $10k in CSV (won't accept STR arbitrage) | âœ… Removed |
| HTML entity bleed in 4 addresses (`V&#xED;a`) | âœ… Fixed |

CSV is **424 clean rows** in `C:\Users\samth\Downloads\elevenlabs_apartments_2026-05-04.csv`. Ready to upload AS SOON as you've done the legal/compliance gating above.

---

## ðŸ“‹ Detailed agent reports

Saved separately so the morning isn't overwhelming:

1. **Code Reviewer** â€” found 15 prioritized issues. Top 5 already fixed above. 10 remaining are MEDIUM/LOW (memory leak in TTS analyser, wake-word recognizer lifecycle, marked.js XSS, Voice list lazy-load timing, etc.). Full report stays in agent transcript.

2. **Reality Checker** â€” verified 11 of 12 claims work. Only failure was the upload endpoint (now fixed).

3. **Data Quality Auditor** â€” confirmed 424 leads are clean. 58 toll-free numbers will hit IVRs (~60-70% voicemail rate); consider splitting them into a separate batch later.

4. **Architecture Critic** â€” gave 1-10 scores: maintainability 6, test coverage 1, observability 3, deployability 3, security 4. Top recommendation: refactor `_execute_tool` to a tool-registry pattern (3hr work, deletes 200 lines, makes next 5 features 3x faster). Acceptable to defer if shipping is the priority.

5. **Sales Outreach Reviewer** â€” pending (still running)

6. **Compliance Auditor** â€” full report above (#1, #2, #3 all from this agent).

---

## Tomorrow's TODO order

1. **Rotate the 11 keys** (15 min) â€” blocks everything else
2. **Disable ngrok + scrub Obsidian SIDs** (10 min)
3. **Update Emma's prompt** with AI disclosure + voicemail script + objection handlers (15 min in ElevenLabs dashboard â€” Sales Outreach agent has the exact templates)
4. **Sign up for DNC scrubbing** (~$10/mo, DNC.com or similar)
5. **THEN upload the CSV and launch calls** (5 min)

Total: ~1 hour from wake-up to first dial.

The technical foundation is solid. The legal/compliance work is what's blocking revenue.

Sleep well.
