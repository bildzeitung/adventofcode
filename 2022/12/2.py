#!/usr/bin/env python
"""
    Day 12
"""
import sys
from pathlib import Path
from rich import print
from queue import PriorityQueue


def main():
    start = None
    goal = None
    phash = {}
    with Path(sys.argv[1]).open() as f:
        puzzle = [list(line.strip()) for line in f]
        for y in range(len(puzzle)):
            for x in range(len(puzzle[0])):
                if puzzle[y][x] == "S":
                    start = (x, y)
                    puzzle[y][x] = "a"
                elif puzzle[y][x] == "E":
                    goal = (x, y)
                    puzzle[y][x] = "z"
                phash[(x, y)] = ord(puzzle[y][x]) - ord("a")

    def delta(pt):  # Manhattan distance
        return abs(goal[0] - pt[0]) + abs(goal[1] - pt[1])

    seen = {start: 0}
    q = PriorityQueue()
    node = (delta(start), start)
    q.put(node)
    while not q.empty():
        _, coord = q.get()
        x, y = coord

        if coord == goal:
            print(f"Found {seen[coord]}")
            return

        def check(dest):
            if dest not in phash:
                return

            # is this a valid child?
            if phash[dest] > phash[coord] + 1:
                return

            # 'a' is a start point, so score it like it's the start
            if phash[coord] == 0:
                new_seen = 1
            else:
                new_seen = seen[coord] + 1

            if dest not in seen or new_seen < seen[dest]:
                seen[dest] = new_seen
                priority = new_seen + delta(dest)
                node = (priority, dest)
                q.put(node)

        check((x - 1, y))
        check((x + 1, y))
        check((x, y - 1))
        check((x, y + 1))


if __name__ == "__main__":
    main()
