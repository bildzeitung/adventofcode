#!/usr/bin/env python
'''
    Day 23
    -> my approximation of what the assembly is doing
'''


def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def main():
    ''' Count the primes in range [106700, 123717], inclusive, and step by 17
    '''
    print sum(not isprime(x) for x in xrange(106700, 123700+17, 17))


if __name__ == '__main__':
    main()