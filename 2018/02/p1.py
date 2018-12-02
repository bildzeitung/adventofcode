#!/usr/bin/env python

import sys
from collections import Counter
from pathlib import Path


def get_checksum(word):
    has_two = 0
    has_three = 0
    c = dict(Counter(word))
    if 2 in c.values():
        has_two = 1
    if 3 in c.values():
        has_three = 1

    return has_two, has_three


def main():
    total_twos = 0
    total_threes = 0
    with Path(sys.argv[1]).open() as f:
        for word in f:
            twos, threes = get_checksum(word.strip())
            total_twos += twos
            total_threes += threes

    print(f"2's: {total_twos}  3's: {total_threes} "
          f"==> {total_twos * total_threes}")


if __name__ == "__main__":
    main()
