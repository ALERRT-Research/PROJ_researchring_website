# Research Ring Website — Dev Log

Entries are newest-first. Each entry: date, status summary, open items, decisions made.

---

## 2026-05-06 (session 9)

**Status:** Publications added, people page links added, Tactical Science section added to landing page.

**Work done:**

- Added `pub-2026-transfer-gap` (Blair 2026, *Evidence Base*) to `public_output.qmd`
- Added `pub-2026-balkans` (Smailbegovic, Blair & Selimic 2026, *Varstvoslovje*) to `public_output.qmd`; placeholder URL used pending DOI
- Added faculty/profile links for all alumni and collaborators in `public_staff.qmd`: Pete Blair, Bill Sandel, Madison Doyle, Beth Quinby, Ian Adams, Matthew McAllister
- Removed Scott Mourtgos from Collaborators (does not meet 2+ projects/4-year rule); commented out with URL preserved for future reinstatement
- Added Tactical Science section to `index.qmd` (between Active Attacks and News & Updates); links to Pete Blair's Substack via `transparent_crosshair.png` thumbnail
- Copied `transparent_crosshair.png` to `resources/`

**Decisions:**

- Collaborator listing rule: 2+ active/completed projects in the past 4 years (Peter enforces manually)
- Tactical Science section links image only; no inline text link

**Open items:**
- `pub-2026-balkans` — replace placeholder URL with DOI when located
- `resources/articles/` — 42 PDFs still not linked from any page; decide whether to link, relocate, or delete

---

## 2026-05-06 (session 8)

**Status:** Favicon added.

**Work done:**

- Added `favicon.png` to project root (copy of `resources/research_ring_logos/research_ring_circle.png`)
- Added `favicon: "favicon.png"` to `_quarto.yml` under `website:`

---

## 2026-05-06 (session 7)

**Status:** Announcements added, crosslink system established, ID naming convention locked in.

**Work done:**

- Added ISC West / DHI conference announcement (`secured-doors-2026`) to `_media_entries.yaml` with `sia_conferences.png` thumbnail, description focused on the ISC West talk, DHI upcoming mention at end, and link to `grant-sia-2025`
- Updated PERF announcement (`perf-2026`) to link directly to the Lancet LEO mortality article (`pub-2025-leo-mortality`)
- Added `pub-YYYY-slug` anchor IDs to all 32 entries in `public_output.qmd` (callout block syntax: `{#id .callout-note collapse="true"}`)
- Retrofitted all 9 grant headings in `public_grants.qmd` from short slugs to `grant-` prefix convention; updated internal PASS crosslink accordingly
- Removed menstrual cycle paper from `public_output.qmd` (not a Research Ring product)
- Updated custom domain walkthrough (`r_quarto_custom_domain.qmd`) with troubleshooting note: URL forwarding on primary domain in Namecheap blocks GitHub DNS check; secondary domains only

**Decisions:**

- ID naming convention established:
  - Publications (articles, book chapters): `pub-YYYY-slug`
  - Grants: `grant-[funder/topic]-[year]`
  - Media/announcement entries: no prefix (e.g., `perf-2026`, `secured-doors-2026`)

**Open items:**
- `resources/articles/` — 42 PDFs still not linked from any page; decide whether to link, relocate, or delete

---

## 2026-05-06 (session 6)

**Status:** Custom domain fully operational. Walkthrough updated with discovered gotcha.

**Work done:**

- Identified root cause of GitHub DNS check failures: URL forwarding (301 redirect) was configured in Namecheap on the primary domain (`alerrtresearch.org`), which conflicts with the A Record / CNAME setup GitHub needs to perform DNS verification. Removing the redirect from the primary domain resolved the check immediately. Secondary domain redirects were unaffected and remain correct.
- Added new troubleshooting entry to `r_quarto_custom_domain.qmd` documenting the conflict and fix.

**Open items:**
- `resources/articles/` — 42 PDFs still not linked from any page; decide whether to link, relocate, or delete

---

## 2026-05-05 (session 5)

**Status:** Custom domain live. HTTPS enforcement pending TLS cert provisioning.

**Work done:**

- Domains purchased at Namecheap: `alerrtresearch.org` (primary), `alerrtresearch.com`, `alerrt-research.org`, `alerrt-research.com`
- DNS configured at Namecheap: 4 A records for primary, `www` CNAME to `alerrt-research.github.io`, URL forwarding on 3 secondary domains → `https://alerrtresearch.org`
- Added `CNAME` file to project root (content: `alerrtresearch.org`), registered under `resources:` in `_quarto.yml`
- GitHub Pages custom domain set to `alerrtresearch.org` — DNS check passed
- Created `r_quarto_custom_domain.qmd` — step-by-step walkthrough guide for custom domain setup, added to "Working with R" section in Ring Resources sidebar
- Added `README.md` to repo root — visible on GitHub repo page
- Added GitHub icon (`bi-github`, 1.4rem) to footer right side, links to repo

**Open items:**
- `resources/articles/` — 42 PDFs still not linked from any page; decide whether to link, relocate, or delete

---

## 2026-05-05 (session 4)

**Status:** Custom domain setup deferred — domains not yet purchased.

**Work done:** Reverted CNAME file and `_quarto.yml` resource entry added in session 3. Nothing committed.

**Open items:**
- Purchase domains at **Namecheap** (namecheap.com): `alerrtresearch.org` (primary), `alerrtresearch.com`, `alerrt-research.org`, `alerrt-research.com`
- Once purchased, follow this order:
  1. Configure DNS at registrar — 4 A records for primary (`185.199.108.153`–`.111.153`), plus `www` CNAME to `alerrt-research.github.io`; set URL forwarding on the 3 secondary domains → `https://alerrtresearch.org`
  2. Add `CNAME` file to project root (content: `alerrtresearch.org`), add `"CNAME"` to `resources:` in `_quarto.yml`, render, commit, push
  3. GitHub repo → Settings → Pages → Custom domain → `alerrtresearch.org` → Save
  4. Enable Enforce HTTPS once DNS check passes

---

## 2026-05-05 (session 3)

**Status:** Resource cleanup. Pushed to remote. Render clean (20 pages).

**Work done:**

- Audited `resources/` against all source files for unused or broken references
- Deleted 10 unused files: 4 headshot PNGs, 2 unused hex tile logos, 2 redundant book cover variants, 2 `.DS_Store` files
- Removed dead `background-image: url('resources/research_ring_hex/hex_8.png')` rule from `.sidebar-title` in `styles.css` — file never existed and class never renders in Quarto output
- Confirmed `resources/grants/sia_2026_report.pdf/.png` references in `public_grants.qmd` are intentionally commented out — files needed when the SIA door lock report ships (est. May 2026)

**Open items:**
- `resources/articles/` — 42 PDFs not linked from any page; decide whether to link from `public_output.qmd`, relocate, or delete

---

## 2026-05-05 (session 2)

**Status:** Landing page and people page updates. Pushed to remote. Render clean (20 pages).

**Work done:**

- Landing page (`index.qmd`): Added three right-sidebar TOC entries — Welcome (hidden heading, anchor only), Active Attacks, News & Updates
- Dropped the duplicate "News & Updates" label that was being rendered by `render_news_strip_html()` in `_render_media.R`
- Removed redundant dark border and excess top margin from `.rr-media-strip` now that the H2 header handles visual separation
- Fixed missing Oxford comma in `public_reports.qmd` page title: "Books, Book Chapters & Reports" → "Books, Book Chapters, and Reports"
- People page (`public_staff.qmd`): Replaced placeholder headshot images with maroon hex + "Photo / Coming Soon" text via `.rr-hex-placeholder` CSS class
- Added `CLAUDE.md` to project root with Oxford comma style rule (enforced going forward)
- Set `project: render: ["*.qmd"]` in `_quarto.yml` to exclude `DEVLOG.md` and other `.md` files from site output

**Decisions:**
- Oxford comma is now a written rule in `CLAUDE.md` — applies to all site copy and headers
- Placeholder headshots stay as text until real photos are provided; swap by replacing the `<div class="rr-hex-placeholder">` with a `![](path){.hex-photo}` inside `.hex-photo-wrap`

---

## 2026-05-05 (session 1)

**Status:** Auth gate added to Ring Resources section. Render clean (21 pages).

**Work done:** Client-side password overlay on all Ring Resources pages.
- Gate fires on any page whose sidebar title contains "Ring Resources"
- Full-screen dark maroon overlay with gold-accented card; matches site design
- `localStorage` persistence — team members unlock once per browser
- Wrong password: card shakes, input clears
- Correct password: overlay fades out, page revealed

**Files added/changed:**
- `resources/auth-gate.js` — gate logic and overlay injection
- `styles.css` — auth gate CSS block appended at bottom
- `_auth-gate-include.html` — script loader (one line)
- `_quarto.yml` — `include-in-header: _auth-gate-include.html` added under `format: html:`

**Open items:** Verify gate fires on Resources pages and not on Home/public pages in browser.

---

## 2026-05-05 (initial)

**Status:** Post-launch polish. Branch clean, no outstanding changes.

**Stack:** Quarto website, `lux` theme, custom CSS (`styles.css`), deployed to GitHub Pages. Two sidebars: public-facing and internal Ring Resources.

**Site sections:**
- Public: Home (`index.qmd`), Research Output, In Progress, Reports, Staff, Grants, Media, Work With Us
- Internal (Ring Resources): Research process guides, R/Quarto tutorials, TX State links, Training (OpXR, Tobii)

---

<!-- Add new entries above this line, above the most recent entry. -->
<!-- The CONFIGURATION section below is permanent — do not overwrite it. -->

---

## CONFIGURATION (permanent reference)

### Auth Gate

| Item | Value |
|---|---|
| Default password | `ring2026` |
| Storage key | `rr_gate_v1` |
| Gate logic file | `resources/auth-gate.js` |
| Persistence | `localStorage` — unlocked once per browser until storage cleared |

**To change the password:**
1. Open `resources/auth-gate.js`
2. Update the `PASSWORD` constant (line ~8)
3. Bump `STORAGE_KEY` to `rr_gate_v2` (or next increment) — this forces everyone to re-authenticate
4. Re-render and deploy

**To invalidate a single user's session:**
Have them open DevTools → Application → Local Storage → delete the `rr_gate_v1` key.

**Security model:** Deterrent-level only. Content is in the HTML source. Not suitable for genuinely sensitive data.
