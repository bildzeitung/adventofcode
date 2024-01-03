#!/usr/bin/env python
"""
    Day 11

    This is one of those days where both parts of the problem can be made
    into the same program. EXPANSION == 2 for part 1.
    
"""
import sys
from itertools import combinations
from pathlib import Path
from typing import List

from rich import print

EXPANSION = 1_000_000


def apsp(galaxies: List[int]) -> int:
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(galaxies, 2))


def main():
    puzzle = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            puzzle.append([*line.strip()])

    pivot = [[r[i] for r in puzzle] for i in range(len(puzzle[0]))]

    empty_rows = [idx for idx, r in enumerate(puzzle) if "#" not in r]
    empty_cols = [idx for idx, r in enumerate(pivot) if "#" not in r]

    print(f"Empty rows: {empty_rows}  Empty cols: {empty_cols}")

    galaxies = []
    y_offset = 0
    for ridx, rows in enumerate(puzzle):
        if ridx in empty_rows:
            y_offset += EXPANSION - 1

        x_offset = 0
        for idx, col in enumerate(rows):
            if idx in empty_cols:
                x_offset += EXPANSION - 1
            if col == "#":
                galaxies.append((idx + x_offset, ridx + y_offset))

    return sum(x for x in apsp(galaxies))


if __name__ == "__main__":
    print(main())
