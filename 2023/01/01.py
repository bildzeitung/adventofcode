#!/bin/env python
"""
    Day 1
"""
import re
import sys
from pathlib import Path


def main():
    with Path(sys.argv[1]).open() as f:
        return sum(
            (int)(re.search(r"\d", line)[0]) * 10
            + (int)(re.search(r"\d", line[::-1])[0])
            for line in f
        )


if __name__ == "__main__":
    print(main())
