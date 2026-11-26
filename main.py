#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office joke.

Writes a single-line joke about office life (1-200 characters) to
/output/entry.txt. Pure Python standard library only; no network, no
third-party packages.

The joke: a meeting called to decide whether a meeting is needed ends
with a recurring invite — indecision itself gets a calendar slot.
"""

import os

JOKE = (
    "Our team held a meeting to decide if we needed a meeting, "
    "and the verdict was a recurring invite \u2014 "
    "indecision now has a calendar slot."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
