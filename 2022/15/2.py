#!/usr/bin/env python
"""
    Day 15
"""
import sys
from pathlib import Path
from rich import print
from shapely import Polygon, box
from shapely.ops import unary_union


def delta(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    puzzle = {}
    radius = {}
    sensors = set()
    limit = int(sys.argv[1])
    with Path(sys.argv[2]).open() as f:
        for line in f:
            sensor, beacon = line.strip().replace(",", "").split(":")
            sensor = tuple(int(c.split("=")[-1]) for c in sensor.split(" ")[-2:])
            beacon = tuple(int(c.split("=")[-1]) for c in beacon.split(" ")[-2:])
            puzzle[sensor] = "S"
            puzzle[beacon] = "B"
            radius[sensor] = delta(sensor, beacon)
            sensors.add(sensor)

    polys = []
    for s in sensors:
        # each sensor is a polygon
        r = radius[s]
        polys.append(
            Polygon(
                [
                    (s[0], s[1] - r),
                    (s[0] + r, s[1]),
                    (s[0], s[1] + r),
                    (s[0] - r, s[1]),
                ]
            )
        )

    altogether = unary_union(polys)
    search_space = box(0, 0, limit, limit)
    b = search_space.difference(altogether)
    print(b.bounds)
    print(f"Sol'n: {(b.bounds[0] + 1) * limit + (b.bounds[1]+1)}")


if __name__ == "__main__":
    main()
