#!/usr/bin/env python
''' Day 5
'''
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
    print(all_res)

    polymer = load_polymer()
    print(len(polymer), 'units')
    while (True):
        current_len = len(polymer)
        polymer = process(all_res, polymer)
        print(len(polymer), 'units')
        if current_len == len(polymer):
            break


if __name__ == '__main__':
    main()
