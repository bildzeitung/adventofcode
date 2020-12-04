#!/usr/bin/env python
"""
    Day 4
"""
import re
import sys

FIELDS = set([  "byr",  # (Birth Year)
            "iyr",  # (Issue Year)
            "eyr",  # (Expiration Year)
            "hgt",  # (Height)
            "hcl",  # (Hair Color)
            "ecl",  # (Eye Color)
            "pid",  # (Passport ID)
#            "cid",  # (Country ID)
])

EYES = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

hair = re.compile('^#[0-9a-f]{6}$')
id = re.compile('^[0-9]{9}$')


def read_passport(f):
    passport = {}
    while l := f.readline():
        l = l.strip()
        if not l:
            return passport
        passport.update(dict(entry.split(':') for entry in l.split(' ')))
    return passport


def is_valid(passport):
    k = [x for x in passport.keys()]

    if 'cid' in k:
        k.remove("cid")

    if len(set(k) ^ FIELDS) != 0:
        return False

    if not 1920 <= int(passport['byr']) <= 2002:
        return False

    if not 2010 <= int(passport['iyr']) <= 2020:
        return False

    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    if 'cm' in passport['hgt']:
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            return False
    elif 'in' in passport['hgt']:
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            return False
    else:
        return False

    if not hair.search(passport['hcl']):
        return False

    if passport['ecl'] not in EYES:
        return False

    if not id.search(passport['pid']):
        return False

    return True


def main():
    with open(sys.argv[1]) as f:
        def feed():
            while passport := read_passport(f):
                yield is_valid(passport)

        return sum(x for x in feed())

if __name__ == "__main__":
    print(main())
