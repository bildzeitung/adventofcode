#!/usr/bin/env python
''' Supplemental: find most common 2-digit in a list of primes
'''
import operator
from collections import defaultdict
from pathlib import Path


def main():
    track = defaultdict(int)
    with Path("./numbers.txt").open() as f:
        for line in f:
            numbers = [x for x in line.strip().split(' ')]
            for n in numbers:
                for k in [''.join(x) for x in zip(n, n[1:])]:
                    track[k] += 1

    for k in sorted(track.items(), key=operator.itemgetter(1)):
        print(k)


if __name__ == "__main__":
    main()
