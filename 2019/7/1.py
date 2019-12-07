#!/usr/bin/env python
""" 
    Day 7
"""
import sys
from itertools import permutations
from pathlib import Path

from apollo import Apollo


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    max_val = -1
    for combo in permutations(range(5)):
        previous = 0
        for phase in combo:
            m = Apollo(code, [phase, previous]).run()
            previous = m.output_buffer
        # print(combo, "=>", previous)
        max_val = max(max_val, previous)
    print("Final", max_val)


if __name__ == "__main__":
    main()
