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
    return (br[0] >= ar[0] and br[1] <= ar[1]) or (ar[0] >= br[0] and ar[1] <= br[1])


def main():
    with Path(sys.argv[1]).open() as f:
        print(f"Total: {sum(check(line.strip()) for line in f)}")


if __name__ == "__main__":
    main()
