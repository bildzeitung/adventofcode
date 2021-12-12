#!/usr/bin/env python
"""
    Day 8    
"""
import sys
from collections import Counter
from itertools import chain
from pathlib import Path

from rich import print

SEGMENT_MAP = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def decode(digits):
    """Sort out what's what
     aa
    b  c
     dd
    e  f
     gg
    """
    segments = {}
    assert len(digits) == 10  # cross-check
    # 1 and 7 together give us a guess for 'a'
    one_and_seven = [
        y for y in chain.from_iterable(x for x in digits if len(x) in (2, 3))
    ]
    # print(f"1 & 7 => {one_and_seven}")
    segments["a"] = [k for k, v in Counter(one_and_seven).items() if v == 1][0]

    # a use 1, 0, 6, & 9 to get c & f
    c_and_f = [x for x in digits if len(x) == 2][0]
    # print(f"[1]: {c_and_f}")
    sixer_and_cf = [y for y in chain.from_iterable(x for x in digits if len(x) == 6)]
    # print(sixer_and_cf)
    if sixer_and_cf.count(c_and_f[0]) == 2:
        segments["c"] = c_and_f[0]
        segments["f"] = c_and_f[1]
    else:
        segments["c"] = c_and_f[1]
        segments["f"] = c_and_f[0]

    d_and_e = [
        k
        for k, v in Counter(x for x in sixer_and_cf if x not in c_and_f).items()
        if v == 2
    ]
    # print(f"d and e => {d_and_e}")

    delta_1_and_4 = [
        k
        for k, v in Counter(
            y for y in chain.from_iterable(x for x in digits if len(x) in (2, 4))
        ).items()
        if v == 1
    ]
    # print(f"1 - 4 ==> {delta_1_and_4}")
    combine = Counter(chain(delta_1_and_4, d_and_e))
    # print(f"Quartet ==> {combine}")
    segments["d"] = [k for k, v in combine.items() if v == 2][0]
    segments["b"] = (set(delta_1_and_4) - set(segments["d"])).pop()
    segments["e"] = (set(d_and_e) - set(segments["d"])).pop()
    segments["g"] = (set("abcdefg") - set(segments.values())).pop()
    print(f"Segments ==> {segments}")
    return dict(map(reversed, segments.items()))


def get_value(segments, output):
    v = 0
    for d in output.split():
        de = "".join(sorted(segments[x] for x in d))
        v = v * 10 + SEGMENT_MAP[de]
        # print(f"{d} -> {de} -> {SEGMENT_MAP[de]}")
    return v


def main():
    LENGTHS = (2, 3, 4, 7)
    results = []
    with Path(sys.argv[1]).open() as f:
        s = 0
        for line in f:
            digits, output = line.strip().split("|")
            print(f"Digits -> {digits}")
            segments = decode(digits.strip().split())
            print(f"Coded: {segments}")
            number = get_value(segments, output)
            print(f"Value: {number}")
            s += number
    print(f"Final: {s}")


if __name__ == "__main__":
    main()
