#!/usr/bin/env python

import re
import sys

FINDER=re.compile(r'(.)\1*')

start = sys.argv[1]
iters = 50

def genseq(line):
    result = ''

    while line:
        match = FINDER.match(line)
        item = match.group()
        result += str(len(item)) + item[0]
        line = line[len(item):]

    return result

for i in xrange(iters):
    start = genseq(start)
    print i, len(start)

