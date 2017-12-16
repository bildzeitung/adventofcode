#!/usr/bin/env python
'''
    Day 16
'''
import sys

PROGRAMS = 16


def dance(moves):
    a = [chr(ord('a')+i) for i in range(PROGRAMS)]
    for move in moves:
        m, x = move[0], move[1:]
        if m == 's':
            x = int(x)
            a = a[-x:] + a[0:len(a)-x]
        elif m == 'x':
            x, y = [int(x) for x in x.split('/')]
            a[x], a[y] = a[y], a[x]
        else:
            x, y = x.split('/')
            x = a.index(x)
            y = a.index(y)
            a[x], a[y] = a[y], a[x]

    print ''.join(a)


def main():
    for line in sys.stdin:
        dance(line.strip().split(','))


if __name__ == '__main__':
    main()