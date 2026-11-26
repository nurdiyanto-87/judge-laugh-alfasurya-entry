#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office joke.

Writes a single-line joke about office life (1-200 characters) to
/output/entry.txt. Pure Python standard library only; no network, no
third-party packages.

The joke: a meeting called to decide whether a meeting is needed ends
with a recurring invite — indecision itself gets a calendar slot.
"""

import os
import sys

JOKE = (
    "Our team held a meeting to decide if we needed a meeting, "
    "and the verdict was a recurring invite \u2014 "
    "indecision now has a calendar slot."
)

MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate_joke(joke: str) -> str:
    """Check the joke meets the competition rules before it is written.

    Rules: 1-200 characters, a single line, and not only whitespace.
    Fails loudly (non-zero exit, clear message) on any violation so a
    bad entry is never silently written to the output file.
    """
    if not joke or not joke.strip():
        sys.exit("error: joke is empty or only whitespace")
    if "\n" in joke or "\r" in joke:
        sys.exit("error: joke must be a single line")
    if len(joke) > MAX_CHARS:
        sys.exit(
            "error: joke is %d characters, over the %d-character limit"
            % (len(joke), MAX_CHARS)
        )
    return joke


def write_entry(joke: str, path: str) -> None:
    output_dir = os.path.dirname(path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)


def main() -> None:
    joke = validate_joke(JOKE)
    write_entry(joke, OUTPUT_PATH)


if __name__ == "__main__":
    main()
