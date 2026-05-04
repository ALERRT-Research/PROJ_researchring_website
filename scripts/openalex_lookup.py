#!/usr/bin/env python3
"""
OpenAlex journal lookup for Research Output page.

Scans public_output.qmd for callout entries missing a .rr-journal-label
div, queries OpenAlex by title, prints a review table, and writes
journal name + DOI link after user confirmation.

Usage:
    python3 scripts/openalex_lookup.py            # interactive
    python3 scripts/openalex_lookup.py --dry-run  # preview, no writes
"""

import re
import sys
import time
import unicodedata
from difflib import SequenceMatcher

try:
    import requests
except ImportError:
    sys.exit("Install requests first:  uv pip install requests")

# ── Config ────────────────────────────────────────────────────────────────────

QMD_PATH        = "public_output.qmd"
API_KEY         = "czQWdVxoRuiWUTT8l3mdV1"
EMAIL           = "ptt2@txstate.edu"
BASE_URL        = "https://api.openalex.org"
EXACT_THRESHOLD = 0.95   # score >= this → "ready"
FUZZY_THRESHOLD = 0.75   # score >= this → "verify"

# ── Normalization ─────────────────────────────────────────────────────────────

def normalize(text):
    """Lowercase, strip punctuation, collapse whitespace."""
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()

def similarity(a, b):
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()

# ── OpenAlex ──────────────────────────────────────────────────────────────────

NON_JOURNAL_TYPES = {"repository", "database", "ebook platform", "metadata"}

def search_openalex(title):
    params = {
        "search":   title,
        "per_page": 5,
        "select":   "id,title,doi,primary_location,locations,publication_year",
        "api_key":  API_KEY,
        "mailto":   EMAIL,
    }
    r = requests.get(f"{BASE_URL}/works", params=params, timeout=15)
    r.raise_for_status()
    return r.json().get("results", [])

def pick_best(title, results):
    best, best_score = None, 0.0
    for r in results:
        s = similarity(title, r.get("title") or "")
        if s > best_score:
            best, best_score = r, s
    return best, best_score

def extract_metadata(result):
    """
    Prefer a location whose source.type == 'journal' over repositories
    or databases. Falls back to primary_location if no journal source found.
    Returns (journal_name, doi, is_non_journal).
    """
    locations = result.get("locations") or []
    journal_sources = [
        (loc.get("source") or {})
        for loc in locations
        if (loc.get("source") or {}).get("type") == "journal"
    ]

    if journal_sources:
        source = journal_sources[0]
        is_non_journal = False
    else:
        source = (result.get("primary_location") or {}).get("source") or {}
        is_non_journal = source.get("type", "") in NON_JOURNAL_TYPES

    journal = source.get("display_name", "")
    doi     = result.get("doi") or ""
    return journal, doi, is_non_journal

def normalize_doi(doi):
    """Ensure DOI is a full https://doi.org/... URL."""
    if not doi:
        return ""
    doi = doi.strip()
    if doi.startswith("http"):
        return doi
    return f"https://doi.org/{doi.lstrip('/')}"

# ── QMD parsing ───────────────────────────────────────────────────────────────

LABEL_MARKERS = {"::: {.rr-journal-label}", "<!-- journal TK -->"}

def find_unlabeled(lines):
    """
    Walk lines looking for .callout-note blocks that have no label marker.
    Handles nested ::: blocks via depth tracking.

    Returns list of dicts:
        title           – article title string
        title_line_idx  – line index of the '## Title' line
    """
    targets = []
    i = 0

    while i < len(lines):
        if re.match(r'^:::\s*\{\.callout-note', lines[i]):
            depth          = 1
            title          = None
            title_line_idx = None
            has_label      = False
            j = i + 1

            while j < len(lines):
                stripped = lines[j].strip()

                # Inspect content BEFORE updating depth so that an opening
                # marker like '::: {.rr-journal-label}' is caught at depth==1
                if depth == 1:
                    m = re.match(r'^## (.+)$', lines[j])
                    if m and title is None:
                        title          = m.group(1).strip()
                        title_line_idx = j
                    if stripped in LABEL_MARKERS:
                        has_label = True

                # Update depth after content inspection
                if stripped.startswith(":::") and stripped != ":::":
                    depth += 1
                elif stripped == ":::":
                    depth -= 1
                    if depth == 0:
                        break

                j += 1

            if title and not has_label:
                targets.append({
                    "title":          title,
                    "title_line_idx": title_line_idx,
                })

            i = j + 1
        else:
            i += 1

    return targets

# ── Lookup loop ───────────────────────────────────────────────────────────────

def run_lookups(targets):
    results = []
    total   = len(targets)

    for idx, t in enumerate(targets, 1):
        sys.stdout.write(f"  [{idx}/{total}] {t['title'][:58]}...\r")
        sys.stdout.flush()

        try:
            oa_results    = search_openalex(t["title"])
            match, score  = pick_best(t["title"], oa_results)
        except Exception:
            match, score = None, 0.0

        entry = dict(t)

        if match and score >= EXACT_THRESHOLD:
            journal, doi, is_non_journal = extract_metadata(match)
            if is_non_journal:
                # Exact title match but source is a repo/database — needs check
                entry.update(status="verify", journal=journal,
                             doi=normalize_doi(doi), score=score,
                             oa_title=match.get("title", ""),
                             flag="non-journal source")
            else:
                entry.update(status="exact", journal=journal,
                             doi=normalize_doi(doi), score=score)

        elif match and score >= FUZZY_THRESHOLD:
            journal, doi, is_non_journal = extract_metadata(match)
            entry.update(status="verify", journal=journal,
                         doi=normalize_doi(doi), score=score,
                         oa_title=match.get("title", ""))
        else:
            entry.update(status="not_found", journal="", doi="", score=score)

        results.append(entry)
        time.sleep(0.12)  # polite pool ceiling is 10 req/s; stay well under

    sys.stdout.write(" " * 80 + "\r")
    return results

# ── Report ────────────────────────────────────────────────────────────────────

def print_report(results):
    W = 92
    print("\n" + "─" * W)
    print(f"  {'ARTICLE TITLE':<46} {'JOURNAL':<26} STATUS")
    print("─" * W)

    for r in results:
        t = r["title"]
        t = (t[:44] + "..") if len(t) > 46 else t

        j = r.get("journal", "")
        j = (j[:24] + "..") if len(j) > 26 else (j or "—")

        if r["status"] == "exact":
            status = "ready"
        elif r["status"] == "verify":
            flag = r.get("flag", "")
            if flag:
                status = f"[verify — {flag}]"
            else:
                status = f"[verify — score {r['score']:.2f}]"
        else:
            status = "[not found — placeholder]"

        print(f"  {t:<46} {j:<26} {status}")

    print("─" * W)
    n_ready  = sum(1 for r in results if r["status"] == "exact")
    n_verify = sum(1 for r in results if r["status"] == "verify")
    n_miss   = sum(1 for r in results if r["status"] == "not_found")
    print(f"\n  {n_ready} ready  ·  {n_verify} need verification  ·  {n_miss} not found\n")

    verify_entries = [r for r in results if r["status"] == "verify"]
    if verify_entries:
        print("  [verify] — OpenAlex returned a close but non-exact match:")
        for r in verify_entries:
            print(f"    Input : {r['title'][:70]}")
            print(f"    Match : {r.get('oa_title','')[:70]}")
            print()

# ── Writing ───────────────────────────────────────────────────────────────────

def build_label_lines(journal, doi):
    if doi:
        link = f'[{journal}]({doi}){{target="_blank"}}'
    else:
        link = journal
    return ["", "::: {.rr-journal-label}", link, ":::", ""]

def apply_insertions(lines, results):
    """
    Insert label blocks after each title line.
    Processes in reverse line order so earlier indices stay valid.
    """
    insertions = {}

    for r in results:
        idx = r["title_line_idx"]
        if r["status"] == "exact" and r.get("journal"):
            insertions[idx] = build_label_lines(r["journal"], r["doi"])
        else:
            insertions[idx] = ["", "<!-- journal TK -->", ""]

    new_lines = list(lines)
    for idx in sorted(insertions.keys(), reverse=True):
        insert_after = idx + 1
        for line in reversed(insertions[idx]):
            new_lines.insert(insert_after, line)

    return new_lines

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv

    with open(QMD_PATH) as f:
        content = f.read()

    lines   = content.splitlines()
    targets = find_unlabeled(lines)

    if not targets:
        print("Nothing to do — all entries already have a journal label.")
        return

    print(f"\nSearching OpenAlex for {len(targets)} unlabeled article(s)...")
    results = run_lookups(targets)
    print_report(results)

    if dry_run:
        print("Dry run — no changes written.")
        return

    answer = input("Write labels to public_output.qmd? [y/N] ").strip().lower()
    if answer != "y":
        print("Aborted — no changes written.")
        return

    new_lines   = apply_insertions(lines, results)
    new_content = "\n".join(new_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"

    with open(QMD_PATH, "w") as f:
        f.write(new_content)

    n_written = sum(
        1 for r in results
        if r["status"] == "exact" and r.get("journal")
    )
    print(f"\nDone — {n_written} label(s) written.")
    print(f"Re-render with:  quarto render {QMD_PATH}")

if __name__ == "__main__":
    main()
