#!/usr/bin/env python
"""
    Day 10
"""
import sys
from math import atan2, pi
from pathlib import Path


def calc(p, rest):
    """ Create a full ordering of the asteroids
    """

    def d(q):
        # relative position, for atan2
        return q[1] - p[1], q[0] - p[0]

    # sort by distance
    # - this disambiguates asteroids hidden behind others
    rest.sort(key=lambda z: (p[0] - z[0]) ** 2 + (p[1] - z[1]) ** 2)

    # sort by radians
    # - asteroids at the same angle, but further away, are
    #   listed in the proper order, because python sort is stable
    rest.sort(key=lambda x: atan2(*d(x)))

    # re-arrange a little
    #     A|
    #    --+--
    #      |
    #
    # - items in quadrant A are listed first; shuffle them to the back
    final = [x for x in rest if atan2(*d(x)) >= -pi / 2] + [
        x for x in rest if atan2(*d(x)) < -pi / 2
    ]

    last = 0
    idx = 0
    while final:
        i = final.pop(0)
        a = atan2(*d(i))
        # skip points with the same radian value (ie. hidden asteroids)
        if a == last and len(final) > 1:
            # print(f"Skip {i} {a}")
            final.append(i)
            continue
        last = a
        idx += 1
        print(idx, i, i[0] * 100 + i[1], len(final), last)


def main():
    stn_x, stn_y = int(sys.argv[2]), int(sys.argv[3])
    points = []
    with Path(sys.argv[1]).open() as f:
        j = 0
        for r in f:
            for i, a in enumerate(r.strip()):
                if a != ".":
                    points.append((i, j))
            j += 1

    p = (stn_x, stn_y)
    q = points[:]
    q.remove(p)
    calc(p, q)


if __name__ == "__main__":
    main()
