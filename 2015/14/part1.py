#!/usr/bin/env python
""" Day 14 """

import sys

REINDEER = []
with open(sys.argv[1]) as infile:
    for line in infile:
        parts = line.rstrip().split(' ')
        REINDEER.append([int(parts[3]), int(parts[6]), int(parts[13])])

RACE = int(sys.argv[2])

def total_travelled(reindeer):
    """ Calc total distance """
    speed, duration, rest = reindeer
    pairs = RACE / (duration + rest)
    total_dist = speed * pairs * duration

    total_dist += min(duration, RACE % (duration + rest)) * speed

    return total_dist

print max(total_travelled(x) for x in REINDEER)
