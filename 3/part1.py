#!/usr/bin/env python

path = open('santa.in').read().rstrip()

memo = set()
x, y = 0, 0

for i in path:
    memo.add('%s|%s' % (x, y))
    if i == '>':
        x += 1
    elif i == '<':
        x -= 1
    elif i == '^':
        y -= 1
    elif i == 'v':
        y += 1
    else:
        raise Exception('bad op')

memo.add('%s|%s' % (x, y))

print 'UNIQUE HOUSES: %s' % len(memo)
