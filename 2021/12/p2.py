#!/usr/bin/env python
"""
    Day 12
"""
import string
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

import attr
from rich import print


@attr.s
class Node:
    name: str = attr.ib()
    parents: list = attr.ib(default=attr.Factory(list))

    def has_cave(self, cave):
        p = [
            x.name for x in (*self.parents, self) if x.name[0] in string.ascii_lowercase
        ]
        return (cave in p) and (2 in Counter(p).values())

    @property
    def plist(self):
        return ",".join(x.name for x in self.parents)


def solve(puzzle):
    oset = deque([Node("start")])
    while oset:
        current = oset.popleft()
        if current.name == "end":
            yield current.plist
            continue
        for child in puzzle[current.name]:
            if child == "start":
                continue  # skip start
            if child[0] in string.ascii_lowercase and current.has_cave(child):
                continue  # skip certain small cave paths
            n = Node(child, [*current.parents, current])
            oset.append(n)


def main():
    puzzle = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        for line in f:
            s, e = line.strip().split("-")
            puzzle[s].append(e)
            puzzle[e].append(s)

    solutions = [x for x in solve(puzzle)]
    # print("\n".join([f"{x},end" for x in solutions]))
    print(f"Number of paths: {len(solutions)}")


if __name__ == "__main__":
    main()
