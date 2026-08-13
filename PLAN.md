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
(Each phase's model appends: date, model, decisions made, open issues. Deliverables
are tracked as checkboxes above — this log is for the *why*, not a restated file list.)

- 2026-08-12 — Fable — Wrote CLAUDE.md brief and this plan from Dylan-site conventions + @revsnapmedia research.
- 2026-08-12 — Fable — Folded in Clark's feedback: satisfaction pricing ($50–100, never "tip") per CLAUDE.md "Pricing model"; commercial custom-quoted on a separate path; Cars/Motorcycles never blended; no videography anywhere; people shoots unlisted (one About line on experimental collabs only). Budget set at $1,000 — quality bar unchanged. Photos arrive via Lightroom share (manual download into `Assets/`).
- 2026-08-12 — Haiku — Phase 1: extracted 148 images from the Lightroom share, adapted the Dylan-site toolchain, scrubbed EXIF/GPS, generated 1,184 responsive JPEG/WebP files into `images/`, built `content/image-manifest.json`. Initial vehicle sort (cars 74 / motorcycles 73) — **corrected below, it was wrong.**
- 2026-08-12 — Opus 5 — Phase 2: **re-sorted the images** after visual review showed Haiku's split was wrong — true counts **cars 33 / motorcycles 107 / bicycles 6** (bicycles excluded from the site; one portrait of a person moved to `Assets/_excluded-people/`). Chose accent **`#FF5A1F`**: a hue histogram of Clark's own photos put the complement of his dominant sky/dusk band directly on his own sodium-light band — maximum separation from the photography while staying native to his grading (6.31:1 contrast). Type: Archivo (display) + Inter (body). Built `css/style.css` and `index.html`. Lighthouse 100/100/96/100 desktop, 99/100/96/100 mobile (Best Practices dinged only by the missing favicon, Phase 4's job). **Open:** portfolio is thin on genuine exotics (~3 cars) against a brief ranking supercar owners #1 (now tracked as a TODO in Phase 1 above); phone number; domain purchase; vehicle model names for alt text.
- 2026-08-13 — Greg — Contact email confirmed (`revsnapmedia@gmail.com`, in `js/site-config.js`); phone still open. Clark will send more photos and model names later — until then, alt text should stay generic (no guessed models) and the Cars gallery shouldn't be padded with duplicates to compensate.
- 2026-08-13 — Sonnet 5 — Phase 3: built `portfolio.html` (Cars/Motorcycles split, sub-filters, keyboard-accessible lightbox added to `js/main.js`), `services.html` (owner pricing promise — the only place the $50–100 figure appears), `about.html`, `contact.html` (two Netlify forms with honeypots, `#owner-shoot`/`#commercial`), `thanks.html`. Filled the remaining 135 manifest alt-text entries (generic, no model guesses) and added a `subcategory` field to Cars (Exotics 4 / Events 1 / Builds 28) — **a build-time judgment call, not confirmed** — worth a sanity check once Clark's model list arrives. Verified via headless-browser checks: no console errors on any page, lightbox keyboard behavior (focus trap, arrow nav, Escape, focus return) all pass, no mobile overflow, reduced-motion honored. Didn't run Lighthouse this session — Phase 4 should, since `portfolio.html` is new and image-heavy. **Open:** no per-page OG:image/JSON-LD yet (Phase 4's checklist item), favicon still missing, phone still blank.
- 2026-08-13 — Greg — Reviewed the Phase 3 build on a public GitHub Pages preview (pushed to `gbmisa/revsnap-media-site`, live at `https://gbmisa.github.io/revsnap-media-site/` — repo is public because free-tier Pages requires it) and approved it. Proceeding to Phase 4.
