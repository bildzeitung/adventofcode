#!/usr/bin/env python
"""
    Day 15
"""
import sys
from pathlib import Path
from attrs import define, field
import heapq


@define(order=True)
class Node:
    point = field(eq=False)
    parent = field(default=None, eq=False)
    fscore = field(default=None)
    gscore = field(default=None, eq=False)


def solve(puzzle, mx, my):
    # looks like this needs A* at least
    def h(p):  # Manhattan distance
        return mx + my - sum(p)

    openSetTracker = set()
    openSet = []
    start = Node((0,0))
    start.fscore = h(start.point)
    start.gscore = 0
    heapq.heappush(openSet, start)
    openSetTracker.add(start.point)
    allnodes = {start.point: start}

    END = (mx,my)
    while openSet:
        current : Node
        current = heapq.heappop(openSet)
        if current.point == END:
            print(f"Solution: {current}")
            return

        openSetTracker.remove(current.point)

        # check around
        around = ( (current.point[0]-1, current.point[1]),
                   (current.point[0]+1, current.point[1]),
                   (current.point[0], current.point[1]-1),
                   (current.point[0], current.point[1]+1)
        )
        for p in around:
            if p not in puzzle:  # bounds check
                continue

            tentative_gScore = current.gscore + puzzle[p]
            if p not in allnodes or tentative_gScore < allnodes[p].gscore:
                np = Node(p)
                np.parent = current
                np.gscore = tentative_gScore
                np.fscore = tentative_gScore + h(p)
                if p not in openSetTracker:
                    openSetTracker.add(p)
                    heapq.heappush(openSet, np)

    assert False, "no solution"


def main():
    puzzle = {}
    with Path(sys.argv[1]).open() as f:
        y = 0
        for line in f:
            for x, v in enumerate(line.strip()):
                puzzle[(x,y)] = int(v)
            y += 1
    mx = max(x[0] for x in puzzle)
    my = max(x[1] for x in puzzle)
    solve(puzzle, mx, my)


if __name__ == "__main__":
    main()