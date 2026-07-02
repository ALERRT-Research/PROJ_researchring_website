---
project: Research Ring Website
type: website
status: active
priority: medium
path: /Users/PTT2/Documents/GitHub/PROJ_researchring_website
deadline: null
target: Ongoing — keep content current; add publications, grants, news as they occur
effort_remaining: as-needed
weekly_commitment: 1–2h
last_updated: 2026-07-02
blockers: null
blocking_others: null
---

## Objectives

- Maintain the public-facing Research Ring website at alerrt.org/research (or equivalent custom domain)
- Keep publications, grants, media/news, staff, and in-progress project entries current
- Support Hunter in adding content without requiring Peter's involvement for routine updates

## Pending Content (Hunter's queue)

Items Hunter has identified as needing to be added — work through these in a single session:

- [ ] New publications (list TBD — confirm with Hunter)
- [ ] News announcements (list TBD — confirm with Hunter)
- [ ] New grant entry (list TBD — confirm with Hunter)

## Workflow Notes

See `CLAUDE.md` for full instructions on adding each content type. Short version:

1. Edit the appropriate source file(s)
2. `quarto render` (or render only changed pages)
3. `git add -A && git commit -m "..." && git push`

GitHub Pages auto-deploys within ~1 minute of push.

## Recent Activity

- 2026-07-02: Registered with bob; content-editing guidelines added to CLAUDE.md
- 2026-05-19: SIA report announcement added; landing_url field added to media renderer
- 2026-05-12: All four team member headshots added; staff page fully populated
