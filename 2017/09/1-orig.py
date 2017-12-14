#!/usr/bin/env python
'''
    Day 9
'''
import re
import sys

def calc_score(l):
    score = 0
    total = 0
    for x in l:
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

    # replace garbage contents
    regex = re.compile(r'<(.*?)>')
    while True:
        f = regex.search(line)
        if not f:
            break

        start, stop = f.span(1)
        # print start, stop, f.group(0)
        line = line[:start-1] + 'x' + line[stop+1:]

    # print line

    print o, nob, line, calc_score(line)


def main():
    groups = 0
    for line in sys.stdin:
        process(line.strip())

if __name__ == '__main__':
    main()
