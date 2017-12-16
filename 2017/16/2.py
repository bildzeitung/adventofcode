#!/usr/bin/env python
'''
    Day 16
'''
import sys


def dance(moves, a):
    for move in moves:
        m, x = move[0], move[1:]
        if m == 's':  # spin
            x = int(x)
            a = a[-x:] + a[0:len(a)-x]
        elif m == 'x':  # exchange
            x, y = [int(x) for x in x.split('/')]
            a[x], a[y] = a[y], a[x]
        else:  # partner
            x, y = x.split('/')
            x = a.index(x)
            y = a.index(y)
            a[x], a[y] = a[y], a[x]

    return a


def main():
    for line in sys.stdin:
        moves = line.strip().split(',')

    # list of all permutations
    config = ['abcdefghijklmnop']
    a = list('abcdefghijklmnop')
    x = 1
    while True:
        # at some point, this cycles
        a = dance(moves, a)
        s = ''.join(a)
        if s in config:
            print 'CYCLE AT', x
            break
        config.append(s)
        x += 1

    # turns out it cycles back to 'abcdef....', so that's nice
    # cycle length determines position after 1 billion dances
    print config[1000000000 % x]


if __name__ == '__main__':
    main()