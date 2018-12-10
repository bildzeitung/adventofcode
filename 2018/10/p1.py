#!/usr/bin/env python
""" Day 10

    n.b. Both parts in this file

    Runs the simulation one timestep at a time, stops when points
    are converged.
"""
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# line:
#   position=< 51781,  41361> velocity=<-5, -4>
#
# In hindsight, probably easier to capture < .. > and split on the
# comma.
DATA_RE = re.compile(r"(-?\d+),\s+(-?\d+).+?(-?\d+),\s+(-?\d+)")


@dataclass
class Point:
    x: int
    y: int
    velocity: tuple

    def blink(self) -> None:
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def unblink(self) -> None:
        self.x -= self.velocity[0]
        self.y -= self.velocity[1]


def load():
    points = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            px, py, vx, vy = [int(x) for x in DATA_RE.search(line.strip()).groups()]
            points.append(Point(px, py, (vx, vy)))

    return points


def bounding(points):
    """ Return the bounding box <min x, min y> -> <max x, max y>
    """
    min_x = min(t.x for t in points)
    min_y = min(t.y for t in points)
    max_x = max(t.x for t in points)
    max_y = max(t.y for t in points)

    return ((min_x, min_y), (max_x, max_y))


def render(points, iter):
    """ Draw the points in ASCII art
    """
    min_corner, max_corner = bounding(points)
    range_x = abs(max_corner[0] - min_corner[0]) + 1
    range_y = abs(max_corner[1] - min_corner[1]) + 1

    g = [x[:] for x in [[0] * range_x] * range_y]
    for p in points:
        g[p.y - min_corner[1]][p.x - min_corner[0]] = 1
    for i in g:
        print("".join("X" if x else "." for x in i))


def blink(points):
    # perform the calculation
    for p in points:
        p.blink()

    min_corner, max_corner = bounding(points)

    return ((max_corner[0] - min_corner[0]) + 1) * (max_corner[1] - min_corner[1] + 1)


def main():
    """ What I noticed in the data was that the overall bounding box
        shrunk, and then grew.

        Assuming that the smallest bounding box is the image, iterate
        until it became bigger, and stop.
    """
    points = load()
    old_area = blink(points)
    new_area = old_area
    i = 0
    while new_area <= old_area:
        old_area = new_area
        new_area = blink(points)
        i += 1

    print("FINAL", i)

    # Went one step too far to see the picture! Backup by a single step
    for p in points:
        p.unblink()
    render(points, new_area)


if __name__ == "__main__":
    main()
