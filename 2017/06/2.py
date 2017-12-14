#!/usr/bin/env python
'''
   Day 6
'''
import sys

from collections import deque


def getmax(banks):
  return max(xrange(len(banks)), key=banks.__getitem__)


def churn(banks):
  idx = getmax(banks)
  value = banks[idx]
  banks[idx] = 0
  add_to_all = value / len(banks)
  mod  = value % len(banks)
  mask = [1] * mod
  mask.extend([0] * (len(banks) - mod))
  d = deque(mask)
  d.rotate(idx + 1)

  for i in xrange(len(banks)):
    banks[i] += add_to_all + d[i]


def main():
  banks = map(int, sys.stdin.readline().strip().split())
  n = 0

  all_lists = dict()
  while tuple(banks) not in all_lists:
    print banks
    all_lists[tuple(banks)] = n
    churn(banks)
    n += 1

  print 'N:', n
  print 'L:', n - all_lists[tuple(banks)]


if __name__ == '__main__':
  main()
