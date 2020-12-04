#!/usr/bin/env python
"""
    Day 4
"""
import sys

# all of the fields required to be in the passport
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
        if not l:  # blank line separating passports
            yield passport
            passport = {}
            continue
        passport.update(dict(entry.split(":") for entry in l.split(" ")))
    yield passport


def is_valid(passport):
    if "cid" in passport:
        del passport["cid"]

    return len(set(passport.keys()) ^ FIELDS) == 0


def main():
    with open(sys.argv[1]) as f:
        return sum(is_valid(x) for x in read_passport(f))


if __name__ == "__main__":
    print(main())
