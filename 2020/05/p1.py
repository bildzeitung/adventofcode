#!/usr/bin/python
"""
  Day 5
"""
import sys


def id(bsp):
    """ Calculate the ID
        - convert the strings to 1's and 0's; let Python convert to int
        - alternately: re.sub("F|L", "0", re.sub("B|R", "1", bsp))
    """
    return int(
        bsp.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2
    )


def main():
    with open(sys.argv[1]) as f:
        return max(id(bp) for bp in f)


if __name__ == "__main__":
    print(main())
