#!/usr/bin/env python
"""
    Day 7
"""
import functools
import sys
from pathlib import Path


@functools.cache
def gauss(n):
    return (n * (n + 1)) / 2


def main():
    with Path(sys.argv[1]).open() as f:
        crabs = sorted(int(x) for x in next(f).strip().split(","))

    def residuals(x):
        return sum(gauss(abs(x - c)) for c in crabs)

    r = residuals(min(crabs))
    for x in range(min(crabs) + 1, max(crabs)):
        nr = residuals(x)
        if nr > r:
            print("-->", x - 1, r)
            return r
        r = nr


if __name__ == "__main__":
    main()
