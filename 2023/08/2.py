#!/usr/bin/env python
"""
    Day 8

    Part 2 is a lowest common multiple problem for the cycles to align
"""
import sys
from itertools import cycle
from math import lcm
from pathlib import Path

from rich import print

DIRECTIONS = {
    "L": 0,
    "R": 1,
}

graph = {}
commands = None


def find_cycle(start: str) -> int:
    current = start
    to_end = 0
    i = cycle(commands)
    while not current.endswith("Z"):
        current = graph[current][next(i)]
        to_end += 1

    # print(f"Took {start} {to_end} iters to get to {current}")

    for_cycle = 1
    current = graph[current][next(i)]
    # print(f"Next from finish: {current}")
    while not current.endswith("Z"):
        current = graph[current][next(i)]
        for_cycle += 1
    print(f"Took {graph[current][next(i)]} {for_cycle} iters to get to {current}")
    print("---")
    return for_cycle


def main():
    global graph
    global commands
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

    i = cycle(commands)
    currents = set(x for x in graph.keys() if x.endswith("A"))
    steps = 0

    print(currents)  # , stops)
    print("---")

    cycle_lengths = [find_cycle(start) for start in currents]
    return lcm(*cycle_lengths)


if __name__ == "__main__":
    print(main())
