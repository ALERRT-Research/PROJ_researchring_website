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
last_updated: 2026-09-28
blockers: null
blocking_others: null
---

## Objectives

- Maintain the public-facing Research Ring website at alerrt.org/research (or equivalent custom domain)
- Keep publications, grants, media/news, staff, and in-progress project entries current
- Support Hunter in adding content without requiring Peter's involvement for routine updates

## Team & Dependencies

| Name | Role | Affiliation | Waiting on Peter? |
|------|------|-------------|-------------------|
| Hunter Martaindale | Co-maintainer, content source, push approver | ALERRT / Texas State | No |

## This Week

- Install gitleaks as a pre-commit hook (not installed; no hook in `.git/hooks`)
- Decision for Peter: the Scholar-stats design conversation with Hunter has been unscheduled since 2026-07-29 — schedule it, or shelve the pipeline and accept the hardcoded banner
- LCAN In Progress card: confirm it still matches the design fixed 2026-09-09 (first course Nov 2026)

## Upcoming Milestones

- ~Dec 2026 (AJPH First Look): replace "Article forthcoming." on the correctional officer mortality entry with the AJPH DOI — trigger is `PROJ_noms_co_cod` production
- When the Brazil gun-ownership paper appears online at IJCACJ: replace its "Article forthcoming." with the article link

## Start Here Next Session

- Check `git log` for anything Hunter pushed since 2026-09-28 (none between 09-04 and 09-28; tree clean, `main` matches `origin/main`).
- Scholar-stats question: read `~/.claude/projects/-Users-PTT2--claude/memory/research_ring_scholar_stats_architecture.md` (2026-07-29) and `docs/logs/2026-09-04_bob-prune.md` before resuming. Do not re-investigate `PROJ_alerrt_cv` from scratch.
- Key-exposure record and open items: `docs/logs/2026-09-06_openalex-key-exposure.md`.
- Content-editing and render/deploy procedure: `CLAUDE.md`. Push requires separate explicit approval from Peter or Hunter.

## Notes

- Scholar-stats banner on the Research page is hardcoded; a pipeline sourced from Hunter's `PROJ_alerrt_cv` is a candidate but unresolved pending a design conversation with Hunter. Open questions in the memory file and `docs/logs/2026-09-04_bob-prune.md` (see Start Here).
- Credentials never go in tracked files (convention in `CLAUDE.md`, added 2026-09-06 after an outside reader found a hardcoded OpenAlex key; key rotated, live tree scrubbed, history rewrite declined). Same habit exists in `PROJ_allostasis_stress/code/2_census.R` — fix when that project is next touched.
- Supported Output = projects ALERRT funds without providing research support, not outside team-member collaborations (settled with Hunter 2026-07-29).
- History: `DEVLOG.md` covers build-out through 2026-05-19; `docs/logs/` from 2026-09-04 onward. Conventions live in `CLAUDE.md`, not here.

<!-- Budget: ≤ 150 lines total. History lives in docs/logs/, conventions in CLAUDE.md. -->
