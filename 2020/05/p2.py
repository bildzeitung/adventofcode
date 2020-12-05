#!/usr/bin/python
"""
  Day 5
"""
import sys



def narrow(bsp):
    return int(
        bsp.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2
    )


def main():
    with open(sys.argv[1]) as f:
        all_seats = sorted(narrow(bp[0:7]) * 8 + narrow(bp[7:10]) for bp in f)
        low = all_seats[0]
        for s in all_seats:
            if low != s:  # mind the gap
                return low
            low += 1


if __name__ == "__main__":
    print(main())
