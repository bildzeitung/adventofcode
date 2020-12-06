#!/usr/bin/env python
"""
  Advent 6
"""
import sys


def read_group(f):
    """ same logic as Day 4 for reading records
    
        this time, though, return size of union of all elements
    """
    g = set()
    while l := f.readline():
        l = l.strip()
        if not l:  # blank line separating passports
            yield len(g)
            g = set()
            continue
        g |= set(l)
    yield len(g)


def main():
    with open(sys.argv[1]) as f:
        return sum(x for x in read_group(f))


if __name__ == "__main__":
    print(main())
