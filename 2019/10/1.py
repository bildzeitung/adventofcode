#!/usr/bin/env python
"""
    Day 10
"""
import sys
from math import gcd
from pathlib import Path

max_x = 0
max_y = 0


def calc(p1, points):
    global max_x, max_y

    found = []
    count = 0
    points.sort(key=lambda z: (p1[0] - z[0]) ** 2 + (p1[1] - z[1]) ** 2)
    # print(f"CALC {p1} {points}")
    for p2 in points:
        if p2 in found:
            # print("Skpping", p2)
            continue

        found.append(p2)
        count += 1
        dx, dy = (p2[0] - p1[0]), (p2[1] - p1[1])
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        # print(p1, p2, dx, dy)
        while p2[0] <= max_x and p2[1] <= max_y and p2[0] > -1 and p2[1] > -1:
            p2 = (p2[0] + dx, p2[1] + dy)
            if p2 in points and p2 not in found:
                # print("Got one", p2)
                found.append(p2)

    # print(p1, count)
    return count


def main():
    global max_x, max_y

    points = []
    with Path(sys.argv[1]).open() as f:
        j = 0
        for r in f:
            max_x = len(r.strip())
            for i, a in enumerate(r.strip()):
                if a == "#":
                    points.append((i, j))
            j += 1

    max_y = j
    # print(f"MAX ({max_x}, {max_y})")
    max_count = []
    for p in points:
        q = points[:]
        q.remove(p)
        max_count.append((p, calc(p, q)))

    print("MAX", max(max_count, key=lambda x: x[1]))


if __name__ == "__main__":
    main()
