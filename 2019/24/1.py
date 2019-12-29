#!/usr/bin/env python
"""
    Day 24
"""
import sys
from itertools import chain
from pathlib import Path


def step(grid):
    def mget(r, c):
        if r < 0 or c < 0:
            return 0
        if r > 4 or c > 4:
            return 0
        return grid[r][c]

    g = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    for row in range(5):
        for col in range(5):
            v = sum(
                [
                    mget(row - 1, col),
                    mget(row, col - 1),
                    mget(row, col + 1),
                    mget(row + 1, col),
                ]
            )
            if grid[row][col] and v == 1:
                g[row][col] = 1
            elif not grid[row][col] and 0 < v < 3:
                g[row][col] = 1

    return g


def draw(grid):
    for row in grid:
        print("".join(["#" if x else "." for x in row]))


def calc(grid):
    return sum(v << idx for idx, v in enumerate(chain.from_iterable(grid)))


def main():
    grid = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            grid.append([1 if x == "#" else 0 for x in line.strip()])
    states = set([calc(grid)])
    while True:
        grid = step(grid)
        if (c := calc(grid)) in states:
            print(f"Duplicate state: {c}")
            return
        else:
            states.add(c)


if __name__ == "__main__":
    main()
