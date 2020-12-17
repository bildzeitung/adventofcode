#!/usr/bin/env python
"""
  Day 16

  ** Actual p2 calc
"""
import math
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

        next(f)  # skip header
        while r := f.readline().strip():
            my_ticket = [int(x) for x in r.split(",")]

        # read nearby
        nearby = []
        next(f)  # skip header
        while r := f.readline().strip():
            nearby.append([int(x) for x in r.split(",")])

    # rotate tickets for easier processing
    columns = [[x[i] for x in nearby] for i in range(len(rules))]
    to_deduce = []
    for c in columns:
        to_deduce.append(
            set.intersection(
                *[set([k for k, rule in rules.items() if rule(i)]) for i in c]
            )
        )
    # print(to_deduce)

    final = {}
    while True:
        to_remove = set()
        for i, x in enumerate(to_deduce):
            if len(x) == 1:
                print(f"{i} -> {x}")
                to_remove |= x
                final[x.pop()] = i

        if not to_remove:
            break

        to_deduce = [x - to_remove for x in to_deduce]

    x = [my_ticket[final[x]] for x in final if "departure" in x]
    print(x)
    return math.prod(x)


if __name__ == "__main__":
    print(main())
