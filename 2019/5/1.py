#!/usr/bin/env python
""" 
    Day 5
"""
import sys
from pathlib import Path

from apollo import Apollo


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    Apollo(code).run()


if __name__ == "__main__":
    main()
