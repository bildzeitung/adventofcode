#!/usr/bin/env python
"""
    Day 24
"""
import sys
from itertools import chain
from pathlib import Path


def step(grids, idx):
    # print(f"Procesing grid {idx}")

    def mget(r, c):
        # look to upper grid
        if r < 0:
            if idx > 0:
                return grids[idx - 1][1][2]
            else:
                return 0
        if c < 0:
            if idx > 0:
                return grids[idx - 1][2][1]
            else:
                return 0
        if r > 4:
            if idx > 0:
                return grids[idx - 1][3][2]
            else:
                return 0
        if c > 4:
            if idx > 0:
                return grids[idx - 1][2][3]
            else:
                return 0

        return grids[idx][r][c]

    g = newgrid()

    def get_state(cell, v):
        if cell and v == 1:
            return 1
        if not cell and 0 < v < 3:
            return 1
        return 0

    for row in range(5):
        for col in range(5):
            # these cases introspect into a lower grid
            if row == 1 and col == 2:
                continue
            if row == 2 and col == 1:
                continue
            if row == 2 and col == 2:
                continue  # middle!
            if row == 2 and col == 3:
                continue
            if row == 3 and col == 2:
                continue

            v = sum(
                [
                    mget(row - 1, col),
                    mget(row, col - 1),
                    mget(row, col + 1),
                    mget(row + 1, col),
                ]
            )
            g[row][col] = get_state(grids[idx][row][col], v)
            # if idx > 0:
            #    print(f"{row}, {col} -> {v} [{grids[idx][row][col]}]")
    # draw(g)
    v = grids[idx][0][2] + grids[idx][1][1] + grids[idx][1][3]
    if (idx + 1) < len(grids):
        v += sum(grids[idx + 1][0])
    g[1][2] = get_state(grids[idx][1][2], v)

    v = grids[idx][1][1] + grids[idx][2][0] + grids[idx][3][1]
    if (idx + 1) < len(grids):
        v += sum(grids[idx + 1][x][0] for x in range(5))
    g[2][1] = get_state(grids[idx][2][1], v)

    v = grids[idx][1][3] + grids[idx][2][4] + grids[idx][3][3]
    if (idx + 1) < len(grids):
        v += sum(grids[idx + 1][x][4] for x in range(5))
    g[2][3] = get_state(grids[idx][2][3], v)

    v = grids[idx][3][1] + grids[idx][3][3] + grids[idx][4][2]
    if (idx + 1) < len(grids):
        v += sum(grids[idx + 1][4])
    g[3][2] = get_state(grids[idx][3][2], v)

    return g


def draw(grid):
    for row in grid:
        print("".join(["#" if x else "." for x in row]))


def calc(grid):
    return sum(chain.from_iterable(grid))


def newgrid():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def tots(grids):
    return sum(calc(g) for g in grids)


def main():
    grid = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            grid.append([1 if x == "#" else 0 for x in line.strip()])

    grids = [grid]
    for i in range(200):
        if calc(grids[0]):
            grids.insert(0, newgrid())
        if calc(grids[-1]):
            grids.append(newgrid())
        grids = [step(grids, g) for g in range(len(grids))]
        # for g in grids:
        #    draw(g)
        #    print()
        # print("---")
        print(f"[{i+1}] Total bugs: {tots(grids)}")


if __name__ == "__main__":
    main()
