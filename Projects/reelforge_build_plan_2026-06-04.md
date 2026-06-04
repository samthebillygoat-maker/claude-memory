# ReelForge — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax. Run a **Reality Checker** agent gate at the end of every phase — do NOT mark a phase done on "the diff looks right"; render real frames and verify.

**Goal:** Build an original, clean-room 9:16 reel-generation engine + Claude Code skill that turns a sentence into on-brand, voiced, captioned vertical videos — sold as a $19 one-time product that beats ReelStack on configurability, voices, captions, and the prompt→reel pipeline.

**Architecture:** A Remotion (React/TS) renderer driven by a typed, Zod-validated `ReelSpec`. A theme layer (tokens: palette/fonts/motion/grain) makes every visual brand-configurable from one file or a URL scan. A Claude Code skill (`/reel`) plus three sub-agents (strategist → writes specs, brand-extractor → builds themes from a URL, QA critic → reality-checks renders) form the "magic." Offline TTS (Kokoro) + Whisper captions make reels voiced and subtitled with zero API keys. A CLI ties init/add/render/tts/captions/doctor together. Sold via Gumroad with a license-key gate + installable skill.

**Tech Stack:** Remotion 4.x, TypeScript (strict), Zod, `@remotion/google-fonts`, `@remotion/install-whisper-cpp` (caption timing), `kokoro-js` (offline TTS) with optional ElevenLabs/OpenAI providers, `@remotion/media-utils` (audio duration → audio-locked timing), Vitest (unit tests), Commander (CLI), Gumroad (license keys). Node 20+.

**Working name:** ReelForge (alts: Reelsmith, Showrunner, Vertical, ReelKit — pick before Phase 10; check trademark + handle availability).

---

## ⚠️ Phase 0 — CLEAN-ROOM MANDATE (do first, non-negotiable)

The existing `~/reelstack-reels` project is **derived from the licensed @devinilabs/reelstack product** (its reference reels + `designSystem.ts` "extracted from devini.io"). **None of that code, tokens, fonts mapping, reference reels, or naming may ship in this product.** This repo is a fresh clean-room build.

**Allowed to reuse:** only original code authored for Sam's batch — the *ideas* in `EditorialReel.tsx` (data-driven scenes, the `Scene` discriminated union, Sequence-based timing). **Re-author it from scratch here**; do not import anything from `reelstack-reels` or `@devinilabs/reelstack`.

- [ ] **Step 1:** Create repo `C:\Users\samth\projects\reelforge`, `git init`, Node 20 check (`node -v`).
- [ ] **Step 2:** `npx create-video@latest --blank` (Remotion) into a temp, copy only `package.json`/`tsconfig` baseline; remove any Remotion template demo content.
- [ ] **Step 3:** Add deps: `npm i zod kokoro-js commander` ; `npm i -D vitest @types/node` ; `npx remotion versions` to confirm; add `@remotion/google-fonts`, `@remotion/media-utils`, `@remotion/install-whisper-cpp`.
- [ ] **Step 4:** Write `LICENSE-COMMERCIAL.md` (single-seat, no-resale-of-source) + `README.md` stub. Add `NOTICE.md` stating the product is original and ships no third-party reel templates.
- [ ] **Step 5:** Add `.github/workflows/ci.yml` running `tsc --noEmit` + `vitest run` on push.
- [ ] **Step 6: Reality-check gate** — dispatch a `general-purpose` agent to grep the whole repo for `devini`, `reelstack`, `graphify`, `extracted from` and confirm ZERO matches. Commit: `chore: clean-room scaffold`.

---

## Differentiation (the "blows Devini out of the water" checklist — every item is a task below)
1. **Brand-from-URL** — paste your site, get a theme (Phase 7).  Devini: hand-coded tokens.
2. **Prompt→reel** — "5 reels about X" → finished specs (Phase 7).  Devini: you write every reel.
3. **Offline voices** — Kokoro TTS, no API key, audio-locked timing (Phase 5).  Devini: bring-your-own VO.
4. **Auto-captions** — Whisper-timed, on-brand caption styles (Phase 6).  Devini: none.
5. **Theme switch** — one flag re-skins all reels; 3 themes shipped (Phases 1,4).
6. **10+ scene types** + registry so buyers add their own (Phase 3).
7. **Multi-aspect** — 9:16 / 1:1 / 16:9 from one spec (Phase 2).
8. **Built-in reality-check QA** — 5-dimension critic agent gates every render (Phase 9).
9. **$19 one-time + installable skill** (Phase 10).

---

## File Structure (lock decomposition here)
```
reelforge/
  src/
    theme/
      schema.ts          # Zod Theme schema + Theme type
      themes/
        editorial.ts     # cream/olive (Sam's validated look, re-authored)
        cinematic.ts     # dark
        mono.ts          # bold black/white
      index.ts           # theme registry + getTheme()
    spec/
      schema.ts          # Zod Scene union + ReelSpec + totalFrames()
    engine/
      Reel.tsx           # main renderer: backdrop + sequence map + footer
      Backdrop.tsx       # themed background (wash/grid/grain)
      motion.ts          # rise(), sceneFade(), easings
      Words.tsx          # staggered word reveal
    scenes/
      registry.ts        # type -> component map
      Title.tsx Stat.tsx Steps.tsx List.tsx Quote.tsx Cta.tsx
      Comparison.tsx Bento.tsx Testimonial.tsx Timeline.tsx Captioned.tsx
    audio/
      tts.ts             # Kokoro + provider interface (ElevenLabs/OpenAI optional)
      captions.ts        # whisper-cpp transcription -> caption cues
      lock.ts            # audio-locked timing: vo duration -> scene.seconds
    Root.tsx             # registers compositions from a specs dir
    cli.ts               # init/add/render/render-all/tts/captions/doctor
    license.ts           # Gumroad license-key verification
  skill/
    SKILL.md             # /reel skill entry
    agents/
      strategist.md      # topic -> ReelSpec[]
      brand-extractor.md # URL -> Theme
      qa-critic.md       # render frames -> 5-dim critique gate
  examples/specs/        # YOUR original demo specs (no Devini content)
  tests/                 # vitest
  docs/plan.md           # this file
```

---

## Phase 1 — Theme system

**Files:** Create `src/theme/schema.ts`, `src/theme/themes/editorial.ts`, `src/theme/index.ts`, `tests/theme.test.ts`.

- [ ] **Step 1: Write failing test** `tests/theme.test.ts`:
```ts
import { describe, it, expect } from "vitest";
import { ThemeSchema } from "../src/theme/schema";
import { editorial } from "../src/theme/themes/editorial";
describe("theme", () => {
  it("editorial theme is valid", () => {
    expect(() => ThemeSchema.parse(editorial)).not.toThrow();
  });
  it("rejects a theme missing palette.accent", () => {
    const bad = { ...editorial, palette: { ...editorial.palette, accent: undefined } };
    expect(() => ThemeSchema.parse(bad)).toThrow();
  });
});
```
- [ ] **Step 2:** Run `npx vitest run tests/theme.test.ts` → FAIL (module not found).
- [ ] **Step 3:** Implement `src/theme/schema.ts`:
```ts
import { z } from "zod";
export const ThemeSchema = z.object({
  name: z.string(),
  palette: z.object({
    bg: z.string(), bgAlt: z.string(), ink: z.string(),
    inkMuted: z.string(), accent: z.string(), accent2: z.string(),
    card: z.string(), hairline: z.string(),
  }),
  fonts: z.object({ display: z.string(), label: z.string(), body: z.string() }),
  motion: z.object({ riseFrames: z.number(), blurStart: z.number() }),
  grain: z.number().min(0).max(1),
});
export type Theme = z.infer<typeof ThemeSchema>;
```
- [ ] **Step 4:** Implement `src/theme/themes/editorial.ts` (re-author Sam's cream/olive tokens — `bg:#F3EEE3, ink:#26241D, accent:#BF6B43, accent2:#535A3E, card:#FBF8F1`; fonts Cormorant Garamond / Marcellus / Jost loaded via `@remotion/google-fonts`). Implement `src/theme/index.ts` with `themes` record + `getTheme(name)`.
- [ ] **Step 5:** Run test → PASS. Commit `feat: theme schema + editorial theme`.
- [ ] **QA gate:** none (pure data) — typecheck must pass.

## Phase 2 — Core engine + spec schema

**Files:** Create `src/spec/schema.ts`, `src/engine/{motion.ts,Words.tsx,Backdrop.tsx,Reel.tsx}`, `src/Root.tsx`, `tests/spec.test.ts`.

- [ ] **Step 1: Failing test** `tests/spec.test.ts` for `totalFrames`:
```ts
import { totalFrames } from "../src/spec/schema";
it("sums scene seconds * fps", () => {
  expect(totalFrames({ id:"x", handle:"@x", theme:"editorial", scenes:[
    { type:"title", lines:["a"], seconds:5 },
    { type:"cta", word:"GO", handle:"@x", seconds:5 },
  ]}, 30)).toBe(300);
});
```
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement `src/spec/schema.ts` — Zod discriminated union `SceneSchema` (title|stat|steps|list|quote|cta to start), `ReelSpecSchema` (`id`, `handle`, `theme`, `aspect: "9:16"|"1:1"|"16:9"` default 9:16, `scenes[]`), and `totalFrames(spec, fps)`. IDs must match `/^[A-Za-z0-9-]+$/` (Remotion rejects underscores — enforce in schema with `.regex`).
- [ ] **Step 4:** Run → PASS.
- [ ] **Step 5:** Implement `src/engine/motion.ts` (`rise`, `sceneFade`, eases), `Words.tsx` (staggered reveal, themed), `Backdrop.tsx` (theme-driven wash + grid + grain), `Reel.tsx` (takes `{spec}`, resolves theme via `getTheme`, maps scenes to `<Sequence>`, renders footer handle, sizes to aspect). `Root.tsx` reads `examples/specs/*.ts` and registers a `<Composition>` each.
- [ ] **Step 6:** Add `examples/specs/demo.ts` (one ORIGINAL demo reel).
- [ ] **Step 7: Reality-check gate** — `npx remotion render demo out/demo.mp4`; extract frames at each scene (`ffmpeg -ss t -i out/demo.mp4 -frames:v 1 f.png`); dispatch **qa-critic** agent (or Reality Checker) to confirm: text inside safe zones, legible, theme colors correct, no overlaps. Fix until pass. Commit `feat: core engine renders demo`.

## Phase 3 — Scene library (10+ types)

**Files:** Create `src/scenes/*.tsx` + `src/scenes/registry.ts`; extend `src/spec/schema.ts` union; `tests/scenes.test.ts`.

For EACH scene type (title, stat, steps, list, quote, cta, comparison, bento, testimonial, timeline, captioned):
- [ ] **Step A:** Add its variant to `SceneSchema` (exact fields).
- [ ] **Step B:** Implement `src/scenes/<Name>.tsx` reading `theme` from context, using `motion` helpers. One responsibility per file.
- [ ] **Step C:** Register in `registry.ts` (`type -> component`).
- [ ] **Step D: Reality-check** — render a one-scene demo, frame-grab, qa-critic verifies layout/legibility/safe-zone. Commit per scene (`feat(scene): stat`).
- [ ] **Step E:** `tests/scenes.test.ts` asserts every union `type` has a registry entry (prevents missing-renderer bugs).

## Phase 4 — More themes

**Files:** `src/theme/themes/{cinematic.ts,mono.ts}`, `tests/theme.test.ts` (extend).
- [ ] Author `cinematic` (dark olive-deep ground, terracotta/cream) and `mono` (black/white, one accent). Both must pass `ThemeSchema`.
- [ ] **Reality-check:** render `demo` under all 3 themes (`--props='{"spec":{...,"theme":"cinematic"}}'`), frame-grab a 3-up, qa-critic confirms each reads well + on-theme. Commit `feat: cinematic + mono themes`.

## Phase 5 — Voiceover (offline, audio-locked)

**Files:** Create `src/audio/tts.ts`, `src/audio/lock.ts`, `tests/tts.test.ts`. Add optional `vo?: string` to relevant scenes in `SceneSchema`.

- [ ] **Step 1:** `src/audio/tts.ts` — `interface TTSProvider { synth(text:string, voice:string): Promise<{wavPath:string}> }`. Implement `KokoroProvider` (kokoro-js, downloads model on first run, **no API key**). Add `ElevenLabsProvider` + `OpenAIProvider` guarded behind env keys (optional premium).
- [ ] **Step 2: Failing test** `tts.test.ts`: KokoroProvider.synth("hello","af_sky") returns a path to a non-empty .wav. Run → FAIL → implement → PASS.
- [ ] **Step 3:** `src/audio/lock.ts` — `lockTiming(spec)`: for each scene with `vo`, synth wav, measure duration via `@remotion/media-utils getAudioDurationInSeconds`, set `scene.seconds = max(scene.seconds, voDur + 0.6)`. Returns spec + per-scene wav paths. (This is the "audio-locked" advantage — text never outruns the voice.)
- [ ] **Step 4:** In `Reel.tsx`, mount `<Audio>` per scene wav inside its `<Sequence>`.
- [ ] **Step 5: Reality-check:** render `demo` with `vo` on every scene; play output; qa-critic + manual check that VO aligns to scene cuts. Commit `feat: offline TTS + audio-locked timing`.

## Phase 6 — Auto-captions

**Files:** Create `src/audio/captions.ts`, `src/scenes/Captioned.tsx`, `tests/captions.test.ts`.
- [ ] **Step 1:** Install whisper via `@remotion/install-whisper-cpp` (programmatic, downloads model). `captions.ts` — `transcribe(wavPath): Promise<Caption[]>` (`{text,startMs,endMs}`).
- [ ] **Step 2: Failing test:** transcribe a known short wav → returns ≥1 caption with ascending timestamps. Implement → PASS.
- [ ] **Step 3:** Caption renderer: word-by-word highlight synced to cues, themed (accent highlight, Marcellus/Jost). Toggle via `spec.captions: true`.
- [ ] **Step 4: Reality-check:** render with captions; qa-critic verifies caption timing, safe-zone (above the bottom 22%), readability. Commit `feat: whisper auto-captions`.

## Phase 7 — Skill + agents (the magic)

**Files:** Create `skill/SKILL.md`, `skill/agents/{strategist,brand-extractor,qa-critic}.md`, `src/cli.ts` hooks.
- [ ] **strategist.md** — input: topic + count + handle + theme. Output: validated `ReelSpec[]` written to `examples/specs/<slug>.ts`. Must follow a copy rubric (one-idea hook, concrete numbers, single-word CTA) and pick scene types per beat. Include the rubric inline (no placeholder).
- [ ] **brand-extractor.md** — input: a URL. Uses WebFetch to read CSS/colors/fonts → emits a `Theme` object validated by `ThemeSchema`, written to `src/theme/themes/<brand>.ts`. (Mirrors the value of `ads-dna` but outputs a ReelForge theme.)
- [ ] **qa-critic.md** — input: a rendered mp4 path. Extracts frames (ffmpeg), scores 5 dimensions (palette, motion, timing, hierarchy, brand-fit) 0–10 each, returns Keep/Fix list; **fails the gate if any dimension < 7**.
- [ ] **SKILL.md** — `/reel <topic>` orchestration: brand-extractor (if URL) → strategist → `render-all` → qa-critic gate → report. Document trigger phrases.
- [ ] **Reality-check:** run `/reel "3 reels about cold email" --theme editorial`; confirm 3 valid specs render + pass qa-critic. Commit `feat: /reel skill + strategist/brand/qa agents`.

## Phase 8 — CLI

**Files:** `src/cli.ts` (Commander), `package.json` bin, `tests/cli.test.ts`.
- [ ] Commands: `init` (scaffold brand config + sample spec), `add <type>` (append a scene), `render <id>`, `render-all` (loop spec ids → `out/<id>.mp4` → copy to `--out` dir), `tts <id>`, `captions <id>`, `doctor` (checks Node/ffmpeg/whisper/kokoro model). 
- [ ] **Test:** `cli.test.ts` runs `node dist/cli.js doctor` → exit 0 and prints all checks. Implement → PASS. Commit `feat: CLI`.

## Phase 9 — Reality-check QA harness (productized)

**Files:** `src/qa/contactSheet.ts`, wire into `render-all`.
- [ ] Build `contactSheet(ids)` (ffmpeg hstack/vstack of hook+cta frames — reuse the approach Sam used for the 20-reel QA). `render-all --qa` produces `out/qa/ALL.png` + dispatches qa-critic per reel; prints a pass/fail table. Commit `feat: built-in reality-check QA`.

## Phase 10 — Packaging + license + distribution

**Files:** `src/license.ts`, `scripts/package.ts`, Gumroad product.
- [ ] `license.ts` — verify a Gumroad license key via their `/v2/licenses/verify` API; cache locally; gate `render-all` behind a valid key (clear error + purchase URL if missing). **Test with a mocked fetch.**
- [ ] `scripts/package.ts` — produce `reelforge.zip` (src + skill + examples + README, excluding node_modules/.git/out).
- [ ] Create the **Claude Code skill install** path: `skill/SKILL.md` + an `install.md` so buyers drop it in `~/.claude/skills/`.
- [ ] Gumroad: product page, $19 one-time, license keys ON, deliver the zip + a "getting started" PDF. Commit `feat: license gate + packaging`.
- [ ] **Reality-check:** on a clean clone, `npm i && npx reelforge doctor && npx reelforge render-all` works from zero with no Devini deps.

## Phase 11 — Launch assets (marketing)
- [ ] Build a 25–35s **demo reel of ReelForge itself** (meta: a reel that sells the reel tool) using ReelForge.
- [ ] One-page landing (Framer/static) with the demo, 3 theme screenshots, feature list, $19 buy button.
- [ ] 5 launch posts for Sam's accounts (the tool's own reels are the ads). Cross-post TikTok/Shorts.

---

## Reality-Check Gates (how "done" is judged every phase)
A phase is done only when: (1) `tsc --noEmit` clean, (2) `vitest run` green, (3) for any visual change, **frames rendered + qa-critic agent returns all 5 dimensions ≥ 7**. Never accept "diff matches spec" as done — render and look. (Mirrors Sam's standing rule: review every task with real agent-driven QA.)

## Self-Review (done)
- Spec coverage: every differentiation item maps to a phase (1–10). ✓
- Placeholder scan: schemas/interfaces/tests are concrete; agent docs require inline rubrics (flagged in their tasks). ✓
- Type consistency: `Theme`, `ReelSpec`, `Scene`, `TTSProvider`, `Caption`, `totalFrames(spec,fps)` names used consistently across phases. ✓
- IP: Phase 0 gate greps for Devini/ReelStack = 0 matches before anything else. ✓

---

# Standout Upgrades — Deep Dive (v1.1 scope, prioritized)

**Core insight:** what makes a reel *perform* is not the template — it's the **hook (first 1.5s), retention pacing, captions, and audio**. v1 (Phases 1–11) ships a clean engine; these phases make the OUTPUT genuinely better and the product hard to compete with. Build in this priority order.

## TIER 1 — makes the reels themselves measurably better (do first)

### Phase 12 — Hook & Retention Engine (highest ROI)
The single biggest lever. Specs shouldn't have *one* hook — they should have the *best* hook, chosen from variants.
- **strategist v2**: for each reel, generate **5 hook variants** across proven formulas (negativity/"stop doing X", curiosity gap, big number, contrarian, "nobody tells you"), then self-score each on a rubric (specificity, tension, scroll-stop, ≤7 words) and pick the winner; keep the other 4 as `altHooks` for A/B.
- **Retention structure**: enforce a beat map — pre-hook (0–0.5s static frame so the thumbnail/loop reads), hook (0–2s), payoff cadence (a new idea every 2–3s), pattern interrupt at ~50%, **seamless loop** ending (last frame ≈ first frame to farm replays).
- **Open-loop CTA**: CTA scene teases the DM payoff ("the 3 numbers I check") instead of a flat ask.
- Files: extend `skill/agents/strategist.md` rubric; add `altHooks?: string[]` to spec; add `loop?: boolean` handling in `Reel.tsx` (crossfade tail→head).
- **QA gate:** qa-critic adds a "hook strength" dimension; fail if winning hook scores <8.

### Phase 13 — High-Retention Captions ("karaoke" word-sync)
Word-by-word animated captions are the most proven retention booster on Reels/TikTok. v1 captions are basic; make them best-in-class.
- Word-level timing from Whisper (`@remotion/install-whisper-cpp` returns word timestamps) → **active-word highlight** (accent color/scale pop), 1–3 words on screen at a time, bottom-third safe.
- Ship **4 caption styles**: Clean, Bold-Box, Highlight-Sweep, Karaoke-Pop. Auto-emphasis: bold the noun/number in each phrase.
- Auto-emoji injection (optional, off by default — tasteful).
- Files: rewrite `src/scenes/Captioned.tsx` + `src/audio/captions.ts` (word cues); `captionStyle` on spec.
- **QA gate:** legibility contrast check (WCAG AA against the frame) + safe-zone validation.

### Phase 14 — Music + Beat-Synced Motion
Audio is half the reel. Silent card reels lose.
- Ship a small **CC0/royalty-free music library** (verified licenses, stored in `assets/music/`, NOT copyrighted tracks) tagged by mood (calm/energetic/cinematic/upbeat).
- **Beat detection** (analyze BPM + onsets via `web-audio-beat-detector` or an ffmpeg/aubio pass) → snap scene cuts and text-pops to the beat grid (productizes Sam's `reelstack-beats` idea, automated).
- **Audio-reactive accents**: subtle scale/glow pulse on the beat for stat/CTA scenes.
- Auto-duck music under VO (sidechain-style gain).
- Files: `src/audio/music.ts` (pick track by mood + loop to length), `src/audio/beats.ts` (beat grid), wire into timing in `src/audio/lock.ts`.
- **Honesty:** must ship genuinely license-clear music; document each track's license in `assets/music/LICENSES.md`. Do not bundle anything ambiguous.

### Phase 15 — Media Layer (b-roll, screenshots, Ken Burns)
Top reels mix media; all-typography reels cap out.
- **Stock media**: Pexels/Pixabay API (free, buyer's key) — fetch relevant photo/video by scene keywords, Ken Burns slow-zoom, themed color-grade overlay so stock matches brand.
- **Website capture**: headless-Chrome screenshot / scroll-capture of a URL (reuse the approach Sam used: `chrome --headless --screenshot`) for product/SaaS reels.
- **Image slot**: spec scene `image`/`video` that drops user media with safe framing + grain/tint to stay on-theme.
- Files: `src/media/stock.ts`, `src/media/capture.ts`, `src/scenes/Media.tsx`.
- **QA gate:** ensure media never covers caption/CTA safe zones; color-grade applied.

## TIER 2 — scale & differentiation

### Phase 16 — Variation Engine (A/B at scale)
- `reelforge vary <id> --n 4`: emit N variants (swap winning vs alt hooks, theme, scene order, music mood) for testing which hook/edit wins.
- `reelforge batch <topics.csv>`: a column of topics → a folder of finished reels.
- **Repurpose**: `reelforge from <url|transcript.txt>` → strategist chunks a blog post / YouTube transcript / long caption into a 3–6 reel series. This is a killer acquisition feature (creators have content, not time).

### Phase 17 — Brand Fidelity++ (from a URL, go deep)
- brand-extractor v2 pulls: exact **colors**, **fonts (download + self-host)**, **logo** (favicon/og-image → cleaned mark), product **screenshots**, and a **voice profile** (tone, do/don't words) from the site copy.
- Auto-generate a **logo lockup** (like the CitySide arch mark) when no logo exists.
- Output a `brand.json` the buyer can tweak — one source of truth for every reel.

### Phase 18 — Multi-Platform & Localization
- Per-platform **safe-zone masks** (TikTok caption/UI overlap ≠ Reels ≠ Shorts) baked into render presets, not just aspect ratio.
- One spec → 9:16 + 1:1 + 16:9 in one command.
- **Localization**: translate copy (LLM) + regenerate TTS per language → same reel in N languages.

## TIER 3 — later / v2 (don't block launch)
- **Cloud render** via `@remotion/lambda` for batch speed (consumer CPUs are slow at 30fps+effects; default 30fps, offer Lambda).
- **Auto-post / scheduling** (Postiz/Buffer/Meta Graph API) + a content-calendar export. High maintenance — v2.
- **Analytics loop**: log which hook/variant was posted → manual win-rate input → strategist learns. v2.
- **Theme/template marketplace** (community-contributed themes) — moat + recurring revenue.

## Honest constraints to design around
- **TTS ceiling:** Kokoro is good-not-ElevenLabs. Make ElevenLabs/OpenAI **first-class optional** (buyer's key) and ship the *best* Kokoro voices as the free default. Voice quality is a top reason a reel feels pro.
- **Music licensing:** only ship verifiably CC0/licensed tracks; one bad track = takedown. Keep a `LICENSES.md`.
- **API keys:** stock media + premium voice need buyer keys — make the tool fully functional *without* them (Kokoro + typography), keys unlock extras. Zero-config first run is the demo.
- **Render time:** budget it; default 30fps, parallel concurrency, Lambda escape hatch. A tool that takes 8 min/reel on a laptop feels broken.
- **Scope creep:** Tiers 1–2 are the standout. Ship v1 (Phases 0–11) → add Tier 1 (12–15) before charging premium → Tier 2 → Tier 3. Don't build Tier 3 before launch.

## Re-prioritized launch sequence
1. **MVP to sell ($19):** Phases 0–11 + **Phase 13 (karaoke captions)** + **Phase 14 (music+beat-sync)**. Captions + music are non-negotiable for "good reels" — pull them forward into v1.
2. **v1.1 (justify $19, drive word-of-mouth):** Phase 12 (hook engine), Phase 15 (media), Phase 16 (repurpose/batch).
3. **v1.2:** Phase 17 (brand++), Phase 18 (multi-platform/localization).
4. **v2:** Tier 3.

---

## Open product decisions (resolve before Phase 10)
- Final product name + Gumroad handle (working: ReelForge).
- Premium-voice strategy: ship Kokoro-only free, or bundle an ElevenLabs option behind buyer's own key.
- License model: single-seat vs unlimited-personal.
```
