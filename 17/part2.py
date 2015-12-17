#!/usr/bin/env python
""" Day 17 """

from collections import defaultdict

TARGET = 150  # fill 150 litres

with open('containers.in') as infile:
    CONTAINERS = sorted([int(line.rstrip()) for line in infile], reverse=True)

def solver(items, partial=TARGET, span=0):
    """ brute force tree searcher

        span is the number of containers used so far in the solution
    """
    if partial == 0:
        return [span]

    # prune branches that cannot lead to a solution
    if sum(items) < partial:
        return []

    count = []
    for idx, remaining in enumerate(items):
        # would the next step be too big? optimise this away
        if partial - remaining < 0:
            continue

        count.extend(solver(items[idx+1:], partial - remaining, span + 1))

    return count

# consolidate results
SOLUTION = defaultdict(int)
for item in solver(CONTAINERS):
    SOLUTION[item] += 1

# get the smallest # of items required for a solution, and the number of
# instances of solutions of that size
print 'MAGIC ANSWER: %s' % SOLUTION[min(SOLUTION.keys())]
