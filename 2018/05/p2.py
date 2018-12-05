#!/usr/bin/env python
''' Day 5
'''
import string
import sys
from pathlib import Path

replacements = []


def process(polymer):
    c = polymer
    for replacement in replacements:
        c = c.replace(replacement, "")

    return c


def react(polymer):
    while (True):
        current_len = len(polymer)
        polymer = process(polymer)
        if current_len == len(polymer):
            break

    return len(polymer)


def load_polymer():
    with Path(sys.argv[1]).open() as f:
        return f.readline().strip()


def main():
    for (uc, lc) in zip(string.ascii_uppercase, string.ascii_lowercase):
        replacements.append(f"{uc}{lc}")
        replacements.append(f"{lc}{uc}")

    polymer = load_polymer()
    print(min(react(polymer.replace(uc, '').replace(lc, ''))
              for uc, lc in zip(string.ascii_uppercase, string.ascii_lowercase)
              )
          )


if __name__ == '__main__':
    main()
