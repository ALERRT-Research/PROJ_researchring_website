# 2026-09-06 — OpenAlex API key exposure (external report)

**Status:** closed. Key rotated, live tree scrubbed, history rewrite declined.

## What happened

An outside reader of the public ALERRT GitHub emailed that
`scripts/openalex_lookup.py` and `scripts/openalex_doi_links.py` contained a hardcoded
OpenAlex API key and a contact email. Confirmed. Both values entered the repo in
commit `dfc5a50` (2026-05-04, "last major update before launch") and were public for
roughly four months. Neither script is part of the Quarto site build; the exposure was
limited to the two helper scripts. The key existed nowhere else on the local machine.

Risk, per the reporter and agreed: OpenAlex keys are free, but misuse of an exposed key
would be attributed to ALERRT.

## Response

1. Peter rotated the key at OpenAlex (2026-09-06). The old key is dead.
2. Both scripts now read `OPENALEX_API_KEY` and `OPENALEX_MAILTO` from the environment
   and exit with a clear message if either is unset. `.env`, `.Renviron`, and
   `__pycache__/` added to `.gitignore`. Commit `f2d2705`, pushed 2026-09-06.
3. History rewrite declined (Peter, 2026-09-06): the rotated key is dead, the content is
   not sensitive, and a force push on a shared repo is not worth the coordination cost.
   Commit `dfc5a50` remains in public history with the revoked key.
4. Open: thank-you reply to the reporter.

## Lessons

- Credentials go in the environment, never in a tracked file, even for "free" APIs and
  even in a repo that starts private. This one launched public with the key already in it.
- A secret scanner (gitleaks) as a pre-commit hook would have caught this. Not yet installed.
- Same habit spotted in `PROJ_allostasis_stress/code/2_census.R` (commented-out Census
  key, private repo). Fix when next touched.
