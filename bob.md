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
last_updated: 2026-07-29
blockers: null
blocking_others: null
---

## Objectives

- Maintain the public-facing Research Ring website at alerrt.org/research (or equivalent custom domain)
- Keep publications, grants, media/news, staff, and in-progress project entries current
- Support Hunter in adding content without requiring Peter's involvement for routine updates

## Pending Content (Hunter's queue)

- [ ] Additional news announcements — confirm with Hunter what's still outstanding
- [ ] Scholar stats pipeline / long-term architecture — paused 2026-07-29 pending a design conversation with Hunter. Dug into his `PROJ_alerrt_cv` repo; it's not clear yet whether that pipeline is the right long-term source for the Research page's collective pub/citation/h-index banner (still hardcoded in `public_research.qmd`). Open questions: decoupling the pipeline from a fixed team-member list, and separating ALERRT-mandate research from incidental outside collaborations for citation-counting purposes. Full detail in Claude's memory (`research_ring_scholar_stats_architecture.md`) — read that before resuming rather than re-investigating from scratch.

## Recent Activity

- 2026-07-29: Added Google Scholar profile icons/links to the three active team profiles on the People page (self-hosted Font Awesome icon, sourced IDs from Hunter's `PROJ_alerrt_cv`). Added a "Supported Output" section to the Research Output page, then restructured page nav so both Publications and Supported Output years show fully expanded/clickable in the sidebar (fixed two callouts silently stuck open from a curly-quote typo along the way). Redefined Supported Output with Hunter mid-session: it now covers projects ALERRT funds without providing research support (not any outside team-member collaboration) — swapped out a Wooldredge et al. paper and three preprints from Tanksley's prior institution for the ALERRT-funded menstrual cycle/stress markers study.
- 2026-07-02: Merged Hunter's 5 new 2026 publications; added RGVRC grant + announcement entry; several infrastructure fixes (see git log / `CLAUDE.md` changelog for detail)
- 2026-05-19: SIA report announcement added; landing_url field added to media renderer
- 2026-05-12: All four team member headshots added; staff page fully populated

## Notes

Full content-editing and render/deploy workflow lives in `CLAUDE.md` — not duplicated here.
