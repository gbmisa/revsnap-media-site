# Phase 2 Handoff for Opus 5
**Design System + Homepage Build**

## Project Brief (TL;DR)
- **Client:** Clark Farmer, RevSnap Media (automotive photographer, Provo, Utah)
- **Budget:** $1,000 (but quality bar: "make it like it's $10,000")
- **Goal:** Professional portfolio site that reads as established studio, not hobbyist
- **Aesthetic:** "Cinematic Automotive" — near-black UI ground, photography as loudest element, one accent color

Read [CLAUDE.md](CLAUDE.md) in full before starting.

## What's Done (Phase 1 Complete)

**Image Pipeline:**
- 147 original photos (4 responsive sizes each: 400/800/1200/1600px)
- 588 web-ready files: JPEG + WebP (AVIF attempted, optional)
- All EXIF/GPS scrubbed from originals (location privacy)
- Organized by vehicle category:
  - **Cars:** 74 photos (exotics, supercars, sports cars)
  - **Motorcycles:** 73 photos (sportbikes, cruisers, detail shots)
  - **Bicycles:** 0 (none in portfolio)
- Manifest: `content/image-manifest.json` (147 entries with format variants, dimensions, empty alt text)

**Stack:**
- Static HTML/CSS/vanilla JS (no build, no framework)
- Netlify deployment (TOML configured)
- Netlify Forms for contact (honeypot, thank-you redirect)
- Google Fonts (already in CSP header)
- LocalBusiness schema for SEO

## Your Job (Phase 2)

**Build:**
1. `css/style.css` — Design tokens (color, type, spacing) + shared chrome (nav, footer)
2. `index.html` — Full homepage per CLAUDE.md "Home" spec:
   - Full-viewport hero (real image from manifest)
   - One-line positioning statement
   - Taste of portfolio (3–4 hero images, one each from Cars/Motorcycles)
   - Services teaser (satisfaction-pricing promise + commercial note)
   - Single primary CTA button ("Book a shoot")

**Critical Constraints:**
- **Color:** Derive accent color from Clark's photo grading (he shoots cool or warm? choose accent from there). Monochrome UI + this one color only.
- **Typography:** Wide/condensed geometric display sans for headings (editorial energy, not gaming). Legible body sans. NO script fonts, NO textures.
- **Motion:** Minimal, physical (slow reveals, subtle parallax). Respect `prefers-reduced-motion`. GPU-accelerated CSS only.
- **Imagery:** Full-bleed, edge-to-edge. NO letterboxing on desktop. NO awkward crops. Minimal captions (car name, location, optional).
- **Ground:** Near-black (e.g. #0f0f0f, #1a1a1a, deep charcoal). This is NOT optional — it's the foundation.
- **Framing:** UI chrome stays minimal. Photography is the loudest. If design element competes with photos, cut it.

**Pricing copy rule (MANDATORY — see CLAUDE.md "Pricing model"):**
- Owner shoots: *"You pay what the work is worth to you — after you've seen it. Most clients choose $50–100."*
- NEVER use words: "tip," "tip-based," "donation," "pay what you can"
- Frame as confident artisan guarantee, not hobbyist charity
- Commercial/fleet work: "Custom-quoted — inquire" (never show $50–100 on commercial copy)

**Draft copy flagging:**
- Mark all placeholder/draft copy with `<!-- COPY: draft -->`
- Keep it terse (no placeholder paragraphs)
- This gets polished in Phase 5

**Mobile-first design:**
- Test at 375px viewport first (hero, portfolio taste, CTA)
- Then 1440px desktop
- Everything must work at both extremes

**Testing:**
- Use real images from `images/cars/` and `images/motorcycles/` (sample 3–5 hero shots, pick the strongest)
- Verify Lighthouse (mobile + desktop): ≥ 90 on all four metrics (if under, list blockers for Phase 4)
- Verify `prefers-reduced-motion` honored (no auto-play animations, CSS only)

## State of Repo

```
clark website/
├── CLAUDE.md               ← Read this (design brief)
├── PLAN.md                 ← Phase checklist + handoff log
├── content/
│   └── image-manifest.json ← 147 images with metadata
├── images/
│   ├── cars/               ← 296 files (74 originals × 4 sizes)
│   └── motorcycles/        ← 292 files (73 originals × 4 sizes)
├── css/
│   └── style.css           ← YOUR DESIGN SYSTEM GOES HERE
├── js/
│   ├── main.js             ← Placeholder
│   └── site-config.js      ← Canonical URLs, site metadata
├── netlify.toml            ← Already configured
└── index.html              ← YOUR HOMEPAGE GOES HERE
```

Assets/ and originals (748 MB) are not published.

## Key Decisions Already Made

1. **No videography anywhere** — Clark requested photos only. No hero reel, no video previews.
2. **Cars and Motorcycles are separate top-level portfolio sections** — never blended. This is baked into CLAUDE.md and will appear in Phase 3 portfolio.html.
3. **Satisfaction-based pricing ($50–100 for owner shoots)** — framed as artisan confidence, not tipping. Commercial work custom-quoted on separate path.
4. **People/experimental shoots unlisted** — one line on About only ("open to experimental collaborations").
5. **EXIF scrubbed** — all GPS data removed. Client shoot locations are protected.

## What Happens After Phase 2

**Phase 3 (Sonnet 5):** Inner pages against your design system (portfolio.html with category filters, services.html, about, contact, thanks).

**Phase 4 (Sonnet → Haiku):** SEO/metadata, sitemap, accessibility audits, favicon, Lighthouse fixes.

**Phase 5 (Opus 5):** Copy polish (kill hobbyist language, fill alt text, real prices/testimonials).

**Phase 6 (Fable, brief critique → Sonnet fixes):** Design critique vs. brief, final tweaks.

**Phase 7 (Haiku):** Pack and deploy.

## Questions for You Before Starting

- **Hero images:** Sample 3–5 from both Cars and Motorcycles folders. Which feel strongest? (I'll use those in the homepage.)
- **Accent color:** Look at a few images (especially well-edited sunsets, studio shots). Cool tones (blue, silver) or warm (amber, orange)? This drives the whole palette.
- **Type preference:** Do you lean toward something more geometric/modern (e.g. Inter, Space Grotesk) or editorial/high-contrast (e.g. DM Sans, IBM Plex Sans)? No flowery scripts.

---

**Next step:** Paste the Phase 2 prompt from PLAN.md and go build a homepage that makes Clark's work the hero.
