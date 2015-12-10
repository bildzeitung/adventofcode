#!/usr/bin/env python

import sys

start = sys.argv[1]
iters = int(sys.argv[2])

def genseq(line):
    result = ''

    start = line[0]
    runlength = 1
    for i in line[1:]:
        if i == start:
            runlength += 1
        else:
            result += str(runlength) + start
            start = i
            runlength = 1

    result += str(runlength) + start

    return result

for i in xrange(iters):
    start = genseq(start)
    print i+1, len(start)

