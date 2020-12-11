#!/usr/bin/env python
"""
  Day 10
"""
import sys
from collections import defaultdict


def main():
    with open(sys.argv[1]) as f:
        joltages = [int(x.strip()) for x in f]

    joltages = sorted(joltages)
    joltages.insert(0, 0)  # make sure we have the right beginning

    """ Build up a tree of possible bi-(tri-)furcations

      - only care about the parents of a node, so just store those
  """
    tree = {}
    prev = []  # running set of potential parents
    for i, j in zip(joltages, joltages[1:]):
        prev = [x for x in prev if j - x < 4]
        tree[j] = prev
        prev.append(i)

    """ Roll up the tree, calculating sums as we go
  """
    sums = defaultdict(int)
    for j in reversed(joltages):
        if j not in tree:  # this is the top of the tree
            return sums[j]
        to_send = sums[j] if j in sums else 1
        for i in tree[j]:
            sums[i] += to_send


if __name__ == "__main__":
    print(main())
