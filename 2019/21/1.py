#!/usr/bin/env python
""" 
    Day 21
"""
import sys
from time import sleep
from collections import defaultdict
from itertools import product
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    def __init__(self, script):
        self._script = list(script)
        self._buffer = []

    def pop(self, _):
        return ord(self._script.pop(0))

    def send(self, val):
        if val < 128:
            self._buffer.append(chr(val))
        else:
            self._buffer.append(str(val))

    @property
    def output(self):
        return "".join(self._buffer)


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    springscript = "\n".join(["NOT C T", "AND D T", "NOT A J", "OR T J", "WALK"]) + "\n"
    provider = InputOutputProvider(springscript)
    m = Apollo("A", code, provider)
    m.output = provider
    m.run()
    print(provider.output)


if __name__ == "__main__":
    main()
