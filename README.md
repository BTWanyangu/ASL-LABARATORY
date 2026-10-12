# Aurum Standard Laboratories — Website

A complete, modular, mobile-responsive, production-buildable website for **Aurum Standard Laboratories (ASL)**, designed around the supplied official gold balance-scale logo and the caption *Assay of Minerals, Gold, Diamonds & Gemstones*.

## What is included

**Expanded 12 October 2026:** The original six service pages now sit alongside seven service categories identified on Valcambi’s official site (Transportation, Reception, Assaying, Refining, Manufacturing, Financing and Storage), plus two ASL owner-requested pages for Mineral Buying and Mineral Trading. There is a dedicated `/trade/` landing page. The project contains original copy, not Valcambi proprietary copy or unverified ASL facility/credential claims. See `SERVICE_SCOPE_AND_REFERENCES.md`.

- **30 standalone routed pages** plus a dedicated `404.html`: home; About; Services; 15 individual service pages and a mineral buying & trading overview; Process; Quality; Knowledge and four full articles; Resources; Contact; Privacy; Terms.
- Fourteen optimized WebP editorial-image files (six original generated scenes plus tracked alternate crops), user-supplied full logo, extracted crest, and favicon.
- Three working, printable PDF guides: sample submission checklist, material enquiry guide, and understanding reported results.
- Responsive desktop dropdown / keyboard-operable mobile navigation, honest enquiry drafting and validation, page metadata, accessible labels, responsive cards and reduced-motion support.
- Render Blueprint `render.yaml`, local build scripts, asset manifest, QA tests and handover notes.

## Implementation choice

The brief **preferred** React/Vite/TypeScript, but also required an actual functioning, verifiable deployment build. This delivery continues to use a **dependency-free modular prerendered static-site architecture** rather than introducing an unrelated framework migration in this revision. Python files under `content/` and `templates/` supply the reusable structured content and page components; `scripts/build.py` generates the HTML routes in `dist/`. Plain CSS and a small vanilla JS file implement the responsive frontend. No React or Vite build is claimed or included. This approach means pages, nested direct URLs, downloaded PDFs and SEO metadata work without client-side routing or an external npm registry.

For ongoing edits, `content/data.py` and `content/expanded_services.py` are the sources of truth for service and article details; `templates/pages.py` controls section layouts and `templates/components.py` controls shared header, cards, footer and CTAs. Site styling is in `public/styles.css` and behaviour in `public/app.js`.

## Requirements

- Python 3.10+ to build the website.
- Node 18+ and npm are optional conveniences for the standard `npm` scripts. The package has no third-party npm dependencies.
- The script that regenerates PDFs and WebPs (`scripts/prepare_assets.py`) requires Pillow and ReportLab and the original AI-generation inputs. Those source inputs are not required for normal builds because processed assets are committed under `public/`.

## Quick start

```bash
npm ci
npm run build
npm run dev
```

Open **http://localhost:4173/**. Alternatively, without npm:

```bash
python3 scripts/build.py
python3 -m http.server 4173 --directory dist
```

**A ready-built `dist/` folder is included** in the ZIP, so it can be hosted without running a local build.

## Render deployment

1. Push the extracted project to a Git repository, keeping `public/`, `scripts/`, `content/`, `templates/`, `package.json` and `render.yaml`.
2. In Render, select **New > Blueprint** and connect the repository, or select a **Static Site** manually.
3. Build command: `npm ci && npm run build`.
4. Publish directory: `dist`.
5. The `render.yaml` Blueprint sets the static runtime, caching/safety headers and rewrite mappings for routes without trailing slashes. URLs ending in `/` resolve to real directories such as `services/gold-assay/index.html`.
6. Configure your genuine domain in Render, then set `ASL_SITE_URL` to the **real full origin** (for example, your actual `https://...` domain) and rebuild to generate canonical tags and `sitemap.xml`. If unset, the website omits fictional canonical URLs and does not publish a sitemap.
7. Optionally set `ASL_PUBLIC_EMAIL` to the **verified official ASL public email**, then rebuild. The contact page will enable a `mailto:` draft option with the supplied details. See below.

The deployment blueprint follows Render's official static-site Blueprint syntax: https://render.com/docs/blueprint-spec

## New service routes

Seven Valcambi-category route names: `/services/transportation/`, `/services/reception/`, `/services/assaying/`, `/services/refining/`, `/services/manufacturing/`, `/services/financing/` and `/services/storage/`.

New commercial pages: `/services/mineral-buying/`, `/services/mineral-trading/` and the `/trade/` overview. All 15 service names can be selected in the contact form using the query string `?service=<slug>`.

The local content is enquiry-led and must be reconciled with ASL’s confirmed operational scope, approvals and partners. Do not represent it as proof that ASL owns a refinery, provides regulated financing, holds assets in a vault or has obtained trading permits.

## Contact behaviour — important

The supplied brief did not include a verified ASL email, working server endpoint, physical address or phone number. Consequently:

- The form **validates fields and prepares an enquiry draft locally**. It offers clipboard copy, not a false "sent" confirmation.
- Once `ASL_PUBLIC_EMAIL` is provided, the form also offers **Open email draft** to the verified recipient using the user's installed email client.
- It **does not store, deliver or transmit an enquiry server-side** and does not create a customer record.
- Production server submission requires a separately configured and tested backend with anti-abuse protection. No backend credentials or made-up contact details are included.

This should be explained by any administrator when enabling public enquiries.

## Editing content

- Company name/caption: `content/data.py`, `SITE`.
- Services: `content/data.py`, `SERVICES`, and `content/expanded_services.py` (`EXPANDED_SERVICES` and grouped `SERVICE_GROUPS`). Slugs must remain unique; the generator creates routes automatically.
- Articles: `content/data.py`, `ARTICLES`.
- Menu/footer/reusable CTAs: `templates/components.py`.
- Homepage/other page composition: `templates/pages.py`.
- Imagery: `public/images/` and `IMAGE_MANIFEST.json`.
- Colour, layout, mobile breakpoints: `public/styles.css`.
- Metadata logic: `scripts/build.py`.
- Legal copy: `templates/pages.py` (`privacy()` and `terms()`) — owner/legal review required before live publishing.

## Test commands

```bash
npm run typecheck
npm run lint
npm test
python3 tests/browser_smoke.py
npm run build
```

`tests/browser_smoke.py` uses locally installed Python Playwright, BeautifulSoup and Chromium for browser-level checks. If these tools are not installed, the core site can still build and the standard-library unit tests can run when BeautifulSoup is available. The browser screenshots in `tests/screenshots/` are QA artifacts, not website assets.

## Files

```text
content/data.py                Central material, process, commercial-service and article content
scripts/build.py              Prerendered site builder and SEO metadata
scripts/prepare_assets.py     One-time WebP, logo derivative and PDF creation
public/styles.css             Responsive design tokens and layout
public/app.js                 Mobile nav, dropdown and enquiry behaviour
public/images/brand/          Original supplied logo and derived crest
public/images/generated/      Original generated conceptual imagery and crops
public/downloads/             Three actual PDFs
templates/components.py       Shared UI building blocks
templates/pages.py            Page layouts
render.yaml                   Render Static Site Blueprint
dist/                         Ready-to-publish static site
tests/                        Automated checks and QA screenshots
HANDOVER.md                   Remaining actual owner decisions
QA_REPORT.md                  Tests performed and limitations
IMAGE_MANIFEST.md             Asset provenance and usage
```

## Originality and rights

The company logo was supplied by the user and is used as the primary identity. All website scene images were newly generated as conceptual editorial visuals. **They are not documentary evidence of ASL's facilities or equipment.** The visual benchmark was the navigation discipline of Valcambi's public website; Valcambi copy, images, trademarks and product imagery were not copied.
