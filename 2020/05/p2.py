#!/usr/bin/python
"""
  Day 5
"""
import sys


def id(bsp):
    return int(
        bsp.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2
    )


def main():
    with open(sys.argv[1]) as f:
        all_seats = sorted(id(bp) for bp in f)
        low = all_seats[0]
        for s in all_seats:
            if low != s:  # mind the gap
                return low
            low += 1


if __name__ == "__main__":
    print(main())
