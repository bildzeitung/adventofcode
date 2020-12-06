#!/usr/bin/env python
"""
  Advent 6
"""
import sys
from functools import reduce


def common(g):
    """ Group is a list of sets; find the intersection of all of them
    """
    return len(reduce(lambda x, y: x & set(y), g[1:], set(g[0])))


def read_group(f):
    g = []
    while l := f.readline():
        l = l.strip()
        if not l:  # blank line separating passports
            yield common(g)
            g = []
            continue
        g.append(l)
    yield common(g)




def main():
    with open(sys.argv[1]) as f:
        return sum(g for g in read_group(f))


if __name__ == "__main__":
    print(main())
