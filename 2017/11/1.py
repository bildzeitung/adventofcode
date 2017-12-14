#!/usr/bin/env python
'''
    Day 11

    Uses: https://www.redblobgames.com/grids/hexagons/

'''
# import operator
import sys

MAP = {'s': (0, -1, 1),
       'sw': (-1, 0, 1),
       'nw': (-1, 1, 0),
       'n': (0, 1, -1),
       'ne': (1, 0, -1),
       'se': (1, -1, 0)
       }


def cube_dist(loc):
    return sum(abs(x) for x in loc) / 2


def process(walk):
    loc = (0, 0, 0)
    for step in walk:
        loc = tuple(i[0] + i[1] for i in zip(MAP[step], loc))

    print loc, cube_dist(loc)


def main():
    for line in sys.stdin:
        process(line.strip().split(','))


if __name__ == '__main__':
    main()
