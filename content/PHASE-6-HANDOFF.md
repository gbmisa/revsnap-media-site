# Phase 6 Handoff — design critique & final punch list (Opus 5)

**Model change:** PLAN.md originally routed this phase to Fable for the critique.
**Greg's call (2026-08-13): Opus 5 runs Phase 6 instead** — critique *and* the
fixes. PLAN.md has been updated to match. The practical difference: the original
plan forced a critique-only session because Fable was expensive, so the punch
list had to survive a handoff to Sonnet. That constraint is gone. Write the
critique to `content/final-critique.md` anyway — it's the record of *why* the
final changes were made, and Greg reviews it before Clark sees the site — but you
can apply your own items in the same session.

Phases 1–5 are done. Read `CLAUDE.md` in full first, then this file, then
`content/facts-to-confirm.md`.

---

## ⚠️ Read this first: the site makes promises nobody confirmed

Phase 5's biggest finding, and it is not a design issue. The site currently
publishes these as firm commercial commitments, and **every one was invented by
Phase 2 or Phase 3**, not supplied by Clark:

- **"First edits back within 48 hours"** — stated **6 times** across home,
  services and about. The most-repeated promise on the site.
- **"25–40 fully edited frames"**
- **"A session runs 60–90 minutes"**
- **"Full usage rights — print it, post it, sell the car with it"** (a licensing
  term, not just copy)

Confirmed and safe: the satisfaction pricing (`$50–100`, services only) and
"commercial is custom-quoted". Full table in `content/facts-to-confirm.md`.

**Do not quietly soften these to de-risk them** — vague delivery terms read
hobbyist and would undo the positioning the whole site is built on. They either
get confirmed by Clark or replaced with numbers he can actually hold. If Greg
hasn't heard back by the time you run, flag it in the critique and leave the copy
alone.

---

## State of the site as verified (Phase 5, re-run from scratch)

Phase 4's audit numbers were taken on a machine that OOM'd partway through and
are unreliable — the "81 performance" figure in the older half of
`content/audit-results.md` is wrong. Real numbers:

| Page | Perf desktop | Perf mobile | A11y | Best Prac. | SEO |
|---|---|---|---|---|---|
| index | **100** | **99** | 100 | 100 | 100 |
| portfolio | **98** | **89** | 100 | 100 | 100 |
| services / about / contact | — | — | 100 | 100 | 100 |
| thanks / 404 | — | — | 100 | 100 | 66\* |

\* `noindex` on purpose. Lighthouse scores that as an SEO failure. Not a defect.

Also verified across all 7 pages at 390px and 1440px: **zero console errors, zero
horizontal overflow**, all seven at **100 accessibility with no failed audits**.

**Re-run Lighthouse after any image or DOM change.** Serve locally
(`python3 -m http.server`) — `file://` gives meaningless numbers.

---

## The one real technical debt: AVIF was never generated

This is the highest-value mechanical job left, and it's the only thing standing
between the site and ≥90 everywhere.

`CLAUDE.md` specifies "AVIF/WebP with JPEG fallback". `images/` contains **584
WebP + 584 JPEG and zero AVIF**. `tools/prep_images.py` *does* have an AVIF
branch (~line 87) but it needs a Pillow AVIF plugin that isn't installed, so it
has been failing silently since Phase 1 and nobody noticed.

Measured during Phase 5, not estimated:

- `cars/001-800`: **16.5 KB AVIF vs 36.3 KB WebP — 54% smaller**
- Renders correctly in Chromium at full dimensions (verified via Playwright)

Applied across the gallery this clears portfolio-mobile's 89 comfortably.

**Do it properly:** repair the encoder in `prep_images.py` so the pipeline stays
reproducible, then regenerate and add the `<source type="image/avif">` ahead of
the WebP source in every `<picture>`. Do not hand-roll the files with ffmpeg —
the next `prep_images.py` run would leave them inconsistent.

Environment notes: `pip install pillow-avif-plugin` is blocked by PEP 668 on this
machine (needs a venv, `--break-system-packages`, or the distro package). ffmpeg
with `libaom-av1` is present as a fallback encoder. **This is bulk mechanical
work across ~590 files and 7 pages — good candidate to hand to Sonnet 5 while you
do the design pass.**

---

## Open design-judgment calls — deliberately left for you

Phase 5 was copy polish and did not touch the design system. These are all real
and all yours to decide:

**1. No persistent "Book a shoot" in the desktop nav.**
`.nav__cta` is `display: none` globally and only appears inside the mobile menu
(`css/style.css:387` and `:437`). So on desktop the booking CTA exists only in
page body content. Phase 2 chose this for minimal chrome, and it is consistent —
but CLAUDE.md wants "a booking path so clear that a private owner never has to
hunt for how to hire Clark". Weigh minimal chrome against the conversion goal.

**2. The Cars gallery is thin, and the sub-filters expose it.**
Cars 33 / Motorcycles 107. Within Cars: **Exotics 4, Builds 28, Events 1.**
A filter chip that resolves to a single photo looks broken rather than curated,
and "Exotics & Supercars" — the audience-#1 category — yields four frames. This
was flagged in Phase 3 and is still unresolved. Options: drop or merge the Events
filter, drop the sub-filters entirely until the library supports them, or hold
for Clark's additional photos. **Do not pad with near-duplicates** (standing
instruction from Greg, 2026-08-13).

**3. 107 motorcycles in one flat masonry dump.**
CLAUDE.md suggests sets "can group into shoots ('stories') rather than a flat
dump". They don't — both grids are flat, and the manifest has no `shoot` field to
group by (`id, category, number, src, alt, width, height, orientation,
subcategory, _from`). Grouping would mean deriving shoots visually. Genuinely
optional, but 107 ungrouped frames is the weakest scroll on the site.

**4. Zero social proof.** No testimonials, no client logos. None were invented —
this is an honest gap, not an oversight. If Clark has even one repeat client
willing to be named, it's worth more than any design change on this list.

**5. Two privacy items in published photos** (Clark's call, neither changed):
- `images/cars/023` — the **license plate is legible** ("704 DRA"). A client's
  plate on a public marketing site. Used on the homepage grid and in the
  portfolio. EXIF/GPS was scrubbed for exactly this class of reason.
- `images/cars/010` — a **bystander's face is clearly identifiable**, wearing a
  shirt with a business name. It's the Cars category tile on the homepage. Shot
  at a public meet so there's no legal problem, but it's a stranger fronting a
  commercial page.

Fixes if wanted: a light plate blur on 023; a crop or a different frame for the
Cars tile.

**6. The wordmark is type-only and provisional.** Clark never supplied a mark.
It's set in Archivo (`.wordmark`) and holds up fine if he never does.

---

## What Phase 5 changed, so you don't undo it

- **All 31 `<!-- COPY: draft -->` blocks rewritten, flags removed.** There are no
  draft markers left anywhere. Copy is final pending the facts above.
- **Killed a three-page repetition** — the "canyon roads at last light /
  sodium-lit storefronts after close / empty decks at blue hour" triple appeared
  near-verbatim on home, services and about. About keeps the full version (it's
  the only one that earns each item with a reason); home and services got
  distinct angles. **Don't reintroduce the list on more than one page.**
- Split three cross-page duplications: home vs. services pricing promise, and the
  home closing CTA which was word-for-word the contact `<h1>`.
- **Vehicle IDs audited against the actual frames.** Confirmed from badges and
  kept: Mustang GT (S650), 911 GT3 (991), Lexus SC, BMW 4 Series Gran Coupe.
  **`cars/004` upgraded to "718 Cayman GT4 RS"** — the badge is legible on the
  mirror and it had been labelled a plain GT4. Removed as guesses: "Yamaha R1",
  "S 1000 RR", "SC300", "Mount Timpanogos", "Alpine loop", "Provo" as a location.
  Manifest alt fields updated to match. **Standing rule still applies: no
  make/model in copy or alt text unless it's legible in the frame.**
- **Bugs fixed:** the art-directed hero swaps to a *different car* on phones
  (`cars/018`, a BMW) than desktop (`cars/007`, the Mustang) while sharing one
  alt string — alt is now true of both; `404.html` was rendering unstyled below
  the fold (its footer used six class names absent from `css/style.css`) and is
  rebuilt on the real design system; footer headings were `<h3>` after an `<h1>`,
  failing heading-order on every page — promoted to `<h2>`, with `.footer h3` →
  `.footer h2` in the stylesheet.
- **Portfolio image priority rebalanced** — was 8 tiles at `loading="eager"` +
  `fetchpriority="high"` all competing; now 2 high-priority, 4 eager, rest lazy.

---

## Conventions that still bind you

- **Extend the design system, don't redesign it.** Accent `#FF5A1F` was derived
  from a hue histogram of Clark's own photos — the reasoning is at the top of
  `css/style.css`. Keep it there and keep the accent.
- **No inline `<script>`** — CSP is `script-src 'self'`. Inline `<style>` and
  `style=""` are fine.
- Every page needs the `<noscript>` reveal-unhide block in `<head>`; content must
  never depend on JS to be readable.
- `<picture>` everywhere with explicit `width`/`height`, `loading="lazy"` below
  the fold, and `sizes` matching the **actual rendered slot**.
- Never overlay body copy on unpredictable photography below 800px.
- **Pricing wording is non-negotiable** — the `$50–100` figure lives on
  `services.html` in the owner section only, never on the homepage or anywhere
  commercial-facing. Never write "tip", "tip-based", "donation", or "pay what you
  can". See CLAUDE.md "Pricing model".
- No videography anywhere. Cars and motorcycles never blended.

## Still blocked on Greg / Clark

- **Phone number** — `js/site-config.js` `phone: ""`. Nothing renders it so
  there's no broken output, but email-only is a real conversion drag on
  commercial/fleet buyers (audience #2).
- **Domain** — `revsnapmedia.com` is baked into canonicals, OG tags, JSON-LD and
  the sitemap but purchase is unconfirmed. If it changes, run
  `tools/set_site_url.py <url>`.
- **More car photos + vehicle model names** from Clark.
- **The four service commitments** at the top of this file.

## Your deliverable

`content/final-critique.md` — a prioritized punch list, written as a $10,000-site
design director reviewing against CLAUDE.md's "What Done Looks Like": hierarchy,
typography, spacing rhythm, image curation, conversion flow, anything template-y
or hobbyist. Then apply it, top priority first, and re-verify Lighthouse. Update
PLAN.md checkboxes and the handoff log.

The bar to review against: *a Lamborghini rental fleet manager in Lehi would
trust this with their content pipeline after 30 seconds of scrolling on their
phone.* Review it on a 390px viewport before a desktop one.
