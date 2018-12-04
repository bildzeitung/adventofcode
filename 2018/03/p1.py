#!/usr/bin/env python
""" Day 3

    Brute force mark an array to determine overlaps

"""
import re
import sys
from pathlib import Path

CLAIM_RE = re.compile(r".+@ (\d+),(\d+): (\d+)x(\d+)")
ARRAY = 1000

master = []


def process_claim(l, t, w, h):
    """ Loop through the rectangle and light up squares in the matrix
    """
    for i in range(w):
        for j in range(h):
            master[t + j][l + i] += 1


def main():
    for i in range(ARRAY):
        master.append([0] * ARRAY)

    with Path(sys.argv[1]).open() as f:
        for line in f:
            from_l, from_t, w, h = [int(x) for x in CLAIM_RE.search(line).groups()]
            process_claim(from_l, from_t, w, h)

    """ Count the number of elements that have been marked more than one time
    """
    print("TOTAL:", sum([sum(x > 1 for x in i) for i in master]))


if __name__ == "__main__":
    main()
