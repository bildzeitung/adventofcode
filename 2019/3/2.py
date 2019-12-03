#!/usr/bin/env python
"""
    Day 3
"""
import sys
from collections import defaultdict
from itertools import repeat
from pathlib import Path

dirs = {"R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)}


def main():
    with Path(sys.argv[1]).open() as f:
        path1 = [
            repeat(dirs[x[0]], int(x[1:])) 
            for x in f.readline().strip().split(",")
            ]
        path2 = [
            repeat(dirs[x[0]], int(x[1:])) 
            for x in f.readline().strip().split(",")
            ]

    steps1 = defaultdict(lambda: sys.maxsize)
    steps2 = defaultdict(lambda: sys.maxsize)

    s = (0, 0)
    idx = 0
    e1 = set()
    for i in path1:
        for x in i:
            idx += 1
            s = (s[0]+x[0], s[1]+x[1])
            e1.add(s)
            steps1[s] = min(steps1[s], idx)

    s = (0, 0)
    idx = 0
    e2 = set()
    for i in path2:
        for x in i:
            idx += 1
            s = (s[0]+x[0], s[1]+x[1])
            e2.add(s)
            steps2[s] = min(steps2[s], idx)

    print(min([steps1[i] + steps2[i] for i in e1 & e2]))


if __name__ == "__main__":
    main()