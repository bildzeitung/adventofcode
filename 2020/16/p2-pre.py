#!/usr/bin/env python
"""
  Day 16

  ** need to filter out bad tickets from the data set
  ** this dumps out the input file, less the bad tickets
"""
import sys


def main():
    rules = {}
    with open(sys.argv[1]) as f:
        # read rules
        while r := f.readline().strip():
            label, rs = r.split(":")
            rs = [
                f"({y[0]} <= x <= {y[1]})"
                for y in [x.strip().split("-") for x in rs.split("or")]
            ]
            rules[label] = eval(f'lambda x: {" or ".join(rs)}')
            print(r)

        # skip read me
        print()
        while r := f.readline().strip():
            print(r)
        print()

        # read nearby
        nearby = []
        print(next(f).strip())  # skip header
        while r := f.readline().strip():
            nearby.append([int(x) for x in r.split(",")])

    # evaluate values
    bad_tickets = []
    for ticket in nearby:
        bad = [
            item for item in ticket if not any(rule(item) for rule in rules.values())
        ]
        if not bad:
            print(",".join([str(x) for x in ticket]))


if __name__ == "__main__":
    main()
