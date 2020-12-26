#!/usr/bin/env python
"""
  Day 24
"""
import sys
from collections import defaultdict

DIRS = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1),
}

FLIP = {
    "W": "B",
    "B": "W",
}


def counter(t, puzzle):
    surround = set()
    x, y = t
    s = 0
    for d in DIRS.values():
        cell = (x + d[0], y + d[1])
        if cell in puzzle:
            s += 1
        else:
            surround.add(cell)

    return s, surround


def tick(puzzle):
    """ Day 17 Conway main loop
    """
    new = set()
    surrounds = set()
    # eval the active cells
    for t in puzzle:
        count, around = counter(t, puzzle)
        if 0 < count < 3:
            new.add(t)
        surrounds |= around

    # eval the margin
    for s in surrounds:
        count, _ = counter(s, puzzle)
        if count == 2:
            new.add(s)

    return new


def main():
    puzzle = defaultdict(lambda: "W")
    with open(sys.argv[1]) as f:
        for line in f:

            def getdirs():
                d = [x for x in line.strip()]
                while d:
                    x = d.pop(0)
                    if x in ("n", "s"):
                        x += d.pop(0)
                    yield x

            c = (0, 0)
            for d in getdirs():
                c = (c[0] + DIRS[d][0], c[1] + DIRS[d][1])
            puzzle[c] = FLIP[puzzle[c]]

    # live cells are the black ones, so track only them
    puzzle = [i for i, v in puzzle.items() if v == "B"]
    print(f"Day 0: {len(puzzle)}")
    for i in range(100):
        puzzle = tick(puzzle)
        print(f"Day {i+1}: {len(puzzle)}")
    return f"Final --> {len(puzzle)}"


if __name__ == "__main__":
    print(main())
