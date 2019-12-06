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
            g[source].append(target)

    seen = []
    q = [("YOU", -1)]
    while q:
        n = q.pop(0)
        seen.append(n[0])
        if n[0] == "SAN":
            print(n, n[1] - 1)
            break
        for i in g[n[0]]:
            if i not in seen:
                q.append((i, n[1] + 1))


if __name__ == "__main__":
    main()
