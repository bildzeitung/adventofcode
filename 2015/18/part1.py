#!/usr/bin/env python
""" Day 18 """

import sys


with open(sys.argv[1]) as infile:
    GRID = ['.' + line.rstrip() + '.' for line in infile]

GRID.insert(0, '.' * len(GRID[0]))
GRID.append('.' * len(GRID[0]))

print '\n'.join(GRID), '\n'

REMAP = {'.': 0, '#': 1}
GRID = [[REMAP[char] for char in line]
        for line in GRID]

def churn(start):
    """ Calculate next generation in Conway's Game of Life """
    finish = [[0] * len(start[0])]
    for idx, row in enumerate(GRID[1:-1]):
        nextrow = [0] * len(row)
        for idy, col in enumerate(row[1:-1]):
            neighbours = sum(start[idx][idy:idy+3]) + \
                         sum(row[idy:idy+3]) + \
                         sum(start[idx+2][idy:idy+3])

            if col:  # lit
                if 1 < (neighbours - 1) < 4:
                    nextrow[idy+1] = 1
            else:  # unlit
                if neighbours == 3:
                    nextrow[idy+1] = 1

        finish.append(nextrow)
    finish.append([0] * len(start[0]))

    return finish

for _ in xrange(int(sys.argv[2])):
    GRID = churn(GRID)
    for line in GRID:
        print ''.join([{0: '.', 1: '#'}[i] for i in line])
    print '\n'

print 'LIGHTS: ', sum(sum(row) for row in GRID)
