#!/bin/env python
"""
    Day 2

    The notion of "handfuls" can be discarded entirely, as the goal
    is only to check against a set of max values

"""
import sys
from pathlib import Path

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def isGamePossible(l: str) -> bool:
    l = l.replace(";", "").replace(",", "").split(" ")
    i = iter(l)
    for n in i:
        colour = next(i)
        if int(n) > MAX_CUBES[colour]:
            return False
        # print(int(n), colour)

    return True


def main():
    game = 0
    total = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            game += 1
            if isGamePossible(line.strip().split(":")[1].strip()):
                total += game

    return total


if __name__ == "__main__":
    print(main())
