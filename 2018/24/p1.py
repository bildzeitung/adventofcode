#!/usr/bin/env python
'''
    Day 24: Yet Another Game Simulation
'''
import re
import sys
from pathlib import Path

TEAMRE = re.compile(r'^(.+):$')


def main():
    with Path(sys.argv[1]).open() as f:
        for line in f:
            line = line.strip()
            if TEAMRE.search(line):
                team = TEAMRE.search(line).groups()[0]
                print('TEAM', team)


if __name__ == '__main__':
    main()
