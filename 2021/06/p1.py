#!/usr/bin/env python
"""
    Day 06

    part 1: 80 days
    part 2: 256 days

    .. so just take days on the CLI
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path


def iter(state):
    new_items = state[0]  # save for rollover
    for x in range(8):
        state[x] = state[x + 1]
    state[8] = new_items  # new lanternfish
    state[6] += new_items  # reset for spawning lanternfish


def main():
    days = int(sys.argv[1])
    with Path(sys.argv[2]).open() as f:
        initial_state = [int(x) for x in next(f).strip().split(",")]

    state = defaultdict(int)
    for x, y in Counter(initial_state).items():
        state[x] = y

    print("Initial state...", {x: state[x] for x in sorted(state)})
    for _ in range(days):
        iter(state)
        print({x: state[x] for x in sorted(state)})

    print(sum(state.values()))  # count fish


if __name__ == "__main__":
    main()
