#!/usr/bin/env python
"""
  Advent 3
"""
import math
import sys


TO_CHECK = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def calc(grid, dx, dy):
    """ Walk down the maze

        Brute force; if the line is too short, double it
    """
    total = 0
    x, y = (0, 0)
    while y < len(grid):
        while x >= len(grid[y]):
            grid[y] += grid[y]
        total += grid[y][x] == "#"
        x += dx
        y += dy
    return total


def main():
    with open(sys.argv[1]) as f:
        grid = [x.strip() for x in f.readlines()]

    return math.prod(calc(grid, *t) for t in TO_CHECK)


if __name__ == "__main__":
    print(main())
