#!/usr/bin/env python
'''
    Day 23
'''
import re
import sys

from pathlib import Path


DATARE = re.compile(r'<(.+)>.+=(\d+)')


def main():
    bots = []
    with Path(sys.argv[1]).open() as f:
        # pos=<0,0,0>, r=4
        for line in f:
            pos, radius = DATARE.search(line).groups()
            pos = tuple(int(x) for x in pos.split(','))
            radius = int(radius)
            bots.append((pos, radius))
    best = max(bots, key=lambda x: x[1])
    bpos = best[0]
    total = 0
    for x in bots:
        xpos = x[0]
        if sum(abs(a - b) for a, b in zip(bpos, xpos)) <= best[1]:
            total += 1
    print('IN RANGE', total)


if __name__ == '__main__':
    main()
