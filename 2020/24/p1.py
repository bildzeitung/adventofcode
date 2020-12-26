#!/usr/bin/env python
"""
  Day 24
"""
import sys
from collections import defaultdict

DIRS = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1),
}

FLIP = {
    "W": "B",
    "B": "W",
}


def main():
    puzzle = defaultdict(lambda: "W")
    with open(sys.argv[1]) as f:
        for line in f:

            def getdirs():
                d = [x for x in line.strip()]
                while d:
                    x = d.pop(0)
                    if x in ("n", "s"):
                        x += d.pop(0)
                    yield x

            c = (0, 0)
            for d in getdirs():
                c = (c[0] + DIRS[d][0], c[1] + DIRS[d][1])
            puzzle[c] = FLIP[puzzle[c]]

    return [*puzzle.values()].count("B")


if __name__ == "__main__":
    print(main())
