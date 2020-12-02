#!/usr/bin/env python
"""
  Advent 2
"""
import sys


def is_valid(line):
  """ Evaluate password against the rule

      1-2 x: xpxc
      | | |  ^^^^- password
      | |  +- char to check
      | +---- position 1
      +------ position 2

      n.b. positions are 1-indexed, so adjust

      Rule is that at least one, but not both positions contain the
      character to check.
  """
  rulepart, password = [x.strip() for x in line.split(":")]
  rangepart, item = rulepart.split(' ')
  p1, p2 = [int(x) for x in rangepart.split('-')]
  #
  # TIL! XOR bitwise operator works properly against bool()
  return (password[p1-1] == item) ^ (password[p2-1] == item)


def main():
  with open(sys.argv[1]) as f:
    return sum(is_valid(l) for l in f)

if __name__ == "__main__":
  print(main())