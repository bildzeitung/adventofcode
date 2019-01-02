#!/usr/bin/env python
'''
    Day 19: Analytical sol'n

    Calculate the sum of all of the divisors of a magic number n.

'''
from math import sqrt, floor

n = 10551428
t = 0

for i in range(1, floor(sqrt(n)) + 1):
    if not (n % i):
        t += i
        t += n // i

print('FINAL', t)
