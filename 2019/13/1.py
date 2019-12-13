#!/usr/bin/env python
""" 
    Day 13
"""
import sys
from collections import defaultdict
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    def __init__(self):
        self._pos = (0, 0)
        self.outputs = []

    def pop(self, _):
        raise Exception("Nope.")

    def send(self, val):
        self.outputs.append(val)


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    provider = InputOutputProvider()
    m = Apollo("A", code, provider)
    m.output = provider
    m.run()

    print("Blocks:", provider.outputs[2::3].count(2))
    
    max_x = max(provider.outputs[::3])
    min_x = min(provider.outputs[::3])
    max_y = max(provider.outputs[1::3])
    min_y = min(provider.outputs[1::3])
    print("X", min_x, max_x)
    print("Y", min_y, max_y)


if __name__ == "__main__":
    main()
