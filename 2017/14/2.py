#!/usr/bin/env python
'''
    Day 14
'''
import operator
import sys

from collections import defaultdict


def process(string, length, skip, idx):
    ''' knot hash round '''
    lm = string + string
    lm[idx:idx+length] = reversed(lm[idx:idx+length])

    if (idx + length) > len(string):
        overage = idx + length
        beginning = lm[len(string):overage]
        rest = lm[overage - len(string):len(string)]
        return beginning + rest

    return lm[:len(string)]


def knot(instr):
    ''' given the input string, return a knot hash '''
    lengths = [ord(x) for x in instr]
    string = range(256)

    # as per problem, drop in some magic numbers
    magic = (17, 31, 73, 47, 23)
    lengths.extend(magic)

    idx = 0
    skip = 0

    # ok, do 64 rounds of this madness
    for _ in xrange(64):
        for length in lengths:
            string = process(string, length, skip, idx)
            idx = (idx + skip + length) % len(string)
            skip += 1

    # ok, now we have sparse hash; need dense hash
    dense = []
    for i in xrange(0, 256, 16):
        # dense.append('%0.2X' % reduce(operator.xor, string[i:i+16]))
        dense.append(reduce(operator.xor, string[i:i+16]))

    # return ''.join(dense).lower()
    return dense


def _e(x, y):
    ''' encode a (x,y) coord into a grid position '''
    return 128 * y + x


def add_to_graph(graph, src, x, y):
    ''' add edge to graph, given pair of coords '''
    dst = _e(x, y)
    graph[src].add(dst)
    graph[dst].add(src)


def graph_neighbours(graph, grid, x, y):
    ''' build the graph, given a coord '''
    if not grid[y][x]:
        return
    
    src = _e(x, y)
    graph[src] = set()

    # up
    if y-1 > -1 and grid[y-1][x]:
        add_to_graph(graph, src, x, y-1)

    # down
    if y+1 < 128 and grid[y+1][x]:
        add_to_graph(graph, src, x, y + 1)

    # left
    if x-1 > -1 and grid[y][x-1]:
        add_to_graph(graph, src, x-1, y)

    # right
    if x+1 < 128 and grid[y][x+1]:
        add_to_graph(graph, src, x+1, y)


def walk(graph, node):
    ''' BFS, as DFS ends with a blown stack '''
    seen = set()
    onode = [node]
    while onode:
        n = onode.pop(0)
        if n in seen:
            continue
        seen.add(n)
        for x in graph[n]:
            if x not in seen:
                onode.append(x)

    return seen


def main():
    ''' Day 14 == Day 10 + Day 12 '''
    for line in sys.stdin:
        key = line.strip()

    ''' this sneeze creates a 2D grid:

        [
            [1, 1, 0, 1, 0, 1 ...
            [0, 1, 0, 1, 0, 1, 0, 1 ... ],
            ...
        ]
    '''
    grid = [map(int, list(''.join(['{0:08b}'.format(x)
                          for x in knot(key + '-' + str(i))])
                          )
                ) 
            for i in range(128)
            ]

    ''' then, look at each co-ord, and build connections if neighbours have 
        bits that are set:

        1 -- 1    2
             |    |
             1    2

        for the nodes, give each location in the grid a unique ID:
        
        +---+---+---+---
        | 0 | 1 | 2 |...
        +---+---+---+---
        |128|129|130|...
        +---+---+---+---
        |   | ..
    '''
    graph = defaultdict(set)
    for y in range(128):
        for x in range(128):
            graph_neighbours(graph, grid, x, y)

    # identify connected components
    group = []
    while (graph):
        key = graph.keys()[0]
        seen = walk(graph, key)
        for i in seen:
            del graph[i]

        group.append(key)

    # FINAL ANSWER TIME!
    print 'GROUPS:', len(group)


if __name__ == '__main__':
    main()
