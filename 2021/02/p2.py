#!/usr/bin/env python
"""
    Day 2
"""
from pathlib import Path
import sys


def main():
    horiz = 0
    depth = 0
    aim = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            items = line.split()
            direction, amount = items[0].strip(), int(items[1])
            if direction == "down":
                aim += amount
            if direction == "up":
                aim -= amount
            if direction == "forward":
                horiz += amount
                depth += aim * amount
            assert(depth >= 0)
    print(f"Final h: {horiz}  d: {depth} ==> {horiz*depth}")


if __name__ == "__main__":
    main()