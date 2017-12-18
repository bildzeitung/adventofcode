#!/usr/bin/env python
'''
    Day 17
'''
import sys

ITERS = 50000000


def main(spin):
    buff = -1  # strictly buffer starts at (0), so undef
    idx = 0
    for i in xrange(ITERS):
        idx = (idx + spin) % (i+1) + 1
        if idx == 1:
            buff = i + 1
            print buff

    print 'FINAL', buff


if __name__ == '__main__':
    main(int(sys.stdin.readline().strip()))