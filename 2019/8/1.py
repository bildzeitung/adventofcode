#!/usr/bin/env python
"""
    Day 8
"""
import sys
from pathlib import Path

from collections import Counter


HEIGHT = 6
WIDTH = 25


def main():
    with Path(sys.argv[1]).open() as f:
        image = f.read().strip()

    print("Length:", len(image))
    chunk = WIDTH * HEIGHT
    sections = [image[i : i + chunk] for i in range(0, len(image), chunk)]
    c = [Counter(s) for s in sections]
    lowest = sorted(c, key=lambda x: x["0"])[0]
    print(lowest)
    print(sum(lowest.values()))
    print(lowest["1"] * lowest["2"])


if __name__ == "__main__":
    main()
