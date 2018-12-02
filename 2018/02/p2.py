#!/usr/bin/env python

import sys
from pathlib import Path
from itertools import combinations, compress


def hamming(a, b):
    return len(a) - sum(x[0] == x[1] for x in zip(a, b))


def main():
    words = None
    with Path(sys.argv[1]).open() as f:
        words = [word.strip() for word in f]

    for a, b in combinations(words, 2):
        if hamming(a, b) == 1:
            print(a, b, '==>',
                  f"{''.join(compress(a, [x[0] == x[1] for x in zip(a, b)]))}")


if __name__ == "__main__":
    main()
