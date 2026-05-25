# Tara House West Apt 18 — STR Furnishing & Lease Notes
*2026-05-22*

## Property
- 2 units (Apt 18 and one other), same layout
- Each unit: 1 queen bedroom + 1 queen sofa bed in living room
- Lease signed, PDF generated, EIN 41-5346841 added

## Lease Key Details
- File: `C:\Users\samth\Downloads\TaraHouseWest_Apt18_FINAL_Lease_2026-05-21_v2.docx`
- Commencement: May 22, 2026 | Expiry: July 22, 2027
- Rent-free period: May 22 – July 3 (6 weeks)
- First rent payment: Aug 1
- Landlord obligations added (Section 18): bathroom sink repair, wall paint repainting, water heater maintenance
- Lease reviewer verdict: GREEN — STR ready

## Amazon Orders

### First Order (already placed manually)
Key items received/arriving:
- Zinus 12" Queen Mattress ×2
- JOLLYVOGUE Queen Pillows Set of 4 ×2
- ROARINGWILD Queen Quilt Sets ×6
- Utopia Pillow Protectors Queen ×12
- Bedsure Queen + King blankets ×2 each
- Keurig K-Mini ×2
- Swiffer WetJet ×2
- Luggage Rack (set of 2) ×2
- ZOBER Velvet Hangers 50pk ×1
- Iron + ironing board ×2
- Toiletries (gallon refills: shampoo, conditioner, body wash, lotion, hand soap) ×2
- Disposable razors, toothbrushes ×2
- Shot glasses, ice cube trays ×2
- Laundry hampers ×2
- Coffee consumables (creamer, sugar, stirrers, cups) ×2

### Cart Script (amazon_cart.py)
Script at: `C:\Users\samth\amazon_cart.py`
- Playwright async Python, headless=False
- Cart clearing disabled for current run
- Quantities already set for 2 units (no doubling)

**Items added to cart (current run):**
- Sofa Bed Encasement B00MRH58V0 ×2
- Queen Mattress Encasement B00MRH58V0 ×2
- Sofa Bed Flat Sheets B07NWPP1RD ×6
- Queen Bed Sheets (California Design Den 400TC cotton 4pc) — swap ASIN to full set
- Coffee Table Books B0CT3FWF87 ×2
- Spice Rack B00008WQ3L ×2
- Toaster (Amazon Basics 2-slice) B072P11H8L ×2
- Anker Cube Charger B09PGZHCXR ×8
- Surge Protectors B08QYJMJQ3 ×4
- Hairdryer (Revlon One-Step recommended) ×2
- Shark Cordless Vacuum B07S652B12 ×2
- Stone Bath Mat ×2
- Gallon Pump Caps ×2
- Coffee Station Organizer ×2
- Infuser Kettle ×2
- Mugs 4-pack ×2
- Plus kitchen items: knife block, cutting board, flatware, steak knives, chopsticks, glasses, wine opener, pizza cutter, sponge holder, kitchen towels, soap dispenser stickers, flatware organizer

## Still Needed (NOT on any list)

### Buy on Amazon
- Pots & pans set ×2
- Bath towels (6 sets per unit = 12 total)
- Trash cans (kitchen + bedroom + bathroom, ~6 total)
- Toilet brush + plunger ×2
- Dish drying rack ×2
- Colander/strainer ×2
- Mixing bowls ×2

### Buy Elsewhere
- **Smart TV ×4** → Best Buy open-box (2x 55" living room + 2x 43" bedroom)
- **TV console ×1** → SUPERJARE 55" rattan cane w/ legs — ordered Amazon ~$87 (living room only, both TVs wall-mounted)
- **TV mounts ×2** → ordered Amazon
- **Nightstands** → SUPERJARE rattan set — ordered Amazon
- **Dining table + chairs ×2 sets** → IKEA (LISABO table + TEODORES chairs x4 per unit)
- **Rugs ×2** → HomeGoods (8x10, light natural jute/boho, under $160)
- **Lamps ×4** → HomeGoods (rattan boho, 2 per unit)
- **Coffee tables ×2** → HomeGoods (48-55" rectangular, light wood/rattan, matches 108" sectional)
- **Bed frame ×2** → Facebook Marketplace or IKEA
- **Towels** → Costco (best price/quality ratio)
- **Pots & pans** → TJ Maxx / HomeGoods (find $150 sets for $40-50)

### Tomorrow Shopping Route (2026-05-25)
Starting: 14622 Grenadine Dr, Tampa (car pickup)
1. **Best Buy** — 4x TVs (2x 55" + 2x 43", open-box)
2. **HomeGoods** — rugs x2, lamps x4, coffee tables x2
3. **IKEA** — dining tables x2 + chairs x8

Budget: ~$650 TVs + ~$150 rugs + ~$120 lamps + ~$200 coffee tables + ~$500 dining = ~$1,620

## Estimated Remaining Furnishing Cost
- Furniture (bed frames, sofa, dining, nightstands): $2,500–4,500
- TVs ×2: $600–1,000
- Cookware + towels + misc: $400–600
- **Total remaining: ~$3,500–6,100**

## Florida DOR Tax Registration — IN PROGRESS
- Logged in, got to "Sales, Rentals or Repairs of Products" activities page
- Paused session to install Playwright MCP for Claude to control browser directly
- **Resume next session**: open new Claude Code session, navigate to taxapps.floridarevenue.com, log in, Claude will use Playwright MCP to fill and submit the form
- Script saved at: `C:\Users\samth\Downloads\florida_rev2.py` (can also do via Playwright MCP now)
- Business info: CitySide Stays LLC, EIN 41-5346841, Short-term residential property rental, Disregarded Entity

## Playwright MCP Installed
- Command used: `claude mcp add playwright npx @playwright/mcp@latest`
- Saved to: `C:\Users\samth\.claude.json`
- Next session: Claude can see + control browser directly — no more screenshot workarounds

## Pending — Erik (Landlord)
- Apt 28 lease NOT signed yet (as of 2026-05-25) — keeps saying "today/sure" but hasn't done it
- No key given for unit 28 yet
- 8am text scheduled: ask for lease signature + key, tied to shopping trip deadline
- AC leak in unit 28 still unresolved — documented in Section 18, 24hr clock starts on written notice
- If no action within 24hrs of written notice → hire contractor, deduct from rent (no cap per lease)

## Bathroom Upgrade — Both Units
- Gold theme committed (showerhead, arm, tub spout, overflow cover all ordered)
- KINLIV 8" brushed gold rainfall showerhead x2 — ordered
- 90 degree brushed gold shower arm 16" x2 — ordered (includes escutcheon ring)
- Gold tub spout x2 — ordered
- Gold tub overflow cover x2 — ordered
- Existing 3-handle faucet knobs: clean with Barkeeper's Friend, do not replace
- Ceramic soap dish + towel bar: built into tile, cannot remove, leave as-is (white, neutral)
- Shower arm may be corroded in wall — try WD-40 + strap wrench; if stuck text Erik (landlord obligation)
- Teflon tape needed — get at Home Depot tomorrow

## Decisions Made
- Queen beds in both bedroom and living room (sofa bed) — not king
- Schlage Encode Plus kept despite cost — reliability for STR
- California Design Den 400TC cotton sheets chosen over microfiber (hotel quality, worth the upgrade)
- Revlon One-Step hairdryer recommended over Dyson knockoff
- Shark vacuum kept (already budget model, reliable)
