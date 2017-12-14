#!/usr/bin/env python
""" Day 16 """

# load profile
with open('ticker.in') as data:
    PROFILE = dict((x, int(y)) for x, y in
                   [line.rstrip().split(': ') for line in data])

# simply search data against the profile
ANALYSIS = {}
with open('sue.in') as data:
    for line in data:
        sue = line.rstrip().split(':')[0]
        memory = ':'.join(line.rstrip().split(': ')[1:]).split(', ')
        memory = dict((x, int(y)) for x, y in [z.split(':') for z in memory])

        # if anything doesn't match, try the next Sue
        if [key for key, val in PROFILE.iteritems() if key in memory and memory[key] != val]:
            continue

        print sue
