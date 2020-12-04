#!/usr/bin/env python
"""
    Day 4
"""
import sys

FIELDS = set(
    [
        "byr",  # (Birth Year)
        "iyr",  # (Issue Year)
        "eyr",  # (Expiration Year)
        "hgt",  # (Height)
        "hcl",  # (Hair Color)
        "ecl",  # (Eye Color)
        "pid",  # (Passport ID)
        #            "cid",  # (Country ID)
    ]
)


def read_passport(f):
    passport = {}
    while l := f.readline():
        l = l.strip()
        if not l:
            return passport
        passport.update(dict(entry.split(":") for entry in l.split(" ")))
    return passport


def is_valid(passport):
    if "cid" in passport:
        del passport["cid"]

    return len(set(passport.keys()) ^ FIELDS) == 0


def main():
    with open(sys.argv[1]) as f:

        def feed():
            while passport := read_passport(f):
                yield is_valid(passport)

        return sum(x for x in feed())


if __name__ == "__main__":
    print(main())
