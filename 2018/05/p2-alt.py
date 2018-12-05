#!/usr/bin/env python
""" Day 5
"""
import string
import sys
from pathlib import Path


def react(polymer):
    rc = []
    for x in polymer:
        """ if there's a string, then compare the end of it to
            the current item; otherwise, just append the current item
        """
        if rc:
            """ To find all aA and Aa cases, it's easiest to ensure
                that the items don't match (A != a), but their lowercase
                representations do: lower(a) == lower(A).

                If they do match, then pop off the end of the list,
                otherwise append the current item
            """
            if x != rc[-1] and x.lower() == rc[-1].lower():
                rc.pop()
                continue

        rc.append(x)

    return len(rc)


def load_polymer():
    with Path(sys.argv[1]).open() as f:
        return f.readline().strip()


def main():
    polymer = load_polymer()
    print(
        min(
            react(polymer.replace(uc, "").replace(lc, ""))
            for uc, lc in zip(string.ascii_uppercase, string.ascii_lowercase)
        )
    )


if __name__ == "__main__":
    main()
