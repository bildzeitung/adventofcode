#!/usr/bin/env python
"""
    Day 6
"""
import sys
from math import ceil, prod
from pathlib import Path

from rich import print


def do_race(t: int, d: int) -> int:
    x = ceil(t / 2)
    count = 0
    while x * (t - x) > d:
        count += 1
        x += 1

    return 2 * count - (1 if ceil(t / 2) == t // 2 else 0)


def main():
    times = []
    dists = []
    with Path(sys.argv[1]).open() as f:
        times = [int(x) for x in next(f).split(":")[1].split()]
        dists = [int(x) for x in next(f).split(":")[1].split()]

    return prod(do_race(t, d) for (t, d) in zip(times, dists))


if __name__ == "__main__":
    print(main())
