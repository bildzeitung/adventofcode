#!/usr/bin/env python
'''
  Day 5
'''
import sys


def main():
  jmps = [int(line.strip()) for line in sys.stdin]

  idx = 0
  max = len(jmps)
  count = 0

  while (idx > -1 and idx < max):
    new_idx = idx + jmps[idx]

    if jmps[idx] > 2:
      jmps[idx] -= 1
    else:
      jmps[idx] += 1
    idx = new_idx
    count += 1

  print "COUNT:", count


if __name__ == '__main__':
  main()
