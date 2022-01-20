#!/usr/bin/env python
"""
    Day 18
"""
import sys
from copy import deepcopy
from itertools import combinations
from pathlib import Path

from rich import print


def add(a, b):
    return [deepcopy(a), deepcopy(b)]


def snail_reduce(a):
    # look for explode
    # I think this is an LVR search
    def es(b, depth):
        # left needs explode
        if depth == 3 and isinstance(b[0], list):
            # print(f"Need to explode left: {b} to place: {b[0][0]}")
            to_place = b[0][0]
            if isinstance(b[1], int):
                b[1] += b[0][1]
            else:  # we have a delightful nested case
                z = b[1]
                while not isinstance(z[0], int):
                    z = z[0]
                z[0] += b[0][1]
            b[0] = 0
            # print(f"[L]: {b}")
            return True, to_place, None

        # right needs explode
        if depth == 3 and isinstance(b[1], list):
            # print(f"Need to explode right: {b} to place: {b[1][1]}")
            to_place = b[1][1]
            if isinstance(b[0], int):
                b[0] += b[1][0]
                b[1] = 0
            # print(f"[R]: {b}")
            return True, None, to_place

        exploded, l, r = False, None, None
        if isinstance(b[0], list):  # left tree
            exploded, l, r = es(b[0], depth + 1)
            # print(f"Back from left: {exploded}, {l}, {r}")
            if exploded:
                if r:
                    if isinstance(b[1], int):
                        b[1] += r
                        return True, None, None
                    z = b[1]
                    while not isinstance(z[0], int):
                        z = z[0]
                    # print(f"Found: {z}")
                    z[0] += r
                    return True, None, None
                return exploded, l, r

        if isinstance(b[1], list):  # right tree
            exploded, l, r = es(b[1], depth + 1)
            # print(f"Back from right: {exploded}, {l}, {r}")
            if exploded:
                if l:
                    if isinstance(b[0], int):
                        b[0] += l
                        return True, None, None
                    z = b[0]
                    while not isinstance(z[1], int):
                        z = z[1]
                    z[1] += l
                    return True, None, None
                return exploded, l, r

        return exploded, l, r  # no explode

    def sp(b):
        # split
        rv = False
        if isinstance(b[0], list):
            rv = sp(b[0])
        elif b[0] > 9:
            b[0] = [b[0] // 2, b[0] // 2 + b[0] % 2]
            return True

        if rv:
            return True

        if isinstance(b[1], list):
            rv = sp(b[1])
        elif b[1] > 9:
            b[1] = [b[1] // 2, b[1] // 2 + b[1] % 2]
            return True

        return rv

    did_a_thing = True
    while did_a_thing:
        while did_a_thing:
            did_a_thing, *_ = es(a, 0)
        did_a_thing = sp(a)
    return a


def magnitude(a) -> int:
    if isinstance(a, int):  # base case
        return a
    return 3 * magnitude(a[0]) + 2 * magnitude(a[1])


def to_snailfish(a: str):
    stack = []
    for x in a.strip():
        if x in ("[", ","):
            continue
        if x == "]":
            right = stack.pop()
            left = stack.pop()
            stack.append([left, right])
            continue
        stack.append(int(x))
    assert len(stack) == 1, "bad stack!"
    print(f"Got snail -> {stack[0]}")
    return stack[0]


def main():
    with Path(sys.argv[1]).open() as f:
        snails = [to_snailfish(x) for x in f]
    return max(
        max(magnitude(snail_reduce(add(x, y))), magnitude(snail_reduce(add(y, x))))
        for x, y in combinations(snails, 2)
    )


if __name__ == "__main__":
    print(f"Max: {main()}")
