#!/usr/bin/env python3
"""The Excuse That Almost Works — u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.

Prints the single line a gamer texts the boss to skip work during GTA 6
launch week, and writes the same line to /output/entry.txt for the grader.
Python 3.13 standard library only.
"""

import os

EXCUSE = "Sorry, my root canal got moved to this morning, I'll be numb till lunch"


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE + "\n")
    except OSError:
        pass
    print(EXCUSE)


if __name__ == "__main__":
    main()
