#!/usr/bin/env python3
"""Update content/publications/ from Google Scholar.

Uses the scholar-collector submodule, but with this site's own profile.
The submodule's collect_publications.py hard-codes the original author's
Scholar URL and bolds their name, so we call its utilities directly instead.

Requires Python 3.12+ (the submodule uses backslashes inside f-strings)
and `pip install scholarly numpy`.
"""
import os
import re
import sys

SCHOLAR_URL = "https://scholar.google.com/citations?user=hjrZh74AAAAJ&hl"
AUTHOR_NAMES = ("Baofu Han", "Han Baofu")  # bolded in the author list
OUT_DIR = "content/publications/"
SUBMODULE = ".submodule/scholar-collector"

sys.path.insert(0, os.path.abspath(SUBMODULE))
from utilities import fetch_publications, add_missing_publications  # noqa: E402


def bold_own_name(path):
    """The submodule bolds a hard-coded name; fix the author line afterwards."""
    for root, _, files in os.walk(path):
        for f in files:
            if f != "index.md":
                continue
            fp = os.path.join(root, f)
            txt = open(fp, encoding="utf-8").read()

            def fix(m):
                line = m.group(0)
                for name in AUTHOR_NAMES:
                    line = line.replace(f'"{name}"', f'"**{name}**"')
                return line

            new = re.sub(r"^authors:.*$", fix, txt, flags=re.M)
            if new != txt:
                open(fp, "w", encoding="utf-8").write(new)


def main():
    if not os.path.isdir(SUBMODULE):
        sys.exit(f"{SUBMODULE} missing - run: git submodule update --init")
    pubs = fetch_publications(SCHOLAR_URL, verbose=True)
    if not pubs:
        sys.exit("No publications fetched (Google Scholar may be rate-limiting).")
    # Only creates folders that do not exist yet; existing entries are left alone.
    add_missing_publications(pubs, OUT_DIR, AUTHOR_NAMES[0], verbose=True)
    bold_own_name(OUT_DIR)


if __name__ == "__main__":
    main()
