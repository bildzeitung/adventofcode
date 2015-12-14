#!/usr/bin/env python
""" Day 14 """

import sys

from collections import defaultdict

REINDEER = {}
WINNERS = defaultdict(int)

with open(sys.argv[1]) as infile:
    for line in infile:
        parts = line.rstrip().split(' ')
        REINDEER[parts[0]] = [int(parts[3]), int(parts[6]), int(parts[13])]

RACE = int(sys.argv[2])

def total_travelled(reindeer, race):
    """ Calc total distance """
    speed, duration, rest = reindeer
    pairs = race / (duration + rest)
    total_dist = speed * pairs * duration

    total_dist += min(duration, race % (duration + rest)) * speed

    return total_dist

#
# this time, run each race to calculate points each second
#
for x in xrange(RACE):
    RUN = dict((name, total_travelled(val, x)) for name, val in REINDEER.iteritems())
    WINNERS[sorted(RUN, key=RUN.get)[-1]] += 1

print max(WINNERS.values())
