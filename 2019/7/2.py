#!/usr/bin/env python
""" 
    Day 7
"""
import sys
from itertools import permutations
from pathlib import Path

from apollo import Apollo


def main():
    fname = sys.argv[1]
    with Path(fname).open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    max_val = -1
    for combo in permutations(range(5, 10)):
        machines = [
            Apollo("a", code, [combo[0], 0]),
            Apollo("b", code, [combo[1]]),
            Apollo("c", code, [combo[2]]),
            Apollo("d", code, [combo[3]]),
            Apollo("e", code, [combo[4]]),
        ]
        machines[0].output = machines[1]
        machines[1].output = machines[2]
        machines[2].output = machines[3]
        machines[3].output = machines[4]
        machines[4].output = machines[0]

        while any(m.state == Apollo.WAIT for m in machines):
            for m in machines:
                m.run()

        max_val = max(max_val, machines[-1]._last_output)

    print("MAX", max_val)


if __name__ == "__main__":
    main()
