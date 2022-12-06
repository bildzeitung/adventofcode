#!/usr/bin/env python
"""
    Day 6
"""
import sys
from pathlib import Path


def main():
    with Path(sys.argv[1]).open() as f:
        line = next(f).strip()
    
    for idx in range(len(line)):
        s = line[idx:idx+14]
        if len(set(s)) == 14:
            print(idx+14)
            return


if __name__ == "__main__":
    main()