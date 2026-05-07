---
type: sales-doc
source_file: sales\STRIPE_SETUP.md
tags:
  - #sales-kit
  - #sales/stripe-setup
---

# Stripe Setup

# Stripe Setup — Sole Proprietor Edition

Use **Stripe Payment Links** as the primary tool. They're hosted, no-code, shareable URLs you drop into a Gmail reply or Calendly confirmation in 30 seconds — perfect for our fixed-price tiers.

Use **Stripe Invoices** only when a contractor explicitly asks for an invoice doc.
Use a second **Payment Link** for the $40/mo retainer (recurring).
Skip Checkout / Connect / API stuff — Payment Links cover everything we need for v1.

## Setup checklist (~20 min)

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

## Realistic take-home (US cards, 2.9% + $0.30)

| Tier | Gross | Stripe fee | **Net** |
|---|---|---|---|
| $300 | $300.00 | $9.00 | **$291.00** |
| $750 | $750.00 | $22.05 | **$727.95** |
| $1,500 | $1,500.00 | $43.80 | **$1,456.20** |
| $40/mo | $40.00 | $1.46 | **$38.54** |

## Payouts timing

- First payout: held 7-14 days (Stripe new-account standard)
- After that: T+2 rolling, daily

## Refunds — the gotcha

When you refund Tier 1's $300, **you eat the $9 fee**. Stripe keeps the processing fee on refunds.

Two options:
- Build a 3% buffer into Tier 1 pricing (charge $309)
- Or shorten the refund window from 7 days to 5 days to reduce chargeback risk

I'd vote: keep the refund window at 7 days for trust + just absorb the $9. It's a nothing cost if it converts the deal.

## 1099-K reporting

Stripe issues a 1099-K if you exceed:
- 2026: $2,500
- 2027+: $600

So once you hit ~9 Tier 1 sales (or 4 Tier 2's, or 2 Tier 3's), Stripe reports to the IRS. Track expenses (this code, this laptop, internet bill, Twilio, etc.) so you can deduct against it.

## Alternatives considered

- **PayPal Business** — 2.9% + 49¢, worse UX, weaker brand control. Skip.
- **Square** — 2.6% + 10¢ for invoices, no payment links. Skip.
- **Wave** — free invoicing, 2.9% + 60¢ to actually process. Lower fee on small charges sometimes — but UX is dated. Skip.

Stripe wins for our use case.

## After your first dollar

- Open Mercury or Relay business checking. Free, takes 5 min, separates client money from your personal.
- Set up automatic Stripe → Mercury payouts.
- Track every business expense in a Google Sheet or Notion table.
- File quarterly estimated taxes (1040-ES) starting the quarter you cross ~$1,500 net.

## Reference

- Payment Links: https://docs.stripe.com/payment-links
- Refund mechanics: https://docs.stripe.com/refunds
- Statement descriptors: https://docs.stripe.com/statement-descriptors
- Payouts: https://docs.stripe.com/payouts
- 1099-K: https://docs.stripe.com/connect/1099-K


## Links
- MOC: [[Cold Outreach]]
- MOC: [[Sales Kit]]
