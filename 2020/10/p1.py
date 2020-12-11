#!/usr/bin/env python
"""
  Day 10
"""
import sys
from collections import defaultdict


def main():
    with open(sys.argv[1]) as f:
        joltages = [int(x.strip()) for x in f]

    joltages = sorted(joltages)
    print(joltages)
    er = 0
    delta = defaultdict(int)
    for j in joltages:
        delta[j - er] += 1
        er = j
    delta[3] += 1  # last one
    print(delta)

    return delta[1] * delta[3]


if __name__ == "__main__":
    print(main())
