#!/usr/bin/env python
"""
  Day 11
"""
import sys
from collections import defaultdict


def tick(puzzle, state):
    made_changes = False
    newstate = defaultdict(dict)
    for i in puzzle:
        x, y = i
        sum = 0
        for xx in range(x - 1, x + 2):
            for yy in range(y - 1, y + 2):
                # skip middle
                if xx == x and yy == y:
                    continue
                if (xx, yy) in puzzle and state[xx][yy] == "#":
                    sum += 1
        newstate[x][y] = state[x][y]
        if state[x][y] == "L" and sum == 0:
            newstate[x][y] = "#"
            made_changes = True
        elif state[x][y] == "#" and sum > 3:
            newstate[x][y] = "L"
            made_changes = True
    return newstate, made_changes


def main():
    puzzle = []
    state = defaultdict(dict)
    maxy, maxx = (0, 0)
    with open(sys.argv[1]) as f:
        y = 0
        for line in f:
            line = line.strip()
            maxx = len(line)
            for x, v in enumerate(line):
                if v == "L":
                    puzzle.append((x, y))
                    state[x][y] = "L"
            y += 1
    maxy = y

    while True:
        state, churned = tick(puzzle, state)
        if not churned:
            break
        print("TICK")
    return sum(state[i[0]][i[1]] == "#" for i in puzzle)


if __name__ == "__main__":
    print(main())
