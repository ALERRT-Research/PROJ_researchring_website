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
last_updated: 2026-07-02
---

## Objectives

- Maintain the public-facing Research Ring website at alerrt.org/research (or equivalent custom domain)
- Keep publications, grants, media/news, staff, and in-progress project entries current
- Support Hunter in adding content without requiring Peter's involvement for routine updates

## Pending Content (Hunter's queue)

- [ ] Additional news announcements — confirm with Hunter what's still outstanding

## Workflow Notes

See `CLAUDE.md` for full instructions on adding each content type. Short version:

1. Edit the appropriate source file(s)
2. `quarto render` (or render only changed pages)
3. `git add -A && git commit -m "..." && git push`

GitHub Pages auto-deploys within ~1 minute of push.

## Recent Activity

- 2026-07-02: Major session — see details below
- 2026-05-19: SIA report announcement added; landing_url field added to media renderer
- 2026-05-12: All four team member headshots added; staff page fully populated

### 2026-07-02 Session Summary

**Content added:**
- Verified and merged Hunter's 5 new 2026 publications (SISMS, martial arts cadets, UoF integrative review, box breathing RCT, firefighter inflammation biomarkers)
- Added RGVRC grant entry (ERPO/firearm suicide, $49,999, Hunter PI / Peter Co-PI)
- Added ERPO grant announcement to media/news with RGVRC logo (borderless thumbnail)

**Infrastructure improvements:**
- `_grants_ledger.yaml` created — authoritative source for grant amounts; portfolio stat block on grants page now computed programmatically
- `CLAUDE.md` expanded with full content-editing guidelines (publications, grants, media, cross-referencing, naming conventions, render/deploy workflow)
- `.claude/settings.json` — PreToolUse hook blocks all `git push` attempts without explicit user approval; committed to repo so it applies to all teammates
- `.gitignore` updated to track `.claude/settings.json` while keeping local settings gitignored
- Landing strip navigation policy fixed: internal announcements now always link to media page (not directly to grant/report entries); `landing_url` reserved for bare external news only
- Borderless thumbnail support added (`thumb_borderless: true` YAML field + CSS class) for logo/transparent-bg images
- GitHub Pages deployment fixed: switched from quarto-actions publish to JamesIves deploy action pushing `_site/` directly to gh-pages branch; resolved `deployment_queued` timeout issue
- Fixed smart-quote encoding bug on 2011 "Reasonableness" article link
