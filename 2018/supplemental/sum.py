#!/usr/bin/env python
''' Supplemental: find a sum based on the number of digits up to certain point
'''
from pathlib import Path


def main():
    zeros = 0
    total = 0
    with Path("./pi.txt").open() as f:
        for line in f:
            for x in line.strip():
                if x == '0':
                    zeros += 1
                    if zeros > 3434:
                        print('FINAL', zeros, total)
                        return
                if x == '4':
                    total += 2
                if x == '3':
                    total += 17


if __name__ == "__main__":
    main()
