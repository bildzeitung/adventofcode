#!/usr/bin/env python
"""
  Day 15

  Used this for part 1 and brute forced part 2, too.

"""
import sys


def main():
    with open(sys.argv[1]) as f:
        input = [int(x) for x in f.readline().strip().split(",")]

    last_spoken = input[-1]
    last_seen = {x: i + 1 for i, x in enumerate(input[:-1])}
    turn = len(input)
    #  while turn < 2020:  # part 1
    while turn < 30000000:  # part 2
        if last_spoken not in last_seen:
            spoken = 0
        else:
            spoken = turn - last_seen[last_spoken]
        last_seen[last_spoken] = turn
        # print(f"Turn,{turn+1},spoke,{spoken}")
        turn += 1
        last_spoken = spoken

    return spoken


if __name__ == "__main__":
    print(main())
