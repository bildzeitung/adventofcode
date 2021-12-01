#!/usr/bin/env python
"""
    Day 1
"""
from pathlib import Path
import sys

def main():
    with Path(sys.argv[1]).open() as f:
        report = [int(x) for x in f]
    return sum(y > x for x,y in zip(report, report[1:]))


if __name__ == "__main__":
    print(main())