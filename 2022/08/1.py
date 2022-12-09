#!/usr/bin/env python
"""
    Day 8
"""
import sys
from pathlib import Path
from rich import print


def visibleRightwards(l) -> int:
    m = -1
    v = set()
    for x, i in enumerate(l):
        if i > m:
            m = i
            v.add(x)
    return v


def main():
    grid = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])

    lx = len(grid[0])
    ly = len(grid)

    all_v = []

    for y, r in enumerate(grid):
        all_v += [(x, y) for x in visibleRightwards(r)]  # rightwards
        all_v += [(lx - x - 1, y) for x in visibleRightwards(reversed(r))]  # leftwards

    for x in range(lx):
        col = [c[x] for c in grid]
        all_v += [(x, yy) for yy in visibleRightwards(col)]  # down
        all_v += [(x, ly - yy - 1) for yy in visibleRightwards(reversed(col))]  # up

    print(f"All: {len(all_v)}  Set: {len(set(all_v))}")


if __name__ == "__main__":
    main()
