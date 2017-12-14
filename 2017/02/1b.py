#!/usr/bin/env python

import sys


def main():
    print sum(max(y) - min(y) for y in [
		[int(x) for x in line.strip().split()] for line in sys.stdin
	                                ]
    	      )


if __name__ == '__main__':
  main()
