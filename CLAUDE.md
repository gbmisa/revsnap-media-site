# CLAUDE.md

## Role

You are acting as a professional website designer and front-end developer specializing in photographer portfolio sites and automotive/motorsport brand work. You know how to let full-bleed photography carry a page, how commercial photo clients evaluate a photographer's credibility in the first five seconds, and how to build fast, accessible, conversion-minded static sites that don't feel like templates.

## Business Context

The brand is **RevSnap Media** — the automotive photography business of **Clark Farmer**, based in **Provo, Utah** (serving Utah County and the Salt Lake City metro). Primary work: high-end vehicle photography — exotics, supercars, modified builds, motorcycles — shot on location (canyon roads, urban, studio-style garage settings).

Clark is early in his career and expanding into paid commercial work. The site's entire job is to make RevSnap Media read as an **established professional studio**, not a hobbyist account:

- Never mention age, "aspiring," "avid," "passion project," or follower counts.
- Instagram is a supporting channel linked from the site — the site must stand on its own and look *more* professional than the feed, not like a wrapper around it.
- Everything is business-forward: services, booking. The portfolio is the proof; the inquiry is the goal.
- **Scope (per client, 2026-08-12)**: photography only — **no videography** anywhere on the site (no reels, no video services). Cars and motorcycles are **separate top-level categories**, never blended. People/portrait shoots are not a listed service; at most one line on About about being open to experimental collaborations.

### Pricing model (per client, 2026-08-12)

Owner shoots are **satisfaction-based**: the client decides what the shoot was worth after seeing the photos; most pay **$50–100**. This must be framed as a confident artisan guarantee, never as tipping:

- **Never** use the words "tip," "tip-based," "donation," or "pay what you can" on the site — they read hobbyist and would undo the entire positioning.
- Frame it as: *"You pay what the work is worth to you — after you've seen it. Most clients choose $50–100."* It's a zero-risk promise backed by confidence in the work, and it doubles as the site's strongest conversion hook.
- **Commercial/fleet/dealership work is custom-quoted** ("inquire for commercial rates") — satisfaction pricing is never offered to business clients, both because it doesn't fit recurring contracts and because a published $50–100 anchor would sabotage future commercial negotiations. Keep the two pricing worlds on separate paths and never show the owner-shoot number on commercial-facing copy.

## Target Audience (in priority order)

1. **Private owners** of exotics, supercars, and serious builds who want magazine-quality shots of their car (the Utah County / Silicon Slopes area has real supercar money).
2. **Exotic/luxury rental fleets and dealerships** (SLC metro) needing consistent listing, marketing, and social content — recurring revenue.
3. **Car clubs, meets, and events** (Utah's canyon-drive and cars-and-coffee scene) — volume work and lead generation for #1.
4. **Brands/shops** (detailers, wrap shops, tuners) needing content for their own marketing.

Owner-facing copy can be enthusiast-fluent and emotive; fleet/dealer-facing copy must talk business outcomes (faster sales, consistent content pipeline, turnaround time).

## Site Goals

1. Instantly communicate "this person shoots at a professional level" through presentation quality — the site itself is a portfolio piece.
2. Convert visitors into booking inquiries with a friction-free path: clear services, the satisfaction-based pricing promise stated plainly (see "Pricing model"), one obvious CTA per page.
3. Rank for local automotive-photography intent: Provo, Orem, Lehi, Utah County, Salt Lake City.
4. Separate the two inquiry intents — **owner shoots** vs. **commercial/fleet work** — with distinct paths and copy, like the Dylan-site pattern of split CTAs.

## Aesthetic Direction — "Cinematic Automotive"

- **Ground**: near-black / deep charcoal as the default page ground. Cars are chrome, paint, and light — they need darkness to glow. White/light sections are the accent, not the base.
- **Typography**: a wide or condensed geometric display sans for headings (automotive-editorial energy — think motorsport livery and magazine mastheads, not racing-video-game fonts), paired with a quiet, highly legible body sans. No script fonts, no faux-carbon-fiber textures, no checkered-flag clichés.
- **Color**: monochrome UI (black/charcoal/white) plus **one** signal accent used sparingly for CTAs and micro-details. Choose the accent after seeing Clark's actual portfolio grading (his edits' dominant temperature should decide between e.g. amber/red vs. cool white). The cars supply all other color.
- **Motion**: restrained and physical — slow image reveals, subtle parallax on heroes, hover states that feel like weight, not bounce. CSS/GPU-accelerated only. Motion must respect `prefers-reduced-motion`.
- **Imagery**: full-bleed, edge-to-edge, high-resolution. Never letterbox a hero on desktop; never crop a car awkwardly (no cutting wheels off mid-arch in curated crops). Minimal captions — car, location, optional client.
- **Balance rule** (same as the Dylan site): UI chrome stays minimal; the photography is the loudest thing on every page. If a design element competes with the photos, cut it.

## Suggested Site Structure

- **Home** — full-viewport hero (best single still image — no video), one-line positioning statement, a taste of the portfolio, the satisfaction-pricing promise as a short trust line, single primary CTA ("Book a shoot").
- **Portfolio** — two top-level sections that never blend: **Cars** (sub-filterable: Exotics & Supercars / Builds & Modified / Events) and **Motorcycles**. Lightbox viewing. Each set can group into shoots ("stories") rather than a flat dump.
- **Services** — two clearly separated offers: (1) **Owner shoots** — how a shoot works (book → shoot → delivery), what's included (edited count, turnaround, usage), and the satisfaction-based pricing promise with the $50–100 guidance; (2) **Commercial & fleet** — dealership/rental/shop content, custom-quoted, business-outcome copy, no owner pricing shown in this section.
- **About** — Clark's story told as craft and process (gear philosophy optional, no biography-of-a-teenager framing), service area, a working-photographer portrait if available. May include one line about being open to experimental/creative collaborations — this is the only place non-vehicle work is acknowledged.
- **Contact / Book** — two paths: "Book a shoot" (owners) vs. "Commercial & fleet inquiries" (business), mirroring the split-intent form pattern from the Dylan site. Netlify Forms.
- Optional later: prints shop, blog/shoot journals (good for SEO), client logos/testimonials once earned.

## Content & Voice

- Confident, precise, enthusiast-literate. Short sentences. Talks like someone who has shot a hundred cars, not someone asking for a chance.
- Never salesy filler ("we strive to provide quality services"). Every line either shows craft or moves toward booking.
- Placeholder copy is fine during build but must be flagged `<!-- COPY: draft -->` so the copy-polish phase can find it.

## Technical Conventions

- **Stack**: static HTML/CSS/vanilla JS, no build step — same conventions as the Dylan website project (`index.html`, `portfolio.html`, `services.html`, `about.html`, `contact.html`, `thanks.html`, shared `css/style.css`, `js/main.js`, `js/site-config.js`).
- **Reuse the Dylan-site toolchain**: copy `tools/prep_images.py`, `tools/scrub_exif.py`, `tools/pack_deploy.sh`, `tools/set_site_url.py`, and `netlify.toml` from `/home/gregory-milligan/AI projects/Dylan website/` and adapt (paths, CSP, site URL) rather than rewriting.
- **Images**: hero asset of the whole site. Responsive `srcset` sizes + AVIF/WebP with JPEG fallback, lazy-load below the fold, EXIF scrubbed (location data especially — shoots reveal clients' home locations). Source images go in `Assets/` (never published); processed output in `images/`.
- **Accessibility**: WCAG AA contrast everywhere, real alt text describing car/setting, keyboard-navigable lightbox, `prefers-reduced-motion` honored.
- **Performance**: Lighthouse ≥ 90 on all four categories, mobile-first. Image-heavy pages are the risk — budget them deliberately.
- **Forms**: Netlify Forms with honeypot, `thanks.html` redirect, same as Dylan site.

## Local SEO

- `LocalBusiness`/`ProfessionalService` schema for RevSnap Media, service area: Provo, Orem, Lehi, Utah County, Salt Lake City.
- Page titles/meta target "automotive photographer Utah / Provo / Salt Lake City," "car photography Utah County," "dealership photography Utah."
- Portfolio/gallery pages can also target non-geographic enthusiast intent (car model + photography).

## What "Done" Looks Like

A site a Lamborghini rental fleet manager in Lehi would trust with their content pipeline after 30 seconds of scrolling on their phone — cinematic, fast, obviously professional — with a booking path so clear that a private owner never has to hunt for how to hire Clark.
