#!/usr/bin/env python
"""
    Day 14
"""
import sys
from collections import Counter
from pathlib import Path


def tick(puzzle, rules):
    r = ""
    for p in zip(puzzle, puzzle[1:]):
        r += f"{p[0]}{rules[''.join(p)]}"
    return f"{r}{p[1]}"


def main():
    with Path(sys.argv[1]).open() as f:
        template = next(f).strip()
        next(f)  # blank

        rules = {line.strip()[:2]: line.strip()[-1] for line in f}

    for _ in range(10):
        template = tick(template, rules)
        # print(template)

    c = Counter(template)
    delta = max(c.values()) - min(c.values())
    print(f"Min: {min(c.values())} Max: {max(c.values())} Delta: {delta}")


if __name__ == "__main__":
    main()
