#!/usr/bin/env python

import sys


def checksum(items):
  print sum( max(x) - min(x) for x in items)

def main():
    checksum(
      [int(x) for x in line.strip().split()] for line in sys.stdin
    )

if __name__ == '__main__':
  main()
