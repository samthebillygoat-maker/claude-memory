# Friday Pack Tracker — v2 Dark Editorial Patch

Target file: `C:\Users\samth\projects\landlord-outreach\scripts\build_friday_pack_delivery.py`

**Status correction (2026-05-15).** A previous version of this patch shipped a *light cream/navy* CSS — that was a wrong guess at the brand. After pulling computed styles off `thefridaypack.com/samples/tampa` via Playwright, the actual brand is **dark editorial**: `#0A0A0A` bg, ivory text, Fraunces serif headings, JetBrains Mono numerals, squared CTAs, deep green `#1C3F2E` + amber `#E8A33D` accents, hairline rules instead of card shadows.

This patch replaces the light v2 already in your build script with the corrected dark v2 **and** inlines a small runtime polish script so every regenerated tracker ships with:
- "Sample listing" links rebranded as squared `Link` buttons
- Raw Craigslist URLs in `.addr-block` swapped for `Link` buttons (preserves real addresses via `dataset.csvAddrs` so CSV export keeps the URLs)
- Source link surfaced on every card (not hidden behind the collapsed opener)
- `📅 Follow up` filter button injected next to the existing filter row
- `aria-label` on the reset button, `aria-pressed` on filter toggles, `role="heading" aria-level="2"` on each owner
- `exportCSV` patched to use `dataset.csvAddrs` + UTF-8 BOM (Excel-safe)

Reference rendered output (use to verify): `C:\Users\samth\Desktop\friday_pack_tracker_v2_PREVIEW.html` (66-lead Miami pack).

---

## 1. Swap font link

In `build_html()` page template, replace:

```python
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
```

with:

```python
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
```

## 2. Replace the entire `<style>...</style>` block

In `build_html()`, the page template's `<style>` block currently holds light cream/navy CSS. Replace the **entire block** (from `<style>` through `</style>` — everything between those two tags) with the dark editorial CSS below.

Every CSS `{` and `}` is doubled because the template is an f-string. Copy as-is.

```python
<style>
:root{{
  --bg:#0A0A0A;
  --surface:#121212;
  --surface-2:#161616;
  --surface-3:#1C1C1A;
  --ivory:#FAF9F6;
  --muted:#B0B0AA;
  --dim:#9A9A95;
  --rule:rgba(250,249,246,.08);
  --rule-strong:rgba(250,249,246,.16);
  --green:#1C3F2E;
  --green-2:#26553E;
  --green-soft:rgba(28,63,46,.30);
  --amber:#E8A33D;
  --amber-ink:#0A0A0A;
  --amber-soft:rgba(232,163,61,.14);
  --red-soft:rgba(220,80,80,.12);
  --red:#E59090;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-text-size-adjust:100%}}
:focus-visible{{outline:2px solid var(--amber);outline-offset:2px;border-radius:0}}
button:focus-visible,a:focus-visible,summary:focus-visible,textarea:focus-visible{{outline:2px solid var(--amber);outline-offset:2px}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--ivory);line-height:1.5;padding:0 24px 80px;-webkit-font-smoothing:antialiased;font-size:14px;font-weight:400}}
.wrap{{max-width:1040px;margin:0 auto;padding-top:32px}}
.banner{{border:none;background:none;padding:8px 0 24px;margin-bottom:8px;border-bottom:1px solid var(--rule);position:relative}}
.wordmark{{font-family:'Inter',sans-serif;font-size:11px;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}}
.banner h1{{font-family:'Fraunces',Georgia,serif;font-size:68px;font-weight:300;color:var(--ivory);letter-spacing:-.025em;line-height:1.02;font-feature-settings:"ss01"}}
.banner .meta{{color:var(--muted);font-size:14px;margin-top:14px;max-width:62ch;line-height:1.55}}
.counter{{display:inline-block;font-family:'JetBrains Mono',ui-monospace,monospace;font-size:11px;color:var(--muted);background:transparent;border:1px solid var(--rule-strong);padding:8px 14px;margin-top:18px;letter-spacing:.06em;text-transform:uppercase}}
.counter b{{color:var(--ivory);font-weight:500;margin:0 4px;font-size:13px}}
.intro{{border:none;background:none;box-shadow:none;padding:24px 0 28px;margin-bottom:0;border-bottom:1px solid var(--rule);font-size:14px;color:var(--muted);line-height:1.65;max-width:68ch}}
.intro b{{color:var(--ivory);font-weight:500}}
.controls{{display:flex;gap:6px;margin:28px 0 8px;flex-wrap:wrap;align-items:center}}
.controls button{{background:transparent;border:1px solid var(--rule-strong);color:var(--muted);padding:10px 18px;border-radius:0;cursor:pointer;font-size:13px;font-weight:500;font-family:inherit;letter-spacing:.01em;transition:all .15s ease}}
.controls button:hover{{border-color:var(--ivory);color:var(--ivory)}}
.controls button.active{{background:var(--ivory);border-color:var(--ivory);color:var(--bg);font-weight:600}}
.controls button.export{{background:var(--green);border-color:var(--green);color:var(--ivory);font-weight:500}}
.controls button.export:hover{{background:var(--green-2);border-color:var(--green-2)}}
.controls::after{{content:"Tap a phone number to call. Status saves to this browser.";flex-basis:100%;order:99;font-size:12px;color:var(--dim);padding:10px 0 18px;letter-spacing:.01em}}
.grid{{display:flex;flex-direction:column;gap:0;border-top:1px solid var(--rule)}}
.card{{background:transparent;border:none;border-bottom:1px solid var(--rule);border-radius:0;padding:28px 0;display:grid;grid-template-columns:60px 1fr 280px;grid-template-areas:"rank head head" "rank owner phone" "rank tags phone" "rank addr phone" "rank why why" "rank script script" "rank actions actions" "rank notes notes";gap:10px 24px;align-items:start;box-shadow:none;position:relative;transition:opacity .15s ease}}
.card::before{{display:none}}
.card.done{{opacity:.4}}
.card.hidden{{display:none}}
.card-head{{grid-area:head;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--rule);padding-bottom:10px;margin-bottom:4px}}
.card-title{{display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}}
.rank-badge{{grid-area:rank;display:block;align-self:start;background:transparent;color:rgba(250,249,246,.55);padding:0;font-family:'Fraunces',Georgia,serif;font-size:60px;font-weight:300;letter-spacing:-.025em;line-height:.95;font-variant-numeric:tabular-nums}}
.card.done .rank-badge{{color:var(--dim)}}
.score-tag{{background:transparent;color:var(--muted);padding:0;font-family:'JetBrains Mono',ui-monospace,monospace;font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase}}
.score-tag::before{{content:"• ";color:var(--dim)}}
.entity-tag{{background:transparent;color:var(--amber);border:1px solid rgba(232,163,61,.4);padding:2px 8px;border-radius:0;font-family:'Inter',sans-serif;font-size:10px;font-weight:600;letter-spacing:.12em;text-transform:uppercase}}
.props{{color:var(--dim);font-size:12px;font-weight:400;font-family:'JetBrains Mono',ui-monospace,monospace;letter-spacing:.02em}}
.status{{font-family:'Inter',sans-serif;font-size:11px;color:var(--dim);font-weight:600;letter-spacing:.12em;text-transform:uppercase;white-space:nowrap}}
.card.done .status{{color:var(--amber)}}
.owner{{grid-area:owner;font-family:'Fraunces',Georgia,serif;color:var(--ivory);font-weight:400;font-size:26px;letter-spacing:-.015em;line-height:1.15}}
.tags{{grid-area:tags;display:flex;flex-wrap:wrap;gap:6px}}
.tags span{{background:transparent !important;color:var(--muted) !important;padding:2px 8px !important;border-radius:0 !important;font-family:'Inter',sans-serif !important;font-size:10px !important;font-weight:600 !important;letter-spacing:.12em !important;text-transform:uppercase !important;border:1px solid var(--rule-strong) !important}}
.addr-block{{grid-area:addr;color:var(--muted);font-size:13px;line-height:1.6;background:transparent;padding:0;border:none;word-break:break-word;font-family:'Inter',sans-serif}}
.addr-block span{{color:var(--dim) !important;font-size:11px !important;font-style:italic}}
.addr-block .addr-line{{padding:2px 0}}
.addr-block.links-only{{display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
.addr-block .link-btn{{margin:0}}
.addr-block .addr-more{{flex-basis:100%;color:var(--dim);font-size:11px;margin-top:4px}}
.addr-block.has-source-link{{display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center}}
.addr-block.has-source-link .addr-line{{flex:1 1 200px;padding:0;min-width:0}}
.addr-block .addr-link-btn{{flex:0 0 auto}}
@media (min-width:480px){{.addr-block .addr-link-btn{{margin-left:auto}}}}
.big-phone{{grid-area:phone;display:flex;align-items:center;justify-content:center;gap:8px;background:var(--green);color:var(--ivory) !important;text-decoration:none;padding:14px 22px;border-radius:0;font-size:16px;font-weight:500;font-family:'JetBrains Mono',ui-monospace,monospace;letter-spacing:.01em;border:none;align-self:start;transition:background .15s ease;min-height:44px}}
.big-phone:hover{{background:var(--green-2)}}
.big-phone:active{{background:#163326}}
.no-phone{{grid-area:phone;background:transparent;color:var(--muted);border:1px dashed var(--rule-strong);padding:22px 20px;border-radius:0;font-size:13px;font-family:'Inter',sans-serif;text-align:center}}
.why{{grid-area:why;color:var(--ivory);font-size:14px;line-height:1.6;background:transparent;padding:0;border:none;margin-top:2px}}
.why b{{color:var(--amber);font-weight:600;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;display:block;margin-bottom:4px;font-family:'Inter',sans-serif}}
.script{{grid-area:script;background:var(--surface);border:1px solid var(--rule);border-radius:0;margin-top:6px}}
.script summary{{padding:14px 16px;cursor:pointer;font-family:'Inter',sans-serif;font-size:11px;color:var(--muted);font-weight:600;list-style:none;display:flex;align-items:center;gap:10px;user-select:none;letter-spacing:.14em;text-transform:uppercase}}
.script summary::-webkit-details-marker{{display:none}}
.script summary::before{{content:"+";display:inline-block;color:var(--amber);font-size:14px;line-height:1;font-weight:400;width:12px;text-align:center}}
.script[open] summary::before{{content:"−"}}
.script summary:hover{{color:var(--ivory)}}
.script-body{{padding:0 16px 16px;display:flex;flex-direction:column;gap:12px;font-size:13.5px;color:var(--muted);line-height:1.65}}
.script-block{{background:transparent;padding:12px 0 0;border:none;border-top:1px solid var(--rule);border-radius:0;line-height:1.65}}
.script-block:first-child{{border-top:none;padding-top:4px}}
.script-block b{{color:var(--amber);display:block;margin-bottom:6px;font-family:'Inter',sans-serif;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}}
.script-block a{{color:var(--amber) !important;text-decoration:none;font-weight:500}}
.script-block a:hover{{text-decoration:underline}}
.link-btn{{display:inline-block;background:transparent;color:var(--amber) !important;border:1px solid rgba(232,163,61,.4);padding:6px 14px;border-radius:0;font-family:'Inter',sans-serif !important;font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;text-decoration:none !important}}
.link-btn:hover{{background:var(--amber-soft);color:var(--ivory) !important;border-color:var(--amber)}}
.actions{{grid-area:actions;display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}}
.actions button{{flex:1;min-width:120px;background:transparent;border:1px solid var(--rule-strong);color:var(--muted);padding:11px 14px;border-radius:0;cursor:pointer;font-size:12px;font-weight:500;font-family:inherit;letter-spacing:.02em;transition:all .12s ease}}
.actions button:hover{{border-color:var(--ivory);color:var(--ivory)}}
.actions button.green,.actions button.blue,.actions button.red,.actions button.vm,.actions button.followup{{background:transparent;color:var(--muted);border-color:var(--rule-strong)}}
.actions button.green:hover,.actions button.blue:hover,.actions button.red:hover,.actions button.vm:hover,.actions button.followup:hover{{background:transparent;color:var(--ivory);border-color:var(--ivory)}}
.actions button.reset{{flex:0 0 auto;min-width:42px;padding:11px 14px;color:var(--dim)}}
.user-notes{{grid-area:notes;background:var(--surface);border:1px solid var(--rule);color:var(--ivory);padding:12px 14px;border-radius:0;font-size:13px;line-height:1.6;font-family:inherit;resize:vertical;min-height:44px;width:100%;margin-top:6px}}
.user-notes::placeholder{{color:var(--dim)}}
.user-notes:focus{{outline:none;border-color:var(--amber);box-shadow:none}}
.legend{{font-family:'Inter',sans-serif;font-size:11px;color:var(--dim);margin-top:48px;padding-top:24px;border-top:1px solid var(--rule);text-align:center;letter-spacing:.12em;text-transform:uppercase;font-weight:500}}
@media (max-width:820px){{
  body{{padding:0 18px 60px}}
  .wrap{{padding-top:20px}}
  .banner h1{{font-size:38px;letter-spacing:-.02em}}
  .card{{grid-template-columns:42px 1fr;grid-template-areas:"rank head" "rank owner" "rank tags" "rank addr" "phone phone" "why why" "script script" "actions actions" "notes notes";gap:8px 16px;padding:24px 0}}
  .rank-badge{{font-size:28px}}
  .big-phone{{font-size:20px;padding:18px 16px;margin-top:6px}}
  .owner{{font-size:22px}}
  .actions button{{min-width:0;flex:1 1 calc(33.33% - 4px);padding:12px 8px;min-height:44px}}
  .actions button.reset{{flex:1 1 100%}}
}}
@media (max-width:480px){{
  .banner h1{{font-size:30px}}
  .card{{grid-template-columns:32px 1fr}}
  .rank-badge{{font-size:22px}}
}}
@media print{{
  body{{background:#fff;color:#000;padding:0}}
  .controls,.actions,.user-notes,.counter{{display:none !important}}
  .banner,.intro,.card{{border-color:#bbb !important}}
  .card{{page-break-inside:avoid;break-inside:avoid;padding:18px 0;display:block}}
  .card > *{{display:block;margin-bottom:8px}}
  .rank-badge{{color:#000;font-size:28px}}
  .owner,.banner h1{{color:#000}}
  .big-phone{{background:#fff !important;color:#000 !important;border:2px solid #000;font-size:20px;padding:14px}}
  .why{{background:#faf3e0;color:#000;border-left-color:#000}}
  .why b{{color:#000}}
  .script-body{{display:flex !important}}
  .script,.script-block{{background:#fff;border-color:#bbb}}
  .script summary::before{{display:none}}
  .script-block b{{color:#000}}
  a{{color:#000 !important;text-decoration:none}}
  .legend{{color:#000}}
}}
</style>
```

---

## 3. Split the H1 to just the place name

Find this line in the page template (likely near line 364 in the patched script):

```python
<h1>{html.escape(market)} · {html.escape(week)}</h1>
<div class="meta">{n} landlords · {with_phone} with direct phone · sorted by score (highest first)</div>
```

Replace with:

```python
<h1>{html.escape(market)}</h1>
<div class="meta">{html.escape(week)} · {n} landlords · {with_phone} with direct phone</div>
```

The H1 now reads as the editorial place-name (matches `thefridaypack.com/samples/tampa`'s "Tampa, FL"). The week and counts demote to the meta line right below.

---

## 4. Inject the runtime polish JS into the page template

In the page template's `<script>` block, find the final `updateCounter();` line (the existing build script has it as the last statement before `</script>`). Insert the polish block **immediately after** `updateCounter();` and **before** `</script>`.

Every `{` and `}` is doubled because the template is an f-string. Backticks and `${{...}}` inside template literals stay as-is.

```python
updateCounter();

(function v2Polish(){{
  // 1. Rebrand "Sample listing" anchors inside the opener panel as Link buttons.
  document.querySelectorAll('.script-block a[href^="http"]').forEach(a => {{
    a.textContent = 'Link';
    a.classList.add('link-btn');
    a.removeAttribute('style');
  }});

  // 2. Replace bare URLs in .addr-block with Link buttons. Stash the ORIGINAL
  //    textContent on dataset.csvAddrs so CSV export keeps the URLs/addresses.
  document.querySelectorAll('.addr-block').forEach(blk => {{
    blk.dataset.csvAddrs = (blk.textContent || '').replace(/\\s+/g,' ').trim();
    const html = blk.innerHTML;
    const parts = html.split(/<br\\s*\\/?>/i);
    const pieces = [];
    parts.forEach(p => {{
      const trimmed = p.trim();
      if (!trimmed) return;
      let span = '';
      let head = trimmed;
      const m = trimmed.match(/<span\\b[\\s\\S]*?<\\/span>\\s*$/i);
      if (m) {{ span = m[0]; head = trimmed.slice(0, m.index).trim(); }}
      if (head) {{
        const tmp = document.createElement('div'); tmp.innerHTML = head;
        const text = (tmp.textContent || '').trim();
        if (/^https?:\\/\\//.test(text)) {{
          pieces.push(`<a href="${{text}}" target="_blank" rel="noopener" class="link-btn">Link</a>`);
        }} else {{
          pieces.push(`<div class="addr-line">${{head}}</div>`);
        }}
      }}
      if (span) pieces.push(`<div class="addr-more">${{span}}</div>`);
    }});
    blk.innerHTML = pieces.join('');
    if (blk.querySelectorAll('.link-btn').length && !blk.querySelector('.addr-line')) {{
      blk.classList.add('links-only');
    }}
  }});

  // 3. Surface a source-listing Link on every card (don't bury behind opener).
  document.querySelectorAll('.card').forEach(card => {{
    const blk = card.querySelector('.addr-block');
    if (!blk || blk.querySelector('.link-btn')) return;
    const src = card.querySelector('.script-block a.link-btn');
    if (!src) return;
    const clone = src.cloneNode(true);
    clone.classList.add('addr-link-btn');
    blk.appendChild(clone);
    blk.classList.add('has-source-link');
  }});

  // 4. Label reset buttons for screen readers. Inject "Follow up" button if the
  //    build script didn't already emit one (defensive — see step 5 below).
  document.querySelectorAll('.actions').forEach(act => {{
    const card = act.closest('.card');
    if (!card) return;
    const id = card.dataset.id;
    const reset = act.querySelector('.reset');
    if (reset && !reset.getAttribute('aria-label')) {{
      reset.setAttribute('aria-label', 'Reset this lead');
      reset.setAttribute('title', 'Reset this lead');
    }}
    if (act.querySelector('.followup')) return;
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'followup';
    btn.textContent = '📅 Follow up';
    btn.onclick = () => setStatus(id, '📅 Follow up');
    if (reset) act.insertBefore(btn, reset);
    else act.appendChild(btn);
  }});

  // 5. Add Follow-up filter button and ARIA roles to the filter row.
  const controls = document.querySelector('.controls');
  if (controls && !controls.querySelector('button[data-filter="followup"]')) {{
    const fu = document.createElement('button');
    fu.type = 'button';
    fu.setAttribute('data-filter','followup');
    fu.textContent = '📅 Follow up';
    fu.onclick = function(){{ setFilter(this, 'followup'); }};
    const exp = controls.querySelector('button.export');
    if (exp) controls.insertBefore(fu, exp); else controls.appendChild(fu);
  }}
  controls?.setAttribute('role','group');
  controls?.setAttribute('aria-label','Filter leads');
  function syncPressed(){{
    document.querySelectorAll('.controls button[data-filter]').forEach(b => {{
      b.setAttribute('aria-pressed', b.classList.contains('active') ? 'true' : 'false');
    }});
  }}
  syncPressed();

  // 6. Expose owner names as headings so SR users can jump card-to-card.
  document.querySelectorAll('.card .owner').forEach(el => {{
    el.setAttribute('role','heading');
    el.setAttribute('aria-level','2');
  }});

  // 7. Extend setFilter (wrap, don't replace — preserves the contract).
  const _origSetFilter = window.setFilter;
  window.setFilter = function(btn, f){{
    if (f === 'followup') {{
      document.querySelectorAll('.controls button[data-filter]').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.card').forEach(c => {{
        const id = c.dataset.id;
        const status = (state[id] && state[id].status) || '';
        c.classList.toggle('hidden', !/Follow up/i.test(status));
      }});
      syncPressed();
      return;
    }}
    _origSetFilter(btn, f);
    syncPressed();
  }};

  // 8. Patch exportCSV: read addresses from dataset.csvAddrs (preserves originals)
  //    and prepend UTF-8 BOM so Excel on Windows opens the file correctly.
  window.exportCSV = function(){{
    let csv = '\\ufeffrank,score,owner,phone,n_properties,addresses,status,notes\\n';
    document.querySelectorAll('.card').forEach(c => {{
      const id = c.dataset.id;
      const rank = c.dataset.rank;
      const scoreEl = c.querySelector('.score-tag');
      const score = scoreEl ? scoreEl.textContent.replace('Score ','').replace(/^•\\s*/, '').trim() : '';
      const owner = (c.querySelector('.owner')?.textContent || '').replace(/"/g,'""');
      const phoneEl = c.querySelector('.big-phone');
      const phone = phoneEl ? phoneEl.textContent.replace('📞 ','').trim() : '';
      const props = c.querySelector('.props')?.textContent || '';
      const addrBlk = c.querySelector('.addr-block');
      const addrs = ((addrBlk && addrBlk.dataset.csvAddrs) || addrBlk?.textContent || '')
        .replace(/\\s+/g,' ').replace(/"/g,'""').trim();
      const status = (state[id]&&state[id].status) || 'Not called';
      const notes = ((state[id]&&state[id].notes) || '').replace(/"/g,'""');
      csv += `"${{rank}}","${{score}}","${{owner}}","${{phone}}","${{props}}","${{addrs}}","${{status}}","${{notes}}"\\n`;
    }});
    const blob = new Blob([csv], {{type:'text/csv;charset=utf-8'}});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'friday-pack-' + new Date().toISOString().slice(0,10) + '.csv';
    a.click();
  }};
}})();
</script>
```

> Note on f-string escaping. Inside the polish block, every `{` and `}` is doubled — including the ones inside template-literal `${{...}}` (so they render as `${...}`). The string `'\\ufeffrank,...'` uses double-backslash so Python emits `﻿` into the JS source (the BOM). Same for `\\s`, `\\n`, `\\/`. If you copy this and a regex looks weird, count the backslashes.

---

## 5. Verify

Re-run the build:

```powershell
cd C:\Users\samth\projects\landlord-outreach
uv run python scripts/build_friday_pack_delivery.py `
    --by-owner data/by_owner_miami_FINAL_PLUS_MANUAL_2026-05-15.csv `
    --raw      data/broader_miami_FINAL_2026-05-15.csv `
    --market   "Miami, FL" `
    --week     "Week of 15 May 2026" `
    --top      75 `
    --out-dir  data/friday_pack_FINAL_2026-05-15
```

Open the generated `friday_pack_tracker.html` and confirm:

1. Page is dark `#0A0A0A`, H1 "Miami, FL" in big serif.
2. Every card has a big serif rank number on the left, ivory owner name, dim mono metadata, deep-green phone block on the right.
3. Click a status pill → card dims; status pill highlights.
4. Click `📅 Follow up` filter → only follow-up cards visible.
5. Click `⬇ Export CSV` → CSV opens in Excel with proper unicode (no mojibake) and the `addresses` column still contains real URLs/addresses (not the word "Link").
6. Print preview (Ctrl+P) → controls/actions/notes hidden, cards readable with hairline borders.
7. Tab through with keyboard → 2px amber focus rings visible on every button/link/textarea/summary.

Reference render: `C:\Users\samth\Desktop\friday_pack_tracker_v2_PREVIEW.html`. The generated file should be visually identical (modulo lead data).

---

## 6. Rollback

All changes are contained inside the f-string template in `build_html()`. Revert that single function body and the previous styling returns. No state, no JS function names, no CSV columns, no `localStorage` key were touched.
