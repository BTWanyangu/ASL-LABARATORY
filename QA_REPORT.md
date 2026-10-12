# QA Report — Expanded ASL Website

**Revision:** 12 October 2026. **Status:** Local build and browser/static checks passed; deployment to the owner's real Render account remains outside the local test scope.

## Verification results (actually executed)

| Check | Status | Observation |
| --- | --- | --- |
| `npm ci --ignore-scripts` | PASS | Dependency-free package install; zero reported vulnerabilities |
| `npm run build` | PASS | 30 routed HTML pages, dedicated 404, three PDFs, fourteen WebPs |
| `npm run typecheck` | PASS | Python module compilation (the project is not TypeScript) |
| `npm test` | PASS (10 tests) | Route inventory; seven Valcambi categories; trade paths; unique metadata; links; image paths; PDFs; form integrity; meaningful detail pages |
| `python3 tests/browser_smoke.py` | PASS | 5 viewport widths: 320, 375, 768, 1024, 1440; home nav; 30 route injection tests; HTTP direct deep links; form validation and non-sent draft |
| `python3 tests/expanded_smoke.py` | PASS | `/services/`, `/trade/`, refining, mineral buying and mineral trading across 5 widths; desktop 15-link mega-menu; mobile nested category navigation; no horizontal overflow |
| PDF download files | PASS | Existing three real PDFs have correct `%PDF` file signature and download links |
| Original image manifest | PASS | All fourteen public images exist and are referenced correctly |
| Live Render deployment / custom domain | NOT RUN | Requires owner's hosting account and domain settings |
| Actual email delivery / real purchase execution | NOT RUN | Not implemented without real backend and verified business details |
| Financial/trading licensing and operations | NOT VERIFIED | Site descriptions are informational and enquiry-led; owner verification required |

## Architecture / acceptance details

- All existing routes retained. Nine additional service pages plus a new `/trade/` overview were added, taking the site from 20 to 30 content routes.
- Every service page contains at least three distinct substantive sections, five preparation items, and two FAQs.
- The service selector includes all 15 categories and service links pre-select the matching value through `?service=`.
- Service navigation groups link to 15 routes without unsupported fake features, checkout, vault lookup, shipment tracking, credit approval or certificate validation.
- Both `public/images/` and generated `dist/images/` retain the supplied logo and the original conceptual image assets. The additional foundry image is also included in two editorial crops.
- Existing downloadable documents remain generic customer education, not ASL-issued assay reports or formal certificates.

## Browser environment details

Due to restrictions on headless Chromium direct navigation to local sandbox URLs, page interaction was tested with HTML/CSS/JS and image data locally inlined using `page.set_content()`. A separate HTTP local-server test checked that **all 30** actual prerendered routes respond successfully when loaded directly with a trailing slash. Explicit Render rewrites for extensionless routes are included but live Render behaviour has not been verified.

`tests/screenshots/` includes automated viewport screenshots, including the expanded Services and Trade pages. These are QA evidence only, not site content.
