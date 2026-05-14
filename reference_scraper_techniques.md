---
name: Scraper Techniques & Anti-Bot Notes
description: JSON-LD phone trick on Zumper, anti-bot blocked sources, Apify rules, workarounds
type: reference
---

# Scraper Techniques & Anti-Bot Notes

Hard-won from 4 days of lead extraction across rental sites. Updated 2026-05-04.

## What works

- **Zumper JSON-LD phone trick.** The `telephone` field in page source yields the phone ~87% of the time even when the "Request Tour" UI hides it. Always parse JSON-LD before assuming a Zumper listing has no phone.

## What's blocked (returns 403 / bot wall to direct fetch)

- Furnished Finder
- Zillow FRBO
- Realtor.com
- Apartments.com search pages
- Reddit (blocks Claude entirely)

**Workaround:** manual browser session with logged-in cookies, or Playwright headless with a real user-agent and warmed session.

## Apify rules

- Headless-only.
- **No concurrent runs per actor** — track in a `scrape_log` table to avoid silent collision/throttling.

## Honesty rule

If web tools are blocked for a source, **say so**. Don't fabricate addresses or phone numbers — wastes Sam's hours and risks harassing real people. (See `feedback_no_fabricated_leads.md`.)
