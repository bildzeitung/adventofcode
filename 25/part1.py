#!/usr/bin/env python
""" Day 25 """

# To continue, please consult the code grid in the manual.
# Enter the code at row 2947, column 3029.

ROW = 2947
N = 1 + (ROW * ROW - ROW) / 2

COL = 3029
CANTOR = N + ((COL-1) * (2*ROW + COL)) / 2

print CANTOR

START = 20151125
for x in xrange(CANTOR-1):
    START = (START * 252533) % 33554393

print START
