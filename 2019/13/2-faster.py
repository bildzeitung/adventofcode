#!/usr/bin/env python
""" 
    Day 13
"""
import sys
from time import sleep
from collections import defaultdict
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    def __init__(self):
        self._canvas = defaultdict(int)
        self.outputs = []
        self.score = 0
        self.ball = None
        self.paddle = None

    def draw(self):
        print("\033[0;0H")  # cursor to top of term
        min_x = min(x[0] for x in self._canvas)
        min_y = min(x[1] for x in self._canvas)
        max_x = max(x[0] for x in self._canvas)
        max_y = max(x[1] for x in self._canvas)
        chars = {0: " ", 1: "X", 2: "O", 3: "=", 4: "*"}
        for y in range(min_y, max_y + 1):
            print("".join(chars[self._canvas[(x, y)]] for x in range(min_x, max_x + 1)))
        print(self.ball, self.paddle, self.score, "\033[K")

    def pop(self, _):
        # super basic AI -- position paddle under ball
        if self.ball[0] > self.paddle[0]:
            return 1
        elif self.ball[0] < self.paddle[0]:
            return -1
        return 0

    def send(self, val):
        self.outputs.append(val)
        if len(self.outputs) == 3:
            x, y, v = self.outputs
            self.outputs = []
            if x == -1 and y == 0:
                self.score = v
            else:
                self._canvas[(x, y)] = v
                if v == 4:
                    self.ball = (x, y)
                elif v == 3:
                    self.paddle = (x, y)


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    code[0] = 2  # free play
    provider = InputOutputProvider()
    m = Apollo("A", code, provider)
    m.output = provider
    m.run()

    # draw final game state
    provider.draw()


if __name__ == "__main__":
    main()
