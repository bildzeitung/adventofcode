#!/usr/bin/python
"""
  Day 5
"""
import sys


def narrow(bsp):
    """ Type conversion is hard; let Python do it
    """
    return int(
        bsp.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2
    )


def main():
    with open(sys.argv[1]) as f:
        return max(narrow(bp[0:7]) * 8 + narrow(bp[7:10]) for bp in f)


if __name__ == "__main__":
    print(main())
