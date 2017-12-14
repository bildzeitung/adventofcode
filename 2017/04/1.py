#!/usr/bin/env python
'''
    Day 4
'''
import sys


def is_valid_passphrase(line):
  words = line.split(' ')
  return len(set(words)) == len(words)


def main():
  print sum(is_valid_passphrase(line.strip()) for line in sys.stdin)


if __name__ == '__main__':
  main()
