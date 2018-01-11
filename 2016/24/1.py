#!/usr/bin/env python
'''
    Day 24
'''
import sys
from collections import defaultdict
from itertools import permutations


def get_poi(maze, poi):
    ''' Return a tuple with the coords for 0
    '''
    for y, row in enumerate(maze):
        try:
            x = row.index(poi)
            return (x, y)
        except ValueError:
            continue


def make_graph(graph, maze, poi):
    ''' Given a Point of Interest, return reachable edges
    '''
    print 'Graphing', poi
    p = [(get_poi(maze, poi), 0)]
    seen = set()
    new_endpoints = []
    while p:
        point, steps = p.pop(0)
        if point in seen:
            continue

        x, y = point
        seen.add(point)

        # reached a number
        if maze[y][x] != '.' and maze[y][x] != poi:
            endpoint = maze[y][x]
            # no dupes
            if poi in graph and endpoint in graph[poi]:
                continue
            new_endpoints.append(endpoint)
            graph[poi][endpoint] = steps
            graph[endpoint][poi] = steps
            print 'Found', poi, '->', endpoint
            continue

        # down
        if maze[y+1][x] != '#' and (x, y + 1) not in seen:
            p.append(((x, y + 1), steps + 1))

        # up
        if maze[y-1][x] != '#' and (x, y - 1) not in seen:
            p.append(((x, y - 1), steps + 1))

        # right
        if maze[y][x+1] != '#' and (x + 1, y) not in seen:
            p.append(((x + 1, y), steps + 1))

        # left
        if maze[y][x-1] != '#' and (x - 1, y) not in seen:
            p.append(((x - 1, y), steps + 1))

    return new_endpoints


def main(data):
    ''' Read in the maze. Create a graph. Find the shortest path.
    '''
    maze = [list(line.strip()) for line in data]
    maze_size = len(maze[0]) * len(maze)
    print 'MAZE IS (', len(maze[0]), 'x', len(maze), ') ==>', maze_size

    # create a graph with paths for all accessible nodes
    top = ['0']
    graph = defaultdict(dict)
    while top:
        top.extend(make_graph(graph, maze, top.pop(0)))
    print 'TOTAL GRAPH', graph

    def maxintdict():
        return defaultdict(lambda: maze_size)

    # APSP [Floyd-Warshall]
    dist = defaultdict(maxintdict)
    for vertex in graph.keys():
        dist[vertex][vertex] = 0
    for u, edges in graph.iteritems():
        for v, weight in edges.iteritems():
            dist[u][v] = weight
    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # ok, now find the shortest walk through, starting from 0
    shortest_walk = maze_size
    vertices = graph.keys()
    vertices.remove('0')
    for c in permutations(vertices):
        # for each permutation, calc the path
        current = '0'
        walk = 0
        for i in xrange(len(c)):
            item = c[i]
            walk += dist[current][item]
            current = item
        if walk < shortest_walk:
            shortest_walk = walk

    print 'WALK', shortest_walk


if __name__ == '__main__':
    with open(sys.argv[1]) as infile:
        main(infile)
