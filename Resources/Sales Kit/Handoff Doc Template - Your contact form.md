---
type: sales-section
parent: Handoff Doc Template
tags:
  - #sales-kit
  - #sales/handoff-doc-template
---

# Your contact form

## Context
From [[Handoff Doc Template]].

## Content

When someone fills out the contact form, the email goes to: **{{FORM_RECIPIENT_EMAIL}}**

To change that:
1. Log into Cloudflare → Pages → **{{CLOUDFLARE_PROJECT_NAME}}** → "Settings" → "Functions"
2. Find the env var `FORM_RECIPIENT` and change it
3. Redeploy

## Links
- Parent: [[Handoff Doc Template]]
- MOC: [[Sales Kit]]
