---
project: Research Ring Website
type: website
status: active
priority: medium
importance: medium
path: /Users/PTT2/Documents/GitHub/PROJ_researchring_website
deadline: null
target: Ongoing — keep content current; add publications, grants, news as they occur
effort_remaining: as-needed
weekly_commitment: 1–2h
last_updated: 2026-07-20
blockers: null
blocking_others: null
---

## Objectives

- Maintain the public-facing Research Ring website at alerrt.org/research (or equivalent custom domain)
- Keep publications, grants, media/news, staff, and in-progress project entries current
- Support Hunter in adding content without requiring Peter's involvement for routine updates

## Pending Content (Hunter's queue)

- [ ] Additional news announcements — confirm with Hunter what's still outstanding
- [ ] Scholar stats pipeline integration — Hunter has an automated process that computes the collective publication/citation/h-index numbers on the Research page banner. Currently those three numbers are hardcoded in `public_research.qmd` and updated manually whenever Hunter reports a refresh (see 2026-07-01 and 2026-07-17 commits). Need to talk to Hunter about his pipeline's output format, then wire it in the same way `_grants_ledger.yaml` feeds the grants portfolio stat block — an authoritative data file his pipeline writes to, with the banner computed from it programmatically instead of copy-pasted. Until this lands, don't treat mismatches between the banner and a manual Scholar-profile spot-check as bugs — the pipeline is the source of truth, not individual profile pages.

## Recent Activity

- 2026-07-02: Merged Hunter's 5 new 2026 publications; added RGVRC grant + announcement entry; several infrastructure fixes (see git log / `CLAUDE.md` changelog for detail)
- 2026-05-19: SIA report announcement added; landing_url field added to media renderer
- 2026-05-12: All four team member headshots added; staff page fully populated

## Notes

Full content-editing and render/deploy workflow lives in `CLAUDE.md` — not duplicated here.
