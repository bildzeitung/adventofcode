#!/usr/bin/env python
"""
  Day 11

  Use a 2D array representation, since the puzzle size is fixed.

  It's a ray-casting exercise, I s'pose? This implementation doesn't do
  anything super smart -- cast along a vector & return what it hits
  (if anything).
"""
import sys
from copy import copy


def tick(puzzle, maxx, maxy):
    made_changes = False
    new = []

    def e(x, y):
        def see_delta(offset, x, y):
            x += offset[0]
            y += offset[1]
            while x > -1 and y > -1 and x < maxx and y < maxy:
                if puzzle[y][x] == "#":
                    return 1
                if puzzle[y][x] == "L":
                    return 0
                x += offset[0]
                y += offset[1]
            return 0

        return sum(
            [
                see_delta((-1, -1), x, y),
                see_delta((0, -1), x, y),
                see_delta((1, -1), x, y),
                see_delta((-1, 0), x, y),
                see_delta((1, 0), x, y),
                see_delta((-1, 1), x, y),
                see_delta((0, 1), x, y),
                see_delta((1, 1), x, y),
            ]
        )

    for y in range(len(puzzle)):
        new.append(copy(puzzle[y]))
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == ".":
                continue

            if puzzle[y][x] == "L" and e(x, y) == 0:
                new[y][x] = "#"
                made_changes = True

            if puzzle[y][x] == "#" and e(x, y) > 4:
                new[y][x] = "L"
                made_changes = True

    return new, made_changes


def vis(puzzle):
    for y in puzzle:
        print("".join(y))
    print()


def main():
    puzzle = []
    with open(sys.argv[1]) as f:
        puzzle = [[c for c in x.strip()] for x in f]
    maxx, maxy = (len(puzzle[0]), len(puzzle))
    vis(puzzle)
    while True:
        puzzle, churned = tick(puzzle, maxx, maxy)
        vis(puzzle)
        if not churned:
            break
    return sum(i.count("#") for i in puzzle)


if __name__ == "__main__":
    print(main())
