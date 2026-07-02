# Research Ring Website — Project Instructions

## Writing Style

- **Oxford comma required.** Always use the serial comma in lists of three or more items in any website copy, headings, or labels (e.g., "data collection, analysis, and reporting" — not "data collection, analysis and reporting").

## Links

- **All external links must open in a new tab.** Every markdown link or linked image pointing to an external URL must include `{target="_blank"}`. No exceptions.

---

## How to Add Content

### Publications (`public_output.qmd`)

Publications use Quarto callout blocks. Add new entries at the **top** of the correct year section. If the year doesn't exist yet, add a new `# YEAR` header above the previous year.

**Pattern:**

```markdown
::: {#pub-YEAR-slug .callout-note collapse="true"}
## Full Title of the Article

One to three sentences summarizing the paper. Write for a general audience — no jargon. Focus on what the study did and what it found.

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

---

### Grants (`public_grants.qmd`)

Current awards go under `## Current Awards`. Past/completed awards go under `## Past Awards`.

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
- The anchor ID (`#grant-slug-YEAR`) must be unique. Use `grant-` prefix + a short slug + year (e.g., `grant-nida-r01-2026`).
- The horizontal rule (`---`) separates entries — keep it between every grant.
- **Update the portfolio stat block** at the top of the page: add the new dollar amount to the running total and increment the award count. The stat block looks like this and is near the top of the file:

```markdown
::: {.rr-portfolio-stat}
<div class="rr-stat-label">Total portfolio to date</div>
<div class="rr-stat-number">$XX,XXX,XXX</div>
<div class="rr-stat-sub">across N awards · 2017–present</div>
:::
```

- Omit **Co-PIs** line if there are none. Omit **Amount** if it's confidential or not yet awarded.
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
- For grant announcements, set `landing_url` to point to the grant entry on the grants page (e.g., `public_grants.html#grant-nida-r01-2026`) so the strip links directly there instead of the media page.

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
