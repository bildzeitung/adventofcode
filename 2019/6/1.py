#!/usr/bin/env python
"""
    Day 6
"""
import sys

from collections import defaultdict
from pathlib import Path


def main():
    g = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        for line in f:
            target, source = line.strip().split(")")
            g[target].append(source)

    q = [("COM", 0)]
    sum = 0
    while q:
        n = q.pop(0)
        sum += n[1]
        for i in g[n[0]]:
            q.append((i, n[1] + 1))
    print(sum)


if __name__ == "__main__":
    main()
