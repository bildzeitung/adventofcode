#!/usr/bin/env python
"""
    Day 13
"""
import sys
from pathlib import Path


def fold_y(puzzle: set, amt):
    print(f"Fold y -> {amt}")
    pts = [p for p in puzzle if p[1] > amt]
    for p in pts:
        puzzle.remove(p)
        new_p = (p[0], p[1] - 2 * (p[1]-amt))
        puzzle.add(new_p)
    return puzzle


def fold_x(puzzle, amt):
    print(f"Fold x -> {amt}")
    pts = [p for p in puzzle if p[0] > amt]
    for p in pts:
        puzzle.remove(p)
        new_p = (p[0] - 2 * (p[0]-amt), p[1])
        puzzle.add(new_p)
    return puzzle


def fold(puzzle, direction):
    dir, amt = direction
    if dir == "y":
        return fold_y(puzzle, amt)
    return fold_x(puzzle, amt)


def render(puzzle):
    mx = max(puzzle, key=lambda x: x[0])[0] + 1
    my = max(puzzle, key=lambda x: x[1])[1] + 1
    for y in range(my):
        print("".join("#" if (x,y) in puzzle else " " for x in range(mx)))


def main():
    puzzle = set()
    directions = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            if not line.strip():
                break
            x, y = [int(x) for x in line.strip().split(",")]
            puzzle.add((x,y))
        for line in f:
            a, amount = line.strip().split("=")
            directions.append((a[-1], int(amount)))
    
    render(puzzle)
    for d in directions:
        puzzle = fold(puzzle, d)
        render(puzzle)
        # for part 1:
        #print(f"Points: {len(puzzle)}")
        #return


if __name__ == "__main__":
    main()