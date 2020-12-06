#!/usr/bin/env python
"""
  Advent 6
"""
import sys


def read_group(f):
    g = set(f.readline().strip())
    while l := f.readline():
        l = l.strip()
        if not l:  # blank line separating passports
            yield len(g)
            g = set(f.readline().strip())
            continue
        g &= set(l)
    yield len(g)


def main():
    with open(sys.argv[1]) as f:
        return sum(g for g in read_group(f))


if __name__ == "__main__":
    print(main())
