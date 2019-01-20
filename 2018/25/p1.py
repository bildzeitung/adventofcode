#!/usr/bin/env python
'''
    Day 25: Build-a-graph

    The problem statement basically asks to generate a graph, and then
    calculate the number of connected components.

    IMHO, a "connected component" includes single elements, but networkx
    disagrees, so the calculation is the number of connected components
    plus the number of left over nodes that are not in any of those components.
'''
import sys
from itertools import combinations
from pathlib import Path

import networkx as nx


def main():
    stars = []
    with Path(sys.argv[1]).open() as f:
        stars = [tuple(int(x) for x in l)
                 for l in [line.strip().split(',') for line in f]]

    G = nx.Graph()
    for i, j in combinations(stars, 2):
        # calc 4-D Manhattan distance the slow way
        if sum(abs(a - b) for a, b in zip(i, j)) <= 3:
            G.add_edge(i, j)

    total = (nx.number_connected_components(G) +
             len(stars) - sum(len(c) for c in nx.connected_components(G)))
    print('TOTAL', total)


if __name__ == "__main__":
    main()
