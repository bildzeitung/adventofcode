#!/usr/bin/env python
'''
    Day 12
'''
import sys

from collections import defaultdict

GRAPH = defaultdict(set)


def walk(node, seen):
    ''' Walk the graph, record the nodes we saw

        Depth-first, but it doesn't matter, really
    '''
    for n in GRAPH[node]:
        if n in seen:
            continue
        seen.add(n)
        walk(n, seen)


def main():
    ''' Load the graph, walk it
    '''
    for line in sys.stdin:
        src, dst = line.strip().split('<->')
        dst = set(int(x) for x in dst.split(','))
        src = int(src)
        GRAPH[src] = GRAPH[src] | dst

    # walk through group 0
    seen = set()
    walk(0, seen)
    print 'SAW:', len(seen)


if __name__ == '__main__':
    main()