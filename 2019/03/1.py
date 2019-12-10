#!/usr/bin/env python
"""
    Day 3
"""
import sys
from itertools import repeat
from pathlib import Path

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def main():
    with Path(sys.argv[1]).open() as f:

        def readpath():
            return [
                repeat(dirs[x[0]], int(x[1:])) for x in f.readline().strip().split(",")
            ]

        def drawpath(points):
            s = (0, 0)
            e = set()
            for i in points:
                for x in i:
                    s = (s[0] + x[0], s[1] + x[1])
                    e.add(s)
            return e

        e1 = drawpath(readpath())
        e2 = drawpath(readpath())

    m = [abs(x[0]) + abs(x[1]) for x in e1 & e2]
    print(min(m))


if __name__ == "__main__":
    main()
