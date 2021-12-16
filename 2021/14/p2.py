#!/usr/bin/env python
"""
    Day 14
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path


def tick(puzzle: defaultdict, final: defaultdict, rules):
    tally = defaultdict(int)
    for k, v in puzzle.items():
        left = f"{k[0]}{rules[k]}"
        right = f"{rules[k]}{k[1]}"
        tally[left] += v
        tally[right] += v
        final[rules[k]] += v
    return tally


def main():
    tally = defaultdict(int)
    with Path(sys.argv[1]).open() as f:
        template = next(f).strip()
        next(f)  # blank

        rules = {line.strip()[:2]: line.strip()[-1] for line in f}

    for a, b in zip(template, template[1:]):
        tally[f"{a}{b}"] += 1

    final = defaultdict(int)
    for x in template:
        final[x] += 1

    for _ in range(40):
        tally = tick(tally, final, rules)

    delta = max(final.values()) - min(final.values())
    print(f"Min: {min(final.values())} Max: {max(final.values())} Delta: {delta}")


if __name__ == "__main__":
    main()
