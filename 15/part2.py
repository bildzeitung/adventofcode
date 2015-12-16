#!/usr/bin/env python
""" Day 15 """

import numpy as np
import sys

COOKIES = []
CALORIES = []
with open(sys.argv[1]) as infile:
    for line in infile:
        values = line.rstrip().split(' ')
        COOKIES.append([int([x.replace(',', '')
                             for x in values][y]) for y in (2, 4, 6, 8)])
        CALORIES.append(int(values[-1]))

def get_next(size):
    """ Calc next set of factors """
    prev = [0] * size
    prev[0] = 100

    while sum(prev) > 0:
        output = np.array(prev)
        #
        # part 2: filter for caloric value
        #
        if np.dot(output, CALORIES) == 500:
            yield output

        for idx in xrange(len(prev)-1, -1, -1):
            if not prev[idx]:
                continue

            prev[idx] -= 1

            if (idx+1) < len(prev):
                prev[idx+1] = 100 - sum(prev)

            if sum(prev) < 100:
                prev[idx] = 0
                continue

            break

MATRIX = np.array(COOKIES)
CALORIES = np.array(CALORIES)

def score():
    """ Calculate per-combo score """
    for item in get_next(len(COOKIES)):
        product = np.dot(item, MATRIX).clip(0)
        yield np.product(product)

print 'BEST SCORE: ', max(x for x in score())
