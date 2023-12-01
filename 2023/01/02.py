#!/bin/env python
"""
    Day 1

    - got tripped up by overlapping matches!
    - instead of doing anything fancy, use 3rd party regex module, as it
      supports finding overlapping matches out of the box

"""
import regex as re
import sys
from pathlib import Path
from operator import itemgetter


def main():
    regex = re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")
    lookup = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    g = itemgetter(0, -1)
    h = lambda x: lookup[x[0]] * 10 + lookup[x[1]]
    with Path(sys.argv[1]).open() as f:
        return sum(h(g(re.findall(regex, line, overlapped=True))) for line in f)
        #for line in f:
        #    r = re.findall(regex, line, overlapped=True)
        #    print(line.strip(), r, h(g(r)))


if __name__ == "__main__":
    print(main())
