#!/usr/bin/env python
"""
    Day 16
"""
import math
import sys
from itertools import repeat, chain
from pathlib import Path

BASE = [0, 1, 0, -1]


def phase(signal):
    new_signal = []
    for i in range(1, len(signal) + 1):
        sequence = [y for y in chain.from_iterable(repeat(x, i) for x in BASE)]
        n = math.ceil(max(0, (len(signal) - len(sequence) + 1)) / len(sequence))
        new_signal.append(
            abs(sum(a * b for a, b in zip(signal, sequence[1:] + sequence * n))) % 10
        )
    return new_signal


def main():
    with Path(sys.argv[1]).open() as f:
        signal = [int(x) for x in f.read().strip()]

    for _ in range(100):
        signal = phase(signal)
    print("".join([str(x) for x in signal[:8]]))


if __name__ == "__main__":
    main()
