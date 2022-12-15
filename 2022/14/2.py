#!/usr/bin/env python
"""
    Day 11
"""
import sys
from pathlib import Path
from rich import print


def viz(puzzle):
    min_x = min(x[0] for x in puzzle)
    max_x = max(x[0] for x in puzzle)
    min_y = min(x[1] for x in puzzle)
    max_y = max(x[1] for x in puzzle)
    for y in range(min_y, max_y + 1):
        print(
            "".join(
                puzzle[(x, y)] if (x, y) in puzzle else "."
                for x in range(min_x, max_x + 1)
            )
        )


def main():
    what = {}

    with Path(sys.argv[1]).open() as f:
        for line in f:
            nodes = [
                tuple(int(z) for z in y.split(","))
                for y in [x.strip() for x in line.split("->")]
            ]
            a = nodes[0]
            for b in nodes[1:]:
                for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                    for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                        what[(x, y)] = "#"
                a = b

    # ok, now simulate ...
    bottom = max(x[1] for x in what) + 2
    units = 0
    while True:
        sx, sy = (500, 0)
        while True:
            sy += 1

            # close to the bottom?
            if sy >= bottom - 1:
                # expand bottom
                what[(sx - 1, bottom)] = "#"
                what[(sx, bottom)] = "#"
                what[(sx + 1, bottom)] = "#"

            # can I fall down?
            if (sx, sy) not in what:
                continue

            # can I fall left?
            if (sx - 1, sy) not in what:
                sx -= 1
                continue

            # can I fall right?
            if (sx + 1, sy) not in what:
                sx += 1
                continue

            # I am at rest
            what[(sx, sy - 1)] = "o"

            break
        units += 1
        if sx == 500 and sy == 1:
            viz(what)
            return units


if __name__ == "__main__":
    print(f"Total: {main()}")
