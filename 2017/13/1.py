#!/usr/bin/env python
'''
    Day 13
'''
import sys


def main():
    ''' Day 13 '''
    layers = dict((int(l), int(d)) for l, d in 
                  [line.strip().split(':') for line in sys.stdin])
    scanners = dict((x, 0) for x in layers.keys())
    scanner_dirs = dict((x, 1) for x in layers.keys())

    severity = 0
    current = -1
    last_layer = sorted(layers.keys())[-1]
    while current <= last_layer:
        current += 1
        # is a scanner there?
        if current in scanners and scanners[current] == 0:
            print 'Collision layer', current, 'depth', layers[current]
            severity += current * layers[current]

        # move scanners
        for i in scanners.keys():
            scanners[i] += scanner_dirs[i]
            if scanners[i] == layers[i] - 1 or not scanners[i]:
                scanner_dirs[i] = -scanner_dirs[i]
            
    print 'TOTAL SEVERITY:', severity


if __name__ == '__main__':
    main()
