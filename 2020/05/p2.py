#!/usr/bin/python
"""
  Day 5
"""
import sys


def getrow(bsp):
    left = 0
    right = 127
    for k in bsp:
        if k == "F":
            right = (right - left) / 2 + left
        else:
            left = (right - left + 1) / 2 + left
    assert left == right
    return left


def getcol(bsp):
    left = 0
    right = 7
    for k in bsp:
        if k == "L":
            right = (right - left) / 2 + left
        else:
            left = (right - left + 1) / 2 + left
    assert left == right
    return left


def main():
    with open(sys.argv[1]) as f:
        all_seats = [getrow(bp[0:7]) * 8 + getcol(bp[7:10]) for bp in f]
        all_seats = sorted(all_seats)
        low = all_seats[0]
        for s in all_seats:
            if low != s:
                return low
            low += 1


if __name__ == "__main__":
    print(main())
