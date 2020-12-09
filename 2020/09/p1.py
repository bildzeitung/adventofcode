#!/usr/bin/env python
"""
  Day 9
"""
import sys

from itertools import combinations


def is_sum(l, i):
    """ Do the inefficient thing 
    
        use an O(n^2) algorithm to sort out whether the sum is possible
    """
    return any(i for x in combinations(l, 2) if sum(x) == i)


def main():
    preamble = []
    with open(sys.argv[2]) as f:
        for i in range(int(sys.argv[1])):
            preamble.append(int(f.readline().strip()))
        while i := f.readline().strip():
            i = int(i)
            if is_sum(preamble, i):
                preamble.append(i)
                preamble.pop(0)
            else:
                return i


if __name__ == "__main__":
    print(main())
