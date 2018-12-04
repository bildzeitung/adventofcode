#!/usr/bin/env python
""" Brute force solution

    Look at all pairs; stop when a solution candidate is found.

    The zip / compress business does more work than is strictly
    necessary (stopping after 2nd mismatch is more efficient),
    but is nice and short :)
"""
import sys
from pathlib import Path
from itertools import combinations, compress


def main():
    words = None
    with Path(sys.argv[1]).open() as f:
        words = [word.strip() for word in f]

    # Need a match of all but one character
    target_len = len(words[0]) - 1

    # Brute force; look at all pairs
    for a, b in combinations(words, 2):
        # compress() maps string 'a' against:
        #   [True, False, False, False, ...]
        # so if the string matches by all but one character,
        # then the length of 'x' is the target length
        #
        # zip(a, b) produces [(a[0], b[0]), (a[1], b[1]), ...]
        #
        x = "".join(compress(a, [x[0] == x[1] for x in zip(a, b)]))
        if len(x) == target_len:
            print(a, b, "==>", x)
            break  # Done!


if __name__ == "__main__":
    main()
