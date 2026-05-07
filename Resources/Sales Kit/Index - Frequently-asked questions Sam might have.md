---
type: sales-section
parent: Index
tags:
  - #sales-kit
  - #sales/index
---

# Frequently-asked questions Sam might have

## Context
From [[Index]].

## Content

**"Where do I keep client photos / files?"**
For now, Google Drive folder per client. Future: a `clients/{license}/` folder in the repo.

**"How do I track which subject line is winning?"**
Run `python send_outreach.py stats` — shows reply rate by send. (Subject A/B variation is wired in src/email_send/sender.py per license_num hash.)

**"How do I rotate to a different mockup variant?"**
Re-render with: `rm out/mockups/{license}.html out/screenshots/{license}.png && python send_outreach.py mockup --limit 1`

**"How do I handle a contractor who's pushy on price?"**
Read [OBJECTIONS_LIVE.md](OBJECTIONS_LIVE.md) row "Can you do it cheaper?" → offer $50 off in exchange for testimonial after launch.

**"What if I'm losing my voice on a call?"**
Read [PHONE_SCRIPTS.md](PHONE_SCRIPTS.md) "When they get aggressive" — stay calm, validate their concern, offer to remove them from list.

## Links
- Parent: [[Index]]
- MOC: [[Sales Kit]]
