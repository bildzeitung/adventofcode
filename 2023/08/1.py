#!/usr/bin/env python
"""
    Day 8
"""
import sys
from itertools import cycle
from pathlib import Path

from rich import print

DIRECTIONS = {
    "L": 0,
    "R": 1,
}


def main():
    graph = {}
    with Path(sys.argv[1]).open() as f:
        commands = [DIRECTIONS[x] for x in list(next(f).strip())]
        next(f)  # blank line
        for line in f:
            node, l, r = (
                line.replace("=", "")
                .replace("(", "")
                .replace(")", "")
                .replace(",", "")
                .strip()
                .split()
            )
            graph[node] = (l, r)

    print(commands)
    print(graph)
    i = cycle(commands)
    current = "AAA"
    steps = 0
    while current != "ZZZ":
        current = graph[current][next(i)]
        steps += 1
        # print(current)

    return steps


if __name__ == "__main__":
    print(main())
