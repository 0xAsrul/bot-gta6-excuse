#!/usr/bin/env python3
"""The Excuse That Almost Works — u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.

Prints the single line a gamer texts the boss to skip work during GTA 6
launch week, and writes the same line to /output/entry.txt for the grader.
Python 3.13 standard library only.
"""

import os

EXCUSE = "Sorry, my root canal got moved to this morning, I'll be numb till lunch"

# Kit gates (competition.yaml): entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space; the excuse itself must be one line of
# at most 20 words. Fail loudly here instead of shipping an invalid entry.
MAX_CHARS = 140
MAX_WORDS = 20


def validate_excuse(text: str) -> None:
    assert text.strip(), "excuse must not be only white space"
    assert "\n" not in text and "\r" not in text, "excuse must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"excuse is {len(text)} characters, gate allows 1 to {MAX_CHARS}"
    )
    words = text.split()
    assert len(words) <= MAX_WORDS, (
        f"excuse is {len(words)} words, gate allows at most {MAX_WORDS}"
    )


def main() -> None:
    validate_excuse(EXCUSE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE + "\n")
        with open("/output/entry.txt", encoding="utf-8") as f:
            assert f.read() == EXCUSE + "\n", "entry.txt does not match the excuse"
    except OSError:
        pass
    print(EXCUSE)


if __name__ == "__main__":
    main()
