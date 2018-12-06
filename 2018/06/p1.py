#!/usr/bin/env python
""" Day 6
"""
import sys
from collections import defaultdict
from pathlib import Path


def load_data():
    with Path(sys.argv[1]).open() as f:
        return {tuple([int(p.strip()) for p in line.split(",")]) for line in f}


def find_closest(x, y, data):
    """ Create a list of tuples: (point, manhattan distance)
        
        Sort the list by manhattan distance, then
        pick out the smallest.

        If the next smallest is the same as the smallest, then
        it's a shared point: return None

        Otherwise, return the point (not the distance)
    """
    hats = sorted(
        [(p, abs(p[0] - x) + abs(p[1] - y)) for p in data], key=lambda x: x[1]
    )

    # check for shared point (same distance between at least 2 points)
    if hats[0][1] == hats[1][1]:
        return

    return hats[0][0]


def main():
    data = load_data()

    # create a bounding box
    left, right = sorted([*zip(*data)][0])[:: len(data) - 1]
    top, bottom = sorted([*zip(*data)][1])[:: len(data) - 1]
    print(left, top, "->", right, bottom)

    infinibands = set()
    totals = defaultdict(int)
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            closest = find_closest(x, y, data)
            # every point on an edge will extend to infinity
            # so track which points extend out that far
            if x in (left, right) or y in (top, bottom):
                infinibands.add(closest)

            # keep track of each point -> size of area
            if closest:
                totals[closest] += 1

    print("TOTALS", totals)
    # remove all points that extend infinitly
    totals = {k: v for k, v in totals.items() if k not in infinibands}
    print("    RM", totals)
    # find the largest total, and that's the biggest area
    print("LARGEST AREA:", max(totals.values()))


if __name__ == "__main__":
    main()
