#!/usr/bin/env python
"""
    Day 3
"""
import math
import sys
from pathlib import Path


def a2b(l):
    return sum(x * math.pow(2, i) for i, x in enumerate(reversed(l)))


def main():
    nl = 0
    with Path(sys.argv[1]).open() as f:
        totals = [int(x) for x in next(f).strip()]
        nl += 1
        for line in f:
            for i, x in enumerate(line.strip()):
                totals[i] += int(x)
            nl += 1

    final = [x // (nl / 2) for x in totals]
    print(final)
    gamma = a2b(final)
    epsilon = a2b([(x + 1) % 2 for x in final])
    print(f"gamma = {gamma} ; epsilon = {epsilon} ; power = {gamma*epsilon}")


if __name__ == "__main__":
    main()
