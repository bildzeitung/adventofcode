#!/usr/bin/env python
'''
    Day 24
'''
import sys

from copy import deepcopy


def search_paths(from_port, ports, orig_strength, orig_path=[]):
    ''' Do a depth-first search
    '''
    joins = [x for x in ports if from_port in x]
    if not joins:
        return orig_strength

    max_value = 0
    for port in joins:
        path = deepcopy(orig_path)
        path.append(port)
        strength = orig_strength + sum(port)
        to_port = port[0] if port[0] != from_port else port[1]
        new_ports = deepcopy(ports)
        new_ports.remove(port)
        value = search_paths(to_port, new_ports, strength, path)
        max_value = value if value > max_value else max_value

    return max_value


def main():
    ''' Load data file and enter recursive routine
    '''
    ports = [tuple([int(x), int(y)]) for x, y in
             [line.strip().split('/') for line in sys.stdin]]

    print search_paths(0, ports, 0)


if __name__ == '__main__':
    main()
