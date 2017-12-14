#!/usr/bin/env python
'''
    Straight up matching approach -- rotate the list by 1/2 and sum if equal
'''

import sys

from collections import deque
from itertools import izip


def process(line):
    items = [int(x) for x in list(line)]
    r = deque(items)
    r.rotate(len(items)/2)
    print sum(i for i, j in izip(items, r) if i == j)


if __name__ == '__main__':
    for line in sys.stdin:
        process(line.strip())
