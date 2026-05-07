---
type: sales-doc
source_file: sales\HANDOFF_DOC_TEMPLATE.md
tags:
  - #sales-kit
  - #sales/handoff-doc-template
---

# Handoff Doc Template

# Your Website Handoff — {{CLIENT_BUSINESS}}

Sam ships this with every launch. 1-page reference for the contractor on what they own, how to log in, how to make basic changes.

---

## You own this site

Your domain: **{{CLIENT_DOMAIN}}**
Your hosting account: Cloudflare Pages, project **{{CLOUDFLARE_PROJECT_NAME}}**
Your code repository: GitHub, repo **{{REPO_NAME}}** (you're the owner)

I'm a "collaborator" on these accounts so I can help when needed — you can remove me anytime by going to Cloudflare Pages → Settings → Members and removing samthebillygoat@gmail.com.

## To log in (3 places)

**Cloudflare** (where the site lives):
- URL: https://dash.cloudflare.com
- Email: {{CLIENT_EMAIL}}
- Reset password: click "Forgot Password" — they email you

**Domain registrar** (where {{CLIENT_DOMAIN}} is registered):
- Provider: {{REGISTRAR}}
- Login: {{REGISTRAR_LOGIN_URL}}

**GitHub** (where the code lives — only if you want to edit code yourself):
- URL: https://github.com
- Email: {{CLIENT_EMAIL}}

## To make a change without me

### Change a phone number / email / business hours

1. Log into Cloudflare → Pages → **{{CLOUDFLARE_PROJECT_NAME}}** → "Source" tab
2. Click `index.html` → "Edit"
3. Use Ctrl+F to find the old phone/email/hours
4. Change it, click "Commit changes"
5. Cloudflare auto-deploys in ~30 seconds

### Swap a photo

1. Log into Cloudflare → Pages → **{{CLOUDFLARE_PROJECT_NAME}}** → "Source" tab
2. Click `assets/` → drag your new photo in (rename it to match the old one, e.g. `hero.png`)
3. Cloudflare auto-deploys

### Add a new service or page

This is bigger — text me at {{SAM_PHONE}} or email {{SAM_EMAIL}} and I'll do it.

If you'd rather DIY, I wrote the code to be readable. Open the GitHub repo, look in `index.html`, find the section with the existing services, copy-paste-modify.

## What's in your warranty

For 90 days from launch:
- I fix any bug you report (broken link, image not loading, form not submitting, etc.) at no charge.
- If your hosting goes down because of something on my end, I fix it.

Beyond 90 days, if you want help making changes:
- $40/mo retainer = unlimited small changes (under 1 hour each)
- Or $75 per change request

## Your contact form

When someone fills out the contact form, the email goes to: **{{FORM_RECIPIENT_EMAIL}}**

To change that:
1. Log into Cloudflare → Pages → **{{CLOUDFLARE_PROJECT_NAME}}** → "Settings" → "Functions"
2. Find the env var `FORM_RECIPIENT` and change it
3. Redeploy

## Your reviews

If you went with Tier 2 or Tier 3, your live Google/Yelp reviews are pulled onto the site every 24 hours. Nothing to do — they update automatically.

## What I will NEVER do

- Charge you a monthly fee for the site itself (one-time at launch)
- Lock you in (you can move to a different host in an afternoon)
- Hold your domain hostage (it's registered to YOU, not me)
- Sell your customer info or website data

## How to reach me

- Email: samthebillygoat@gmail.com (best for non-urgent)
- Phone/text: {{SAM_PHONE}} (urgent)
- I usually reply within 1 business day

## What to do if I disappear

Hopefully I don't. But if you can't reach me for >1 week and something is broken:
1. Code is on YOUR GitHub
2. Hosting is on YOUR Cloudflare
3. Domain is on YOUR registrar

Hire any web developer on Upwork ($25-50/hr). Show them the GitHub repo. They can pick it up in an afternoon — I write it readable, no proprietary frameworks.

---

**Saved this? Print it / bookmark it. You shouldn't need it often.**

— Sam Lieberman, {{LAUNCH_DATE}}


## Links
- MOC: [[Cold Outreach]]
- MOC: [[Sales Kit]]
