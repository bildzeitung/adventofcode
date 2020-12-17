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
                f"({y[0]} <= x <= {y[1]})"
                for y in [x.strip().split("-") for x in rs.split("or")]
            ]
            rules[label] = eval(f'lambda x: {" or ".join(rs)}')

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
            item for item in ticket if not any(rule(item) for rule in rules.values())
        )

    return sum(bad_tickets)


if __name__ == "__main__":
    print(main())
