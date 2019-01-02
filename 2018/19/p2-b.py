#!/usr/bin/env python
'''
    Day 19: Analytical sol'n

    Calculate the sum of all of the divisors of a magic number n.

'''
n = 10551428
t = 0

for i in range(1, n + 1):
    if not (n % i):
        t += i

print('FINAL', t)
