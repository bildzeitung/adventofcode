#!/usr/bin/env python
""" 
    Day 11
"""
import sys
from collections import defaultdict
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    COLOUR = True
    DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def draw(self):
        min_x = min(x[0] for x in self._canvas)
        min_y = min(x[1] for x in self._canvas)
        max_x = max(x[0] for x in self._canvas)
        max_y = max(x[1] for x in self._canvas)
        chars = {0: " ", 1: "."}
        print(min_x, min_y, max_x, max_y)
        for y in range(min_y, max_y + 1):
            print("".join(chars[self._canvas[(x, y)]] for x in range(min_x, max_x + 1)))

    def __init__(self):
        self._pos = (0, 0)
        self._canvas = defaultdict(int)
        self._accept = self.COLOUR
        self._dir = 0  # up
        self._didpaint = set()

    def set_start(self, val):
        self._canvas[(0, 0)] = val

    def pop(self, _):
        return self._canvas[self._pos]

    def send(self, val):
        if self._accept == self.COLOUR:
            # print(f"Draw colour {val} on {self._pos}")
            self._canvas[self._pos] = val
            self._didpaint.add(self._pos)
        else:  # change direction
            old = self._dir
            if val:  # turn right
                self._dir = (self._dir + 1) % len(self.DIRS)
            else:
                self._dir = (len(self.DIRS) + self._dir - 1) % len(self.DIRS)
            # print(f"Change direction {val}: {old} -> {self._dir}")
            self._pos = (
                self._pos[0] + self.DIRS[self._dir][0],
                self._pos[1] + self.DIRS[self._dir][1],
            )
        self._accept = not self._accept

    @property
    def didpaint(self):
        return len(self._didpaint)


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    provider = InputOutputProvider()
    provider.set_start(int(sys.argv[2]))
    m = Apollo("A", code, provider)
    m.output = provider
    m.run()
    print(provider.didpaint)
    provider.draw()


if __name__ == "__main__":
    main()
