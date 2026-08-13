# Phase 3 Handoff — inner pages (Sonnet 5)

Phase 2 is done. The design system is decided. **Extend it, do not redesign it.**
Read `CLAUDE.md` in full, then `index.html` and `css/style.css` before writing anything.

**Update (2026-08-13, Greg's decisions — see PLAN.md handoff log for the full note):**
- Contact email is confirmed: `revsnapmedia@gmail.com`, already in `js/site-config.js`. Phone is still open.
- Clark is sending **more photos later** — the exotics-shortage flag below still stands until they arrive. Don't pad the Cars gallery with near-duplicates to paper over it in the meantime.
- Clark will supply **vehicle model names later**. Write alt text for the remaining 135 images using only what's visually certain — color, body style, setting, lighting — and skip make/model guesses. That way nothing needs re-verification once his list lands. See "Alt text" below.

---

## ⚠️ Read this first: Phase 1's categorisation was wrong, and has been fixed

Phase 1 recorded "Cars: 74, Motorcycles: 73". That was inaccurate — it was
inferred from filename prefixes plus a small visual sample. A full visual pass
over all 147 images found the `cars/` folder was **majority motorcycles**, and
`motorcycles/` contained bicycles and a car.

**Corrected, verified counts:**

| Category | Count | Notes |
|---|---|---|
| Cars | 33 | includes 1 image moved out of `motorcycles/` |
| Motorcycles | 107 | includes 41 moved out of `cars/` |
| Bicycles | 6 | `images/bicycles/` — **not linked from the site** |
| Excluded | 1 | a portrait of a person → moved to `Assets/_excluded-people/` |

Files were **renumbered sequentially within each corrected category**, so
`images/cars/007` is not the old `cars/007`. `content/image-manifest.json` was
rebuilt to match and each entry now carries `orientation` and a `_from` field
recording its pre-fix path. **Trust the manifest, not any older note.**

Bicycles and the portrait stay out of the portfolio: bicycles aren't a service
Clark offers, and CLAUDE.md keeps people shoots off the services list.

---

## 🚩 Flag for Greg — a positioning risk, not a build blocker

CLAUDE.md ranks **private exotic/supercar owners as audience #1**. The portfolio
does not currently support that claim well:

- **73% of the portfolio is motorcycles.** Cars are 23%.
- The 33 car images are roughly **12–14 distinct vehicles**, and most of the
  frames are repeats of three cars: a black BMW 4 Series (~10 frames), a white
  Lexus SC (~7), and a black BMW mural set (~5).
- **Genuine exotics/supercars: about three cars** — a white Porsche 911 GT3, a
  magenta Porsche 718 Cayman, and a blue Dodge Viper. Plus a current Mustang GT,
  which is a strong hero but not an exotic.

A Lehi rental-fleet manager scrolling the Cars section will see mostly one BMW.
Two options, both Greg's call:

1. **Get more car work from Clark** before launch — even two or three more
   distinct cars would change the read. This is the better fix.
2. **Rebalance the positioning** so motorcycles are an equal headline rather than
   the second category. The portfolio genuinely is strong on bikes.

The homepage as built hedges: it leads with a car hero and gives Cars and
Motorcycles equal billing. Nothing needs to change to ship — but the Cars gallery
will look thin next to Motorcycles, and Phase 3 should not try to disguise that
by padding it with near-duplicate frames.

---

## Design system as built

### Accent: `#FF5A1F` (signal orange)

Derived, not picked. A hue histogram over all 146 portfolio images (529k sampled
pixels) shows:

- Dominant saturated field **195–240°** (30.4%) — Utah sky, dusk, mountain haze.
  This is Clark's *background*, and an accent in that range would vanish into it.
- Second band **15–45°** (19.5%) — sodium storefronts, sunset alpenglow,
  headlights. This is Clark's *light*.

The complement of his background field lands on his own light, so `#FF5A1F`
(~22°) is simultaneously maximally separated from the photography and native to
his grading. It also reads motorsport rather than corporate. Contrast is
**6.31:1** on the page ground. The reasoning is repeated at the top of
`css/style.css` — keep it there.

### Type

- **Display** — Archivo (variable, `wdth` 100–124 / `wght` 550–800). Wide
  grotesque for masthead energy. Headings run uppercase at `wdth` 120–122.
- **Body** — Inter 400/500/600.
- Both from Google Fonts, already allowed by the CSP in `netlify.toml`.

### Tokens

Ground `#08080a` → `#0e0e11` → `#16161a`; hairlines `#1f1f25`/`#2a2a32`; text
`#7e7e8c` (5.01:1) / `#a8a8b4` (8.52:1) / `#e4e4e9`. Every grey in the palette
clears AA on the ground — don't introduce new ones without checking.

Fluid type scale, 4px spacing scale, `--wrap: 1360px`, `--gutter` fluid. Motion
uses two eases (`--ease-out`, `--ease-weight`) and three durations.

### Components already available to you

`.wrap` `.section` `.eyebrow` `.display/.h1/.h2/.h3` `.lead` `.btn--primary`
`.btn--ghost` `.link` `.nav` `.wordmark` `.hero` `.statement` `.stat-row`
`.sec-head` `.work-grid` `.tile` `.split` `.cat` `.promise` `.offer` `.cta-band`
`.footer` `.reveal`.

---

## Conventions you must keep

- **Reveals**: add `.reveal` (+ optional `data-delay="1..3"`) to animate in.
  `js/main.js` handles it. Never rely on JS for content to be readable — the
  `<noscript>` block in `<head>` unhides everything, so copy that block onto
  every new page.
- **No inline `<script>`** — the CSP is `script-src 'self'`. Inline `<style>` and
  `style=""` attributes are fine (`'unsafe-inline'` is allowed for styles).
- **Images**: always `<picture>` with a WebP `<source>` + JPEG `<img>` fallback,
  explicit `width`/`height`, `loading="lazy"` below the fold, and a `sizes` value
  that matches the **actual rendered slot** — over-declaring `sizes` was worth
  ~200 KiB of over-fetch on this page alone.
- **Art direction**: the hero swaps to a portrait source under 640px. Do the same
  anywhere a landscape image has to fill a tall phone viewport — a 3:2 frame
  centre-cropped into 375×812 shows a sliver of car and a lot of asphalt.
- **Never overlay body copy on unpredictable photography below 800px.** The
  category cards stack image-then-text on small screens for exactly this reason.
- **Draft copy** stays flagged `<!-- COPY: draft -->`. There are 9 blocks in
  `index.html`.

## Pricing copy — non-negotiable

- Owner shoots: *"You pay what the work is worth to you — after you've seen it."*
  The **$50–100** figure belongs on `services.html`, in the owner section only.
- The homepage deliberately carries the promise **without** the number, because
  it's a mixed-audience page and a published anchor would undercut commercial
  quotes. Keep it that way.
- Commercial/fleet is always "custom-quoted". Never show owner pricing on
  commercial-facing copy.
- Never write "tip", "tip-based", "donation", or "pay what you can".

---

## Verified state of the homepage

Lighthouse, local static server:

| | Perf | A11y | Best Prac. | SEO |
|---|---|---|---|---|
| Desktop | **100** | **100** | 96 | **100** |
| Mobile | **99** | **100** | 96 | **100** |

LCP 0.7s desktop / 1.9s mobile · CLS 0.022 / 0.001 · TBT 0ms.

Also verified directly: no horizontal overflow at 375px; `prefers-reduced-motion`
kills the hero animation, the parallax and all reveals with nothing left hidden;
all 32 focusable elements have accessible names; all images carry alt and
intrinsic dimensions; heading order is h1→h2→h3 with no skips.

**Best Practices is 96 only because `/favicon.ico` 404s** — Phase 4 generates the
favicon set and that resolves both it and the one console error.

`uses-responsive-images` still reports ~86 KiB (desktop) / 42 KiB (mobile) of
theoretical savings. That is the DPR-1 vs DPR-2 trade-off: serving 800w into a
410px slot is deliberate so retina screens stay sharp. Don't "fix" it by dropping
the larger candidates.

---

## Your job (Phase 3)

Build `portfolio.html`, `services.html`, `about.html`, `contact.html`,
`thanks.html` per the Phase 3 prompt in `PLAN.md`. Specific notes:

- **portfolio.html** — Cars and Motorcycles as separate top-level sections that
  never blend. Sub-filters on Cars (Exotics & Supercars / Builds & Modified /
  Events). Keyboard-accessible lightbox: focus trap, Escape to close, arrow keys,
  and focus returned to the triggering thumbnail on close. Pull images from the
  manifest — note it now has an `orientation` field, which makes a masonry or
  mixed-span grid straightforward.
- **Alt text** — 11 entries are filled in the manifest (the images used on the
  homepage), carrying make/model guesses made by visual ID (e.g. "a black BMW 4
  Series coupe"). Those are flagged `alt_status: "draft — model names to be
  confirmed by Clark"` and **must not be trusted as correct**; leave the flag in
  place. For the remaining 135, Clark is supplying model names later, so **don't
  guess makes/models for new entries** — describe only what's visually certain
  (color, body style — "coupe"/"sportbike"/"cruiser" — setting, lighting,
  time of day). A generic-but-correct description beats a specific-but-wrong one;
  getting a car's model wrong on a car photographer's site is the kind of error
  the target audience notices immediately.
- **contact.html** — Netlify Forms, honeypot, redirect to `thanks.html`, and the
  two intents split (`#commercial` is already linked from three places on the
  homepage, so that anchor must exist).
- **The mixed-vehicle frames** — a handful of images show cars and motorcycles in
  the same shot (motorcycle in the foreground). They are filed under motorcycles.
  Don't surface them in the Cars gallery.

## Still open (not Phase 3's problem, but don't undo them)

- `js/site-config.js` email is confirmed (`revsnapmedia@gmail.com`). **Phone is
  still a placeholder** (empty string) — Greg needs Clark's real one.
- The **wordmark is type-only and provisional** (`.wordmark` in the CSS) — Clark
  hasn't supplied a mark. It's set in Archivo and will survive if he never does.
- `revsnapmedia.com` is **assumed, not confirmed as purchased.** It is already
  baked into the canonical URL, OG image and JSON-LD. If the domain changes, run
  `tools/set_site_url.py <url>` — its page list and OG image were still pointing
  at the Dylan site and have been corrected.
- Google Fonts is a **render-blocking request**. The usual fix needs inline JS,
  which the CSP forbids. Perf is 99/100 anyway; leave it unless Phase 4 wants to
  self-host the two families.
