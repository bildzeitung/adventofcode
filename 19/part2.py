#!/usr/bin/env python
""" Day 19: Good Thing It's An Easy Language """

import re
import sys

from collections import defaultdict

MOLECULES = defaultdict(set)
REDUCTIONS = {}

with open(sys.argv[1]) as infile:
    for line in infile:
        if not line.rstrip():
            break

        orig, _, target = line.rstrip().split(' ')
        MOLECULES[orig].add(target)
        REDUCTIONS[target] = orig

    START = infile.next().rstrip()

# Sort by longest substring, so get greedy reductions
SORTED_REDUCTIONS = list(sorted(REDUCTIONS,
                                key=lambda x: '{:2d}{}'.format(len(x), str(reversed(x))),
                                reverse=True))

# pre-compile regexes, for speed!
RE_REDUCTIONS = list((x, re.compile(x)) for x in SORTED_REDUCTIONS)

def shrink(string):
    """ Recursive bottom-up parser """
    print 'Analysing %s' % string

    if string == 'e':  # start symbol; finished
        return 0

    for item, regex in RE_REDUCTIONS:
        repl = regex.search(string)
        if repl:
            print 'found %s (reduces to %s)' % (item, REDUCTIONS[item])

            new_str = string[0:repl.start()] + REDUCTIONS[item] + string[repl.end():]

            # guard against trying to reduce to start symbol too early
            if 'e' in new_str and new_str != 'e':
                print 'Cannot reduce to e just yet'
                continue

            return 1 + shrink(new_str)

    # if no valid reductions are possible, then this is
    # not a valid string in the language
    assert False, 'Cannot reduce to start symbol'

print 'TRANSFORMATIONS REQUIRED: %s' % shrink(START)
