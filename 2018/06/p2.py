#!/usr/bin/env python
""" Day 6
"""
import sys
from pathlib import Path

LIMIT = 10_000


def load_data():
    with Path(sys.argv[1]).open() as f:
        return {tuple([int(p.strip()) for p in line.split(",")]) for line in f}


def in_region(x, y, data):
    return sum(abs(p[0] - x) + abs(p[1] - y) for p in data) < LIMIT


def main():
    data = load_data()

    left, right = sorted([*zip(*data)][0])[::len(data)-1]
    top, bottom = sorted([*zip(*data)][1])[::len(data)-1]
    print(left, top, "->", right, bottom)

    ''' I can't prove this, but I'm going to assume that all points
        outside the bounding box will automatically be larger than
        the limit, so there's no need to extend the search area beyond
        the bounding box
    '''
    totals = 0
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            totals += in_region(x, y, data)

    print('TOTALS', totals)


if __name__ == "__main__":
    main()
