#!/usr/bin/env python
'''
    Day 22

    Use A* to pick out a route.

    ** This solution has the benefit of failing the test problem, but working
       on the actual problem input.

       So it's wrong. Somewhere. Clearly. It should work for both. Sigh.
'''
import sys
from pathlib import Path
from heapq import heappush, heappop
from dataclasses import dataclass, field

ETYPES = ['.', '=', '|']
erosion = {}
regions = {}
target = None


@dataclass(order=True, unsafe_hash=True)
class HeapNode:
    f: int = field(init=False)
    g: int = field(compare=False)
    h: int = field(compare=False)
    tool: str = field(compare=False)
    pos: tuple = field(compare=False)
    is_removed: bool = field(compare=False, default=False, init=False)

    def __post_init__(self):
        self.f = self.g + self.h


def process(depth, target):
    ''' Make the generation arbitrarily large
    '''
    T = (target[0] * 2, target[1] * 2)
    for y in range(0, target[1] * 2 + 1):
        for x in range(0, target[0] * 100 + 1):
            pos = (x, y)
            if pos == (0, 0):
                geo_index = 0
            if pos == T:
                geo_index = 0
            elif y == 0:
                geo_index = x * 16807
            elif x == 0:
                geo_index = y * 48271
            else:
                geo_index = erosion[(x - 1, y)] * erosion[(x, y - 1)]
            erosion[pos] = (geo_index + depth) % 20183
            regions[pos] = ETYPES[erosion[pos] % 3]


def heapNodeFactory(pos, g, tool):
    h = abs(pos[0] - target[0]) + abs(pos[1] - target[1])
    return HeapNode(g, h, tool, pos)


def path(T):
    starting_position = (0, 0)
    node = heapNodeFactory(starting_position, 0, "torch")

    open_list = []
    closed_set = set()
    open_index = {(node.pos, "torch"): node}

    heappush(open_list, node)

    examined = 0
    while open_list:
        examined += 1
        node = heappop(open_list)

        if node.pos == T and node.tool == 'torch':
            print('DONE', examined, node)
            return

        if node.is_removed:
            continue

        k = (node.pos, node.tool)
        if k in closed_set:
            continue
        del open_index[k]
        closed_set.add(k)

        def add_to_open(pos):
            to_add = []
            g = node.g + 1

            if regions[node.pos] == '.':
                if regions[pos] == '.':
                    to_add.append(heapNodeFactory(pos, g, node.tool))
                if regions[pos] == '|':
                    if node.tool == 'torch':
                        to_add.append(heapNodeFactory(pos, g, node.tool))
                    else:
                        to_add.append(heapNodeFactory(node.pos, node.g + 7, 'torch'))
                if regions[pos] == '=':
                    if node.tool == 'climb':
                        to_add.append(heapNodeFactory(pos, g, node.tool))
                    else:
                        to_add.append(heapNodeFactory(node.pos, node.g + 7, 'climb'))

            if regions[node.pos] == '=':
                if regions[pos] == '=':
                    to_add.append(heapNodeFactory(pos, g, node.tool))
                if regions[pos] == '.':
                    if node.tool == 'climb':
                        to_add.append(heapNodeFactory(pos, g, node.tool))
                    else:
                        to_add.append(heapNodeFactory(node.pos, node.g + 7, 'climb'))
                if regions[pos] == '|':
                    if node.tool == 'neither':
                        to_add.append(heapNodeFactory(pos, g, node.tool))
                    else:
                        to_add.append(heapNodeFactory(node.pos, node.g + 7, 'neither'))

            if regions[node.pos] == '|':
                if regions[pos] == '|':
                    to_add.append(heapNodeFactory(pos, g, node.tool))
                if regions[pos] == '.':
                    if node.tool == 'torch':
                        to_add.append(heapNodeFactory(pos, g, node.tool))
                    else:
                        to_add.append(heapNodeFactory(node.pos, node.g + 7, 'torch'))
                if regions[pos] == '=':
                    if node.tool == 'neither':
                        to_add.append(heapNodeFactory(pos, g, node.tool))
                    else:
                        to_add.append(heapNodeFactory(node.pos, node.g + 7, 'neither'))

            assert len(to_add) == 1, len(to_add)
            for i in to_add:
                x = (i.pos, i.tool)
                if x in open_index:
                    if i.g < open_index[x].g:
                        open_index[x].is_removed = True
                    else:
                        continue
                open_index[x] = i
                heappush(open_list, i)

        # left
        pos = (node.pos[0] - 1, node.pos[1])
        if pos[0] > -1:
            add_to_open(pos)

        # right
        pos = (node.pos[0] + 1, node.pos[1])
        add_to_open(pos)

        # up
        pos = (node.pos[0], node.pos[1] - 1)
        if pos[1] > -1:
            add_to_open(pos)

        # down
        pos = (node.pos[0], node.pos[1] + 1)
        add_to_open(pos)


def main():
    global target
    with Path(sys.argv[1]).open() as f:
        depth = int(f.readline().split(':')[1].strip())
        target = [int(x) for x in
                  f.readline().split(':')[1].strip().split(',')]
        print('DEPTH', depth)
    process(depth, target)
    T = (target[0], target[1])
    path(T)


if __name__ == "__main__":
    main()
