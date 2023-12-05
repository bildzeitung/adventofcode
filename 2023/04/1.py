#!/usr/bin/env python
"""
    Day 4
"""
import math
import sys
from pathlib import Path


def main():
    sum = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            line = line.strip()
            winners, have = [x.strip() for x in line.split(":")[1].split("|")]
            winners = [int(x) for x in winners.split()]
            have = [int(x) for x in have.split()]
            assert len(winners) == len(set(winners))
            assert len(have) == len(set(have))
            common = len(set(winners) & set(have))
            if common:
                print(winners, have, common, math.pow(2, max(0, common - 1)))
                sum += math.pow(2, max(0, common - 1))
    return sum


if __name__ == "__main__":
    print(main())
