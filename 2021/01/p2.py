#!/usr/bin/env python
"""
    Day 1
"""
from functools import reduce
from pathlib import Path
import sys

def main():
    with Path(sys.argv[1]).open() as f:
        report = [int(x) for x in f]

    triples = [sum(x) for x in zip(report, report[1:], report[2:])]
    return sum(y > x for x,y in zip(triples, triples[1:]))


if __name__ == "__main__":
    print(main())