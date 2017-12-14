#!/usr/bin/env python
""" Day 20 """

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def makefinite(n):
    result = set()
    top = max(n)
    for x in reversed(sorted(n)):
        if x * 50 >= top:
            result.add(x)
        else:
            return result

TARGET = 3090909

START = TARGET / 4
VALUE = sum(makefinite(factors(START)))
print 'START: %s VALUE: %s' % (START, VALUE)
while VALUE < TARGET:
    START += 1
    VALUE = sum(makefinite(factors(START)))

print START, VALUE

