#!/usr/bin/python
"""
  Day 5
"""
import sys


def getrow(bsp):
  left = 0
  right = 127
  for k in bsp:
    if k == 'F':
      right = (right - left) / 2 + left
    else:
      left = (right - left + 1) / 2 + left
  assert left == right
  return left


def getcol(bsp):
  left = 0
  right = 7
  for k in bsp:
    if k == 'L':
      right = (right - left) / 2 + left
    else:
      left = (right - left + 1) / 2 + left
  assert left == right
  return left


def main():
  with open(sys.argv[1]) as f:
    #for bp in f:
      #row = getrow(bp[0:7])
      #col = getcol(bp[7:10])
      #print(row, col, row * 8 + col)
    return max(getrow(bp[0:7]) * 8 + getcol(bp[7:10]) for bp in f)


if __name__ == "__main__":
  print(main())