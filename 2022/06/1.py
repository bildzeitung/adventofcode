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
        if len(set(line[idx:idx+4])) == 4:
            print(idx+4)
            return


if __name__ == "__main__":
    main()