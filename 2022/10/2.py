#!/usr/bin/env python
"""
    Day 10
"""
import sys
from pathlib import Path
from rich import print


def main():
    X = 1  # starting register value
    wait = False
    val = 0
    raster = []
    beam = 0
    with Path(sys.argv[1]).open() as f:
        while True:
            if X - 1 <= beam <= X + 1:
                raster.append("#")
            else:
                raster.append(" ")
            if not wait:
                try:
                    line = next(f).strip()
                except StopIteration:
                    break
                if "noop" in line:
                    pass
                else:  # it's an addx
                    val = int(line.split(" ")[1])
                    wait = True
            else:
                wait = False
                X += val
            beam += 1
            if beam == 40:
                print("".join(raster))
                raster = []
                beam = 0


if __name__ == "__main__":
    main()
