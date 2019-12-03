#!/usr/bin/env python
''' Day 1
'''
from pathlib import Path

import sys


def main():
    with Path(sys.argv[1]).open() as f:
        s = sum(int(l.strip()) // 3 - 2 for l in f)
        print(s)


if __name__ == "__main__":
    main()