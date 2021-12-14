#!/usr/bin/env python
"""
    Day 10
"""
import sys
from functools import reduce
from pathlib import Path

SCORING = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

OPENERS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def score(line: str) -> int:
    stack = []
    for c in line:
        if c in OPENERS:
            stack.append(c)
            continue
        if OPENERS[stack.pop()] != c:
            # print(f"{line} -> {c}")
            return 0

    # incomplete, so process
    score = reduce(lambda x, y: x * 5 + SCORING[OPENERS[y]], reversed(stack), 0)
    print(f"Incomplete -> {stack} == {score}")
    return score


def main():
    with Path(sys.argv[1]).open() as f:
        scores = sorted(filter(lambda x: x, [score(line.strip()) for line in f]))
        return scores[len(scores) // 2]


if __name__ == "__main__":
    print(f"Score --> {main()}")
