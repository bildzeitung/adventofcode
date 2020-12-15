#!/usr/bin/env python
"""
  Day 16
"""
import sys


def main():
    rules = {}
    with open(sys.argv[1]) as f:
        # read rules
        while r := f.readline().strip():
            label, rs = r.split(":")
            rs = [
                [int(z) for z in y]
                for y in [x.strip().split("-") for x in rs.split("or")]
            ]
            rules[label] = rs

        # skip read me
        while r := f.readline().strip():
            pass

        # read nearby
        nearby = []
        next(f)  # skip header
        while r := f.readline().strip():
            nearby.append([int(x) for x in r.split(",")])

    # evaluate values
    bad_tickets = []
    for ticket in nearby:
        bad_tickets.extend(
            item
            for item in ticket
            if not any(
                any(x[0] <= item <= x[1] for x in rule) for rule in rules.values()
            )
        )

    return sum(bad_tickets)


if __name__ == "__main__":
    print(main())
