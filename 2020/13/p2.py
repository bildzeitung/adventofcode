#!/usr/bin/env python
"""
  Day 13
"""
import math
import sys


def main():
    with open(sys.argv[1]) as f:
        _ = f.readline()  # ignore for part 2

        num, rem = [], []
        for i, x in enumerate(f.readline().strip().split(",")):
            if x == "x":
                continue
            num.append(int(x))
            rem.append(i)

    # Chinese Remainder solver
    # https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
    prod = math.prod(num)
    pp = [prod // x for x in num]
    # TIL! Python 3.8 has a Modular Multiplicative Inverse function!
    inv = [pow(pp[i], -1, x) for i, x in enumerate(num)]
    print(prod, pp, inv)
    earliest = sum(rem[x] * pp[x] * inv[x] for x in range(len(num))) % prod
    print(earliest)
    return prod - earliest


if __name__ == "__main__":
    print(main())
