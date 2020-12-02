#!/usr/bin/env python
"""
  Advent 2
"""
import sys
from collections import Counter


def is_valid(line):
  rulepart, password = [x.strip() for x in line.split(":")]
  rangepart, item = rulepart.split(' ')
  p1, p2 = [int(x) for x in rangepart.split('-')]
  return (password[p1-1] == item) ^ (password[p2-1] == item)


def main():
  with open(sys.argv[1]) as f:
    return sum(is_valid(l) for l in f)

if __name__ == "__main__":
  print(main())