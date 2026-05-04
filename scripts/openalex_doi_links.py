#!/usr/bin/env python3
"""
Switch article button links from local PDF paths to DOI URLs.

Scans public_output.qmd for button links still pointing to local PDFs,
searches OpenAlex by title to get the DOI, and updates after confirmation.
Entries with no DOI found keep the local PDF as fallback.

Usage:
    python3 scripts/openalex_doi_links.py            # interactive
    python3 scripts/openalex_doi_links.py --dry-run
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
MATCH_THRESHOLD = 0.75

# ── Helpers ───────────────────────────────────────────────────────────────────

def normalize(text):
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()

def similarity(a, b):
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()

def normalize_doi(doi):
    if not doi:
        return ""
    doi = doi.strip()
    return doi if doi.startswith("http") else f"https://doi.org/{doi.lstrip('/')}"

def search_openalex(title):
    params = {
        "search":   title,
        "per_page": 5,
        "select":   "id,title,doi,publication_year",
        "api_key":  API_KEY,
        "mailto":   EMAIL,
    }
    r = requests.get(f"{BASE_URL}/works", params=params, timeout=15)
    r.raise_for_status()
    return r.json().get("results", [])

def best_doi(title, results):
    best, best_score = None, 0.0
    for r in results:
        s = similarity(title, r.get("title") or "")
        if s > best_score:
            best, best_score = r, s
    if best and best_score >= MATCH_THRESHOLD:
        return normalize_doi(best.get("doi") or ""), best_score
    return "", best_score

# ── Parse targets ─────────────────────────────────────────────────────────────

LOCAL_PDF_RE = re.compile(
    r'\[View the article here\.\]\((resources/articles/[^)]+)\)'
    r'(\{\.rr-article-pdf[^}]*\})'
)

def find_targets(lines):
    """
    Return list of dicts for entries whose button still points to a local PDF:
        title          – article title
        title_line_idx – line index of '## Title'
        pdf_line_idx   – line index of the button link
        pdf_path       – current local path
        attrs          – link attribute string
    """
    targets = []
    i = 0

    while i < len(lines):
        if re.match(r'^:::\s*\{\.callout-note', lines[i]):
            depth = 1
            title = title_line_idx = None
            j = i + 1

            while j < len(lines):
                stripped = lines[j].strip()

                if depth == 1:
                    m = re.match(r'^## (.+)$', lines[j])
                    if m and title is None:
                        title = m.group(1).strip()
                        title_line_idx = j
                    pm = LOCAL_PDF_RE.search(lines[j])
                    if pm and title:
                        targets.append({
                            "title":          title,
                            "title_line_idx": title_line_idx,
                            "pdf_line_idx":   j,
                            "pdf_path":       pm.group(1),
                            "attrs":          pm.group(2),
                        })

                if stripped.startswith(":::") and stripped != ":::":
                    depth += 1
                elif stripped == ":::":
                    depth -= 1
                    if depth == 0:
                        break

                j += 1

            i = j + 1
        else:
            i += 1

    return targets

# ── Lookup ────────────────────────────────────────────────────────────────────

def run_lookups(targets):
    results = []
    total = len(targets)

    for idx, t in enumerate(targets, 1):
        sys.stdout.write(f"  [{idx}/{total}] {t['title'][:58]}...\r")
        sys.stdout.flush()

        try:
            oa_results    = search_openalex(t["title"])
            doi, score    = best_doi(t["title"], oa_results)
        except Exception:
            doi, score = "", 0.0

        entry = dict(t)
        entry["doi"]   = doi
        entry["score"] = score
        entry["status"] = "doi_found" if doi else "no_doi"
        results.append(entry)
        time.sleep(0.12)

    sys.stdout.write(" " * 80 + "\r")
    return results

# ── Report ────────────────────────────────────────────────────────────────────

def print_report(results):
    W = 92
    print("\n" + "─" * W)
    print(f"  {'ARTICLE TITLE':<46} {'DOI':<36} STATUS")
    print("─" * W)

    for r in results:
        t   = r["title"]
        t   = (t[:44] + "..") if len(t) > 46 else t
        doi = r["doi"]
        doi_disp = (doi[8:44] + "..") if len(doi) > 46 else doi[8:] if doi else "—"
        status = "ready" if r["status"] == "doi_found" else "[no DOI — keep PDF]"
        print(f"  {t:<46} {doi_disp:<36} {status}")

    print("─" * W)
    n_ready = sum(1 for r in results if r["status"] == "doi_found")
    n_keep  = sum(1 for r in results if r["status"] == "no_doi")
    print(f"\n  {n_ready} switching to DOI  ·  {n_keep} keeping local PDF\n")

# ── Apply ─────────────────────────────────────────────────────────────────────

def apply_updates(lines, results):
    new_lines = list(lines)
    for r in sorted(results, key=lambda x: x["pdf_line_idx"], reverse=True):
        if r["status"] != "doi_found":
            continue
        idx  = r["pdf_line_idx"]
        line = new_lines[idx]
        new_link = f'[View the article here.]({r["doi"]}){r["attrs"]}'
        new_lines[idx] = LOCAL_PDF_RE.sub(new_link, line)
    return new_lines

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv

    with open(QMD_PATH) as f:
        content = f.read()
    lines = content.splitlines()

    targets = find_targets(lines)
    if not targets:
        print("No local PDF links found — nothing to update.")
        return

    print(f"\nFetching DOIs from OpenAlex for {len(targets)} article(s)...")
    results = run_lookups(targets)
    print_report(results)

    if dry_run:
        print("Dry run — no changes written.")
        return

    answer = input("Update links in public_output.qmd? [y/N] ").strip().lower()
    if answer != "y":
        print("Aborted.")
        return

    new_lines   = apply_updates(lines, results)
    new_content = "\n".join(new_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"

    with open(QMD_PATH, "w") as f:
        f.write(new_content)

    n = sum(1 for r in results if r["status"] == "doi_found")
    print(f"\nDone — {n} link(s) updated to DOI URLs.")
    print(f"Re-render with:  quarto render {QMD_PATH}")

if __name__ == "__main__":
    main()
