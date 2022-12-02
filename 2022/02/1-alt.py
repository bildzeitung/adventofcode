#!/usr/bin/env python
"""
    Day 2
"""
import sys
from pathlib import Path

states = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

with Path(sys.argv[1]).open() as f:
    print(f"Total: {sum(states[line.strip()] for line in f)}")
