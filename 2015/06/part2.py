#!/usr/bin/env python

import numpy
import sys

m = numpy.zeros((1000, 1000), dtype=numpy.int)

turn = {'on': 1, 'off': -1}

def str2coord(item):
    return [int(x) for x in item.split(',')]

def getslice(pfrom, pto):
    pfrom, pto = str2coord(pfrom), str2coord(pto)
    x, y = slice(pfrom[0], pto[0]+1), slice(pfrom[1], pto[1]+1)

    return x, y

with open(sys.argv[1]) as instructions:
    for line in instructions:
        # [turn <on|off>|toggle] <coord> through <coord>
        elements = line.rstrip().split(' ')

        if elements[0] == 'turn':
            value = turn[elements[1]]
            xslice, yslice = getslice(elements[2], elements[4])

            # clamp floor value to 0 (no negative brightness)
            m[xslice, yslice] = numpy.maximum(m[xslice, yslice] + value, 0)
        else:
            xslice, yslice = getslice(elements[1], elements[3])
            m[xslice, yslice] = m[xslice, yslice] + 2
    
print '{0} total brightness'.format(sum(sum(m)))
