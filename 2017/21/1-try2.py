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


def gen_newgrid(size, grid, ruleset):
    ''' Given a grid, subdivide it into size x size blocks and apply rules

        The return value is an array of arrays, where the inner array
        is a row of resolved pattern strings; those can then be
        recombined from being separate blocks into a single block
    '''
    newgrid = []
    for y in xrange(0, len(grid), size):
        newrow = []
        for x in xrange(0, len(grid), size):
            block = '/'.join([''.join(r[x:x+size]) for r in grid[y:y+size]])
            newrow.append(ruleset[block])
        newgrid.append(newrow)

    return newgrid


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

    ''' add all variations in (all rotations + flips + combinations thereof)
        upshot is that only an O(1) lookup is required for each block, instead
        of having to rotate / flip each block until it matches a rule
    '''
    newrules = {}
    for rule, synth in ruleset.iteritems():
        if len(rule) == 5:  # 2x2 rule
            for xrule in rotate2x2(rule):
                newrules[xrule] = synth
        else:  # 3x3 rule
            # take the original rule and rotate it
            for xrule in rotate3x3(rule):
                newrules[xrule] = synth

            # take each flip, add it, and then add rotations of it
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

        # subdivide & apply rules
        grid = [list(x) for x in pattern.split('/')]
        size = len(grid) % 2 + 2
        newgrid = gen_newgrid(size, grid, ruleset)

        # combine results
        pattern = '/'.join(['/'.join([''.join(a)
                                      for a in izip(*[i.split('/') for i in row])
                                      ])
                            for row in newgrid])

        print 'AFTER ', item + 1
        print 'HASHES:', Counter(pattern)['#']

    # print '\n'.join(pattern.split('/'))


if __name__ == '__main__':
    main()
