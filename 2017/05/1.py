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

  # print 'START:', jmps

  while (idx > -1 and idx < max):
    new_idx = idx + jmps[idx]
    jmps[idx] += 1
    idx = new_idx
    count += 1
    # print jmps, '|', idx

  print "COUNT:", count


if __name__ == '__main__':
  main()
