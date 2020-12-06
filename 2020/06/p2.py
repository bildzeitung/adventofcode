#!/usr/bin/env python
"""
  Advent 6
"""
import sys
from functools import reduce


def read_group(f):
    g = []
    while l := f.readline():
        l = l.strip()
        if not l:  # blank line separating passports
            yield g
            g = []
            continue
        g.append(l)
    yield g


def common(g):
    return len(reduce(lambda x, y: x & set(y), g[1:], set(g[0])))


def main():
    with open(sys.argv[1]) as f:
        return sum([x for x in [common(g) for g in read_group(f)]])


if __name__ == "__main__":
    print(main())
