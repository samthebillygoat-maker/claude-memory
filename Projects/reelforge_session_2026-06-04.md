---
type: project
created: 2026-06-04
tags: [reelforge, build, video, saas]
---

# ReelForge — Build Session 2026-06-04 (big one)

Sam's own sellable ($19 one-time) prompt-to-reel tool. Repo: `C:\Users\samth\projects\reelforge`.
Renderer = **Remotion** (license risk accepted — see below). Clean-room (zero Devini/ReelStack IP).

## State at end of session
**Phases 0–12 + 14 of PLAN.md done** + a big v1.1+ push this session. ~50 vitest passing, tsc clean.
Latest meaningful SHAs: studio `1621fe0`, surprise themes `1d0a3f5`, AI image gen `fae7f44`,
AI-footage reel `3cb722b`, **upload+keys `b6a3952`** (HEAD).

## What got built this session (in order)
1. **Media layer** — `media` scene: full-bleed images, Ken Burns, fast montage cuts, on-brand tint+scrim, overlay headline/sub (`src/scenes/Media.tsx`).
2. **Niche demos** for trades (self-recognition selling): detail-offer, window-clean, story-demo, detail-reel.
3. **Device scene (reel-in-a-reel)** — phone mockup plays a real rendered reel via OffthreadVideo (`src/scenes/Device.tsx`).
4. **sales-reel** — meta demo: industry-ad flash → theme cycle → "$19" → CTA.
5. **Endless theme generator** — `src/theme/generate.ts` `generateThemes(n, seed)` (curated palette+font pools, 12 fonts). `getTheme("gen:<seed>")` resolves generated themes. → `themeCycle` + `industryCycle` scenes flash 20+ looks / trade ads fast.
6. **ReelForge Studio** (the mockup) — local web app, `npm run studio` → **http://localhost:5174**. Dark UI: prompt, theme pills (+ 🎲 Surprise = endless gen themes), voice, music, **Your photos (upload)**, **Keys** section, phone preview, recent renders. Node http server (`studio/server.ts`, runs via tsx) renders via Remotion `--props` override (no spec-registry mutation). `src/studio/promptToSpec.ts` = local zero-config strategist.
7. **Local AI image gen** — `stable-diffusion.cpp` (`src/media/sdImage.ts`, `gen-image` CLI, doctor check, `docs/AI-IMAGE.md`). Binary at `C:\Users\samth\bin\sd-cpp\sd-cli.exe`; model `C:\Users\samth\bin\sd-models\sd-turbo2.safetensors` (5GB fp32, valid). **WORKS on CPU but output quality is weak/slow** → Sam said "looks bad."
8. **PIVOT (Sam's call):** default = **upload your own photos**; **optional BYO API keys** for the good path. `src/keys.ts` (~/.reelforge/keys.json), `src/media/openaiImage.ts` (gpt-image-1, BYO OPENAI key). Studio Keys UI saves OpenAI/ElevenLabs/Fal. Verified: upload → photo-first reel renders with photo full-bleed.

## Key decisions
- **Remotion license:** researched — "prompt-to-video apps" are the PAID "Automators" tier ($100/mo min). Sam's model = sell code/instructions, buyer self-installs + renders locally → strongest defensible reading. **Sam accepted the risk, declined the confirming email, ships on Remotion.** (Don't relitigate.)
- **Image quality:** local SD-Turbo/CPU not good enough → upload-photos default, paid key (OpenAI/Fal) = optional AI upgrade. Local SD kept as optional/GPU path, not default.
- **Tiering:** free = upload photos + Kokoro voice; +key = AI images + ElevenLabs/OpenAI voice. Base stays $19 one-time, no subscription, buyer's key = buyer's cost.

## How to run
- Studio UI: `npm run studio` → localhost:5174 (server was left running)
- Live preview all comps: `npm run dev` (Remotion Studio)
- Render: `npx reelforge render <id>` ; `npx reelforge gen-image "<prompt>"` (local SD or OpenAI key)
- ffmpeg at `C:\Users\samth\bin\ffmpeg.exe`. Render via the `demo` composition + `--props` for ad-hoc specs.

## Open / next
- Wire premium voice (ElevenLabs/OpenAI key) INTO the render pipeline (key set but VO swap not yet wired through studio).
- **Live preview** in studio (`@remotion/player` + bundler) — instant theme/prompt feedback, no 30s render. Bigger architectural lift (needs Vite). Deferred.
- Piper + Chatterbox local voice — queued, each to be verified not shipped unverified.
- Fal image/video provider hook.
- Manual: Gumroad product, Vercel landing deploy (see repo DISTRIBUTION.md).

Related: [[reelforge_build_plan_2026-06-04]]. Auto-memory: `project_reelforge_build_status_2026-06-04.md`.
