#!/usr/bin/env python
'''
    Day 9
'''
import re
import sys

def calc_score(l):
    score = 0
    total = 0
    ignore = False
    for x in l:
        if x == '<':
            ignore = True

        if ignore and x != '>':
            continue

        if ignore:
            ignore = False
            continue

        if x == '{':
            score += 1

        if x == '}':
            total += score
            score -= 1

    return total


def process(line):
    o = line
    # remove cancelled pieces
    while line.find('!') > -1:
        p = line.index('!')
        line = line[:p] + line[(p+2):]
    
    nob = line

    print o, nob, line, calc_score(line)


def main():
    groups = 0
    for line in sys.stdin:
        process(line.strip())

if __name__ == '__main__':
    main()
