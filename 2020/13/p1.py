#!/usr/bin/env python
"""
  Day 13
"""
import sys


def main():
    with open(sys.argv[1]) as f:
        earliest = int(f.readline().strip())
        buses = [int(x) for x in f.readline().strip().replace("x,", "").split(",")]

    print(earliest, buses)
    busmod = {x: x - earliest % x for x in buses}
    print(busmod)
    catch_this_one = sorted(busmod, key=lambda x: busmod[x])[0]
    print(f"-> {catch_this_one}")
    return catch_this_one * busmod[catch_this_one]


if __name__ == "__main__":
    print(main())
