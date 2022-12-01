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

    print(f"{sorted(sums)[-3:]}")
    print(f"Max: {sum(sorted(sums)[-3:])}")


if __name__ == "__main__":
    main()