#!/usr/bin/env python
""" Day 8

    A little bit of n-ary tree manipulation
"""
import sys
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Node:
    """ A tree node has m children and n metadata elements
    """

    children: list = field(default_factory=list)
    metadata: list = field(default_factory=list)


def load_tree(f):
    """ Read the single line in and turn it into a list
    """
    spec = [int(x) for x in f.readline().strip().split(" ")]

    return get_node(spec, 0)[0]


def get_node(spec, i):
    """ Recursive node loading

        This indexes the data, and does not move it around at all.
        A Node() and the index of the next item to process is returned.
    """
    # read the header
    num_children = spec[i]
    num_meta = spec[i + 1]
    # advance the index pointer
    i += 2

    # read the children, recursively
    children = []
    for _ in range(num_children):
        child, i = get_node(spec, i)
        children.append(child)

    metadata = spec[i : i + num_meta]
    return Node(children, metadata), i + num_meta


def get_sum(tree):
    """ Depth-first tree traversal
    """
    return sum(tree.metadata) + sum(get_sum(x) for x in tree.children)


def main():
    with Path(sys.argv[1]).open() as f:
        tree = load_tree(f)

    print(tree)
    print(get_sum(tree))


if __name__ == "__main__":
    main()
