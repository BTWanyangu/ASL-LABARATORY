# ASL Website — Expanded Services Handover

**Revision date:** 12 October 2026  
**Website:** Aurum Standard Laboratories (ASL)  
**Scope:** Expanded portfolio, original copy and project source, source assets, downloads, tests and Render configuration.

## Delivered

- **30 prerendered content routes** and a separate 404 page; this includes 15 distinct service detail routes.
- Preserved original ASL mineral, gold, diamond, gemstone, sample-handling and reporting content.
- Added all **seven** Valcambi-reference service categories: Transportation, Reception, Assaying, Refining, Manufacturing, Financing and Storage. Independent ASL-focused, enquiry-led descriptions with three detailed sections, client preparation lists, FAQs and related links.
- Added independent **Mineral Buying** and **Mineral Trading** pages and a dedicated `/trade/` landing page.
- Rebuilt Services index into five logical sections and reorganized desktop/mobile navigation, footer links, homepage secondary showcase and the enquiry service selector.
- Added a new original conceptual industrial foundry photograph and alternate crop; fourteen optimized WebP files in total. Original ASL logo retained.
- All four insights and three downloadable PDFs retained and working. No existing route was removed.
- Render static deployment rewrites updated for each new route without trailing slashes.

## Operational inputs to confirm before live publication

1. **New service permissions and actual capabilities:** Confirm whether ASL directly performs refining/manufacturing or works through named and verified partners; whether transportation, reception, vault custody and finance are offered; and the precise scope of any mineral buying/trading activity. Confirm the relevant national trading, transport, processing and financial permissions. All new descriptions intentionally avoid asserting unprovided operational infrastructure, licences, insurance or commercial commitments.
2. **Commercial trading rules:** Confirm minerals accepted, buying jurisdictions, physical locations, ownership and mineral provenance checks, export/import requirements, source policies, contracting authority, payment arrangements and settlement processes. No website transaction execution, shopping-cart or real-time commodity quotes have been enabled.
3. **Regulated activities:** Confirm financing provider authorisations before marketing credit offers, and any security/insurance/contract details before offering storage or shipment booking. The site currently explains these as enquiry topics only, not self-service products.
4. **Contact:** Set verified `ASL_PUBLIC_EMAIL` for optional email-draft functionality or implement and test a real secure delivery backend. The form locally prepares text, validates fields and **does not claim to send**.
5. **Domain & legal:** Set `ASL_SITE_URL` to the actual full HTTPS origin, approve the privacy and terms pages, establish legal entity and jurisdiction, and identify public contact/address/business hours only when verified.
6. **Lab-specific content:** Add independently verified assay methods, standards and credentials only after supporting documentation is supplied.

These are owner decisions, not website UI errors. If service categories are not actually offered, remove them from `content/expanded_services.py` and `SERVICE_GROUPS`, rebuild and re-test before public release.

## Build and deployment

- This revision preserves the prior delivery's **Python-driven prerendered static HTML + CSS + JavaScript architecture**, with a conventional `package.json` build wrapper; it is not claimed to be React/Vite/TypeScript.
- `npm ci && npm run build` generates `dist/`. Static publishing uses directory `dist`.
- `render.yaml` contains explicit rewrites for deep links without trailing slashes. Normal trailing-slash pages resolve to generated `index.html` files; the 404 page is explicitly available.
- Site text is maintained in `content/data.py` and `content/expanded_services.py`; page markup in `templates/pages.py`; navigation/footer in `templates/components.py`; styling in `public/styles.css`; interaction in `public/app.js`.
- The package includes `SERVICE_SCOPE_AND_REFERENCES.md`, `IMAGE_MANIFEST.md`, `QA_REPORT.md` and this handover document.

## Transparency and attribution

Valcambi is a **reference for category selection**, not a supplier, parent, partner or accreditor to ASL. Valcambi's proprietarily named products and its performance, vault, staffing and certification claims were **not copied**. See `SERVICE_SCOPE_AND_REFERENCES.md` for sources and the exact route mapping. Generated scene images are conceptual illustrations, not documentary photos of ASL facilities.
