#!/usr/bin/env python
"""
    Day 15
"""
import sys
from pathlib import Path
from rich import print


def viz(puzzle):
    min_x = min(x[0] for x in puzzle)
    max_x = max(x[0] for x in puzzle)
    min_y = min(x[1] for x in puzzle)
    max_y = max(x[1] for x in puzzle)
    for y in range(min_y, max_y + 1):
        print(
            "".join(
                puzzle[(x, y)] if (x, y) in puzzle else "."
                for x in range(min_x, max_x + 1)
            )
        )


def delta(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    puzzle = {}
    radius = {}
    sensors = set()
    beacons = set()
    target_y = int(sys.argv[1])
    with Path(sys.argv[2]).open() as f:
        for line in f:
            sensor, beacon = line.strip().replace(",", "").split(":")
            sensor = tuple(int(c.split("=")[-1]) for c in sensor.split(" ")[-2:])
            beacon = tuple(int(c.split("=")[-1]) for c in beacon.split(" ")[-2:])
            puzzle[sensor] = "S"
            puzzle[beacon] = "B"
            radius[sensor] = delta(sensor, beacon)
            sensors.add(sensor)
            beacons.add(beacon)

    # viz(puzzle)
    no_beacon = set()
    for s in sensors:
        if s[1] - radius[s] <= s[1] <= s[1] + radius[s]:
            # print(f"Sensor {s} applies")
            for x in range(s[0] - radius[s], s[0] + 1 + radius[s], 1):
                if delta((x, target_y), s) <= radius[s]:
                    # print(f"Taken: {x}, {target_y}")
                    no_beacon.add((x, target_y))
    print(f"There are {len(no_beacon - beacons - sensors)} spots")


if __name__ == "__main__":
    main()
