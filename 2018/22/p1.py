#!/usr/bin/env python
'''
    Day 22
'''
import sys
from pathlib import Path

ETYPES = ['.', '=', '|']


def display(regions, T):
    total = 0
    for y in range(0, T[1] + 1):
        rc = ''
        for x in range(0, T[0] + 1):
            if (x, y) == T:
                rc += 'T'
            else:
                rc += regions[(x, y)]
        print(rc)

    total = 0
    total += sum(i == '=' for i in regions.values())
    total += 2 * sum(i == '|' for i in regions.values())

    print('TOTAL', total)


def process(depth, target):
    erosion = {}
    regions = {}
    T = (target[0], target[1])
    for y in range(0, target[1] + 1):
        for x in range(0, target[0] + 1):
            pos = (x, y)
            if pos == (0, 0):
                geo_index = 0
            if pos == T:
                geo_index = 0
            elif y == 0:
                geo_index = x * 16807
            elif x == 0:
                geo_index = y * 48271
            else:
                geo_index = erosion[(x - 1, y)] * erosion[(x, y - 1)]
            erosion[pos] = (geo_index + depth) % 20183
            regions[pos] = ETYPES[erosion[pos] % 3]
    display(regions, T)


def main():
    with Path(sys.argv[1]).open() as f:
        depth = int(f.readline().split(':')[1].strip())
        target = [int(x) for x in
                  f.readline().split(':')[1].strip().split(',')]
        print('DEPTH', depth)
        print('TARGET', target)
    process(depth, target)


if __name__ == "__main__":
    main()
