#!/usr/bin/env python
"""
  Day 17
"""
import sys


def counter(t, puzzle):
    surround = set()
    x, y, z = t
    s = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i, j, k) == t:  # skip self
                    continue
                if (i, j, k) in puzzle:
                    s += 1
                else:
                    surround.add((i, j, k))

    return s, surround


def tick(puzzle):
    new = set()
    surrounds = set()
    # eval the active cells
    for t in puzzle:
        count, around = counter(t, puzzle)
        if count == 2 or count == 3:  # keep it; anything else will drop out
            new.add(t)
        surrounds |= around

    # eval the margin
    for s in surrounds:
        count, _ = counter(s, puzzle)
        if count == 3:
            new.add(s)

    return new


def vis(puzzle):
    minz, maxz = min(i[2] for i in puzzle), max(i[2] for i in puzzle)
    miny, maxy = min(i[1] for i in puzzle), max(i[1] for i in puzzle)
    minx, maxx = min(i[0] for i in puzzle), max(i[0] for i in puzzle)

    plate = ""
    for z in range(minz, maxz + 1):
        for y in range(miny, maxy + 1):
            plate += (
                "".join(
                    ["#" if (x, y, z) in puzzle else "." for x in range(minx, maxx + 1)]
                )
                + "\n"
            )
        plate += "\n"

    return plate.strip()


def main():
    puzzle = []
    with open(sys.argv[1]) as f:
        y = 0
        for line in f:
            puzzle.extend((i, y, 0) for i, l in enumerate(line.strip()) if l == "#")
            y += 1

    puzzle = set(puzzle)
    print(vis(puzzle))
    t = 0
    while t < 6:
        puzzle = tick(puzzle)
        t += 1
        print(f"After {t}\n{vis(puzzle)}\n{len(puzzle)}")

    return len(puzzle)


if __name__ == "__main__":
    print(main())
