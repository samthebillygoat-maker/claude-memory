# thefridaypack.com — Pre-Zoom Audit
Generated 2026-05-14, ~20 minutes before STR-coach affiliate call.
Live site reachable over HTTPS, redirects apex → www cleanly. No Stripe test-mode badges found on live pages.

---

## 🔴 MUST FIX BEFORE THE CALL (do not screenshare any of these)

1. **Home page "Top 5 ranked leads (preview)" uses fake 555 phone numbers.** Rows 01–05 on the landing page show `(813) 555-0148`, `(727) 555-0193`, `(813) 555-0271`, `(813) 555-0322`, `(813) 555-0419` with made-up owner names ("R. Mendoza", "J. & K. Patel"). The 555 prefix is the universally recognized fake-phone convention. An STR coach will clock this instantly — it reads as fabricated leads on the hero of the site. The /samples/tampa page shows real numbers (e.g. 813-685-7755), so the preview-on-home is the only offender. **Scroll past or zoom out when the hero is up. Do NOT linger on the "Top 5" block.**

2. **/sample-report is live (200) but the "Download PDF" button is a dead `#` link.** If the coach clicks it during share, nothing happens — looks broken. The page itself contains only the headline and the dead button. **Avoid this URL entirely.** (Source file `src/app/sample-report/page.tsx` has a `// TODO: Serve an anonymized sample PDF` comment — never implemented.)

3. **Pricing mismatch with your prep doc.** Prep doc says $97 / $147 / $397. Live site shows **$29 Trial / $97 Starter / $197 Weekly / $347 Pro**. Not embarrassing on its own, but if the coach pulls up your pitch doc you'll contradict yourself. Decide which set of numbers you're quoting before the call and stick to it.

---

## 🟡 TABS TO AVOID (live but stub/broken — fine to fix post-call)

- `/dashboard` — redirects then loads a TODO stub page (`// TODO: Dashboard home`). Coach will see nothing useful.
- `/sign-in` and `/sign-up` — 200 OK, but both are TODO stubs waiting for Clerk integration (`// TODO: Replace with <SignIn /> once Clerk keys are configured`). If coach tries to sign up live, dead end.
- `/markets/austin` — 404, even though Austin is listed in the Red tier on /markets. Same risk for any other /markets/[slug] click — many show a "Coming soon" eyebrow per `src/app/markets/[slug]/page.tsx:97`.
- `/pricing`, `/about`, `/faq`, `/affiliate`, `/sample`, `/checkout`, `/buy` — all return **404**. Pricing and FAQ are on-page anchors (`#pricing`, `#faq`), not separate routes — don't type those URLs into the address bar mid-share.
- `src/lib/stripe.ts` falls back to `sk_test_placeholder` if `STRIPE_SECRET_KEY` env is missing — verify Vercel env is set to live key before live demoing the checkout button. (Webhook gotcha from your memory: piped echo into env leaves trailing newline — use `printf`.)

---

## 🟢 OK TO SHOWCASE

- `https://thefridaypack.com/` — **scroll past the "Top 5 ranked leads (preview)" block fast**; hero copy, How It Works, Why This Works, Roadmap, Vote, FAQ sections are all clean.
- `https://thefridaypack.com/free-sample` — clean lead-gen page, single clear CTA.
- `https://thefridaypack.com/samples/tampa` — strongest screenshare asset. Real phone numbers on leads 1–5, leads 6–50 properly redacted with `(•••) •••-••••`. "Week of 04 May 2026" is 10 days old, still fine.
- `https://thefridaypack.com/markets` — 53 markets with Green/Yellow/Red tier system, looks polished. Just don't click into individual market pages.

---

**Live site state: VERIFIED.** Apex → www redirect, HTTPS clean, no Stripe test URLs on rendered pages, no `{{tokens}}` or "lorem ipsum" anywhere on the home or sample pages.
