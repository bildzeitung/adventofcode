#!/bin/env python
"""
    Day 2

    Again, "handfuls" can be discarded, as the object is to collect
    the max values for each colour in each game, so the code really only
    needs to operate over (tally, colour) pairs.
    
"""
import sys
from math import prod
from pathlib import Path


def tally(l: str) -> bool:
    l = l.replace(";", "").replace(",", "").split(" ")
    i = iter(l)
    tot = {"blue": 0, "red": 0, "green": 0}
    for n in i:
        colour = next(i)
        tot[colour] = max(tot[colour], int(n))

    return prod(tot.values())


def main():
    with Path(sys.argv[1]).open() as f:
        return sum(tally(line.strip().split(":")[1].strip()) for line in f)


if __name__ == "__main__":
    print(main())
