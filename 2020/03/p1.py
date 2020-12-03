#!/usr/bin/env python
"""
  Advent 3
"""
import sys


def main():
    """ Walk down the maze

        Brute force; if the line is too short, double it
    """
    with open(sys.argv[1]) as f:
        grid = [x.strip() for x in f.readlines()]

    print(grid)
    total = 0
    x, y = (0, 0)
    while y < len(grid):
        print(x, y, len(grid[y]))
        while x > len(grid[y]):
            grid[y] += grid[y]
        total += grid[y][x] == "#"
        x += 3
        y += 1
    return total


if __name__ == "__main__":
    print(main())
