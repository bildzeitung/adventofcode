#!/usr/bin/env python
"""
    Day 4
"""
import re
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
        #  "cid",  # (Country ID)
    ]
)

EYES = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

hair = re.compile("^#[0-9a-f]{6}$")
id = re.compile("^[0-9]{9}$")


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

    # completeness check; don't do anything unless this passes
    if len(set(passport.keys()) ^ FIELDS) != 0:
        return False

    # all remaining criteria
    return all(
        [
            1920 <= int(passport["byr"]) <= 2002,
            2010 <= int(passport["iyr"]) <= 2020,
            2020 <= int(passport["eyr"]) <= 2030,
            ("cm" in passport["hgt"] and 150 <= int(passport["hgt"][:-2]) <= 193)
            or ("in" in passport["hgt"] and 59 <= int(passport["hgt"][:-2]) <= 76),
            hair.search(passport["hcl"]),
            passport["ecl"] in EYES,
            id.search(passport["pid"]),
        ]
    )


def main():
    with open(sys.argv[1]) as f:
        return sum(is_valid(x) for x in read_passport(f))


if __name__ == "__main__":
    print(main())
