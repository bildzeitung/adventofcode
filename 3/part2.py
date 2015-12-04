#!/usr/bin/env python
import sys

path = open(sys.argv[1]).read().rstrip()

memo = set()
sx, sy = 0, 0
rx, ry = 0, 0

for i,j in zip(path[::2], path[1::2]):
    memo.add('%s|%s' % (sx, sy))
    memo.add('%s|%s' % (rx, ry))

    if i == '>':
        sx += 1
    elif i == '<':
        sx -= 1
    elif i == '^':
        sy -= 1
    elif i == 'v':
        sy += 1
    else:
        raise Exception('bad op')

    if j == '>':
        rx += 1
    elif j == '<':
        rx -= 1
    elif j == '^':
        ry -= 1
    elif j == 'v':
        ry += 1
    else:
        raise Exception('bad op')

memo.add('%s|%s' % (sx, sy))
memo.add('%s|%s' % (rx, ry))

print 'UNIQUE HOUSES: %s' % len(memo)
