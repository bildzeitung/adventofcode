#!/usr/bin/env python
#
# The key property here is that this is a complete graph; that makes the
# algorithm a brute force O(n^2) affair
#
import sys

from collections import defaultdict
from copy import deepcopy

# load in data
master = defaultdict(dict)
with open(sys.argv[1]) as source:
    for line in source:
        a, _, b, _, dist = line.rstrip().split(' ')
        master[a][b] = int(dist)
        master[b][a] = int(dist)

# simple greedy search
def doit(start, master):
    total = 0 
    while master[start]:
        dest = master[start]
        shortest = sorted(dest, key=dest.get, reverse=True)[0]
        print '%s -> %s (%s)' % (start, shortest, dest[shortest]) 
        total += dest[shortest]
        del master[start]
        for value in master.itervalues():
            del value[start]
        start = shortest

    print '---> %s' % total
    return total

print sorted([doit(start, deepcopy(master)) for start in master.keys()])[-1]
