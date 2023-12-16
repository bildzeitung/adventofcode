#!/usr/bin/env python
"""
    Day 9
"""
import sys
from pathlib import Path

from rich import print


def process_line(lst: list[int]) -> int:
    x = [x for x in lst]
    if all(i == 0 for i in x):
        return 0

    return x[-1] + process_line(y - x for x, y in zip(x, x[1:]))


def main():
    with Path(sys.argv[1]).open() as f:
        return sum(process_line(int(x) for x in line.strip().split()) for line in f)
        # for line in f:
        #    print(process_line(int(x) for x in line.strip().split()))


if __name__ == "__main__":
    print(main())
