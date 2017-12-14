#!/usr/bin/env python
""" Day 20 """
from math import sqrt

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

TARGET = 3400000
#TARGET = 15

print 'TARGET: %s' % TARGET

START = int(sqrt(TARGET))
VALUE = sum(factors(START))+1
print 'START: %s VALUE: %s' % (START, VALUE)
while VALUE < TARGET:
    START += 1
    VALUE = sum(factors(START))

print START, VALUE
