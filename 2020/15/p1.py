#!/usr/bin/env python
"""
  Day 15
"""
import sys


def main():
  with open(sys.argv[1]) as f:
    input = [int(x) for x in f.readline().strip().split(",")]

  last_spoken = input[-1]
  last_seen = {x:i+1 for i, x in enumerate(input[:-1])}
  turn = len(input) + 1
  while turn < 2021:
    if last_spoken not in last_seen:
      spoken = 0
      last_seen[last_spoken] = turn - 1
    else:
      #print(f"Last seen {last_spoken}: {last_seen[last_spoken]}")
      spoken = turn - 1 - last_seen[last_spoken]
      last_seen[last_spoken] = turn - 1
    #print(f"Turn {turn}, spoke: {spoken}")
    turn += 1
    last_spoken = spoken
  
  return spoken


if __name__ == "__main__":
    print(main())