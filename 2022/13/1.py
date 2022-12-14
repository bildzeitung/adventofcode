#!/usr/bin/env python
"""
    Day 13
"""
import sys
from pathlib import Path
from ast import literal_eval
from rich import print
from itertools import zip_longest


def compare(a, b):
    # both integers
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b

    # both lists
    if isinstance(a, list) and isinstance(b, list):
        for c, d in zip_longest(a, b):
            if c == None:
                return True  # right list is longer, so ok

            if d == None:
                return False  # left list is longer, so out of order

            rv = compare(c, d)
            if rv is None:
                continue

            return rv

        return None

    # so one is a list
    if isinstance(a, int):
        a = [a]

    if isinstance(b, int):
        b = [b]

    return compare(a, b)


def main():
    with Path(sys.argv[1]).open() as f:
        i = 0
        allrv = []
        while True:
            i += 1
            rv = compare(literal_eval(next(f).strip()), literal_eval(next(f).strip()))
            if rv:
                allrv.append(i)
            try:
                next(f)
            except StopIteration:
                break
    print(f"Sum: {sum(allrv)}")


if __name__ == "__main__":
    main()
