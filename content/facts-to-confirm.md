# Facts the site currently asserts — needs Clark's confirmation

**Created:** 2026-08-13 (Phase 5, Opus 5)
**Updated:** 2026-08-13 — review fixes pulled the four invented SLAs/license
grants off the live pages. Numbers below are what we *want* to put back once
Clark confirms them.

## Service commitments

| Claim | Status |
|---|---|
| **First edits back within 48 hours** | **Invented Phase 2.** Removed from live copy 2026-08-13. Pages now say “while the shoot is still fresh.” Restore the number in one place (then stamp it) once Clark will hold it. |
| **25–40 fully edited frames** | **Invented Phase 2.** Removed. Live copy says “a full edited gallery.” |
| **Session runs 60–90 minutes** | **Invented Phase 3.** Removed. Live copy says “a focused session on location.” |
| **Full usage rights — print, post, sell the car with it** | **Invented Phase 2.** Licensing grant removed. Live copy says print-ready files / usage terms written into the commercial quote. Do not put a grant back until the contract matches. |
| **Reply to inquiries "usually within a day"** | Written Phase 5, deliberately soft (“usually”). Still on `thanks.html`. |
| **Most clients choose $50–100** | ✅ Confirmed by Clark 2026-08-12. Still the only price on the site. |
| **Commercial work is custom-quoted** | ✅ Confirmed by Clark 2026-08-12. |

If Clark can hold a 48-hour turnaround, that is the single highest-priority
number to restore — it was the most-repeated promise on the site.

## Still blank

- **Phone number** — `js/site-config.js` `phone: ""`. Nothing on the site renders
  a phone number, so there is no broken output, but commercial/fleet buyers
  routinely want to call. Email only (`revsnapmedia@gmail.com`) is a real
  conversion drag on audience #2.
- **Testimonials / client logos** — none exist yet. No placeholder was invented;
  the site has zero social proof by design rather than by oversight.
- **Domain** — `revsnapmedia.com` is still the intended production host in
  canonicals, OG tags, JSON-LD and sitemap. Purchase still unconfirmed (Phase 1
  checkbox is still open). After buying it, run `python3 tools/set_site_url.py`.

## Vehicle identification

Captions and alt text were audited against the actual frames.
Confirmed from badges/bodywork visible in the photo: Ford Mustang GT (S650),
Porsche 911 GT3 (991), **Porsche 718 Cayman GT4 RS** (badge legible on the mirror
— previously mislabelled as a plain GT4), Lexus SC (SC300 vs SC400 not
determinable), BMW 4 Series Gran Coupe.

Removed as unverifiable guesses: "Yamaha R1", "BMW S 1000 RR", "Lexus SC300",
"Mount Timpanogos", "Alpine loop", "Provo" as a shoot location.

Still worth Clark confirming: the 4 Series Gran Coupe call, and the
`subcategory` split on the Cars gallery (Exotics 4 / Builds 29) that
Phase 3 made without model names.

## Privacy

**Done (Phase 6):** plate/address sweep. Identifiable plates and the house
number on `cars/023` were blurred in the `Assets/` masters and regenerated.
The homepage Cars tile moved from `cars/010` (bystander-dominated) to `cars/033`.

**Still Clark's call — not touched:**

1. **`images/cars/010`** — a bystander's face is clearly identifiable, wearing
   a shirt with a business name. Still in the portfolio grid, no longer the
   homepage Cars tile.
2. **`images/motorcycles/062`** — a second identifiable bystander.
3. One rider's shirt text worth Clark's eye (noted in `content/final-critique.md`).
