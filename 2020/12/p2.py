#!/usr/bin/env python
"""
  Day 12
"""
import sys


def main():
    pos = (0, 0)
    waypoint = (10, 1)
    with open(sys.argv[1]) as f:
        for line in f:
            c, q = line[0], int(line.strip()[1:])

            if c == "F":  # forward
                pos = (pos[0] + waypoint[0] * q, pos[1] + waypoint[1] * q)
            if c == "N":
                waypoint = (waypoint[0], waypoint[1] + q)
            if c == "S":
                waypoint = (waypoint[0], waypoint[1] - q)
            if c == "E":
                waypoint = (waypoint[0] + q, waypoint[1])
            if c == "W":
                waypoint = (waypoint[0] - q, waypoint[1])
            if c == "R":  # CW rotation
                for _ in range(q // 90):
                    waypoint = (waypoint[1], -waypoint[0])
            if c == "L":  # CCW rotation
                for _ in range(q // 90):
                    waypoint = (-waypoint[1], waypoint[0])

    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    print(main())
