#!/usr/bin/env python
"""
  Day 25
"""
import sys


def main():
    with open(sys.argv[1]) as f:
        public_keys = [int(line.strip()) for line in f]

    print(f"Looking for: {public_keys}")
    subject = 7  # from the problem, both keys are in this set
    print(f"SN: {subject}")
    s = set()
    d = []
    x = subject
    while x not in s:
        s.add(x)
        d.append(x)
        x = (x * subject) % 20201227

    assert public_keys[0] in s
    assert public_keys[1] in s

    print(f"Position    : {d.index(public_keys[0])}")
    for_key = public_keys[1]
    loop = d.index(public_keys[0])

    print(f"Transforming: {for_key}")
    encryption_key = for_key
    for _ in range(loop):
        encryption_key = (encryption_key * for_key) % 20201227
    return f"         Key: {encryption_key}"


if __name__ == "__main__":
    print(main())
