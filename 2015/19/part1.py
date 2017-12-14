#!/usr/bin/env python
""" Day 19 """

import re
import sys

from collections import defaultdict

MOLECULES = defaultdict(set)

with open(sys.argv[1]) as infile:
    for line in infile:
        if not line.rstrip():
            break

        orig, _, target = line.rstrip().split(' ')
        MOLECULES[orig].add(target)

    START = infile.next().rstrip()

print MOLECULES

SOLUTIONS = set()

for key, val in MOLECULES.iteritems():
    rec = re.compile(key)
    for item in rec.finditer(START):
        for repl in val:
            SOLUTIONS.add(START[0:item.start()] + repl + START[item.end():])

print ', '.join(SOLUTIONS)
print '%s MOLECULES' % len(SOLUTIONS)
