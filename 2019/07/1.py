#!/usr/bin/env python
""" 
    Day 7
"""
import sys
from itertools import permutations
from pathlib import Path

from apollo import Apollo


class DevNull:
    def send(self, val):
        pass


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    max_val = -1
    for combo in permutations(range(5)):
        previous = 0
        for phase in combo:
            m = Apollo("", code, [phase, previous])
            m.output = DevNull()
            m.run()
            previous = m._last_output
        max_val = max(max_val, previous)
    print("Final", max_val)


if __name__ == "__main__":
    main()
