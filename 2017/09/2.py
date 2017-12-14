#!/usr/bin/env python
'''
    Day 9
'''
import sys

def calc_score(l):
    total = 0
    ignore = False
    for x in l:
        if x == '<' and not ignore:
            ignore = True
            continue

        if ignore and x != '>':
            total += 1
            continue

        ignore = False

    return total


def process(line):
    # remove cancelled pieces
    while line.find('!') > -1:
        p = line.index('!')
        line = line[:p] + line[(p+2):]
    
    print line, calc_score(line)


def main():
    for line in sys.stdin:
        process(line.strip())

if __name__ == '__main__':
    main()
