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
last_updated: 2026-09-04
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

- Commit and push the 2026-09-04 content update once Peter approves
- When the AJPH DOI for the correctional officer mortality paper arrives, replace "Article forthcoming." with the article link
- Scholar-stats pipeline: still live (confirmed 2026-09-04). Schedule the design conversation with Hunter; banner in `public_research.qmd` stays hardcoded until then

## Upcoming Milestones

- none — content-driven; no fixed dates

## Start Here Next Session

- Check `git log` for anything Hunter pushed since 2026-09-04. Uncommitted work from 2026-09-04 (two Research Output entries, LCAN added to In Progress, Brazil paper removed) is in `docs/logs/2026-09-04_content-update.md`.
- If resuming the Scholar-stats question: read `docs/logs/2026-09-04_bob-prune.md` first — it holds the open design questions. Do not re-investigate `PROJ_alerrt_cv` from scratch.
- Content-editing and render/deploy procedure: `CLAUDE.md`. Push requires separate explicit approval from Peter or Hunter.

## Notes

- Scholar-stats banner on the Research page is hardcoded; a pipeline sourced from Hunter's `PROJ_alerrt_cv` is a candidate but unresolved — reasoning in `docs/logs/2026-09-04_bob-prune.md`. (The Claude memory file the earlier note pointed at does not exist on this machine; the log is now the only record.)
- Supported Output = projects ALERRT funds without providing research support, not outside team-member collaborations (settled with Hunter 2026-07-29).
- History: `DEVLOG.md` covers build-out through 2026-05-19; `docs/logs/` from 2026-09-04 onward. Conventions live in `CLAUDE.md`, not here.

<!-- Budget: ≤ 150 lines total. History lives in docs/logs/, conventions in CLAUDE.md. -->
