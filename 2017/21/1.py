#!/usr/bin/env python
'''
    Day 21
'''
import sys

# from collections import Counter


def rotations(pattern):
    ''' Given a 2x2, return all of its rotations
    '''
    r0, r1 = pattern.split('/')

    for _ in xrange(3):
        tmp = r1[0] + r0[0]
        r1 = r1[1] + r0[1]
        r0 = tmp
        yield r0 + '/' + r1


def process_2_by_2(pattern, ruleset):
    if pattern in ruleset:
        # print 'Fast match!'
        return ruleset[pattern]
    else:
        for x in rotations(pattern):
            if x in ruleset:
                return ruleset[x]

    raise Exception('Could not resolve 2x2')


def process_by_2(pattern, ruleset):
    ''' Split a 4x4 into quadrants and solve
    '''
    print 'Process 4x4...'
    outlist = []
    subs = pattern.split('/')

    topleft = '/'.join(x[0:2] for x in subs[0:2])
    print 'TL', topleft
    
    topright = '/'.join(x[2:4] for x in subs[0:2])
    print 'TR', topright

    bottomleft = '/'.join(x[0:2] for x in subs[2:4])
    print 'BL', bottomleft

    bottomright = '/'.join(x[2:4] for x in subs[2:4])
    print 'BR', bottomright

    outlist.append(process_2_by_2(topleft, ruleset))
    outlist.append(process_2_by_2(topright, ruleset))
    outlist.append(process_2_by_2(bottomleft, ruleset))
    outlist.append(process_2_by_2(bottomright, ruleset))
    
    return outlist


def rotate3x3(pattern):
    r0, r1, r2 = pattern.split('/')

    for _ in xrange(7):
        a = r1[0] + r0[0] + r0[1]
        b = r2[0] + r1[1] + r0[2]
        c = r2[1] + r2[2] + r1[2]
        r0 = a
        r1 = b
        r2 = c
        yield r0 + '/' + r1 + '/' + r2


def process_by_3(pattern, ruleset):
    print 'Process by 3...', pattern
    if pattern in ruleset:
        # print 'Fast match!', ruleset[pattern]
        return [ruleset[pattern]]
    else:
        for x in rotate3x3(pattern):
            if x in ruleset:
                return [ruleset[x]]

    raise Exception('Incomplete 3x3')


def process(pattern, ruleset):
    new_pattern = []
    for item in pattern:
        # print 'item', item
        if len(item.split('/')[0]) % 2:
            new_pattern.extend(process_by_3(item, ruleset))
        else:
            new_pattern.extend(process_by_2(item, ruleset))
            
    return new_pattern


def main():
    pattern = ('.#./..#/###',)

    ruleset = {}
    for line in sys.stdin:
        rule, synth = [x.strip() for x in line.strip().split('=>')]
        ruleset[rule] = synth

    print 'I have', len(ruleset), 'rules'

    for x in xrange(5):
        pattern = process(pattern, ruleset)
        print 'AFTER ', x + 1, pattern
        print 'ON:', len(''.join(pattern).replace('.', '').replace('/', ''))


if __name__ == '__main__':
    main()
