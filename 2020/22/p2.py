#!/usr/bin/env python
"""
  Day 22

  The game description is pretty clear, so it's more or less directly
  simulated in the code.

  I think the keys here are:
  * recording the game state (a bitset would do, but any O(1) lookup, so a
    hashable type will do; I chose tuples for this)
  * having an interface to the simulator that you can just recurse into
"""
import sys


def play(d1, d2):
    state = set()

    while True:
        # check dupe of previous game state
        current = (tuple(d1), tuple(d2))
        if current in state:
            return d1, []  # win for player 1
        state.add(current)

        # draw top cards
        t1, t2 = d1.pop(0), d2.pop(0)

        # if both: len(deck) >= topcard, then Recursive Combat
        if len(d1) >= t1 and len(d2) >= t2:
            w1, _ = play(d1[0:t1], d2[0:t2])
            if w1:
                d1.append(t1)
                d1.append(t2)
                continue
            else:
                d2.append(t2)
                d2.append(t1)
                continue

        # otherwise, high-value topcard
        if t1 > t2:
            d1.append(t1)
            d1.append(t2)
        else:
            d2.append(t2)
            d2.append(t1)

        # check victory
        if not (d1 and d2):
            return d1, d2


def main():
    with open(sys.argv[1]) as f:
        next(f)  # skip player header
        deck1 = []
        while n := f.readline().strip():
            deck1.append(int(n))

        next(f)  # skip player header
        deck2 = []
        while n := f.readline().strip():
            deck2.append(int(n))

    w1, w2 = play(deck1, deck2)
    print(w1, w2)
    winner = w1 if w1 else w2
    return sum((i + 1) * v for i, v in enumerate(reversed(winner)))


if __name__ == "__main__":
    print(main())
