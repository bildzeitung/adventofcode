#!/usr/bin/env python
''' Day 13
'''
import sys
from collections import Counter
from pathlib import Path
from dataclasses import dataclass, field


DIRMAP = {'>': '-',
          'v': '|',
          '<': '-',
          '^': '|',
          }

DIRS = ['>', 'v', '<', '^']
GONNAS = ['left', 'straight', 'right']


@dataclass
class Cart:
    pos: tuple
    direction: str
    maze: list = field(repr=False)
    gonna_turn: str = 'left'
    dead: bool = False

    def died(self):
        self.dead = True

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def under(self):
        return self.maze[self.y][self.x]

    def tick(self):
        assert(self.under != ' ')

        if self.under == '/':
            if self.direction == '<':
                self.direction = 'v'
            elif self.direction == '>':
                self.direction = '^'
            elif self.direction == 'v':
                self.direction = '<'
            else:  # going up
                self.direction = '>'

        if self.under == '\\':
            if self.direction == '>':
                self.direction = 'v'
            elif self.direction == '<':
                self.direction = '^'
            elif self.direction == 'v':
                self.direction = '>'
            else:  # going up
                self.direction = '<'

        if self.under == '+':
            if self.gonna_turn == 'left':
                self.direction = DIRS[(DIRS.index(self.direction) - 1) % len(DIRS)]
            if self.gonna_turn == 'right':
                self.direction = DIRS[(DIRS.index(self.direction) + 1) % len(DIRS)]

            self.gonna_turn = GONNAS[(GONNAS.index(self.gonna_turn) + 1) % len(GONNAS)]

        if self.direction == '>':
            self.pos = (self.x + 1, self.y)
        if self.direction == '<':
            self.pos = (self.x - 1, self.y)
        if self.direction == 'v':
            self.pos = (self.x, self.y + 1)
        if self.direction == '^':
            self.pos = (self.x, self.y - 1)


def load_file():
    with Path(sys.argv[1]).open() as f:
        maze = [[x for x in line.rstrip()] for line in f]

    carts = []
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if item in DIRMAP.keys():
                maze[i][j] = DIRMAP[item]
                carts.append(Cart((j, i), item, maze))

    return maze, carts


def main():
    maze, carts = load_file()
    total_carts = len(carts)
    while total_carts > 1:
        for cart in sorted(carts, key=lambda x: x.pos):
            # speed up performance a bit when the carts thin out
            if cart.dead:
                continue

            cart.tick()
            common = Counter(x.pos for x in carts if not x.dead).most_common()[0]
            if common[1] > 1:
                print('collision', common)
                total_carts -= 2
                for c in carts:
                    if c.pos == common[0]:
                        c.died()

    print('FINAL', [c for c in carts if not c.dead])



if __name__ == '__main__':
    main()
