#!/usr/bin/env python
"""
    Day 2
"""
import sys
from pathlib import Path

opponent = {"A": "rock", "B": "paper", "C": "scissors"}

strategy = {"X": "rock", "Y": "paper", "Z": "scissors"}

winners = (("rock", "paper"), ("paper", "scissors"), ("scissors", "rock"))

score = {"rock": 1, "paper": 2, "scissors": 3}


def main():
    t = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            r = line.strip().split(" ")
            p = (opponent[r[0]], strategy[r[1]])

            t += score[p[1]]  # lose

            if p[0] == p[1]:  # tie
                t += 3

            if p in winners:  # win
                t += 6

    print(f"Total score: {t}")


if __name__ == "__main__":
    main()
