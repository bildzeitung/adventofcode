#!/usr/bin/env python
"""
    Day 10
"""
import sys
from pathlib import Path


def calc(p1, points):
    # print(f"CALC {p1} {points}")
    found = []
    count = 0
    points.sort(key=lambda z: (p1[0] - z[0]) ** 2 + (p1[1] - z[1]) ** 2)
    for idx, p2 in enumerate(points):
        if p2 in found:
            continue
        found.append(p2)

        count += 1
        for p3 in points:
            if p3 in found:
                continue
            if (
                p1[0] * (p2[1] - p3[1])
                + p2[0] * (p3[1] - p1[1])
                + p3[0] * (p1[1] - p2[1])
            ) == 0:
                found.append(p3)
    print(p1, count)
    return count


def main():
    points = []
    with Path(sys.argv[1]).open() as f:
        j = 0
        for r in f:
            for i, a in enumerate(r.strip()):
                if a == "#":
                    points.append((i, j))
            j += 1

    max_count = 0
    for p in points:
        q = points[:]
        q.remove(p)
        max_count = max(calc(p, q), max_count)

    print("MAX", max_count)


if __name__ == "__main__":
    main()
