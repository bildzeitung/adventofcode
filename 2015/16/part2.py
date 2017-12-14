#!/usr/bin/env python
""" Day 16 """

# load profile
with open('ticker.in') as data:
    PROFILE = dict((x, int(y)) for x, y in
                   [line.rstrip().split(': ') for line in data])

# match against memory
UNSPECIAL = set(PROFILE.keys()) - set(('cats', 'trees', 'pomeranians', 'goldfish'))
with open('sue.in') as data:
    for line in data:
        sue = line.rstrip().split(':')[0]
        memory = ':'.join(line.rstrip().split(': ')[1:]).split(', ')
        memory = dict((x, int(y)) for x, y in [z.split(':') for z in memory])

        #
        # special case handline for ranges
        #
        special = ('cats', 'trees')
        if [item for item in special if item in memory and memory[item] <= PROFILE[item]]:
            continue

        special = ('pomeranians', 'goldfish')
        if [item for item in special if item in memory and memory[item] >= PROFILE[item]]:
            continue

        #
        # straight-up profile matching
        #
        if [item for item in UNSPECIAL if item in memory and memory[item] != PROFILE[item]]:
            continue

        print sue
