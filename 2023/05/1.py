#!/usr/bin/env python
"""
    Day 5
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

        next(f)  # nop

        def read_group():
            next(f)
            src = SortedList()
            dst = {}
            while line := next(f).strip():
                dest, source, span = [int(x) for x in line.strip().split()]
                src.update((source, source + span - 1))
                dst[(source, source + span - 1)] = dest
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
            # print("outside start range", value)
            return value

        if b == len(source):  # outside of a range
            # print("outside end range", value)
            return value

        if b % 2:  # odd, so in an interval
            offset = value - source[b - 1]
            # print("offset", offset, "dest", dest[(source[b - 1], source[b])] + offset)
            return dest[(source[b - 1], source[b])] + offset

        # even, but at the start of an interval
        if not (b % 2) and value == source[b]:  # actually at the start of interval
            # print("align w start", value, source, 'dest', dest[(source[b], source[b+1])])
            return dest[(source[b], source[b + 1])]

        # even, but between intervals (so, unmapped)
        return value

    def seed2location(seed: int) -> int:
        return mapr(
            humidr,
            location_map,
            mapr(
                tempr,
                humidity_map,
                mapr(
                    lightr,
                    temp_map,
                    mapr(
                        water,
                        light_map,
                        mapr(
                            fertilizer,
                            water_map,
                            mapr(soilr, fertilizer_map, mapr(seedr, soil_map, seed)),
                        ),
                    ),
                ),
            ),
        )

    # for seed in seeds:
    #    print(f"Seed {seed} -> location {seed2location(seed)}")
    return min(seed2location(seed) for seed in seeds)


if __name__ == "__main__":
    print(main())
