#!/usr/bin/env python
'''
    Day 7
'''
import sys


def main():
    tree = {}
    for line in sys.stdin:
        node = line.strip().split('->')
        if len(node) > 1:  # skip leaf nodes; they're not roots
            node, children = node
	    node = node.split()[0].strip()
            children = [x.strip() for x in children.split(',')]
	    tree[node] = children

    # to find the head of the tree, prune the leaves
    # via a mark 'n' sweep; (del in iteritems() is bad)
    while len(tree) > 1:
      mark = []
      for n, c in tree.iteritems():
        # if none of the children are in the tree, it is a leaf
        if all(x not in tree for x in c):
          mark.append(n)

      # prune all leaf nodes
      for n in mark:
        del tree[n]

      print tree


if __name__ == '__main__':
    main()
