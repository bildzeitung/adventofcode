#!/usr/bin/env python
"""
    Day 2
"""
from pathlib import Path
import sys

DIRECTIONS = {
    "forward": (1, 0),
    "down": (0, 1),
    "up": (0, -1),
}

def main():
    horiz = 0
    depth = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            items = line.split()
            direction, amount = items[0].strip(), int(items[1])
            horiz = DIRECTIONS[direction][0] * amount + horiz
            depth = DIRECTIONS[direction][1] * amount + depth
            assert(depth >= 0)
    print(f"Final h: {horiz}  d: {depth} ==> {horiz*depth}")


if __name__ == "__main__":
    main()