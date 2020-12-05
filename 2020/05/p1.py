#!/usr/bin/python
"""
  Day 5
"""
import sys


def id(bsp):
    """ Calculate the ID
        - convert the strings to 1's and 0's; let Python convert to int
        - the "000" is a left-shift by 2^3, or 8
    """
    return int(bsp[0:7].replace("F", "0").replace("B", "1") + "000", 2) + int(
        bsp[7:10].replace("L", "0").replace("R", "1"), 2
    )


def main():
    with open(sys.argv[1]) as f:
        return max(id(bp) for bp in f)


if __name__ == "__main__":
    print(main())
