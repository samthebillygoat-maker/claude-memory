---
type: sales-section
parent: Stripe Setup
tags:
  - #sales-kit
  - #sales/stripe-setup
---

# Setup checklist (~20 min)

## Context
From [[Stripe Setup]].

## Content

1. **Create Stripe account** at https://dashboard.stripe.com/register
   - Pick **Individual / Sole Proprietor**
   - Enter legal name (Samuel Lieberman), SSN (just last 4 first; full if flagged), DOB, home address
   - No EIN needed

2. **Link a checking account** — personal is fine for now. Stripe accepts it for sole props. Open a Mercury or Relay business checking *before* tax season for clean separation.

3. **Settings → Public details**:
   - Business name: `Sam Lieberman Web Design`
   - Support email: `samthebillygoat@gmail.com`
   - Logo: upload one (just text on a colored block is fine)
   - Brand color: `#d97706` (orange) or `#0f172a` (slate) to match the mockups

4. **Settings → Customer emails**: enable successful-payment + refund receipts.

5. **Settings → Statement descriptor**: set to `SAMLIEBERMAN` so it shows on the contractor's card statement, not "STRIPE\*".

6. **Settings → Payouts**: set to **daily automatic**.

7. **Create products + prices**:
   - Tier 1 — $300 one-time → generate Payment Link → copy URL
   - Tier 2 — $750 one-time → Payment Link
   - Tier 3 — $1,500 one-time → Payment Link
   - Retainer — $40/mo recurring → Payment Link

8. **Save the 4 Payment Link URLs** somewhere fast to copy from. Suggested: paste them at the top of `sales/REPLY_PLAYBOOK.md` once they exist.

## Links
- Parent: [[Stripe Setup]]
- MOC: [[Sales Kit]]
