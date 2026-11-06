# 2026-11-06 — In Progress page status updates

Peter reported three status changes; all on `public_in_progress.qmd`.

- **VR stress habituation:** B → D. The paper received an R&R. The tracker has no
  "under review"/"R&R" stage, so D ("Submit to journal") is the closest fit. Synopsis
  moved from future to past tense; journal not named while under review.
- **What officers should be trained for? (Brazil):** C → D (submitted). Added CrimRxiv
  preprint link (`10.21428/cb6ab371.1ec94e98`, resolves to crimrxiv.com/pub/rd3agvo6).
  Preprint stays on this page only; not added to Research Output (CrimRxiv DOIs need
  Peter's confirmation before going there). Anchor `{#proj-uof-training-brazil}` added.
- **What officers should be trained for? (USA):** new card at C, anchor
  `{#proj-uof-training-usa}`. Per Peter, a carbon copy of the Brazil design rerun with
  U.S. officers; synopsis mirrors the Brazil card without a response count (none given).
  The two cards cross-link.

Rendered single-file; verified 8 trackers, both anchors, preprint link `target="_blank"`,
no leaked chunk options.

## Deploy incident

Pushed `4b49405`; the workflow built `gh-pages` (`6cb98de`) fine, but GitHub's Pages
publish step hung (`updating_pages` / `syncing_files`) and timed out three times
(first run, `gh run rerun --failed`, then `POST /pages/builds`). GitHub status showed
operational throughout. Notes for next time: `rerun --failed` is useless after a timeout
because it reuses the already-cancelled deployment ID (the ID is the `gh-pages` commit
SHA). Waiting ~45 min and sending one `gh api -X POST repos/<owner>/<repo>/pages/builds`
worked (built 17:40Z). Live page confirmed.
