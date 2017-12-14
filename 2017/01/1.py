#!/usr/bin/env python
'''
    Use matching approach, adding the first element to the tail of the list
    for the wrap-around (circular) effect
'''

import sys

from itertools import izip


def process(line):
    items = [int(x) for x in list(line)]
    items.append(items[0])
    print sum(i for i, j in izip(items, items[1::]) if i == j)


if __name__ == '__main__':
    for line in sys.stdin:
        process(line.strip())
