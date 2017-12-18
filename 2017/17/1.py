#!/usr/bin/env python
'''
    Day 17
'''
import sys


def main(spin):
    buffer = [0, 1]
    idx = 1
    for i in xrange(2, 2018):
        idx = (idx + spin) % len(buffer)
        buffer = buffer[:idx+1] + [i] + buffer[idx+1:]
        idx += 1
        # print 'i', i, 'idx', idx, 'buffer', buffer

    print buffer[idx-3:idx+3]

if __name__ == '__main__':
    main(int(sys.stdin.readline().strip()))