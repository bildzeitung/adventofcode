#!/usr/bin/env python
"""
    Day 4
"""
import sys
from pathlib import Path


def main():
    cards = []  # store the number of matching numbers only
    with Path(sys.argv[1]).open() as f:
        for line in f:
            line = line.strip()
            winners, have = [x.strip() for x in line.split(":")[1].split("|")]
            winners = [int(x) for x in winners.split()]
            have = [int(x) for x in have.split()]
            cards.append(len(set(winners) & set(have)))

    tallys = [1] * len(cards)
    for idx, card in enumerate(cards):
        for x in range(1, card + 1):
            tallys[idx + x] += tallys[idx]

    return sum(tallys)


if __name__ == "__main__":
    print(main())
