#!/usr/bin/env python
''' Day 1
'''
from pathlib import Path

import sys

def g(a):
    s = 0
    while a > 0:
        a = max(a // 3 - 2, 0)
        s += a
    return s


def main():
    with Path(sys.argv[1]).open() as f:
        s = sum(g(int(l.strip())) for l in f)
        print(s)


if __name__ == "__main__":
    main()