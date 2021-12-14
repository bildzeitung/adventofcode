#!/usr/bin/env python
"""
    Day 10
"""
import sys
from pathlib import Path

SCORING = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPENERS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def score(line: str) -> int:
    stack = []
    for c in line:
        if c in OPENERS:
            stack.append(c)
            continue
        if OPENERS[stack.pop()] != c:
            print(f"{line} -> {c}")
            return SCORING[c]

    # incomplete
    return 0


def main():
    with Path(sys.argv[1]).open() as f:
        return sum(score(line.strip()) for line in f)


if __name__ == "__main__":
    print(f"Score --> {main()}")
