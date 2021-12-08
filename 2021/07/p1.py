#!/usr/bin/env python
"""
    Day 7

    it *is* the median, I believe

    But, a linear search seems to be enough.
    Fortunately, no local minima
"""
import sys
from pathlib import Path


def main():
    with Path(sys.argv[1]).open() as f:
        crabs = sorted(int(x) for x in next(f).strip().split(","))

    def residuals(x):
        return sum(abs(x - c) for c in crabs)

    r = residuals(min(crabs))
    print(r)
    for x in range(min(crabs) + 1, max(crabs)):
        nr = residuals(x)
        print(nr)
        if nr > r:
            print("-->", x - 1, r)
            return r
        r = nr

    # print(min(residuals(x) for x in range(min(crabs), max(crabs))))


if __name__ == "__main__":
    main()
