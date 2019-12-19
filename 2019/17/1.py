#!/usr/bin/env python
""" 
    Day 17
"""
import sys
from time import sleep
from collections import defaultdict
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    def __init__(self):
        self.output = ""

    def pop(self, _):
        pass

    def send(self, val):
        self.output += chr(val)


def calc_alignment(output):
    # canvas = [list(x) for x in output.split()]
    # for row in canvas:
    #    print(row)
    canvas = output.split()
    for i in range(len(canvas) - 2):
        rows = canvas[i : i + 3]
        for j in range(len(canvas[i]) - 2):
            if (
                rows[0][j : j + 3] == ".#."
                and rows[1][j : j + 3] == "###"
                and rows[2][j : j + 3] == ".#."
            ):
                yield (i + 1, j + 1)


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    provider = InputOutputProvider()
    m = Apollo("A", code, provider)
    m.output = provider
    m.run()
    print(provider.output)
    print("Alignment:", sum(p[0] * p[1] for p in calc_alignment(provider.output)))


if __name__ == "__main__":
    main()
