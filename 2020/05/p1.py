#!/usr/bin/python
"""
  Day 5
"""
import sys


def narrow(bsp, rb):
    """ Kind of a brute-force binary partition
    """
    left, right = 0, rb
    for k in bsp:
        if k == "F" or k == "L":
            right = (right - left) / 2 + left
        else:
            left = (right - left + 1) / 2 + left
    assert left == right
    return left


def main():
    with open(sys.argv[1]) as f:
        return max(narrow(bp[0:7], 127) * 8 + narrow(bp[7:10], 7) for bp in f)


if __name__ == "__main__":
    print(main())
