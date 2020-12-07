#!/usr/bin/env python
"""
  Day 7
"""
import re
import sys


BAGS = re.compile(" bag(s)?(\.)?")


def main():
    data = {}
    with open(sys.argv[1]) as f:
        for line in f:
            line = BAGS.sub("", line.strip())
            target, source = line.split(" contain ")

            if "no other" in source:
                data[target] = []
                continue

            data[target] = [
                (y[1], int(y[0])) for y in [x.split(" ", 1) for x in source.split(", ")]
            ]

    # depth-first search to keep intermediate results & feed totals up tree
    def count(bag, mult):
        # bag itself plus all its contents
        return mult + mult * sum(count(x[0], x[1]) for x in data[bag])

    # -1 to ignore shiny gold bag itself
    return count("shiny gold", 1) - 1


if __name__ == "__main__":
    print(main())
