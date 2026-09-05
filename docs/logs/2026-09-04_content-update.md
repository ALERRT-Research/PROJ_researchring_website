# 2026-09-04 — Content update: two accepted papers, LCAN added to In Progress

**Trigger.** Peter, via `/bob update research ring`: the Brazil gun-ownership paper is accepted, the correctional officer mortality paper is accepted at AJPH, and LCAN needs to appear on the In Progress page at the earliest stage.

## Research Output (`public_output.qmd`)

Two entries added at the top of `## 2026`, both "Article forthcoming." (no DOI yet):

- `#pub-2026-correctional-officer-mortality` — "Correctional Officer Mortality in the United States, 2020–2023." Journal label: American Journal of Public Health (accepted 2026-09-02; see `PROJ_noms_co_cod/bob.md`). Summary written from the manuscript abstract and discussion.
- `#pub-2026-brazil-gun-ownership` — "Legal Gun Ownership and Carrying Are Not Associated With Homicides in Brazil." Summary written from the CrimRxiv preprint (doi 10.21428/cb6ab371.b1300c2c, 27 states, 2013–2023). Journal: International Journal of Comparative and Applied Criminal Justice (Peter, 2026-09-04).

Pattern followed per `CLAUDE.md`: straight-quoted `collapse="true"`, no author list, preprint link carries `target="_blank"`. Verified in the render that both callouts are collapsed and the anchors resolve.

## In Progress (`public_in_progress.qmd`)

- Removed "Legal gun ownership and homicides in Brazil" (was stage D). Its synopsis and preprint link now live in the Research Output entry above.
- Added "Measuring the Quality of LCAN Situation Reports in Active Attack Response" at stage A (Formal analysis plan), placed first. Synopsis written from `PROJ_lcan/docs/idea_brief.md`; kept deliberately general because the 2026-09-01 redirection with Hunter has not yet been scoped (session set for 2026-09-09). Revisit the synopsis after that session.

## Render

`quarto render public_output.qmd` and `quarto render public_in_progress.qmd` run separately (quarto takes one input per call; passing two silently renders only the first). Both succeeded. Not committed, not pushed.

## bob.md

Also this session: dropped the "outstanding news announcements" item (Peter: dead); Scholar-stats pipeline confirmed still live.

## Addendum (same session): LCAN card rewritten after the redirection scoping

Peter scoped the LCAN redirection in this session rather than waiting for 09-09. The card is now "Training Officers to Give Better LCAN Reports" — a within-course randomized training experiment scored on Core-4 completeness — still at stage A. The measurement-first synopsis written earlier in the session never left the working tree. Full redirection record: `PROJ_lcan/docs/logs/2026-09-04_redirection-scoping.md`.

## Outcome

Committed as `5743705` and pushed to `main` on Peter's explicit approval (2026-09-04, ~15:20). Working tree clean. Follow-ups carried in bob.md: swap in the AJPH DOI for the correctional officer paper, and link the Brazil paper once it appears online. LCAN card revisit after the 2026-09-09 design session.
