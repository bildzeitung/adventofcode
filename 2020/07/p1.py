#!/usr/bin/env python
"""
  Day 7
"""
import re
import sys
from collections import defaultdict


BAGS = re.compile(" bag(s)?(\.)?")


def main():
    data = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line = BAGS.sub("", line.strip())
            target, source = line.split(" contain ")

            # don't need leaf nodes
            if "no other" in source:
                continue

            # discard quantity; don't need it
            for c in [x.split(" ", 1)[1] for x in source.split(", ")]:
                data[c].append(target)

    # level-order traversal; count # of nodes encountered
    count = 0
    walk = data["shiny gold"]
    seen = []
    while walk:
        i = walk.pop(0)
        count += 1
        walk.extend(x for x in data[i] if x not in seen and x not in walk)
        seen.append(i)

    return count


if __name__ == "__main__":
    print(main())
