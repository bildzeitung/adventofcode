#!/usr/bin/env python
""" 
    Day 9
"""
import sys
from pathlib import Path

from apollo import Apollo


class StdOutput:
    def send(self, val):
        print("->", val)


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    m = Apollo("A", code, [int(sys.argv[2])])
    m.output = StdOutput()
    m.run()


if __name__ == "__main__":
    main()
