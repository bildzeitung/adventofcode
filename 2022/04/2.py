#!/usr/bin/env python
"""
    Day 4
"""
from pathlib import Path
import sys


def check(line):
    a, b = line.split(",")
    ar = [int(x) for x in a.split("-")]
    br = [int(x) for x in b.split("-")]

    # make the earliest range ar
    if br[0] < ar[0]:
        br, ar = ar, br

    # if ar's end is past the start of br, then they overlap
    return ar[1] >= br[0]


def main():
    with Path(sys.argv[1]).open() as f:
        print(f"Total: {sum(check(line.strip()) for line in f)}")


if __name__ == "__main__":
    main()
