#!/usr/bin/env python
"""
    Day 1
"""
import sys
from pathlib import Path


def main():
    sums = []
    group = []
    with Path.open(sys.argv[1]) as f:
        for l in f:
            if not l.strip():
                sums.append(sum(group))
                group = []
                continue
            group.append(int(l))
        sums.append(sum(group))

    print(f"Max: {max(sums)}")


if __name__ == "__main__":
    main()