#!/usr/bin/env python
"""
    Day 17
"""
import math
import re
import sys
from pathlib import Path


def simulate(boundx, boundy, startx, starty) -> bool:
    v = (startx, starty)
    p = (0, 0)
    my = 0
    while True:

        def dx(i):
            if i < 0:
                return i + 1
            elif i > 0:
                return i - 1
            return 0

        p = (p[0] + v[0], p[1] + v[1])
        v = (dx(v[0]), v[1] - 1)
        my = max(my, p[1])
        if p[0] > boundx[1]:
            print("Overshoot x")
            return False, my, "over-x"  # miss

        if p[1] < boundy[0]:
            reason = "past-y"
            if p[0] < boundx[0]:
                reason = "short-x"
            print(f"{reason} {p} | {v} => {boundx} | {boundy}")
            return False, my, reason  # miss

        if (boundx[0] <= p[0] <= boundx[1]) and (boundy[0] <= p[1] <= boundy[1]):
            return True, my, None  # hit!


def solve(boundx, boundy):
    # need a reasonable guess for x, to start
    x = math.floor(math.sqrt(boundx[1] * 2 + 0.25) - 0.5)
    # py = math.floor(math.sqrt(-boundy[0] * 2 + 0.25) - 0.5)
    print(f"Starting guess for x: {x}")
    # print(f"Provisional y: {py}")
    y = 0
    state = "inc-y"
    last_round = True
    has_hit = False
    while True:
        r, maxy, reason = simulate(boundx, boundy, x, y)
        if not reason:
            has_hit = True
        print(f"({x}, {y}) -> {r} | {maxy} | {state}")
        if reason == "short-x" and not has_hit:
            x += 1
            continue
        # if not last_round and not r:
        #    return
        last_round = r
        if not r and has_hit:
            if reason == "past-y":
                y += 1
                continue
            if state == "inc-y":
                y -= 1
                state = "dec-x"
            else:
                x += 1
                state = "inc-y"

        if state == "inc-y":
            y += 1
        else:
            x -= 1


def main():
    with Path(sys.argv[1]).open() as f:
        for line in f:
            x, y = re.search("x=(.+), y=(.+)", line.strip()).groups()
            x = [int(i) for i in x.split("..")]
            y = [int(i) for i in y.split("..")]
            solve(x, y)


if __name__ == "__main__":
    main()
