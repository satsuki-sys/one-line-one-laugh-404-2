#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

LINE = "I taught my dog to fetch my slippers. Now he brings the neighbour's slippers, the neighbour's mail, and \u2014 yesterday \u2014 the neighbour."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
