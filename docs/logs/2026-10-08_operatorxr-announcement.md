# 2026-10-08 — OperatorXR visit announcement; announcement headline restyle

## What happened

- Added a `_media_entries.yaml` announcement (`operatorxr-visit-2026`) for the 2026-10-07
  OperatorXR visit: Curry Newton (VP of Sales) and Matt Moore (3D Artist and Customer
  Success Manager) trained Jessie Beck, the new Research Associate, on the VR kit. Two
  photos converted from iPhone HEIC to 1400px JPEG (`resources/media/operatorxr_visit_2026*.jpg`),
  matching the THRC entry's sizing.
- Restyled every announcement on the media page (`_render_media.R`, `styles.css`): the
  source/date line was bold and the title plain, so readers took the title for a run-on
  sentence. Now the source/date is a small muted uppercase eyebrow (`.rr-ann-meta`) and the
  title is a bold maroon block headline (`.rr-ann-title`). Also dropped the zero-padded day
  in announcement dates ("October 7", not "October 07"). News and podcast entries unchanged.

## Decisions

- Peter asked for plain sentences over stacked appositives in announcement bodies; external
  people's titles go in their own sentence rather than as parenthetical asides.
- Headlines stay in title case now that they are visually distinct.

## Verification

- `index.qmd` and `public_media.qmd` rendered separately; no `#| echo` leakage on either page.
- Landing strip's top item links to `public_media.html#operatorxr-visit-2026`; anchor present;
  both images copied to `_site/`; operatorxr.com returns 200.
- Headless Chrome screenshot of the media page checked: thumbnails still sit beside the text.
