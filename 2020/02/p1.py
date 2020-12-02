#!/usr/bin/env python
"""
  Advent 2

  Evaluate a string given a rule, all data-driven

"""
import sys


def is_valid(line):
  """ Evaluate password against the rule

      1-2 x: xpxc
      | | |  ^^^^- password
      | |  +- char to count
      | +---- upper end of range
      +------ low end of range

      n.b. ranges are INCLUSIVE
  """
  rulepart, password = [x.strip() for x in line.split(":")]
  rangepart, item = rulepart.split(' ')
  low, high = [int(x) for x in rangepart.split('-')]
  #
  # TIL! Strings have built-in counters!
  # >>> "foo".count("o") == 2
  #
  return low <= password.count(item) <= high


def main():
  with open(sys.argv[1]) as f:
    return sum(is_valid(l) for l in f)

if __name__ == "__main__":
  print(main())