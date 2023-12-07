#!/usr/bin/env python
"""
    Day 5

    Use the power of guesswork to find the first seed ..
"""
import sys
from pathlib import Path

from rich import print
from sortedcontainers import SortedList


def main():
    seeds = []
    seedr = SortedList()
    soil_map = {}
    soilr = SortedList()
    fertilizer_map = {}
    fertilizer = SortedList()
    water_map = {}
    water = SortedList()
    light_map = {}
    lightr = SortedList()
    temp_map = {}
    tempr = SortedList()
    humidity_map = {}
    humidr = SortedList()
    location_map = {}

    with Path(sys.argv[1]).open() as f:
        # first line is seeds
        seeds = [int(x) for x in next(f).split(":")[1].strip().split()]
        seed_ranges = []
        seeditr = iter(seeds)
        for s in seeditr:
            t = next(seeditr)
            seed_ranges.append((s, s+t-1))

        next(f)  # nop

        def read_group():
            next(f)
            src = SortedList()
            dst = {}
            while line := next(f).strip():
                dest, source, span = [int(x) for x in line.strip().split()]
                t = (dest, dest + span - 1)
                src.update(t)
                dst[t] = source
            return src, dst

        seedr, soil_map = read_group()
        soilr, fertilizer_map = read_group()
        fertilizer, water_map = read_group()
        water, light_map = read_group()
        lightr, temp_map = read_group()
        tempr, humidity_map = read_group()
        humidr, location_map = read_group()

    def mapr(source: SortedList, dest: dict, value):
        b = source.bisect_left(value)

        # cases:
        #  - before first interval
        #  - after last interval
        #  - in an interval
        #  - at the start of a given interval
        #  - between intervals
        #
        if b == 0:  # outside of a range
            return value

        if b == len(source):  # outside of a range
            return value

        if b % 2:  # odd, so in an interval
            offset = value - source[b - 1]
            return dest[(source[b - 1], source[b])] + offset

        # even, but at the start of an interval
        if not (b % 2) and value == source[b]:  # actually at the start of interval
            return dest[(source[b], source[b + 1])]

        # even, but between intervals (so, unmapped)
        return value

    def location2seed(l: int) -> int:
        return mapr(
            seedr,
            soil_map,
            mapr(
                soilr,
                fertilizer_map,
                mapr(
                    fertilizer,
                    water_map,
                    mapr(
                        water,
                        light_map,
                        mapr(
                            lightr,
                            temp_map,
                            mapr(tempr, humidity_map, mapr(humidr, location_map, l)),
                        ),
                    ),
                ),
            ),
        )

    print(f"Seed ranges: {seed_ranges}")
    # 10_000_000
    # too high: 291248263
    #           210388587
    #           178032796
    #           120063312
    for x in range(50_000_000, 100_000_000):
        d = location2seed(x)
        for r in seed_ranges:
            if r[0] <= d <= r[1]:
                print(f"Got one: {d}")
                return x 


if __name__ == "__main__":
    print(main())
