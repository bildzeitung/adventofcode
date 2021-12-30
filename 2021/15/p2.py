#!/usr/bin/env python
"""
    Day 15
"""
import heapq
import sys
from pathlib import Path
from typing import List

from attrs import define, field
from rich import print


@define(order=True)
class Node:
    point = field(eq=False)
    parent = field(default=None, eq=False)
    fscore = field(default=None)
    gscore = field(default=None, eq=False)
    active = field(default=True, eq=False)


def solve(puzzle, mx, my):
    # looks like this needs A* at least
    def h(p):  # Manhattan distance
        return mx + my - sum(p)

    start = Node((0, 0), gscore=0, fscore=h((0, 0)))

    openSetTracker = set()
    openSetTracker.add(start.point)
    openSet: List[Node] = []
    heapq.heappush(openSet, start)
    allnodes = {start.point: start}

    END = (mx, my)
    while openSet:
        current = heapq.heappop(openSet)
        if not current.active:
            continue  # ignore inactive

        if current.point == END:
            print(f"Solution: {current.gscore}")
            return

        # XXX THIS IS POTENTIALLY SLOW XXX
        openSetTracker.remove(current.point)

        # check around
        around = (
            (current.point[0] - 1, current.point[1]),
            (current.point[0] + 1, current.point[1]),
            (current.point[0], current.point[1] - 1),
            (current.point[0], current.point[1] + 1),
        )
        for p in around:
            if p not in puzzle:  # bounds check
                continue

            tentative_gScore = current.gscore + puzzle[p]
            if p not in allnodes:
                np = Node(
                    p,
                    parent=current,
                    gscore=tentative_gScore,
                    fscore=tentative_gScore + h(p),
                )
                openSetTracker.add(p)
                heapq.heappush(openSet, np)
                allnodes[p] = np
            elif tentative_gScore < allnodes[p].gscore:
                np = Node(
                    p,
                    parent=current,
                    gscore=tentative_gScore,
                    fscore=tentative_gScore + h(p),
                )
                old_np = allnodes[p]
                old_np.active = False  # do this instead of re-heaping
                openSetTracker.add(p)
                heapq.heappush(openSet, np)
                allnodes[p] = np

    assert False, "no solution"


def main():
    puzzle = {}
    with Path(sys.argv[1]).open() as f:
        y = 0
        for line in f:
            for x, v in enumerate(line.strip()):
                iv = int(v)
                puzzle[(x, y)] = iv
                for i in range(1, 5):
                    puzzle[(x + (len(line.strip()) * i), y)] = ((iv + i) // 10) + (
                        (iv + i) % 10
                    )
            y += 1
    mx = max(x[0] for x in puzzle)
    my = max(x[1] for x in puzzle)

    for y in range(my + 1):
        for i in range(1, 5):
            for x in range(mx + 1):
                iv = puzzle[(x, y)]
                puzzle[(x, y + ((my + 1) * i))] = ((iv + i) // 10) + ((iv + i) % 10)
    my = max(x[1] for x in puzzle)
    solve(puzzle, mx, my)


if __name__ == "__main__":
    main()
