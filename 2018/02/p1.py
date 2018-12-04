#!/usr/bin/env python

import sys
from collections import Counter
from pathlib import Path


def main():
    total_twos = 0
    total_threes = 0
    with Path(sys.argv[1]).open() as f:
        for word in f:
            c = dict(Counter(word))
            total_twos += 2 in c.values()
            total_threes += 3 in c.values()

    print(f"2's: {total_twos}  3's: {total_threes} " f"==> {total_twos * total_threes}")


if __name__ == "__main__":
    main()
