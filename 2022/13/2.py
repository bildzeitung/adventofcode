#!/usr/bin/env python
"""
    Day 13
"""
import sys
from pathlib import Path
from ast import literal_eval
from rich import print
from itertools import zip_longest
from functools import cmp_to_key


def compare(a, b):
    # both integers
    if isinstance(a, int) and isinstance(b, int):
        return b - a

    # both lists
    if isinstance(a, list) and isinstance(b, list):
        for c, d in zip_longest(a, b):
            if c == None:
                return 1  # right list is longer, so ok

            if d == None:
                return -1  # left list is longer, so out of order

            rv = compare(c, d)
            if rv == 0:
                continue

            return rv

        return 0

    # so one is a list
    if isinstance(a, int):
        a = [a]

    if isinstance(b, int):
        b = [b]

    return compare(a, b)


def main():
    packets = []
    with Path(sys.argv[1]).open() as f:
        while True:
            packets.append(literal_eval(next(f).strip()))
            packets.append(literal_eval(next(f).strip()))
            try:
                next(f)
            except StopIteration:
                break
    # add divider packets
    packets.append([[2]])
    packets.append([[6]])

    ordered = [x for x in reversed(sorted(packets, key=cmp_to_key(compare)))]
    l = ordered.index([[2]]) + 1
    r = ordered.index([[6]]) + 1
    print(f"Key: {l*r}")


if __name__ == "__main__":
    main()
