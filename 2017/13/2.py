#!/usr/bin/env python
'''
    Day 13
'''
import sys

def run(layers, delay):
    return any(not ((delay + l) % d) for l, d in layers.iteritems())


def main():
    ''' Day 13 '''
    layers = dict((int(l), int(d)) for l, d in 
                  [line.strip().split(':') for line in sys.stdin])
    scanner_cycles = dict((x, (layers[x]-2) * 2 + 2) for x in layers.keys())

    delay = 0
    while run(scanner_cycles, delay):
        delay += 1

    print delay


if __name__ == '__main__':
    main()
