#!/usr/bin/env python
"""
  Day 12
"""
import sys

dir = [
    (1, 0),  # E
    (0, 1),  # S
    (-1, 0),  # W
    (0, -1),  # N
]


def F(pos, facing, q):
    return (pos[0] + dir[facing][0] * q, pos[1] + dir[facing][1] * q), facing


def N(pos, facing, q):
    pos, _ = F(pos, 3, q)
    return pos, facing


def S(pos, facing, q):
    pos, _ = F(pos, 1, q)
    return pos, facing


def E(pos, facing, q):
    pos, _ = F(pos, 0, q)
    return pos, facing


def W(pos, facing, q):
    pos, _ = F(pos, 2, q)
    return pos, facing


def L(pos, facing, q):
    facing = (4 + facing - (q // 90)) % 4
    return pos, facing


def R(pos, facing, q):
    facing = (facing + (q // 90)) % 4
    return pos, facing


cmds = {"N": N, "S": S, "E": E, "W": W, "L": L, "R": R, "F": F}


def main():
    facing = 0
    pos = (0, 0)
    with open(sys.argv[1]) as f:
        for line in f:
            c, q = line[0], int(line.strip()[1:])
            pos, facing = cmds[c](pos, facing, q)
    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    print(main())
