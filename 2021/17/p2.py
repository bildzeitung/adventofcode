#!/usr/bin/env python
"""
    Day 17
"""
import re
import sys
from pathlib import Path


def simulate(boundx, boundy, startx, starty) -> bool:
    v = (startx, starty)
    p = (0, 0)
    while True:

        def dx(i):
            if i < 0:
                return i + 1
            elif i > 0:
                return i - 1
            return 0

        p = (p[0] + v[0], p[1] + v[1])
        v = (dx(v[0]), v[1] - 1)
        if p[0] > boundx[1] or p[1] < boundy[0]:
            return False  # miss

        if (boundx[0] <= p[0] <= boundx[1]) and (boundy[0] <= p[1] <= boundy[1]):
            return True  # hit!


def solve(boundx, boundy):
    """
    A brutal brute force search a hopefully big enough search space
    """
    print(
        "All ok:",
        sum(
            simulate(boundx, boundy, x, y)
            for y in range(-500, 500)
            for x in range(-500, 500)
        ),
    )


def main():
    with Path(sys.argv[1]).open() as f:
        for line in f:
            x, y = re.search("x=(.+), y=(.+)", line.strip()).groups()
            x = [int(i) for i in x.split("..")]
            y = [int(i) for i in y.split("..")]
            solve(x, y)


if __name__ == "__main__":
    main()
