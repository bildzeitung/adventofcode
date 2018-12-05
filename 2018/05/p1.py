#!/usr/bin/env python
""" Day 5

    Brute force string replacement.

    The correct solution, a 1-pass, analyzes the string one character
    at a time, keeping a hold of last character of the processed string.

    This solution does replacements until there are no more replacements
    to be done. This is considerably worse.
"""
import string
import sys
from pathlib import Path


def process(res, polymer):
    c = polymer
    for replacement in res:
        c = c.replace(replacement, "")

    return c


def load_polymer():
    with Path(sys.argv[1]).open() as f:
        return f.readline().strip()


def main():
    all_res = []
    for (uc, lc) in zip(string.ascii_uppercase, string.ascii_lowercase):
        all_res.append(f"{uc}{lc}")
        all_res.append(f"{lc}{uc}")

    polymer = load_polymer()
    print(len(polymer), "units")
    while True:
        current_len = len(polymer)
        polymer = process(all_res, polymer)
        print(len(polymer), "units")
        if current_len == len(polymer):
            break


if __name__ == "__main__":
    main()
