#!/usr/bin/env python
""" 
    Day 25
"""
import sys
from time import sleep
from collections import defaultdict
from itertools import product
from pathlib import Path

from apollo import Apollo


class InputOutputProvider:
    def __init__(self, script):
        self._script = script
        self._buffer = []
        self._outbuffer = []

    def pop(self, _):
        if not self._buffer:
            if self._script:
                self._buffer = list(self._script.pop(0))
            else:
                i = input() + "\n"
                self._buffer = list(i)

        return ord(self._buffer.pop(0))

    def send(self, val):
        if val != ord("\n"):
            self._outbuffer.append(chr(val))
        else:
            print("".join(self._outbuffer))
            self._outbuffer = []


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    with Path("script.txt").open() as f:
        script = f.readlines()

    provider = InputOutputProvider(script)
    m = Apollo("A", code, provider)
    m.output = provider
    m.run()


if __name__ == "__main__":
    main()
