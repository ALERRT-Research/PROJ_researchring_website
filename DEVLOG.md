# Research Ring Website — Dev Log

Entries are newest-first. Each entry: date, status summary, open items, decisions made.

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
