#!/usr/bin/env python
"""
    Day 9
"""
import sys
from pathlib import Path

from rich import print


def main():
    with Path(sys.argv[1]).open() as f:
        caves = []
        for l in f:
            caves.append([int(x) for x in l.strip()])
    print(caves)

    def low_eval(x, y) -> bool:
        is_low = True

        def check(val, x, y):
            if not (-1 < x < len(caves[0])):
                return True

            if not (-1 < y < len(caves)):
                return True

            return val < caves[y][x]

        # left
        is_low = is_low and check(caves[y][x], x - 1, y)
        # right
        is_low = is_low and check(caves[y][x], x + 1, y)
        # up
        is_low = is_low and check(caves[y][x], x, y - 1)
        # down
        is_low = is_low and check(caves[y][x], x, y + 1)

        if is_low:
            print(f"({x}, {y}) => {caves[y][x]} is a low point")
        return is_low

    risk = 0
    for r in range(len(caves)):
        for c in range(len(caves[0])):
            if low_eval(c, r):
                risk += 1 + caves[r][c]
    return risk


if __name__ == "__main__":
    print(f"Risk --> {main()}")
