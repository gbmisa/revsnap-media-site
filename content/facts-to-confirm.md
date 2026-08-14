# Facts the site currently asserts — needs Clark's confirmation

**Created:** 2026-08-13 (Phase 5, Opus 5)

PLAN.md Phase 5 assumed a "real facts" file would exist before copy polish. It
didn't, so the copy was finalized against the numbers earlier phases invented.
Those numbers now read as **firm commercial promises on a live site**. Every one
below is currently published. Clark either confirms it or it changes.

## Service commitments the site promises

| Claim | Where it appears | Status |
|---|---|---|
| **First edits back within 48 hours** | index (stat row, promise points, offer list), services (step 03, what's included), about (step 03) | **Invented Phase 2.** Appears 6× — the most-repeated promise on the site. |
| **25–40 fully edited frames** | index (offer list), services (what's included) | **Invented Phase 2.** |
| **Session runs 60–90 minutes** | services (step 02) | **Invented Phase 3.** |
| **Full usage rights — print, post, sell the car with it** | index (promise points, offer list), services (what's included) | **Invented Phase 2.** A licensing term, not just copy. |
| **Reply to inquiries "usually within a day"** | thanks.html | Written Phase 5, deliberately soft ("usually"). |
| **Most clients choose $50–100** | services only | ✅ Confirmed by Clark 2026-08-12. |
| **Commercial work is custom-quoted** | services, contact, index | ✅ Confirmed by Clark 2026-08-12. |

If Clark can't hold 48-hour turnaround, that is the single highest-priority copy
change on the site — it is stated six times and a missed delivery on a paid
commercial job is the kind of thing that ends a fleet contract.

## Still blank

- **Phone number** — `js/site-config.js` `phone: ""`. Nothing on the site renders
  a phone number, so there is no broken output, but commercial/fleet buyers
  routinely want to call. Email only (`revsnapmedia@gmail.com`) is a real
  conversion drag on audience #2.
- **Testimonials / client logos** — none exist yet. No placeholder was invented;
  the site has zero social proof by design rather than by oversight.
- **Domain** — `revsnapmedia.com` is hardcoded in canonicals, OG tags, JSON-LD
  and sitemap. Purchase still unconfirmed (Phase 1 checkbox is still open).

## Vehicle identification

Captions and alt text were audited this phase against the actual frames.
Confirmed from badges/bodywork visible in the photo: Ford Mustang GT (S650),
Porsche 911 GT3 (991), **Porsche 718 Cayman GT4 RS** (badge legible on the mirror
— previously mislabelled as a plain GT4), Lexus SC (SC300 vs SC400 not
determinable), BMW 4 Series Gran Coupe.

Removed as unverifiable guesses: "Yamaha R1", "BMW S 1000 RR", "Lexus SC300",
"Mount Timpanogos", "Alpine loop", "Provo" as a shoot location.

Still worth Clark confirming: the 4 Series Gran Coupe call, and the
`subcategory` split on the Cars gallery (Exotics 4 / Builds 28 / Events 1) that
Phase 3 made without model names.

## Two privacy items in published photos

Neither is a copy problem, so neither was changed — both are Clark's call:

1. **`images/cars/023`** — the car's **license plate is legible** ("704 DRA").
   This is a client's plate on a public marketing site. EXIF/GPS was scrubbed for
   exactly this class of reason. Used on the homepage grid and in the portfolio.
2. **`images/cars/010`** — a **bystander's face is clearly identifiable**, wearing
   a shirt with a business name on it. Used as the Cars category tile on the
   homepage. Shot at a public meet, so there's no legal problem, but it's a
   stranger fronting a commercial page.

Fixes if wanted: a light plate blur on 023, and either a crop or a different
frame for the Cars tile.
