#!/usr/bin/env python
""" Day 13: part 1 """

from collections import defaultdict
from itertools import izip, permutations

import sys

OPS = {'gain': 1, 'lose': -1}
MASTER = defaultdict(dict)

with open(sys.argv[1]) as source:
    for line in source:
        items = line.rstrip().replace('.', '').split(' ')
        name, oper, amount, name2 = items[0], items[2], items[3], items[-1]
        MASTER[name][name2] = OPS[oper] * int(amount)

class AllCombos(object):
    """ Make an iterator """
    def __iter__(self):
        for combo in permutations(MASTER.keys()):
            table = list(combo)
            table.append(combo[0])
            total = 0
            for item1, item2 in izip(table, table[1:]):
                total += MASTER[item1][item2] + MASTER[item2][item1]

            yield total

print 'BEST: ', max(AllCombos())
