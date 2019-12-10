#!/usr/bin/env python
"""
    Day 3
"""
import sys
from collections import defaultdict
from itertools import repeat
from pathlib import Path

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def main():
    with Path(sys.argv[1]).open() as f:

        def readpath():
            return [
                repeat(dirs[x[0]], int(x[1:])) for x in f.readline().strip().split(",")
            ]

        def calcsteps(points):
            s = (0, 0)
            idx = 0
            steps = defaultdict(lambda: sys.maxsize)
            for i in points:
                for x in i:
                    idx += 1
                    s = (s[0] + x[0], s[1] + x[1])
                    steps[s] = min(steps[s], idx)
            return steps

        steps1 = calcsteps(readpath())
        steps2 = calcsteps(readpath())

    print(min([steps1[i] + steps2[i] for i in steps1.keys() & steps2.keys()]))


if __name__ == "__main__":
    main()
