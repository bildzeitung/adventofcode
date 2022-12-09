#!/usr/bin/env python
"""
    Day 9

    To hand-wave finding a proper direction to move the tail in, it's
    easiest to create the delta by taking:
    
        (x2 - x1) / abs(x2 - x1)

    In other words, 
        
        delta(x) / abs(delta(x)) == +/- 1

    .. so the abs() preserves the direction by keeping the sign (otherwise
       it would always be: x / x == 1)

"""
import sys
from pathlib import Path
from rich import print


directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def main():
    T = [(0, 0)] * 10
    allT = set()

    # Manhattan distance is good enough
    def delta(H, T) -> int:
        return max((abs(H[0] - T[0]), abs(H[1] - T[1])))

    def moveTail(H, T):
        if delta(H, T) <= 1:  # head and tail are touching
            return T

        # same row?
        if H[0] == T[0]:
            return (T[0], T[1] + (H[1] - T[1]) // abs(H[1] - T[1]))
        # same col?
        if H[1] == T[1]:
            return (T[0] + (H[0] - T[0]) // abs(H[0] - T[0]), T[1])

        return (
            T[0] + (H[0] - T[0]) // abs(H[0] - T[0]),
            T[1] + (H[1] - T[1]) // abs(H[1] - T[1]),
        )

    with Path(sys.argv[1]).open() as f:
        for line in f:
            l = line.strip().split()
            d = directions[l[0]]
            n = int(l[1])
            for i in range(n):
                allT.add(T[-1])
                # move the head
                T[0] = (T[0][0] + d[0], T[0][1] + d[1])
                # move the tail
                for i in range(1, len(T)):
                    T[i] = moveTail(T[i - 1], T[i])
        print(f"--> Head: {T[0]} Tail: {T[1:]}")
        allT.add(T[-1])
        print(f"Unique: {len(allT)}")


if __name__ == "__main__":
    main()
