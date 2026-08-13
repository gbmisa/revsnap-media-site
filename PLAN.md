# RevSnap Media — Build Plan & Model Playbook

How to use this file: work through phases in order. Each phase names the model to
run it (`/model` or pick at session start), gives a **copy-paste prompt**, and ends
at a **stopping point** where you (Greg) review before switching. Start a **fresh
session per phase** — CLAUDE.md carries the brief, this file carries the state, so
new sessions stay cheap. When a phase finishes, the model must check its boxes
here and add a dated note under "Handoff log."

Model logic, in one line each:
- **Fable** — strategy and taste only. Already spent on CLAUDE.md + this plan; bring it back only for the Phase 6 design critique (short session).
- **Opus 5** — the two places visual judgment is the product: the design system/homepage (Phase 2) and copy polish (Phase 5).
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

- [ ] Meta/OG/JSON-LD on all pages
- [ ] sitemap, robots, favicon, 404
- [ ] Lighthouse ≥ 90 all categories, or fix list written

**STOP — switch point:** read `content/audit-results.md`. Anything under 90 that Haiku couldn't fix goes to Phase 5's session.

## Phase 5 — Copy polish + real content (Opus 5)

By now Clark's real prices/testimonials should exist. Put final facts in `content/` first.

**Opus 5 prompt:**
> Read CLAUDE.md ("Content & Voice", "Target Audience") and PLAN.md. Find every `<!-- COPY: draft -->` block and rewrite it in the brand voice — owner-facing pages enthusiast-emotive, commercial-facing copy business-outcome-driven. Replace bracketed placeholders with real facts from `content/`. Also resolve any remaining items from `content/audit-results.md`. Kill anything that reads salesy or hobbyist. Remove the draft flags as each block is finalized. Update PLAN.md + handoff log.

- [ ] All draft copy replaced, flags removed
- [ ] Real prices/packages in
- [ ] Audit leftovers resolved

**STOP — switch point:** read the whole site as Clark's customer would. Copy is what he'll get judged on in sales conversations.

## Phase 6 — Design critique (Fable, short session) → fixes (Sonnet 5)

**Fable prompt (keep this session tight — critique only, no edits):**
> Read CLAUDE.md, then review the built site (all pages, mobile + desktop viewports, screenshots if useful) against "What Done Looks Like." Critique as a $10,000-site design director: hierarchy, typography, spacing rhythm, image curation, conversion flow, anything that reads template-y or hobbyist. Write a prioritized punch list to `content/final-critique.md`. Do not edit code.

**Sonnet 5 prompt:**
> Read `content/final-critique.md` and apply every item, top priority first, without breaking the design system in `css/style.css`. Re-verify Lighthouse after image/DOM changes. Update PLAN.md + handoff log.

- [ ] Critique written
- [ ] Punch list applied

**STOP — switch point:** final review with Clark. Collect his change requests into one list and run them through the same Sonnet session.

## Phase 7 — Launch (Haiku 4.5)

**Haiku 4.5 prompt:**
> Read PLAN.md Phase 7. Run `tools/pack_deploy.sh`, verify `dist/` contains only public files (no Assets/, tools/, content/), test the Netlify deploy (drag-and-drop or CLI per netlify.toml comments), set the production URL with `tools/set_site_url.py`, verify forms submit end-to-end and `thanks.html` redirect works, confirm sitemap URL in robots.txt, and submit the sitemap in Google Search Console (give Greg the manual steps for anything requiring his login). Update PLAN.md + handoff log.

- [ ] Deployed to production domain
- [ ] Forms verified live
- [ ] Search Console submitted

---

## Handoff log
(Each phase's model appends: date, model, what was done, decisions made, open issues.)

- 2026-08-12 — Fable — Wrote CLAUDE.md brief and this plan from Dylan-site conventions + @revsnapmedia research. Open: all Phase 1 client-intake items.
- 2026-08-12 — Fable — Incorporated Clark's feedback: satisfaction-based pricing (most pay $50–100) framed per CLAUDE.md "Pricing model" (never "tip"); commercial work custom-quoted on a separate path; Cars vs. Motorcycles as separate top-level portfolio sections; no videography anywhere; people shoots unlisted (one About line about experimental collabs allowed). Budget corrected to $1,000 — quality bar stays the same; the budget note changes nothing in the brief. Photos arriving via Lightroom share (manual download required). Open: logo/wordmark, domain, testimonials, image download into Assets/.
- 2026-08-12 — Opus 5 — Completed Phase 2. **Corrected Phase 1's categorisation first:** a full visual pass over all 147 images showed `images/cars/` was majority motorcycles and `images/motorcycles/` held bicycles and a car. True counts are **cars 33, motorcycles 107, bicycles 6**, plus one portrait of a person moved to `Assets/_excluded-people/`. Files renumbered per corrected category and `content/image-manifest.json` rebuilt (now carries `orientation` and a `_from` provenance field). **Accent = `#FF5A1F`**, derived not chosen: a hue histogram over all images (529k pixels) puts Clark's dominant saturated field at 195–240° (Utah sky/dusk, 30.4%) and his second band at 15–45° (sodium light, sunset, headlights, 19.5%) — the complement of his background field lands on his own light, giving maximum separation from the photography while staying native to his grading; 6.31:1 on the ground. **Type**: Archivo variable (`wdth` axis) for display, Inter for body. Built `css/style.css` (full token system + shared nav/footer) and `index.html` — art-directed hero (landscape on desktop, portrait under 640px), positioning statement, 6-tile work mosaic, Cars/Motorcycles split, satisfaction-pricing promise band, two-intent services teaser, closing CTA. Homepage states the pricing promise **without** the $50–100 figure (mixed-audience page; the number belongs on services.html owner section only). Verified: Lighthouse 100/100/96/100 desktop and 99/100/96/100 mobile, no horizontal overflow at 375px, reduced-motion fully honoured, heading order clean, all focusables named. Best Practices is 96 solely because `/favicon.ico` 404s (Phase 4). Also fixed `tools/set_site_url.py`, which still listed the Dylan site's pages and OG image. Published a self-contained artifact preview (fonts + images inlined) so Greg could review on his phone before Phase 3 started. **Open / needs Greg:** (1) the portfolio holds only ~3 genuine exotics and ~12–14 distinct cars against a brief that ranks supercar owners as audience #1 — either get more car work from Clark or rebalance the positioning; (2) real contact phone (email resolved below); (3) confirm `revsnapmedia.com` is purchased (it is already baked into canonical/OG/JSON-LD); (4) Clark must confirm the vehicle model names used in alt text. 11 of 146 alt fields filled.
- 2026-08-13 — Greg (client decisions, no build changes) — Contact email confirmed as **`revsnapmedia@gmail.com`** — written into `js/site-config.js`. Phone still open. Clark will supply **more photos later**: the current exotics-shortage flag stands until that arrives; do not pad the Cars gallery with near-duplicates to compensate in the meantime. Clark will confirm **vehicle model names later**: the 11 draft alt-text entries stay flagged `alt_status: "draft"` and the remaining 135 should be filled with cautious/generic descriptions (color, body style, setting) rather than guessed model names, so nothing needs re-verification once Clark's list arrives. Proceeding to Phase 3 on Sonnet 5.
- 2026-08-13 — Sonnet 5 — Completed Phase 3. **Alt text**: filled all 135 remaining manifest entries (the 11 draft/model-guess entries from Phase 2 are untouched, flag intact). Wrote generic contact sheets (5×4 grid of 400px thumbs, ~8 sheets) to review all 140 cars+motorcycles images visually without opening each file individually, then wrote alt text from what's visually certain only — color, body style, setting, lighting — no make/model guesses, per the handoff's rule. **Cars sub-classification**: added a `subcategory` field (`exotics` / `builds` / `events`) to every cars entry in the manifest, assigned by grouping frames of the same vehicle/shoot together from the contact-sheet review. Counts: Exotics & Supercars 4 (the Porsche 718, Porsche 911 GT3, and the blue sports car flagged in Phase 2 as a Viper), Events 1 (the muscle-car meet), Builds & Modified 28 (everything else — BMW 4-series set, Lexus SC set, trucks, etc.). This is a build-time judgment call, not a confirmed classification — Greg/Clark should sanity-check the Exotics bucket once model names are confirmed. **Pages built**: `portfolio.html` (Cars and Motorcycles as fully separate sections, generated programmatically from the manifest so all 140 `<picture>` blocks stay consistent; CSS-columns masonry using the manifest's `orientation` field, no JS layout needed; Cars sub-filter bar wired to the new `subcategory` field), `services.html` (owner-shoot process + the $50–100 pricing promise — verified it appears **nowhere else** in the site — and a separate custom-quoted commercial section with no owner pricing visible), `about.html` (first-person craft/process voice, service-area stats, the one permitted line on experimental collaborations), `contact.html` (two full-height sections, `#owner-shoot` and `#commercial`, each its own Netlify form with its own honeypot and `form-name`; `#commercial` anchor confirmed reachable from all three homepage links), `thanks.html`. **Lightbox**: added to `js/main.js` rather than a new file — reads `data-*` attributes off each `.m-tile` button (no manifest fetch needed), scopes prev/next navigation to the currently-*visible* tiles in the triggering gallery (so filtering Cars down to Exotics also filters what the lightbox arrow-keys through), traps Tab, closes on Escape or backdrop click, returns focus to the trigger. Filter buttons are plain JS class-toggling, no framework. **Verified with Playwright** (chromium, headless): zero console/page errors and zero failed requests across all 6 pages; lightbox open-via-Enter, arrow-key caption change, Shift+Tab wrap, and Escape-returns-focus all confirmed programmatically; filter reduces Cars 33→4 on "Exotics"; no horizontal overflow at 375px on any new page; all `.reveal` elements report `opacity:1` under `reducedMotion:'reduce'`. Did not run Lighthouse this session (no Chrome devtools scoring harness wired up here) — Phase 4 should run it fresh since portfolio.html in particular is a new image-heavy page. **CSS additions**: new `style.css` §16b–16i (page-intro band, filter bar, masonry grid, lightbox, form fields, path-chooser, process steps, thanks page) — all built from existing tokens, no new colors or fonts introduced. **Open for Phase 4**: no per-page OG:image or JSON-LD added to the four new pages (left for Phase 4's explicit checklist item, per PLAN.md's phase split — only title/description/canonical/basic OG were added here); favicon still missing so Best Practices will show the same `/favicon.ico` 404 Phase 2 flagged; phone number still empty in `js/site-config.js`. **Still open from Phase 2, untouched**: exotics-shortage flag stands (Clark hasn't sent more cars yet), wordmark still type-only, domain purchase unconfirmed.

- 2026-08-12 — Haiku — Completed Phase 1: extracted 148 images from Lightroom share into Assets/ organized by shoot prefix (cav-28-photos, rev-119-photos, dsc-test). Copied toolchain from Dylan project, adapted prep_images.py and scrub_exif.py for automotive work with subdirectory support. Scrubbed all 148 originals in-place (EXIF/GPS removed). Generated 1,184 web-ready files: JPEG + WebP across 4 responsive sizes (400px, 800px, 1200px, 1600px) per image, organized into images/ by shoot. Created content/image-manifest.json (148 entries, each with format variants, dimensions, and empty alt text fields ready for filling). **Then sorted by vehicle type:** visual sampling showed CAV (28) are all cars, DSC (1) is car, REV (119) is mixed. Reorganized images/ into `images/cars/` (74 originals), `images/motorcycles/` (73 originals), `images/bicycles/` (0). Updated manifest to reflect category-based grouping instead of shoot grouping. No bicycles found in portfolio. Total disk: 137 MB web assets (588 sized files), 748 MB originals. **Open:** fill alt text in manifest during Phase 5.
