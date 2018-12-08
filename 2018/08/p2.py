#!/usr/bin/env python
""" Day 8

    A different summation, but still based on the same data structure
"""
import sys
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Node:
    children: list = field(default_factory=list)
    metadata: list = field(default_factory=list)


def load_tree(f):
    spec = [int(x) for x in f.readline().strip().split(" ")]

    return get_node(spec, 0)[0]


def get_node(spec, i):
    num_children = spec[i]
    num_meta = spec[i + 1]
    i += 2

    children = []
    for _ in range(num_children):
        child, i = get_node(spec, i)
        children.append(child)

    metadata = spec[i : i + num_meta]
    return Node(children, metadata), i + num_meta


def get_sum(tree):
    # base case; if there are no children, sum the metadata
    if not tree.children:
        return sum(tree.metadata)

    """ otherwise, recursively descend into the tree until leaf nodes
        bubble back up.

        n.b. for top performance, some memoization could be used, since
             nodes can be referenced repeatedly, but in practice it didn't
             matter
    """
    total = 0
    for i in tree.metadata:
        if i == 0:
            continue
        try:
            total += get_sum(tree.children[i - 1])
        except IndexError:
            pass

    return total


def main():
    with Path(sys.argv[1]).open() as f:
        tree = load_tree(f)

    print(get_sum(tree))


if __name__ == "__main__":
    main()
