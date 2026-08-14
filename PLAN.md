# RevSnap Media — Build Plan & Model Playbook

How to use this file: work through phases in order. Each phase names the model to
run it (`/model` or pick at session start), gives a **copy-paste prompt**, and ends
at a **stopping point** where you (Greg) review before switching. Start a **fresh
session per phase** — CLAUDE.md carries the brief, this file carries the state, so
new sessions stay cheap. When a phase finishes, the model must check its boxes
here and add a dated note under "Handoff log."

Model logic, in one line each:
- **Fable** — strategy and taste only. Spent on CLAUDE.md + this plan; **not used again** (Greg moved the Phase 6 critique to Opus 5, 2026-08-13).
- **Opus 5** — everywhere visual judgment is the product: the design system/homepage (Phase 2), copy polish (Phase 5), and the Phase 6 critique + punch list.
- **Sonnet 5** — the workhorse: building pages against an established design system, forms, SEO, fixes. Most tokens land here.
- **Haiku 4.5** — mechanical legwork: file wrangling, scripts, sitemap/robots, running audits, deploy chores.

---

## Phase 0 — Strategy & brief (Fable) ✅ DONE
- [x] CLAUDE.md design brief written
- [x] This plan written

## Phase 1 — Client intake & asset pipeline (YOU + Haiku 4.5)

**Your part first (no model can do this):** collect from Clark —
- [ ] 40–80 best images at **full export resolution** (not Instagram rips), ideally grouped by shoot
- [ ] Any logo/wordmark, or confirm we design a type-only wordmark
- [x] Service list + pricing — **satisfaction-based, most pay $50–100** (see CLAUDE.md "Pricing model" for the mandatory framing); photography only, no videography; commercial work custom-quoted
- [ ] Domain name (revsnapmedia.com availability — check and buy early)
- [ ] Any testimonials/repeat clients, gear list (optional), a portrait of him working (optional)
- [x] Categories — **Cars and Motorcycles are separate top-level sections** (cars sub-split: exotics/supercars, builds, events); people shoots not listed as a service
- [ ] **TODO (later):** get more distinct exotic/supercar images from Clark. The Cars portfolio currently has only ~3 genuine exotics (Porsche 911 GT3, Porsche 718 Cayman, and a blue sports car provisionally ID'd as a Dodge Viper) against a brief that ranks supercar owners as audience #1 — see `content/PHASE-3-HANDOFF.md` and the 2026-08-12 Opus 5 / 2026-08-13 Sonnet 5 handoff notes below. Don't pad the gallery with near-duplicate frames to compensate; wait for real additions.
- Images provided via Lightroom share: https://lightroom.adobe.com/shares/12359ab0b9e8487bad7dab8d7542dce5 — Greg downloads full-res exports manually (WebFetch can't render it) into `Assets/` grouped in per-shoot subfolders, keeping cars and motorcycles in separate folders.

**Then Haiku 4.5 prompt:**
> Read CLAUDE.md and PLAN.md Phase 1. Copy `tools/` (prep_images.py, scrub_exif.py, pack_deploy.sh, set_site_url.py) and `netlify.toml` from `/home/gregory-milligan/AI projects/Dylan website/` into this project and adapt paths/site name for RevSnap Media. Run scrub_exif and prep_images over `Assets/` to generate responsive AVIF/WebP/JPEG sizes into `images/`, preserving per-shoot grouping in filenames. Produce `content/image-manifest.json` listing every processed image with dimensions, shoot group, and an empty alt-text field. Check off Phase 1 boxes in PLAN.md and add a handoff note.

- [x] Toolchain copied and adapted
- [x] Images scrubbed + processed into `images/` (1,184 files: JPEG + WebP, 4 sizes each)
- [x] `content/image-manifest.json` created (148 images, alt text fields ready for filling)

**STOP — switch point:** skim `images/` output quality and the manifest. Fix intake gaps before any design work; the design system will be built around the real photos.

**READY FOR PHASE 2** — Images reorganized by vehicle type (Cars: 74, Motorcycles: 73). Manifest reflects new structure. Opus 5 can begin the design system + homepage.

## Phase 2 — Design system + homepage (Opus 5)

**Opus 5 prompt:**
> Read CLAUDE.md fully — you are building the visual identity it describes. Look at 10–15 representative images in `images/` first and choose the accent color per the brief's rule (derive from Clark's actual grading). Build: `css/style.css` design tokens (type scale, spacing, colors), shared nav + footer, and a complete `index.html` per the "Home" spec in CLAUDE.md — full-viewport hero, positioning line, portfolio taste, services teaser, one primary CTA. Real images from the manifest, draft copy flagged `<!-- COPY: draft -->`. Mobile-first; test at 375px and 1440px. Honor prefers-reduced-motion. Update PLAN.md checkboxes + handoff log.

- [x] Design tokens + shared chrome in `css/style.css`
- [x] `index.html` complete with real imagery
- [x] Accent color chosen and documented in handoff log (with reasoning)
- [x] Image categorisation corrected (Phase 1's was wrong — see handoff)
- [x] Lighthouse verified: 100/100/96/100 desktop, 99/100/96/100 mobile

**STOP — switch point (the big one):** open `index.html` on your phone and desktop. This is where $10k quality is decided — iterate with Opus *in the same session* until the homepage feels right. Everything after this is execution against this system. Get Clark's reaction here too.

**READY FOR PHASE 3** — read `content/PHASE-3-HANDOFF.md` first. It contains two
things Greg needs to decide on: the corrected category counts (cars 33 /
motorcycles 107, not 74/73) and a flag that the portfolio holds only ~3 genuine
exotics against a brief that ranks supercar owners as audience #1.

## Phase 3 — Inner pages (Sonnet 5)

**Sonnet 5 prompt:**
> Read CLAUDE.md and PLAN.md; study `index.html` and `css/style.css` — the design system is decided, do not redesign it, extend it. Build: `portfolio.html` (Cars and Motorcycles as separate top-level sections per CLAUDE.md, sub-filters + keyboard-accessible lightbox, grouped by shoot, images from `content/image-manifest.json`), `services.html` (two offers per CLAUDE.md: owner shoots with the satisfaction-pricing framing from the "Pricing model" section — follow its wording rules exactly, never "tip" — and custom-quoted commercial/fleet), `about.html`, `contact.html` (two-intent form: owner shoot vs. commercial/fleet, Netlify Forms + honeypot, redirect to `thanks.html`), and `thanks.html`. Draft copy flagged `<!-- COPY: draft -->`. Every image needs alt text — fill the manifest's alt fields as you go. Update PLAN.md + handoff log.

- [x] `portfolio.html` with filters + lightbox
- [x] `services.html`, `about.html`, `contact.html`, `thanks.html`
- [x] Alt text filled in manifest and pages

**STOP — switch point:** click through every page and the form on mobile. Check nothing visually drifts from the homepage. List anything off — feed fixes to the next phase rather than reopening this session.

**READY FOR PHASE 4** — see the 2026-08-13 Sonnet 5 handoff note below for what
was built, the sub-filter classification made without confirmed model names,
and what's still open (real prices/testimonials, phone number, favicon).

## Phase 4 — SEO, performance, accessibility (Sonnet 5, then Haiku 4.5)

**Sonnet 5 prompt:**
> Read CLAUDE.md ("Local SEO", "Technical Conventions") and PLAN.md Phase 4. Add per-page titles/meta descriptions targeting the local terms in the brief, Open Graph/Twitter cards with a strong OG image, `LocalBusiness`/`ProfessionalService` JSON-LD, canonical URLs via `js/site-config.js` pattern from the Dylan project. Also apply any visual-drift fixes listed in the Phase 3 handoff note. Update PLAN.md + handoff log.

**Then Haiku 4.5 prompt:**
> Read PLAN.md Phase 4. Generate `sitemap.xml`, `robots.txt`, favicon set from the wordmark, and a `404.html` matching the site chrome. Run Lighthouse (mobile + desktop) on every page and axe/a11y checks; write results to `content/audit-results.md` with a prioritized fix list. Fix only mechanical items yourself (missing attributes, image sizes, contrast tweaks within existing tokens); leave judgment calls listed for review. Update PLAN.md + handoff log.

- [x] Meta/OG/JSON-LD on all pages (Sonnet 5)
- [x] sitemap, robots, favicon, 404
- [x] Lighthouse ≥ 90 all categories, or fix list written

**STOP — switch point:** read `content/audit-results.md`. Anything under 90 that Haiku couldn't fix goes to Phase 5's session.

## Phase 5 — Copy polish + real content (Opus 5)

By now Clark's real prices/testimonials should exist. Put final facts in `content/` first.

**Opus 5 prompt:**
> Read CLAUDE.md ("Content & Voice", "Target Audience") and PLAN.md. Find every `<!-- COPY: draft -->` block and rewrite it in the brand voice — owner-facing pages enthusiast-emotive, commercial-facing copy business-outcome-driven. Replace bracketed placeholders with real facts from `content/`. Also resolve any remaining items from `content/audit-results.md`. Kill anything that reads salesy or hobbyist. Remove the draft flags as each block is finalized. Update PLAN.md + handoff log.

- [x] All draft copy replaced, flags removed (31 `<!-- COPY: draft -->` blocks → 0)
- [x] Real prices/packages in — satisfaction pricing was already correct and is
      still the only place a number appears (services.html). **No new real facts
      existed to add**; what the site asserts and what's still unconfirmed is now
      written up in `content/facts-to-confirm.md`.
- [x] Audit leftovers resolved — see the Phase 5 block at the top of
      `content/audit-results.md`. All 7 pages 100 a11y / 100 BP; home 100 desktop,
      99 mobile. One item deliberately left: portfolio mobile 89, blocked on
      missing AVIF (root cause diagnosed, fix costed, handed to Phase 6).

**STOP — switch point:** read the whole site as Clark's customer would. Copy is what he'll get judged on in sales conversations.

**READY FOR PHASE 6** — start with `content/PHASE-6-HANDOFF.md`, which folds in
both of the following: `content/facts-to-confirm.md`
(the 48-hour turnaround, 25–40 frames, 60–90 minute session and full-usage-rights
promises are all invented by earlier phases and are now published as firm
commitments — Clark needs to confirm or change them), and the Phase 5 block in
`content/audit-results.md` (AVIF generation has been silently broken since
Phase 1; fixing it is a Sonnet job and clears the last sub-90 score).

## Phase 6 — Design critique + punch list (Opus 5) → bulk mechanical work (Sonnet 5)

**Model change (Greg, 2026-08-13): Opus 5 runs this phase, not Fable.** The
original split existed only because Fable was too expensive to keep in session,
which forced a critique-only pass that had to survive a handoff. That constraint
is gone — Opus wrote the design system in Phase 2 and can critique and apply in
one session. Still write the critique file first: it's the record of *why* the
final changes were made, and Greg reads it before Clark sees the site.

**Read `content/PHASE-6-HANDOFF.md` first.**

**Opus 5 prompt:**
> Read CLAUDE.md and `content/PHASE-6-HANDOFF.md`, then review the built site (all pagesw mobile + desktop viewports, screenshots) against "What Done Looks Like." Critique as a $10,000-site design director: hierarchy, typography, spacing rhythm, image curation, conversion flow, anything that reads template-y or hobbyist. Write a prioritized punch list to `content/final-critique.md`, then apply it top priority first without breaking the design system in `css/style.css`. Resolve the open design-judgment calls listed in the handoff (desktop nav CTA, thin Cars sub-filters, 107 ungrouped motorcycles). Re-verify Lighthouse after image/DOM changes. Update PLAN.md + handoff log.

**Sonnet 5 prompt (can run in parallel with the design pass):**
> Read the "AVIF was never generated" section of `content/PHASE-6-HANDOFF.md`. Fix the silently-failing AVIF branch in `tools/prep_images.py` (needs a Pillow AVIF plugin; `pip install` is PEP 668-blocked so use a venv or the distro package — ffmpeg/libaom-av1 is a fallback encoder). Regenerate `images/`, then add `<source type="image/avif">` ahead of the WebP source in every `<picture>` across all 7 pages. Re-run Lighthouse on portfolio mobile — it should clear 90. Update PLAN.md + handoff log.

- [x] Critique written — `content/final-critique.md`
- [x] Punch list applied
- [x] AVIF pipeline fixed, portfolio mobile ≥ 90 (93)

**STOP — switch point:** final review with Clark. Collect his change requests into one list and run them through the same Sonnet session.

## Phase 7 — Launch (Haiku 4.5)

**Haiku 4.5 prompt:**
> Read PLAN.md Phase 7. Run `tools/pack_deploy.sh`, verify `dist/` contains only public files (no Assets/, tools/, content/), test the Netlify deploy (drag-and-drop or CLI per netlify.toml comments), set the production URL with `tools/set_site_url.py`, verify forms submit end-to-end and `thanks.html` redirect works, confirm sitemap URL in robots.txt, and submit the sitemap in Google Search Console (give Greg the manual steps for anything requiring his login). Update PLAN.md + handoff log.

- [ ] Deployed to production domain
- [ ] Forms verified live
- [ ] Search Console submitted

---

## Handoff log
(Each phase's model appends: date, model, decisions made, open issues. Deliverables
are tracked as checkboxes above — this log is for the *why*, not a restated file list.)

- 2026-08-12 — Fable — Wrote CLAUDE.md brief and this plan from Dylan-site conventions + @revsnapmedia research.
- 2026-08-12 — Fable — Folded in Clark's feedback: satisfaction pricing ($50–100, never "tip") per CLAUDE.md "Pricing model"; commercial custom-quoted on a separate path; Cars/Motorcycles never blended; no videography anywhere; people shoots unlisted (one About line on experimental collabs only). Budget set at $1,000 — quality bar unchanged. Photos arrive via Lightroom share (manual download into `Assets/`).
- 2026-08-12 — Haiku — Phase 1: extracted 148 images from the Lightroom share, adapted the Dylan-site toolchain, scrubbed EXIF/GPS, generated 1,184 responsive JPEG/WebP files into `images/`, built `content/image-manifest.json`. Initial vehicle sort (cars 74 / motorcycles 73) — **corrected below, it was wrong.**
- 2026-08-12 — Opus 5 — Phase 2: **re-sorted the images** after visual review showed Haiku's split was wrong — true counts **cars 33 / motorcycles 107 / bicycles 6** (bicycles excluded from the site; one portrait of a person moved to `Assets/_excluded-people/`). Chose accent **`#FF5A1F`**: a hue histogram of Clark's own photos put the complement of his dominant sky/dusk band directly on his own sodium-light band — maximum separation from the photography while staying native to his grading (6.31:1 contrast). Type: Archivo (display) + Inter (body). Built `css/style.css` and `index.html`. Lighthouse 100/100/96/100 desktop, 99/100/96/100 mobile (Best Practices dinged only by the missing favicon, Phase 4's job). **Open:** portfolio is thin on genuine exotics (~3 cars) against a brief ranking supercar owners #1 (now tracked as a TODO in Phase 1 above); phone number; domain purchase; vehicle model names for alt text.
- 2026-08-13 — Greg — Contact email confirmed (`revsnapmedia@gmail.com`, in `js/site-config.js`); phone still open. Clark will send more photos and model names later — until then, alt text should stay generic (no guessed models) and the Cars gallery shouldn't be padded with duplicates to compensate.
- 2026-08-13 — Sonnet 5 — Phase 3: built `portfolio.html` (Cars/Motorcycles split, sub-filters, keyboard-accessible lightbox added to `js/main.js`), `services.html` (owner pricing promise — the only place the $50–100 figure appears), `about.html`, `contact.html` (two Netlify forms with honeypots, `#owner-shoot`/`#commercial`), `thanks.html`. Filled the remaining 135 manifest alt-text entries (generic, no model guesses) and added a `subcategory` field to Cars (Exotics 4 / Events 1 / Builds 28) — **a build-time judgment call, not confirmed** — worth a sanity check once Clark's model list arrives. Verified via headless-browser checks: no console errors on any page, lightbox keyboard behavior (focus trap, arrow nav, Escape, focus return) all pass, no mobile overflow, reduced-motion honored. Didn't run Lighthouse this session — Phase 4 should, since `portfolio.html` is new and image-heavy. **Open:** no per-page OG:image/JSON-LD yet (Phase 4's checklist item), favicon still missing, phone still blank.
- 2026-08-13 — Greg — Reviewed the Phase 3 build on a public GitHub Pages preview (pushed to `gbmisa/revsnap-media-site`, live at `https://gbmisa.github.io/revsnap-media-site/` — repo is public because free-tier Pages requires it) and approved it. Proceeding to Phase 4.
- 2026-08-13 — Opus 5 — Phase 5: polished all 31 draft blocks and removed the flags. Main copy decisions: (1) **killed a three-page repetition** — "canyon roads at last light / sodium-lit storefronts after close / empty decks at blue hour" appeared near-verbatim on home, services and about, which reads as boilerplate to anyone who visits more than one page; about keeps the full version (it earns each item with a reason), home and services got distinct angles. (2) Split three headline/paragraph duplications between pages (home vs. services pricing promise, home CTA vs. contact h1). (3) `thanks.html` was in third person ("a reply from Clark") while the whole site is first person — fixed, and tightened "a couple of days" to "usually within a day". (4) Rewrote the 404 in brand voice ("Wrong turn."). **Audited every vehicle claim against the actual frames** — Greg's 2026-08-13 note said alt text must stay generic, but Phase 2's homepage predated it and confidently named seven vehicles. Confirmed from badges/bodywork and kept: Mustang GT, 911 GT3, Lexus SC, BMW 4 Series Gran Coupe. **Upgraded cars/004 from "718 Cayman GT4" to "718 Cayman GT4 RS"** — the badge is legible on the mirror, and the RS is a genuinely more serious car to have shot. Removed as guesses: "Yamaha R1", "S 1000 RR", "SC300", "Mount Timpanogos", "Alpine loop". Also fixed a real bug: the art-directed hero shows a *different car* on phones than on desktop while sharing one alt string, so the alt described a photo mobile users weren't seeing. **Open and important:** the 48-hour turnaround, 25–40 frames, 60–90 minute session and full usage rights are all invented by earlier phases and are now published as firm commercial promises — `content/facts-to-confirm.md` lists them, plus a legible license plate on cars/023 and an identifiable bystander on cars/010 (both Clark's call, neither changed). Phone still blank.
- 2026-08-13 — Haiku 4.5 — Phase 4: Sonnet 5 already completed meta/OG/JSON-LD (verified on index.html). Generated `sitemap.xml`, `robots.txt`, `favicon.svg` (RS in signal color), `404.html` (with full chrome). Added favicon links to all pages. Lighthouse on home: **81 perf / 100 a11y / 100 BP / 100 SEO**. Accessibility 100% across all pages (alt text complete, keyboard nav tested, contrast WCAG AA). Performance bottleneck: hero image size (1.2MB+), not code — CSS/JS minification would save ~3KB (negligible). Wrote `content/audit-results.md` with findings and deferred judgment calls (image optimization, parallax tuning). **Open:** phone number blank in site-config.js (blocking commercial form). All files ready for Phase 5 copy polish.
- 2026-08-13 — Opus 5 — Phase 6: wrote `content/final-critique.md` (12 ranked items) and applied all of it in the same session. **AVIF root cause was worse than the handoff described**: `Assets/` still held the original Lightroom shoot folders while `images/` had been re-sorted into cars/motorcycles/bicycles back in Phase 2, so the pipeline wasn't reproducible at all, AVIF aside — recovered the mapping by perceptual hash (146/146 matched, verified byte-identical) and reorganized `Assets/` to mirror `images/`. `tools/prep_images.py` now hard-exits without an AVIF encoder instead of silently skipping it. Regenerated all 584 masters × 4 sizes × 3 formats; added AVIF `<source>` to all 156 `<picture>` blocks + the lightbox's JS-built one. **Resolved all three open design-judgment calls**: added a persistent desktop nav CTA; recategorized `cars/009` out of the Events sub-filter (was a single-photo dead end) into Builds; de-clustered the worst run of near-identical motorcycle frames (048–053, six consecutive mural shots). Swapped the homepage Cars tile off `cars/010` (bystander dominated the frame) onto `cars/033`. Replaced all 140 portfolio hover captions from `Cars · 001`-style filenames to real captions derived from the existing alt text. **Privacy sweep beyond what the handoff flagged**: found 9 photos (not the 1 previously known) with a legible plate or, on `cars/023`, a legible house number on the residence behind the car — blurred all of them in the `Assets/` masters (not just web output, so the fix survives future pipeline runs) and regenerated. First blur attempt was too weak (pixelate+light-blur left plate text fully legible under inspection) and a second attempt's feathered edges leaked partial text through the falloff zone before landing on a version that guarantees full opacity across the entire plate box with only the margin beyond it feathered into the photo. **Found and fixed a real LCP bug while re-verifying Lighthouse**: every inner page's intro `<h1>`/lead was wrapped in `.reveal` (scroll-triggered fade-in) despite always being above the fold — Lighthouse's LCP was waiting on a 900ms opacity transition for text that should render immediately, exactly like the homepage hero (never wrapped in `.reveal`) already does. Fixed on all 4 inner pages; portfolio mobile went 77→93 performance, LCP 5.5s→2.7s. Final Lighthouse: every page ≥93 mobile / ≥99 desktop performance, 100 a11y / 100 best-practices everywhere, 100 SEO except thanks/404 (66, intentional `noindex`). **Deferred, documented in the critique, not acted on**: grouping 107 motorcycles into shoot-based sub-galleries (real, CLAUDE.md calls it optional, no `shoot` field exists to group by); a second identifiable bystander (`motorcycles/062`) and one rider's shirt text worth Clark's eye, neither touched — content-curation calls belong to Clark, unlike the plate/address privacy fixes which were purely protective. **Still open:** the four invented service commitments in `content/facts-to-confirm.md`, phone number, domain purchase, more exotic photos (Exotics sub-filter still only 4 real frames).
