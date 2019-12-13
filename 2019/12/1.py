#!/usr/bin/env python
import re
import sys
from itertools import combinations
from pathlib import Path


def apply_gravity(moons):
    for m, n in combinations(moons, 2):

        def d(a, b):
            if b > a:
                return 1
            elif b < a:
                return -1
            return 0

        m["vel"] = tuple(
            m["vel"][idx] + val
            for idx, val in enumerate([d(i, j) for i, j in zip(m["pos"], n["pos"])])
        )

        n["vel"] = tuple(
            n["vel"][idx] + val
            for idx, val in enumerate([d(i, j) for i, j in zip(n["pos"], m["pos"])])
        )


def apply_velocity(moons):
    for m in moons:
        m["pos"] = tuple(m["vel"][i] + m["pos"][i] for i in range(3))


def energy(moons):
    return sum(
        sum(abs(x) for x in m["pos"]) * sum(abs(x) for x in m["vel"]) for m in moons
    )


def simulate(moons, steps):
    i = 0
    for _ in range(steps):
        i += 1
        apply_gravity(moons)
        apply_velocity(moons)
        # print(f"After {i}")
        # for moon in moons:
        #     print(moon)

        # print()
    print(energy(moons))


def main():
    moons = []
    with Path(sys.argv[1]).open() as f:
        for l in f:
            r = re.search(r"(-?\d+).+?(-?\d+).+?(-?\d+)", l)
            x, y, z = [int(x) for x in r.groups()]
            moons.append({"pos": (x, y, z), "vel": (0, 0, 0)})

    simulate(moons, int(sys.argv[2]))


if __name__ == "__main__":
    main()
