#!/usr/bin/env python
"""
    Day 7
"""
import sys
from collections import Counter
from pathlib import Path

from rich import print

CARDMAP = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}
"""
 1 = five of a kind
 2 = four of a kind
 3 = full house
 4 = three of a kind
 5 = two pair
 6 = one pair
 7 = high card
   + list of cards as int's
"""


def eval_hand(hand: str):
    c = Counter(hand).most_common()
    h = [CARDMAP[x] for x in hand]
    # five of a kind
    if c[0][1] == 5:
        return (1, *h)

    # four of a kind
    if c[0][1] == 4:
        return (2, *h)

    # full house
    if c[0][1] == 3 and c[1][1] == 2:
        return (3, *h)

    # three of a kind
    if c[0][1] == 3:
        return (4, *h)

    # two pair
    if c[0][1] == 2 and c[1][1] == 2:
        return (5, *h)

    # one pair
    if c[0][1] == 2:
        return (6, *h)

    # high card
    return (7, *h)


def main():
    bids = {}
    hands = []

    with Path(sys.argv[1]).open() as f:
        for line in f:
            hand, bid = [x.strip() for x in line.split()]
            bids[hand] = int(bid)
            hands.append(hand)

    s = [
        bids[x] * (idx + 1)
        for idx, x in enumerate(reversed(sorted(hands, key=eval_hand)))
    ]
    return sum(s)


if __name__ == "__main__":
    print(main())
