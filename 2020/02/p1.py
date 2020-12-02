#!/usr/bin/env python
"""
  Advent 2
"""
import sys
from collections import Counter


def is_valid(line):
  rulepart, password = [x.strip() for x in line.split(":")]
  p = Counter(password)
  rangepart, item = rulepart.split(' ')
  low, high = [int(x) for x in rangepart.split('-')]
  return low <= p[item] <= high


def main():
  with open(sys.argv[1]) as f:
    return sum(is_valid(l) for l in f)

if __name__ == "__main__":
  print(main())