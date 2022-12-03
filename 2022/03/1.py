#!/usr/bin/env python
"""
    Day 3
"""
import sys
from pathlib import Path


def getPriority(line):
    line = line.strip()
    fr = line[: len(line) // 2]
    bk = line[len(line) // 2 :]
    i = (set(fr) & set(bk)).pop()  # item in common
    if "a" <= i <= "z":
        p = ord(i) - ord("a") + 1
    else:
        p = ord(i) - ord("A") + 27
    print(i, p)
    return p


def main():
    with Path(sys.argv[1]).open() as f:
        print(f"Sum: {sum(getPriority(line) for line in f)}")


if __name__ == "__main__":
    main()
