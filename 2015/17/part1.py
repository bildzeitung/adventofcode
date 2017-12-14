#!/usr/bin/env python
""" Day 17 """

# fill 150 litres
TARGET = 150

with open('containers.in') as infile:
    CONTAINERS = sorted([int(line.rstrip()) for line in infile], reverse=True)

def solver(items, partial=TARGET):
    """ brute force tree searcher """
    if partial == 0:
        print 'GOT: * %s | %s' % (partial, items)
        return 1

    print 'GOT: %s | %s' % (partial, items)

    # prune branches that cannot lead to a solution
    if sum(items) < partial:
        return 0

    count = 0
    for idx, remaining in enumerate(items):
        # would the next step be too big? optimise this away
        if partial - remaining < 0:
            continue

        count += solver(items[idx+1:], partial - remaining)

    return count

print solver(CONTAINERS)
