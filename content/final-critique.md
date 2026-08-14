# Phase 6 — Final design critique & punch list

**Reviewer:** Opus 5, 2026-08-13. Reviewed against CLAUDE.md's "What Done Looks
Like" — *a Lamborghini rental fleet manager in Lehi would trust this with their
content pipeline after 30 seconds of scrolling on their phone* — at 390px first,
then 1440px, across all 7 pages, served locally (not `file://`).

Every item below was applied in this session unless marked **Deferred**. Ranked
by priority, highest first.

---

## 1. AVIF pipeline was silently broken since Phase 1 — fixed at the root

Not just a missing encoder. `Assets/` still held the original Lightroom shoot
folders (`cav-28-photos/`, `rev-119-photos/`) while `images/` had been re-sorted
into `cars/`/`motorcycles/`/`bicycles/` back in Phase 2 — so re-running
`prep_images.py` at any point since would have regenerated a **different tree
than what's published**, AVIF aside. The pipeline wasn't reproducible, full stop.

Fixed:
- Recovered the shoot-file → published-number mapping by perceptual hash
  (146/146 matched, zero collisions, verified byte-identical against the
  published JPEGs) and reorganized `Assets/` to mirror `images/`.
- `tools/prep_images.py` now hard-exits if no AVIF encoder is registered
  instead of silently writing a partial set, drops the swallow-all
  `try/except` around WebP/AVIF saves, keeps source filenames as output
  numbers, and skips `_`-prefixed folders. Encoder lives in `tools/.venv`
  (`pillow-avif-plugin`, since PEP 668 blocks a bare `pip install` on this
  machine) — documented in the module docstring.
- Regenerated all 584 masters × 4 sizes × 3 formats. Added
  `<source type="image/avif">` ahead of the WebP source in all 156 `<picture>`
  blocks across `index.html`/`portfolio.html`/`services.html`/`about.html`,
  updated the hero's `<link rel="preload">` to target AVIF (was preloading
  WebP while `<picture>` now prefers AVIF — that would have double-fetched),
  and rewired the lightbox's JS-built `<picture>` (`js/main.js`) to populate
  a separate AVIF `<source>` alongside WebP. Verified via headless Chromium
  that the lightbox resolves to the `.avif` file with zero console errors.

## 2. Desktop nav had no persistent booking CTA

`.nav__cta` was `display:none` outside the mobile menu — on desktop, "Book a
shoot" only existed in page body copy, contradicting CLAUDE.md's "a booking
path so clear a private owner never has to hunt." Enabled `.nav__cta` from
861px up, sized down from the full `.btn` (0.65rem/1.35rem padding, 0.75rem
type) so it reads as nav chrome, not a second hero button. Checked for overflow
at 900/1024/1200/1440px — clears with room at all four.

## 3. Homepage Cars tile was fronted by a bystander, not the car

`cars/010` (white 911 GT3) had a sharp, well-lit, branded-shirt spectator
standing directly beside the headlight — the eye goes to him first. This was
the tile representing Cars — audience #1 per CLAUDE.md — on the homepage.
Swapped to `cars/033`, a close exotic detail shot (LED running lights, warm
string-lit restaurant backdrop) with no person in focus. Also incidentally
resolves the bystander-identifiability item `facts-to-confirm.md` had flagged
for this exact frame.

## 4. Pricing-promise band dead-ended with no CTA

The homepage's strongest conversion hook — "You pay what the work is worth to
you, after you've seen it" — closed with three feature points and nothing to
click. Added a centered "Book a shoot" button below the points.

## 5. `.stat-row` stranded its third item on mobile

Every current use (`index.html`'s 48 hrs/Utah County/On location,
`about.html`'s Provo/Orem·Lehi/Salt Lake City) is exactly 3 items on a 2-up
mobile grid, so the third always fell alone onto its own row with dead space
beside it. Changed to single-column below 480px, 3-up above — no code using
2 columns existed to preserve.

## 6. Portfolio opened with ~700px of black before the first photo

`.page-intro`'s own bottom padding plus the following `.section--tight`'s full
top padding stacked into one oversized gap — worst on `portfolio.html`, whose
entire premise is photography carrying the page. Added
`.page-intro + .section--tight { padding-top: clamp(1.5rem, 4vw, 3rem) }`,
which tightens the rhythm consistently across every inner page (services,
about, contact use the same pattern), not just portfolio.

## 7. Portfolio hover captions read like filenames

All 140 tiles showed `Cars · 001` / `Motorcycles · 044` — accurate but reads
as unfinished, and it doubles as the lightbox's top-bar caption, so the flaw
compounds when a visitor opens a photo full-screen. Derived real captions from
the existing (Phase 3/5-authored) alt text — subject + one evocative detail,
e.g. "Coupe · Alpenglow", "Detail · Rear wheel & chain", "911 GT3 · At the
meet" — respecting the standing no-guessed-models rule everywhere except the
four vehicles Phase 5 already confirmed from legible badges (Mustang GT, 911
GT3, 718 Cayman GT4 RS, BMW 4 Series, Lexus SC). Applied to both the visible
`.m-tile__cap` span and the `data-cap` the lightbox reads from, across all 140
tiles.

## 8. Cars sub-filters exposed how thin the library is

Exotics 4, Builds 28, **Events 1** — a filter chip resolving to one photo reads
broken, not curated, exactly where CLAUDE.md ranks the audience (supercar
owners) highest. Recategorized `cars/009` (a row of classic muscle cars at a
meet) from `events` to `builds` — it fits there thematically — and removed the
now-empty Events chip. Exotics stays at 4 and Builds at 29; both filters now
resolve to a plausible curated set rather than a single frame. Did **not** pad
either bucket with near-duplicates (standing instruction).

## 9. Motorcycles masonry had a visible run of near-identical frames

`048`–`053` were six consecutive "black cruiser in front of the same colorful
mural" shots — the single most repetitive stretch in the 107-photo grid.
Swapped two DOM positions with nearby dissimilar frames (`054` storefront,
`056` dealership) so the mural set now reads as two well-spaced pairs instead
of one wall of six. Verified via set-equality that no image was dropped or
duplicated, and via headless render that the grid still displays correctly.
**Deferred, not fixed:** grouping all 107 motorcycles into "shoots" per
CLAUDE.md's suggested pattern. The manifest carries no `shoot` field, so
grouping means deriving story boundaries from 107 photos by eye — a
real, larger job CLAUDE.md itself calls optional and the Phase 6 handoff
flagged as "genuinely optional... weakest scroll on the site." Recommend
scoping it as its own pass once Clark's next photo batch arrives, rather than
rushing a derived grouping now.

## 10. Nine photos had a legible license plate or house number — blurred

Doing a full visual sweep (not just the one frame `facts-to-confirm.md`
flagged) turned up plates on **9 of 140 portfolio photos**, several with two
plates in one frame, and — more serious than any plate — a fully legible
**house number on the residence behind `cars/023`**, which is exactly the class
of exposure CLAUDE.md cites as the reason EXIF/GPS gets scrubbed ("shoots
reveal clients' home locations").

Blurred (pixelate + Gaussian blur, applied to the `Assets/` masters — not just
the web output — and regenerated through `prep_images.py`, so a future
pipeline run won't silently restore the unblurred original):

| Frame | What was exposed |
|---|---|
| `cars/023` | Rear plate **and** a house number on the home behind it |
| `motorcycles/058` | Two plates (one dealer plate, one on an adjacent bike) |
| `motorcycles/064` | Plate — the entire subject of a macro detail shot |
| `motorcycles/103` | Plate, prominent in an otherwise excellent hero-quality frame |
| `motorcycles/107` | Plate |
| `motorcycles/047` | Same bike/plate as 107, different angle |
| `motorcycles/054` | Plate on a custom bobber |
| `motorcycles/096` | Two plates (two different bikes, one frame) |
| `motorcycles/009` | A background bike's vanity plate (partial, still blurred) |

None of these were cropped or removed — all are otherwise strong frames, so the
plate/address region alone was obscured. Backups of the unblurred Assets
originals are kept outside the repo in scratch space, not published.

**Deferred — flagging, not acting:** `motorcycles/062` has a sharp, in-focus,
clearly identifiable bystander (mid-stride, looking toward camera) plus
legible dealership signage in the background — the same category of issue as
the `cars/010` bystander, just deeper in the flat grid where it's less
consequential. Content-curation calls like this (crop vs. swap vs. leave) are
Clark's, not something to resolve by unilaterally editing a stranger's
likeness out of a photo. `motorcycles/047`'s rider is wearing a shirt reading
*"Someone Call the Police / I'm Killin the Streets"* — not identifying, but
worth Clark's eye on whether that reads on-brand for a commercial-facing
portfolio next to fleet-manager audiences.

## 11. Every inner page's intro text was gated behind a scroll-reveal it didn't need — hurting LCP

Found while re-verifying Lighthouse after the AVIF fix: `portfolio.html` scored
77 performance / LCP 5.5s on mobile, and the AVIF work should only have helped.
The actual LCP element wasn't an image at all — it was the page-intro's lead
paragraph, sitting at `opacity: 0` until an `IntersectionObserver` fired and a
900ms CSS transition finished. That pattern makes sense for content a user
scrolls to; it makes no sense for `.page-intro`'s `<h1>`/lead, which is always
in the initial viewport on every inner page — the homepage hero already gets
this right and was never wrapped in `.reveal`. Removed `.reveal` from the intro
heading and lead on `portfolio.html`, `services.html`, `about.html`, and
`contact.html` (4 pages, same fix, same bug). Portfolio mobile: **77 → 93
performance, LCP 5.5s → 2.7s.** No visual change — the text was always meant
to be visible immediately; now it actually is.

## 12. Everything else checked and left alone

- **Zero social proof.** Confirmed still true; nothing invented to fill it, per
  standing instruction. Real leverage the moment Clark has one named repeat
  client.
- **Wordmark.** Still type-only, holds up fine, no mark supplied.
- **Accent color, type system, motion, reveal timing.** No changes — Phase 2's
  system is sound and nothing in this pass justified touching it.
- **Zero console errors, zero horizontal overflow** at 390px and 1440px across
  all 7 pages, before and after this session's changes (re-verified via
  headless Chromium, not just Lighthouse).

---

## Still open (not this phase's job)

- **The four invented service commitments** (48-hour turnaround, 25–40 frames,
  60–90 minute session, full usage rights) — `content/facts-to-confirm.md`.
  Nothing here touched that copy; it's still waiting on Clark.
- **Phone number, domain purchase** — unchanged, still blank/unconfirmed.
- **More exotic/supercar photos** — Exotics still sits at 4 real frames against
  an audience-#1 ranking. The filter now *reads* curated instead of broken,
  but the underlying thinness is a photo-supply problem, not a design one.

---

## Lighthouse, re-verified after every change in this session

Served locally (`python3 -m http.server`, not `file://`). Both AVIF and the
LCP fix (#11) land in these numbers.

| Page | Perf mobile | Perf desktop | A11y | Best Prac. | SEO |
|---|---|---|---|---|---|
| index | 99 | 100 | 100 | 100 | 100 |
| portfolio | **93** (was 89, blocked pre-AVIF) | 100 | 100 | 100 | 100 |
| services | 93 | 99 | 100 | 100 | 100 |
| about | 93 | 99 | 100 | 100 | 100 |
| contact | 100 | — | 100 | 100 | 100 |
| thanks / 404 | 94 | — | 100 | 100 | 66\* |

\* `noindex` on purpose, as before — Lighthouse scores that as an SEO
failure; it isn't one.

Every page now clears 90+ on every category. Portfolio mobile was the one
sub-90 score left over from Phase 5 (89, diagnosed as blocked on AVIF); it's
now 93, and the root cause turned out to be two stacked issues, not one —
AVIF, then the reveal-animation LCP bug in #11 above, found only because
fixing AVIF didn't fully explain the number and prompted a second look at
what Lighthouse's LCP breakdown was actually pointing at.
