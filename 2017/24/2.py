#!/usr/bin/env python
'''
    Day 24
'''
import sys

from copy import deepcopy


def search_paths(from_port, ports, orig_path=[]):
    ''' Do a depth-first search
    '''
    joins = [x for x in ports if from_port in x]
    if not joins:
        return len(orig_path), sum(x[0] + x[1] for x in orig_path)

    max_length = 0
    max_strength = 0
    for port in joins:
        path = deepcopy(orig_path)
        path.append(port)
        to_port = port[0] if port[0] != from_port else port[1]
        new_ports = deepcopy(ports)
        new_ports.remove(port)
        length, strength = search_paths(to_port, new_ports, path)
        if length > max_length:
            max_length = length
            max_strength = strength
        elif length == max_length and strength > max_strength:
            max_strength = strength

    return max_length, max_strength


def main():
    ''' Load data file and enter recursive routine
    '''
    ports = [tuple([int(x), int(y)]) for x, y in
             [line.strip().split('/') for line in sys.stdin]]

    print search_paths(0, ports)


if __name__ == '__main__':
    main()
