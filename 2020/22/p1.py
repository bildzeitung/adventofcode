#!/usr/bin/env python
"""
  Day 22
"""
import sys


def play(d1, d2):
    while d1 and d2:
        t1, t2 = d1.pop(0), d2.pop(0)
        if t1 > t2:
            d1.append(t1)
            d1.append(t2)
        else:
            d2.append(t2)
            d2.append(t1)

    return d1 if d1 else d2


def main():
    with open(sys.argv[1]) as f:
        player1 = f.readline().strip()
        deck1 = []
        while n := f.readline().strip():
            deck1.append(int(n))

        player2 = f.readline().strip()
        deck2 = []
        while n := f.readline().strip():
            deck2.append(int(n))

    winner = play(deck1, deck2)
    print(winner)
    return sum((i + 1) * v for i, v in enumerate(reversed(winner)))


if __name__ == "__main__":
    print(main())
