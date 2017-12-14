#!/usr/bin/env python
'''
    Day 10
'''
import sys


def process(string, length, skip, idx):
    lm = string + string
    print 'length', length
    print 'before', lm
    lm[idx:idx+length] = reversed(lm[idx:idx+length])
    print 'after ', lm

    final = idx + length
    if final > len(string):
        # print 'here'
        overage = idx + length - len(string)
        # wrap-around case
        # print lm
        beginning = lm[len(string):len(string)+overage]
        rest = lm[overage:len(string)]
        print 'over', overage, 'beginning', beginning, 'rest', idx, len(string)-overage, rest
        return beginning + rest
    
    return lm[:len(string)]


def main():
    string = range(256)
    # string = range(5)
    print 'START', string
    for line in sys.stdin:
        lengths = [int(x) for x in line.strip().split(',')]
    
    idx = 0
    skip = 0
    for length in lengths:
        string = process(string, length, skip, idx)
        idx = (idx + skip + length) % len(string)
        skip += 1
        print idx, skip, '|', string

    print 'ANSWER', string[0] * string[1]

if __name__ == '__main__':
    main()