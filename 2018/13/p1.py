#!/usr/bin/env python
''' Day 13

    Rail running simulator

'''
import sys
from collections import Counter
from pathlib import Path
from dataclasses import dataclass, field

# for fixing up the maze when the carts are removed
DIRMAP = {'>': '-',
          'v': '|',
          '<': '-',
          '^': '|',
          }

# DIRMAP.keys() would be ok, but this is a shortcut
DIRS = ['>', 'v', '<', '^']

# list of the intersection criteria, in order for cycling
GONNAS = ['left', 'straight', 'right']


@dataclass
class Cart:
    ''' State info for a cart
    '''
    pos: tuple
    direction: str
    maze: list = field(repr=False)
    gonna_turn: str = 'left'

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def under(self):
        ''' That is, what kind of track is under the cart?
        '''
        return self.maze[self.y][self.x]

    def tick(self):
        ''' Move the cart, according to the track and its direction
        '''
        assert(self.under != ' ')  # cross check! off the rails!

        # TODO: replace with a hash table
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

        # if it's not a corner, it could be an intersection
        if self.under == '+':
            diradjust = 0  # go straight, in other words
            if self.gonna_turn == 'left':
                diradjust = -1
            elif self.gonna_turn == 'right':
                diradjust = 1

            self.direction = DIRS[(DIRS.index(self.direction) +
                                   diradjust) % len(DIRS)]

            self.gonna_turn = GONNAS[(GONNAS.index(self.gonna_turn) + 1)
                                     % len(GONNAS)]

        # finally: move the cart
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

    # remove the carts and place them into their own list
    carts = []
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if item in DIRMAP.keys():
                maze[i][j] = DIRMAP[item]
                carts.append(Cart((j, i), item, maze))

    return maze, carts


def main():
    maze, carts = load_file()
    for x in maze:
        print(''.join(x))

    while True:
        print(carts)
        ''' The lexical ordering is important, as stated in the problem,
            as a crash is registered when it happens, not at the end of
            the tick.

            This loop, therefore, moves a cart, checks for a collision,
            and so forth.
        '''
        for cart in sorted(carts, key=lambda x: x.pos):
            cart.tick()
            common = Counter(x.pos for x in carts).most_common()[0]
            if common[1] > 1:
                print('collision:', common)
                return


if __name__ == '__main__':
    main()
