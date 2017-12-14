#!/usr/bin/env python
'''
   Day 6
'''
import sys

from collections import deque


def getmax(banks):
  # return banks.index(max(banks))
  return max(xrange(len(banks)), key=banks.__getitem__)


def churn(banks):
  idx = getmax(banks)
  value = banks[idx]
  banks[idx] = 0
  add_to_all = value / len(banks)
  print 'Idx:', idx, 'Value:', value, 'a2a:', add_to_all
  mod  = value % len(banks)
  mask = [1] * mod
  mask.extend([0] * (len(banks) - mod))
  d = deque(mask)
  d.rotate(idx + 1)
  # print mask
  # print d

  for i in xrange(len(banks)):
    banks[i] += add_to_all + d[i]

  # print banks


def main():
  banks = map(int, sys.stdin.readline().strip().split())
  n = 0

  all_lists = set()
  while tuple(banks) not in all_lists:
    print banks
    all_lists.add(tuple(banks))
    churn(banks)
    n += 1

  print 'N:', n


if __name__ == '__main__':
  main()
