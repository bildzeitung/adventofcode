#!/usr/bin/env python
"""
    Day 9
"""
import sys
from collections import deque
from math import prod
from pathlib import Path

from rich import print


def main():
    with Path(sys.argv[1]).open() as f:
        caves = []
        for l in f:
            caves.append([int(x) for x in l.strip()])

    def low_eval(x, y) -> bool:
        is_low = True

        def check(val, x, y):
            if not (-1 < x < len(caves[0])):
                return True

            if not (-1 < y < len(caves)):
                return True

            return val < caves[y][x]

        # left
        is_low = is_low and check(caves[y][x], x - 1, y)
        # right
        is_low = is_low and check(caves[y][x], x + 1, y)
        # up
        is_low = is_low and check(caves[y][x], x, y - 1)
        # down
        is_low = is_low and check(caves[y][x], x, y + 1)

        if is_low:
            print(f"({x}, {y}) => {caves[y][x]} is a low point")
        return is_low

    a_basin = set()

    def fill_basin(x, y):
        def can_skip(x, y):
            if not (-1 < x < len(caves[0])):
                return True

            if not (-1 < y < len(caves)):
                return True

            if caves[y][x] == 9:
                return True

            return (x, y) in a_basin

        q = deque()
        q.append((x, y))
        a_basin.add((x, y))
        size = 0
        while q:
            size += 1
            x, y = q.popleft()
            if not can_skip(x - 1, y):
                q.append((x - 1, y))
                a_basin.add((x - 1, y))
            if not can_skip(x + 1, y):
                q.append((x + 1, y))
                a_basin.add((x + 1, y))
            if not can_skip(x, y - 1):
                q.append((x, y - 1))
                a_basin.add((x, y - 1))
            if not can_skip(x, y + 1):
                q.append((x, y + 1))
                a_basin.add((x, y + 1))
        return size

    basin_sizes = []
    for r in range(len(caves)):
        for c in range(len(caves[0])):
            if (c, r) in a_basin:  # skip identified ones
                continue

            if caves[r][c] == 9:  # never a low
                continue

            if low_eval(c, r):
                basin_sizes.append(fill_basin(c, r))
    return basin_sizes


if __name__ == "__main__":
    basins = sorted(main())[-3::]
    print(f"Basins {basins} ==> {prod(basins)}")
