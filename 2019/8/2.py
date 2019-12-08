#!/usr/bin/env python
"""
    Day 8
"""
import sys
from pathlib import Path

from collections import Counter


def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    with Path(sys.argv[3]).open() as f:
        image = f.read().strip()

    chunk = width * height
    sections = [image[i : i + chunk] for i in range(0, len(image), chunk)]
    final = sections[-1]
    for s in reversed(sections[0 : len(sections) - 1]):
        f = []
        for i, v in enumerate(s):
            if v == "2":
                f.append(final[i])
            else:
                f.append(v)
        final = "".join(f)

    for i in range(0, len(final), width):
        print(final[i : i + width].replace("0", " "))


if __name__ == "__main__":
    main()
