#!/usr/bin/env python
"""
  Day 17
"""
import sys


def counter(t, puzzle):
    surround = set()
    x, y, z, w = t
    s = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if (i, j, k, l) == t:  # skip self
                        continue
                    if (i, j, k, l) in puzzle:
                        s += 1
                    else:
                        surround.add((i, j, k, l))

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


def main():
    puzzle = []
    with open(sys.argv[1]) as f:
        y = 0
        for line in f:
            puzzle.extend((i, y, 0, 0) for i, l in enumerate(line.strip()) if l == "#")
            y += 1

    puzzle = set(puzzle)
    t = 0
    while t < 6:
        puzzle = tick(puzzle)
        t += 1
        print(f"After {t}: {len(puzzle)}")

    return len(puzzle)


if __name__ == "__main__":
    print(main())
