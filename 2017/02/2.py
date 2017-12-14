#!/usr/bin/env python

import sys

from itertools import permutations


def cdiv(items):
  for x in permutations(items, 2):
    if x[0] < x[1]:
      continue

    if not (x[0] % x[1]):
      return x[0] / x[1]


def checksum(items):
  print sum( cdiv(x) for x in items)


def main():
    checksum(
      [int(x) for x in line.strip().split()] for line in sys.stdin
    )


if __name__ == '__main__':
  main()
