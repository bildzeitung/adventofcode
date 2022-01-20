#!/usr/bin/env python
"""
    Day 18
"""
import sys
from pathlib import Path

from rich import print


def add(a, b):
    return [a, b]


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
            # print(f"[L] Got a split: {b}")
            b[0] = [b[0] // 2, b[0] // 2 + b[0] % 2]
            return True

        if rv:
            return True

        if isinstance(b[1], list):
            rv = sp(b[1])
        elif b[1] > 9:
            # print(f"[R] Got a split: {b}")
            b[1] = [b[1] // 2, b[1] // 2 + b[1] % 2]
            return True

        return rv

    did_a_thing = True
    while did_a_thing:
        # print("Begin explode pass..")
        did_a_thing, *_ = es(a, 0)
        if did_a_thing:
            # print(f"Finished: {a}")
            continue
        # print("Begin split pass..")
        did_a_thing = sp(a)


def magnitude(a) -> int:
    t = 0
    if isinstance(a[0], list):
        t = 3 * magnitude(a[0])
    else:
        t = 3 * a[0]

    if isinstance(a[1], list):
        t += 2 * magnitude(a[1])
    else:
        t += 2 * a[1]

    return t


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
        first = to_snailfish(next(f))
        for line in f:
            first = add(first, to_snailfish(line))
            snail_reduce(first)
            print(f"Now: {first}")
    return magnitude(first)


if __name__ == "__main__":
    print(f"Magnitude: {main()}")
