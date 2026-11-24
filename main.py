#!/usr/bin/env python3
"""One Word From Your Ex - writes the single word an ex would use.

The word is "project": the ex's verdict, flat and final. Not a partner,
a project - something to fix, renovate, and eventually walk away from
halfway through. One word, lowercase, like a text message with no
punctuation left to give.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Exits non-zero unless the text is exactly one word
and 1-30 characters long.
"""

import os
import sys

WORD = "project"
MAX_CHARS = 30


def main():
    word = WORD.strip()
    if not word or len(word.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    if not 1 <= len(word) <= MAX_CHARS:
        print("entry must be 1-30 characters", file=sys.stderr)
        return 1
    if "\n" in word or "\r" in word:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
