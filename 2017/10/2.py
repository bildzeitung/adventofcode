#!/usr/bin/env python
'''
    Day 10
'''
import operator
import sys


def process(string, length, skip, idx):
    ''' wrap-around case is annoying; double up the string to compensate

        Once the string is doubled, can always reverse a contiguous
        part of it.
    '''
    lm = string + string
    lm[idx:idx+length] = reversed(lm[idx:idx+length])

    if (idx + length) > len(string):
        overage = idx + length
        beginning = lm[len(string):overage]
        rest = lm[overage - len(string):len(string)]
        return beginning + rest
    
    return lm[:len(string)]


def main():
    string = range(256)
    for line in sys.stdin:
        lengths = [ord(x) for x in list(line.strip())]

    # as per problem, drop in some magic numbers
    magic = (17, 31, 73, 47, 23)
    lengths.extend(magic)

    idx = 0
    skip = 0

    # ok, do 64 rounds of this madness
    for _ in xrange(64):
        for length in lengths:
            string = process(string, length, skip, idx)
            idx = (idx + skip + length) % len(string)
            skip += 1

    # ok, now we have sparse hash; need dense hash
    dense = []
    for i in xrange(0, 256, 16):
        dense.append('%0.2X' % reduce(operator.xor, string[i:i+16]))

    print 'DENSE HASH:', ''.join(dense).lower()


if __name__ == '__main__':
    main()