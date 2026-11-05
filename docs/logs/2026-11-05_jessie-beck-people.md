# 2026-11-05 — Jessie Beck added to People page

- Added Jessie Beck (Research Associate, started 2026-10-05) to `public_staff.qmd` after Joe, same
  layout as the other three. Bio and fun facts are Jessie's own text from her `ALERRT Bio.pdf`;
  only edits were lowercasing the degree field and italicizing the journal name to match house style.
- No Google Scholar icon: she didn't supply a profile. Add one to her heading if she creates one.
- Headshot `resources/headshots/headshot_beck.jpg`: her original (1024x1535) was framed loosely,
  so her face read small in the hex next to the others. Cropped to 760x878 (offset y=170, x=132),
  matching the hex aspect; no `object-position` override needed.
- Verified: `quarto render public_staff.qmd`, headless-Chrome screenshot; framing matches the other
  three; nav entry present.
