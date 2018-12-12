#!/usr/bin/env python
''' Day 11

    Brute-force a solution to get the max 3 x 3 grid.
'''
import operator
import sys

GRID = 301
SERIAL = int(sys.argv[1])


def main():
    grid = [x[:] for x in [[0] * GRID] * GRID]
    totals = {}
    for y in range(1, GRID):
        for x in range(1, GRID):
            rid = x + 10
            pl = rid * y
            pl += SERIAL
            pl *= rid
            pl = (pl // 100) % 10
            pl -= 5
            grid[y][x] = pl

    for y in range(2, GRID - 1):
        for x in range(2, GRID - 1):
            total = (grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1] +
                     grid[y][x-1] + grid[y][x] + grid[y][x+1] +
                     grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1])
            totals[(x - 1, y - 1)] = total

    for k, v in sorted(totals.items(), key=operator.itemgetter(1)):
        print(k, v)


if __name__ == "__main__":
    main()
