# Research Ring Website — Project Instructions

## Git Push Policy — MANDATORY

**Never push to GitHub without explicit approval from an approver in a separate message.**

Approvers are **Peter** and **Hunter**. Approval from either one is sufficient.

This applies to everyone working in this project, every time, with no exceptions, even if an approver has already asked for a change to be made. Once the change is complete, present it and wait for a separate "go ahead" before pushing. A project-level hook in `.claude/settings.json` enforces this technically by blocking `git push` tool calls.

---

## Credentials — Never in Tracked Files

This repo is **public**. No API keys, tokens, or passwords in any tracked file, not even a
comment or a "free tier" key. Helper scripts in `scripts/` read credentials from the
environment (`OPENALEX_API_KEY`, `OPENALEX_MAILTO`, set in each maintainer's `~/.zshrc`)
and exit if they are unset. Before committing, `git diff` and look for anything that resembles
a key. Background: an outside reader found a hardcoded OpenAlex key here on 2026-09-06 —
see `docs/logs/2026-09-06_openalex-key-exposure.md`.

## Writing Style

- **Oxford comma required.** Always use the serial comma in lists of three or more items in any website copy, headings, or labels (e.g., "data collection, analysis, and reporting" — not "data collection, analysis and reporting").

## Links

- **All external links must open in a new tab.** Every markdown link or linked image pointing to an external URL must include `{target="_blank"}`. No exceptions.

## Page Nav ("On this page" TOC)

- **Nested headings always show expanded in the sidebar nav**, site-wide.
  Quarto's default behavior hides child headings in a collapsed sub-list
  until scrollspy marks the parent section active (i.e., until you've
  scrolled into it) — this site overrides that in `styles.css`
  (`nav[role="doc-toc"] ul.collapse`) so nested entries are always
  visible and clickable up-front, on every page.

---

## How to Add Content

### Publications (`public_output.qmd`)

All years nest under a top-level `# Research Output` heading (plain text,
no attributes). That heading's text is intentionally invisible — CSS in
`styles.css` (`#research-output > h1`) hides just the `<h1>` itself, so
the page's own title has a corresponding entry in the "On this page" nav
without repeating "Research Output" as visible text right below the
page's own title banner.

**Do not** add a `{.visually-hidden}` (or any hiding class) directly on
the `# Research Output` heading itself. With `section-divs` enabled (this
project's default), pandoc propagates a heading's attributes onto its
*wrapping section* too — a hiding class on the heading hides the entire
section, meaning every year and publication under it disappears from the
page along with the heading text. This actually happened once (fixed
2026-07-29). Keep the heading itself attribute-free and let the scoped
`#research-output > h1` CSS rule do the hiding.

Publications use Quarto callout blocks. Add new entries at the **top** of
the correct year section. If the year doesn't exist yet, add a new
`## YEAR` header (note: `##`, nested under `# Research Output`) above the
previous year.

**Pattern:**

```markdown
::: {#pub-YEAR-slug .callout-note collapse="true"}
## Full Title of the Article

Two to five sentences summarizing the paper. Write for a general audience — no jargon. Focus on what the study did and what it found.

::: {.rr-journal-label}
Journal Name Here
:::

[View the article here.](https://doi.org/XXXXX){.rr-article-pdf target="_blank"}
:::
```

Rules:
- The anchor ID (`#pub-YEAR-slug`) must be unique. Use `pub-YEAR-` prefix + a short kebab-case slug (e.g., `pub-2026-striking-grappling`).
- The link gets the `.rr-article-pdf` class AND `target="_blank"`. Both are required.
- If the article is not yet available online, omit the link line entirely and note "Article forthcoming." instead.
- No author list in the entry — the journal label is sufficient attribution context.

**Gotcha — callout `collapse` attribute must use straight quotes.**
`collapse="true"` must use straight `"` quotes, never curly/smart quotes
(`collapse=”true”`). Pandoc silently fails to parse the curly-quoted
version, and the callout renders **expanded by default** instead of
collapsed — no error, no warning, just wrong behavior that's easy to miss
without checking the rendered HTML (`aria-expanded` on the callout header).
This has actually happened twice in this file (fixed 2026-07-29) — likely
from pasting text that had gone through autocorrect (Word, Google Docs).
If you ever add a callout by pasting from one of those, retype the quotes
by hand or verify with `grep -n 'collapse=”' public_output.qmd` before
committing.

---

### Supported Output (`public_output.qmd`, `# Supported Output` section)

**Definition (redefined 2026-07-29, per Peter + Hunter):** for research
projects **ALERRT contributes financial support to but does not provide
any research support for** — no team member designs, conducts, or
co-authors the work. This is a narrower category than it started as; it
used to cover any team-member collaboration outside the Ring's mandate,
which is why an earlier entry (a Wooldredge et al. paper Tanksley
co-authored, and three preprints from projects Tanksley worked on at his
prior institution before joining ALERRT) got pulled once the definition
tightened. **A project must have been initiated while at ALERRT to
appear anywhere on this site** — work that started elsewhere and simply
lists an ALERRT affiliation because it hasn't published yet doesn't
qualify, regardless of topic.

Because ALERRT's role is purely financial, **it's normal — expected,
even — for zero authors to be bolded** on a Supported Output citation.
Don't force a bolded name if no author is actually ALERRT-affiliated;
check with Hunter's `alerrt_authors` field in `PROJ_alerrt_cv`'s
`alerrt_publications.yaml` if unsure whether a given author counts.

Deliberately bare-bones: a plain citation, not a promoted entry with a
summary like the main Publications list above it.

This section lives at the **bottom of `public_output.qmd`**, after all of
the Publications year sections, as its own `# Supported Output` heading
(a top-level entry in the page nav, same as the Publications years).
Within it, **each year is a real `## YEAR` heading** (so it's a real,
always-visible, clickable nav entry — not consumed as a callout title),
followed immediately by a **title-less collapsible box** holding that
year's citations. This is the opposite grouping from Publications, where
every individual article gets its own titled box — here, one box holds
*all* of a year's supported-output citations, and the box has no title of
its own since the heading right above it already says the year.

**Pattern (add new citations at the top, inside the correct year's box.
Start a new `## YEAR` heading + box, above the previous year, if the year
doesn't exist yet):**

```markdown
## YEAR

::: {#supported-YEAR .callout-note collapse="true"}
Last, F., Last, F. M., & Last, F. (YEAR). Title of the article, in
sentence case. *[Journal Name](https://doi.org/XXXXX){target="_blank"}*,
volume(issue), pages.
:::
```

Rules:
- **The year heading (`## YEAR`) goes outside/above the box**, not as the
  first line inside it — if it were the first line inside the
  `.callout-note` div, Quarto would consume it as the callout's title and
  it would stop being a real, nav-visible heading.
- **Bold only the ALERRT-affiliated author(s)**, if any, in the author
  list — every other author stays plain. If more than one author is an
  ALERRT team member, bold each of them. Since ALERRT's role here is
  purely financial, it's entirely normal for **no** author to be bolded.
- **The link goes on the italicized journal name**, with `target="_blank"`
  — not a separate "View the article" line like the main Publications
  pattern.
- **`collapse="true"` with straight quotes is required** on every year box
  — see the gotcha note above. This is what makes the section default to
  closed.
- The year box's anchor ID (`#supported-YEAR`) must be unique — there's
  only one per year, unlike `#pub-YEAR-slug` which is per-article.
- **Preprints**: use the preprint server/repository name in place of the
  journal name (e.g., "*[bioRxiv preprint](https://doi.org/XXXXX){target="_blank"}*"
  instead of a journal title), still italicized and linked the same way.
  No volume/issue/pages for a preprint.
- **Long author lists (more than ~4 authors)**: truncate to the first
  three authors, an ellipsis, then the final author — e.g., "First, A.,
  Second, B., & Third, C., … Last, Z. (YEAR)." If one of the truncated-out
  authors is the ALERRT-affiliated one, insert their bolded name in
  parentheses between the two ellipses instead of dropping them silently:
  "First, A., Second, B., & Third, C., … (**ALERRT Author, F.**), …
  Last, Z. (YEAR)." A modification of APA's own long-author-list
  convention, chosen to keep these bare-bones citations actually short
  even for large multi-author/consortium papers.
- No per-citation anchor ID, no summary paragraph — each entry is just a
  plain citation paragraph inside the year's box, blank line between
  multiple entries in the same year.
- Title is sentence case, not italicized. Journal name is italicized.

---

### Grants (`public_grants.qmd` + `_grants_ledger.yaml`)

**Adding a grant is always a two-file edit. Both files must be updated together:**

1. **`_grants_ledger.yaml`** — add an entry at the top with `id`, `name`, `funder`, `year`, `amount` (plain integer — no `$`, no commas), and `n_awards`. This is the authoritative source for the portfolio total; the stat block on the grants page is computed from it automatically. Never manually edit the hardcoded dollar total in `public_grants.qmd`. See `_grants_ledger.yaml` for full field documentation. Set `subaward: true` if ALERRT is not the prime awardee — subawards count toward the dollar total but not the award count.

2. **`public_grants.qmd`** — add the full narrative entry (pattern below). Current awards go under `## Current Awards`; past/completed awards go under `## Past Awards`.

**Pattern:**

```markdown
### Full Grant Title {#grant-slug-YEAR}

::: {.rr-grant-meta}
**Funder:** Funder Name &nbsp;·&nbsp; **Year:** YEAR &nbsp;·&nbsp; **Amount:** \$AMOUNT\
**PI:** First Last &nbsp;·&nbsp; **Co-PIs:** First Last, First Last
:::

#### Synopsis

Two to four sentences describing what the project is and why it matters. No jargon.

#### Deliverables

- Bullet list of publications, reports, or other outputs. Link to entries on other pages where they exist.

------------------------------------------------------------------------
```

Rules:
- The anchor ID (`#grant-slug-YEAR`) must match the `id` field in `_grants_ledger.yaml` exactly.
- The horizontal rule (`---`) separates entries — keep it between every grant.
- Omit **Co-PIs** line if there are none. Omit **Amount** if confidential or not yet awarded (but still add a ledger entry with `amount: 0`).
- Use `\$` to escape dollar signs in Quarto markdown.

---

### Media, News, and Announcements (`_media_entries.yaml`)

Add new entries at the **top** of the YAML list (newest first). The file header has full field documentation — read it before adding an entry.

**Minimum required fields:** `date`, `type`, `source`, `title`. Always add `id` too.

**Types:**
- `news` — third-party coverage citing ALERRT (newspaper, TV, web article)
- `podcast` — podcast episode or video interview
- `announcement` — internal news: new grant, award, conference presentation, milestone

**Minimal example (news):**

```yaml
- date: "2026-07-01"
  id: "lancet-reply-2026"
  type: news
  source: The Lancet Regional Health - Americas
  title: "ALERRT researchers respond to commentary on officer mortality study"
  url: "https://doi.org/10.1016/j.lana.XXXX"
  description: >
    One to three sentences. For news: cite ALERRT involvement and the research context.
```

**Announcement example (grant):**

```yaml
- date: "2026-07-01"
  id: "nida-r01-2026"
  type: announcement
  source: ALERRT Research Ring
  title: "NIDA R01 — Substance Use and Mortality among Law Enforcement"
  landing_title: "Peter and Hunter awarded NIDA R01 to study substance use and mortality in law enforcement"
  landing_url: "public_grants.html#grant-nida-r01-2026"
  description: >
    One to three sentences describing the grant and its significance.
```

Rules:
- Always add an `id` — without it, the landing page news strip links to the top of the media page instead of the specific entry.
- Dates must be ISO format: `YYYY-MM-DD`, in quotes.
- **Do not use `landing_url` for internal announcements** (grants, reports, conference appearances). The landing strip should always link to the media page announcement (`public_media.html#id`), which in turn cross-references the grant, report, or other item. This keeps the media page as the editorial record and ensures announcements are actually seen. Reserve `landing_url` only for entries that have no announcement body worth visiting — e.g., a bare news item where the external article IS the destination.

**Cross-referencing:** When a news or announcement entry relates to content that already exists on the site (a publication, report, grant, or in-progress project), link to it in the `description` field using a relative HTML path to the anchor. This drives traffic between pages and keeps things connected. Examples:
- Publication: `[Striking vs. Grappling](public_output.html#pub-2026-striking-grappling)`
- Grant: `[NIDA R01](public_grants.html#grant-nida-r01-2026)`
- Report: `[SIA door locks report](public_reports.html#report-sia-2026)`

**Naming convention for `landing_title` and `description`:**
- **Team members** (anyone listed on `public_staff.qmd`): use first name only. Example: "Hunter presents at ASEBP in DC."
- **External individuals**: use full name plus a brief identifier linking them to ALERRT. Example: "J.C. Barnes, co-author on ALERRT-led Lancet study, featured in Spectrum News piece on officer health." One clause is enough — don't over-explain.
- `landing_title` must mention at least one person and must stay under ~120 characters so it wraps cleanly on mobile.

---

## Render and Deploy Workflow

**After editing any content file, always render before committing.**

```bash
# Render the whole site (safe, ~60 seconds):
quarto render

# Faster: render only the pages you changed:
quarto render public_output.qmd
quarto render public_grants.qmd
quarto render index.qmd public_media.qmd   # always render both when editing _media_entries.yaml
```

**Then commit and push:**

```bash
git add -A
git commit -m "Add [what you added]"
git push
```

GitHub Pages picks up the `_site/` folder automatically on push. The site updates within ~1 minute.

**Never edit files inside `_site/` directly.** That folder is generated output — any direct changes will be overwritten on the next render.

**Don't modify `_render_media.R`** unless you are changing how the media page or news strip is generated (infrastructure, not content). For adding entries, `_media_entries.yaml` is the only file to touch.

---

## File Map (Quick Reference)

| What you want to add | File to edit |
|----------------------|--------------|
| Journal article | `public_output.qmd` |
| Book, book chapter, or report | `public_reports.qmd` |
| In-progress project | `public_in_progress.qmd` |
| Grant (current or past) | `public_grants.qmd` |
| News, podcast, announcement | `_media_entries.yaml` |
| Staff or collaborator | `public_staff.qmd` |
