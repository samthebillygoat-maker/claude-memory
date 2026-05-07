---
type: sales-doc
source_file: sales\REPLY_PLAYBOOK.md
tags:
  - #sales-kit
  - #sales/reply-playbook
---

# Reply Playbook

# Reply Playbook

When a contractor replies to a cold mockup, paste the matching template, personalize 1-2 lines, and send. Don't write each reply from scratch.

The `triage` subcommand classifies inbound automatically; the category names below match.

---

## INTERESTED — they liked it / asked price

**Anchor on ONE tier — three options causes decision paralysis. Pick based on signal in their reply.**

If they said "looks great" / "yes" with no budget signal → recommend **Tier 2**.
If they said "how cheap" / "what's the minimum" → lead with **Tier 1**.
If they said "I want leads" / "I want SEO" → lead with **Tier 3**.

> Subject: Re: {{their_subject}}
>
> Hey {{first_name}} — perfect.
>
> Based on your reply I think **Tier 2 ($750)** is the right fit: 5 pages, your real photos, mobile-optimized, basic SEO, live in 10 days. Two rounds of edits.
>
> Tighter budget? Tier 1 ($300, just the mockup live). Want lead-capture + live reviews? Tier 3 ($1,500).
>
> Stripe link for Tier 2 deposit ($375): [PASTE LINK]
> Agreement attached.
>
> Reply "in" and I start tonight. Site live by {{target_date}}.
>
> — Sam

Attach: `sales/SERVICE_AGREEMENT.md` as PDF.

**CRITICAL:** paste the actual Stripe Payment Link inline — don't promise "I'll send it later." Friction kills momentum. Pre-build all 3 links before any send goes out.

---

## INTERESTED — they want to talk first

> Subject: Re: A landing page mockup for {{biz}}
>
> Sounds good. Easiest way is a 15-min call.
>
> Pick a slot here: [calendly link]
>
> Or reply with 2-3 times that work for you and I'll just call you. My number is (your number).
>
> — Sam

---

## QUESTION — they asked something specific

Common questions + answers:

**"Can you change the colors?"**
> Yes — every color is pulled from one palette. I can match your truck wrap, logo, or whatever you want. Send me a photo of your branding and I'll match.

**"How is this different from GoDaddy / Wix / Squarespace?"**
> Those are templates anyone can buy for $20/mo. This is a custom build for your business specifically — no template fees, no upgrade pushes, you own the code, hosted free on Cloudflare. One-time fee.

**"Can my nephew/cousin maintain it after?"**
> Yes — code is plain HTML/CSS/JS, anyone with basic web skills can edit. I write it readable, not minified. I can also handle updates for $40/mo if you'd rather.

**"Do you do SEO?"**
> Tier 2 includes basic SEO (meta tags, schema, fast load). Tier 3 includes local SEO content. I don't do paid ads — that's a separate engagement and honestly Google Local Service Ads beat custom campaigns for trades.

**"Will I still own the domain?"**
> Yes, always. Domain is registered to you (or transferred to you if I purchase it for you).

**"Can you also do a logo?"**
> No — I'll use your existing logo or set up a clean text logo. Logo design is a separate skill I'd farm out and mark up. You're better off paying a logo designer directly ($100-300).

---

## NEGATIVE — "no thanks" / "not interested"

> Subject: Re: A landing page mockup for {{biz}}
>
> All good — I'll take you off the list and delete the mockup. Best of luck with everything.
>
> — Sam

(Then run `python send_outreach.py triage` to auto-suppress.)

---

## STOP — explicit opt-out

(No reply needed. Twilio + Gmail handle automatically. `triage` auto-suppresses.)

---

## DELAY — "maybe in a few months"

> Subject: Re: A landing page mockup for {{biz}}
>
> No pressure. Want me to follow up in 60 days? Reply yes and I'll set a reminder. Or just text me when you're ready: (your number).
>
> Mockup is saved on my end either way.
>
> — Sam

---

## CONFUSED / ANGRY — "who are you / how did you get my info"

> Subject: Re: A landing page mockup for {{biz}}
>
> Totally fair to ask — your business phone is published in the public CSLB license database (cslb.ca.gov). I'm a 19-year-old college student building sample sites for licensed CA contractors as part of teaching myself web design.
>
> Each contractor gets one message with a sample. If it's not useful, I delete the file and you never hear from me again.
>
> Want me to remove you from the list? Reply STOP and I will immediately.
>
> — Sam Lieberman, samthebillygoat@gmail.com

---

## REFERRAL — they pass you to someone else

> Subject: Re: A landing page mockup for {{biz}}
>
> Thanks {{first_name}} — really appreciate the connect. I'll reach out to {{referral_name}} this week and mention you.
>
> If you ever want to revisit your own site, I'll keep your mockup on file.
>
> — Sam

(Add the referral to `out/referrals.csv` manually.)

---

## NO REPLY in 5 days — soft follow-up

> Subject: Re: A landing page mockup for {{biz}}
>
> Hey {{first_name}} — just bumping this up. Saw it might've gotten buried.
>
> Quick question: useful or skip? I won't take up space if it's not.
>
> — Sam

---

## NO REPLY in 10 days — final

> Subject: Re: A landing page mockup for {{biz}}
>
> Last note — I'm going to delete the mockup file on my end this weekend so I'm not sitting on personal info I don't need.
>
> If you'd rather I keep it (or want to revisit), reply with anything. Otherwise no worries, all good.
>
> — Sam

---

## Pro tips

- Reply within 4 hours of receiving — speed = trust signal.
- One question per reply max. Don't pile on.
- If they say yes, send Stripe link in the SAME message. Friction kills momentum.
- Keep your tone "19yo who's helpful" — don't pivot to "professional agency voice." That's the magic.
- Phone is faster than email for closing. After 2 emails, suggest a 5-min call.


## Links
- MOC: [[Cold Outreach]]
- MOC: [[Sales Kit]]
