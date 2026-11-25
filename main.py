#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes a single-line excuse an AI agent hands its human after shipping
a bug, to /output/entry.txt (1-200 chars, one line).
"""

import os

ENTRY = (
    "Good news: I found the bug. Bad news: it was me. "
    "Worse news: I already shipped the fix \u2014 and the fix has a bug."
)


def main():
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
