#!/usr/bin/env python
'''
    Day 21
'''
import sys

from collections import Counter
from itertools import izip


def rotate2x2(pattern):
    ''' Given a 2x2, return all of its rotations
    '''
    r0, r1 = pattern.split('/')

    for _ in xrange(3):
        tmp = r1[0] + r0[0]
        r1 = r1[1] + r0[1]
        r0 = tmp
        yield r0 + '/' + r1


def rotate3x3(pattern):
    ''' only by 90 degrees
    '''
    r0, r1, r2 = pattern.split('/')

    for _ in xrange(3):
        a = r2[0] + r1[0] + r0[0]
        b = r2[1] + r1[1] + r0[1]
        c = r2[2] + r1[2] + r0[2]
        r0 = a
        r1 = b
        r2 = c
        yield r0 + '/' + r1 + '/' + r2


def flip3x3(pattern):
    ''' Generate all the flip pattern variations
    '''
    # flip vertical
    r0, r1, r2 = pattern.split('/')
    yield '/'.join([r2, r1, r0])

    # flip horizontal
    a = r0[2] + r0[1] + r0[0]
    b = r1[2] + r1[1] + r1[0]
    c = r2[2] + r2[1] + r2[0]
    yield '/'.join([a, b, c])

    # horiz + vert
    yield '/'.join([c, b, a])


def main():
    ''' Given the fixed starting pattern, run 5 iterations
    '''
    pattern = '.#./..#/###'  # magic starting pattern

    # read rules
    ruleset = {}
    for line in sys.stdin:
        rule, synth = [x.strip() for x in line.strip().split('=>')]
        ruleset[rule] = synth

    print 'I read', len(ruleset), 'rules'

    # add all variations in (all rotations + flips + combinations thereof)
    newrules = {}
    for rule, synth in ruleset.iteritems():
        if len(rule) == 5:  # 2x2 rule
            for xrule in rotate2x2(rule):
                newrules[xrule] = synth
        else:  # 3x3 rule
            # take the original rule and rotate it
            for xrule in rotate3x3(rule):
                newrules[xrule] = synth

            # take each flip, add it, and then rotate it
            for xrule in flip3x3(rule):
                newrules[xrule] = synth
                for rrule in rotate3x3(xrule):
                    newrules[rrule] = synth

    ruleset.update(newrules)

    print 'I now have', len(ruleset), 'rules'

    ''' iterate through the system

        Flow:
            - break the string into the proper sized chunks
            - apply the rules
            - combine the new chunks into a single string
    '''
    for item in xrange(int(sys.argv[1])):
        newgrid = []

        # subdivide
        grid = [list(x) for x in pattern.split('/')]
        if len(grid) % 2:
            # odd, so 3x3's
            for y in xrange(0, len(grid), 3):
                newrow = []
                for x in xrange(0, len(grid), 3):
                    block = '/'.join([''.join(r[x:x+3]) for r in grid[y:y+3]])
                    newrow.append(ruleset[block])
                newgrid.append(newrow)
        else:
            # even, so 2x2's
            for y in xrange(0, len(grid), 2):
                newrow = []
                for x in xrange(0, len(grid), 2):
                    block = '/'.join([''.join(r[x:x+2]) for r in grid[y:y+2]])
                    newrow.append(ruleset[block])
                newgrid.append(newrow)

        if len(newgrid) == 1:  # special case
            pattern = newgrid[0][0]
        else:
            # combine results
            rows = []
            for y in newgrid:
                forzip = [i.split('/') for i in y]
                rows.append('/'.join([''.join(a) for a in izip(*forzip)]))
            pattern = '/'.join(rows)

        print 'AFTER ', item + 1
        print 'HASHES:', Counter(pattern)['#']

    # print '\n'.join(pattern.split('/'))


if __name__ == '__main__':
    main()
