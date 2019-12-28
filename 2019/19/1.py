#!/usr/bin/env python
""" 
    Day 17
"""
import sys
from time import sleep
from collections import defaultdict
from itertools import product
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    def __init__(self, canvas):
        self.canvas = canvas
        self._p = None
        self._q = None

    def set_point(self, p):
        self._q = p
        self._p = list(p)

    def pop(self, _):
        return self._p.pop(0)

    def send(self, val):
        self.canvas[self._q] = val



def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    canvas = defaultdict(lambda: -1)
    provider = InputOutputProvider(canvas)

    for p in product(range(50), range(50)):
        m = Apollo("A", code, provider)
        m.output = provider
        provider.set_point(p)
        m.run()

    for y in range(50):
        r = ""
        for x in range(50):
            if canvas[(x, y)] == 1:
                r += "#"
            elif canvas[(x, y)] == -1:
                raise Exception(f"what? {x, y}")
            else:
                r += "."
        print(r)
    
    print(sum(canvas.values()))


if __name__ == "__main__":
    main()
