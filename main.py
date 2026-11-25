#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6 launch
week to /output/entry.txt. Pure standard library; no network, no input.

The line leans on a boring, specific, verifiable-sounding snag (a broken
lift, a floor number, an engineer who cannot come until tomorrow) and the
quiet punchline that the laptop is sitting on the office desk, so working
from home is off the table too. Short, hurried, no greeting beyond the
apology, no signature, no wild story.
"""

import os

EXCUSE = (
    "Sorry boss, the lift broke and I'm stuck on the 14th floor, "
    "engineer says tomorrow, laptop's at my desk."
)


def validate(text: str) -> str:
    """One line, 1-140 chars, at most 20 words, no newline."""
    text = text.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars"
    assert len(text.split()) <= 20, f"entry is {len(text.split())} words"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(EXCUSE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
