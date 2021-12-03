#!/usr/bin/env python
"""
    Day 3
"""
import math
from os import read
import sys
from copy import copy
from pathlib import Path


def a2b(l):
    return sum(x * math.pow(2, i) for i, x in enumerate(reversed(l)))


def calc(readings, adj):
    def grab_totals():
        totals = [0] * len(readings[0])
        for r in readings:
            for i, j in enumerate(r):
                totals[i] += j
    
        final = [(x // (len(readings)/2) + adj )%2 for x in totals]
        return final

    n = -1
    while (n := n + 1) < len(readings[0]):
        readings = [x for x in readings if x[n] == int(grab_totals()[n])]
        if len(readings) == 1:
            return readings[0]

    raise Exception("Oh, there's a problem here")


def main():
    inv_readings = []
    with Path(sys.argv[1]).open() as f:
        readings = [[int(y) for y in x] for x in [l.strip() for l in f]]

    oxygen_generator = a2b(calc(copy(readings), 0))
    co2_scrubber = a2b(calc(copy(readings), 1))

    print(f"O2 gen = {oxygen_generator} CO2 = {co2_scrubber}")
    return oxygen_generator * co2_scrubber


if __name__ == "__main__":
    print(main())
