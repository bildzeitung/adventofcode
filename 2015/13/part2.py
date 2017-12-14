#!/usr/bin/env python
""" Day 13: part 2 """

from collections import defaultdict
from itertools import permutations

import sys

OPS = {'gain': 1, 'lose': -1}
MASTER = defaultdict(dict)

with open(sys.argv[1]) as source:
    for line in source:
        items = line.rstrip().replace('.', '').split(' ')
        name, oper, amount, name2 = items[0], items[2], items[3], items[-1]
        MASTER[name][name2] = OPS[oper] * int(amount)

    # add apathetic me into the mix
    for key in MASTER.keys():
        MASTER[key]['me'] = 0
        MASTER['me'][key] = 0

def calc(combo):
    """ Calculate a table """
    table = list(combo) + [combo[0]]
    return sum(MASTER[item1][item2] + MASTER[item2][item1]
               for item1, item2 in zip(table, table[1:]))

print 'BEST: ', max(calc(combo) for combo in permutations(MASTER.keys()))

