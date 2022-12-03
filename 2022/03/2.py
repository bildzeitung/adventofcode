#!/usr/bin/env python
"""
    Day 3
"""
import sys
from pathlib import Path


def main():
    with Path(sys.argv[1]).open() as f:
        s = 0
        while True:
            try:
                a, b, c = (
                    set(next(f).strip()),
                    set(next(f).strip()),
                    set(next(f).strip()),
                )
                i = (a & b & c).pop()
                if "a" <= i <= "z":
                    s += ord(i) - ord("a") + 1
                else:
                    s += ord(i) - ord("A") + 27
            except StopIteration:
                break
        print(f"Sum: {s}")


if __name__ == "__main__":
    main()
