#!/usr/bin/env python
"""
    Day 9
"""
import sys
from pathlib import Path

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def main():
    H = (0, 0)
    T = (0, 0)
    allT = set()

    def delta() -> int:
        return max((abs(H[0] - T[0]), abs(H[1] - T[1])))

    with Path(sys.argv[1]).open() as f:
        for line in f:
            l = line.strip().split()
            d = directions[l[0]]
            n = int(l[1])
            for i in range(n):
                allT.add(T)
                print(f"Head: {H} Tail: {T}")
                # move the head
                H = (H[0] + d[0], H[1] + d[1])
                # move the tail
                if delta() > 1:
                    # same row?
                    if H[0] == T[0]:
                        # print("same row")
                        T = (T[0], T[1] + (H[1] - T[1]) // abs(H[1] - T[1]))
                        continue
                    # same col?
                    if H[1] == T[1]:
                        # print("same col")
                        T = (T[0] + (H[0] - T[0]) // abs(H[0] - T[0]), T[1])
                        continue
                    # print("diagonal")
                    T = (
                        T[0] + (H[0] - T[0]) // abs(H[0] - T[0]),
                        T[1] + (H[1] - T[1]) // abs(H[1] - T[1]),
                    )
        print(f"--> Head: {H} Tail: {T}")
        allT.add(T)
        print(f"Unique: {len(allT)}")


if __name__ == "__main__":
    main()
