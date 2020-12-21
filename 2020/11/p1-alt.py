#!/usr/bin/env python
"""
  Day 11
"""
import sys
from copy import copy


def tick(puzzle, maxx, maxy):
    made_changes = False
    new = []

    def e(x, y):
        return sum(
            [
                x > 0 and puzzle[y][x - 1] == "#",
                x > 0 and y > 0 and puzzle[y - 1][x - 1] == "#",
                y > 0 and puzzle[y - 1][x] == "#",
                y > 0 and x < maxx - 1 and puzzle[y - 1][x + 1] == "#",
                x < maxx - 1 and puzzle[y][x + 1] == "#",
                x < maxx - 1 and y < maxy - 1 and puzzle[y + 1][x + 1] == "#",
                y < maxy - 1 and puzzle[y + 1][x] == "#",
                y < maxy - 1 and x > 0 and puzzle[y + 1][x - 1] == "#",
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

            if puzzle[y][x] == "#" and e(x, y) > 3:
                new[y][x] = "L"
                made_changes = True

    return new, made_changes


def main():
    puzzle = []
    with open(sys.argv[1]) as f:
        puzzle = [[c for c in x.strip()] for x in f]
    maxx, maxy = (len(puzzle[0]), len(puzzle))

    while True:
        puzzle, churned = tick(puzzle, maxx, maxy)
        if not churned:
            break
    return sum(i.count("#") for i in puzzle)


if __name__ == "__main__":
    print(main())
