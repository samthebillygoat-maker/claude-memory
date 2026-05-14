---
name: DealMemo
description: SMS-only STR deal screener — text any deal, get a verdict in 60 seconds. The demo IS the product. $19/mo unlimited.
type: project
---

# DealMemo

**Repo:** `C:\Users\samth\dealmemo\`
**Initial commit:** `3189dc0` (2026-04-29)

## What it is
Twilio inbound SMS webhook → AI verdict reply. No app, no login. Send "rent $2,400 Tampa 2br, AirDNA $48k annual" → reply in <4 SMS lines: GO/MAYBE/NO-GO + ratio + target rent + walk-away + one-sentence why.

## Why it works
Distribution = the product. Screenshot a real text exchange on Twitter, post "text DEAL to (xxx) xxx-xxxx for free trial." Zero UI to build, asymmetric viral upside.

## Stack
Next.js 16 + TS + Tailwind v4 (green accent) • Twilio SMS webhook → TwiML reply • Anthropic Claude • Postgres via Prisma 7 • Stripe $19/mo (post-launch)

## What's actually working in commit 3189dc0
- `/api/sms` POST handler is **functional**, not stubbed. Has fast-path regex extraction (rent + annual revenue) → deterministic `quickVerdict()`. Falls back to Claude with a fixed system prompt for messy inputs.
- TwiML XML response with proper escape function
- Landing page at `/` shows the phone number and a real example exchange

## Tomorrow morning
1. Twilio: buy US number, set SMS webhook to `/api/sms`, grab SID + auth token
2. Anthropic API key
3. Supabase Postgres
4. (Optional) Stripe $19/mo price + paywall logic
5. ngrok for local Twilio testing

## TODOs in code
- Validate Twilio signature on inbound (security — must do before launch)
- Persist SmsConversation + SmsMessage rows + cost tracking
- Free-trial cap: 3 messages per phone before paywall
- Outbound message logging via Twilio status callback

## Hard constraints
- No phone-tree menus. The product is "text → reply." Don't add complexity.
- Replies must be ≤4 SMS-readable lines.
- Track cost per conversation (Anthropic) — paid users at $19 burning $5 in API are still profitable but watch margin
