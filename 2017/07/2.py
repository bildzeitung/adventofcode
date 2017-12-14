#!/usr/bin/env python
'''
    Day 7

'''
import sys


node_weights = {}

def get_unbalance(key, children):
  if not children:  # leaf nodes are not unbalanced
    return node_weights[key]
 
  weights = [(x, get_unbalance(x, children[x])) for x in children]
  # if the children are out of balance, then adjust the internal node
  # so, this is the 1st point of imbalance and the depth-first search
  # can end; raise an Exception to skip out of the call stack
  if not all(x[1] == weights[0][1] for x in weights):
    raise Exception('{0} is unbalanced:'.format(key) + '\n\t' +
                    '\n\t'.join(['{0} ({1}): {2}'.format(x[0], node_weights[x[0]], x[1]) for x in weights])
                    )

  return node_weights[key] + sum(x[1] for x in weights)


def parse_node(node):
  name, weight = node.split()
  name = name.strip()
  weight = int(weight[1:-1])
  node_weights[name] = weight
  return name


def main():
    tree = {}
    to_process = []
    for line in sys.stdin:
        node = line.strip().split('->')
	name = parse_node(node[0])
        if len(node) > 1:  # internal node
            children = [x.strip() for x in node[1].split(',')]
	    to_process.append([name, children])
        else:  # leaf
            tree[name] = {}

    # assemble tree (breadth-first search)
    while (to_process):
      candidate = to_process.pop(0)
      if all(x in tree for x in candidate[1]):
        tree[candidate[0]] = dict((k, tree[k]) for k in candidate[1])
	for k in candidate[1]:
          del tree[k]
      else:
        to_process.append(candidate)

    # sort out imbalance; depth-first search
    root = tree.keys()[0]
    try:
      get_unbalance(root, tree[root])
    except Exception as e:
      print str(e)


if __name__ == '__main__':
    main()
