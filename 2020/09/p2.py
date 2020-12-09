#!/usr/bin/env python
"""
  Day 9

  Solution from part 1: 530627549
"""
import sys


def locate_range(l, i):
    """ Inch worm down the list to find a proper sum
    """
    left = 0
    right = 1
    s = l[0] + l[1]

    while s != i:
        if s < i:
            right += 1
            s += l[right]
        else:
            s -= l[left]
            left += 1

    return l[left : right + 1]


def main():
    with open(sys.argv[2]) as f:
        candidates = [int(i.strip()) for i in f]
        magic_sum = int(sys.argv[1])
        r = locate_range(candidates, magic_sum)
        print(f"Got: {r}")
        return f"{min(r)} + {max(r)} = {min(r) + max(r)} "


if __name__ == "__main__":
    print(main())
