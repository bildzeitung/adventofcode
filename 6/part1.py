#!/usr/bin/env python

import numpy
import sys

m = numpy.zeros((1000, 1000), dtype=numpy.int)

turn = {'on': 1, 'off': 0}

def str2coord(item):
    return [int(x) for x in item.split(',')]

with open(sys.argv[1]) as instructions:
    for line in instructions:
        # [turn <on|off>|toggle] <coord> through <coord>
        elements = line.rstrip().split(' ')

        if elements[0] == 'turn':
            value = turn[elements[1]]
            from_coord = str2coord(elements[2])
            to_coord = str2coord(elements[4])

            xslice = slice(from_coord[0], to_coord[0]+1)
            yslice = slice(from_coord[1], to_coord[1]+1)

            m[xslice, yslice] = value
        else:
            from_coord = str2coord(elements[1])
            to_coord = str2coord(elements[3])

            xslice = slice(from_coord[0], to_coord[0]+1)
            yslice = slice(from_coord[1], to_coord[1]+1)

            m[xslice, yslice] = (m[xslice, yslice] + 1) % 2
    
print '{0} lights are on'.format(sum(sum(m)))
