#!/usr/bin/env python
"""
    Day 1
"""
from pathlib import Path
import sys

def main():
    with Path(sys.argv[1]).open() as f:
        report = [int(x) for x in f]
    report = sum(y > x for x,y in zip(report, report[1:]))
    print(report)


if __name__ == "__main__":
    main()