#!/usr/bin/env python
""" 
    Day 15
"""
import sys
from time import sleep
from collections import defaultdict
from pathlib import Path

from apollo import Apollo

WALL = "#"
HALL = "."


class FinishedException(Exception):
    pass


class InputOutputProvider:
    """ Run the robot around the entire maze

        If we break once the oxygen is found, we have no guarantee that we
        have the shortest path. Since Part 2 needs a complete map anyway,
        build it up and then use the data to answer the questions.
    """

    MOVES = [0, 1, 2, 3]  # N, S, W, E
    MOVEDIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    OPPOSITE = [1, 0, 3, 2]

    def __init__(self):
        self._canvas = defaultdict(lambda: " ")
        self._canvas[(0, 0)] = HALL
        self._moves = [{"move": None, "to-try": self.MOVES[:]}]
        self._pos = (0, 0)
        self._last_move = None
        self._oxygen = None
        self._backtrack = False

    @property
    def canvas(self):
        return self._canvas

    @property
    def oxygen(self):
        return self._oxygen

    def draw(self):
        print("\033[2J")  # clear screen
        print("\033[0;0H")  # cursor to top of term
        min_x = min(x[0] for x in self._canvas)
        min_y = min(x[1] for x in self._canvas)
        max_x = max(x[0] for x in self._canvas)
        max_y = max(x[1] for x in self._canvas)
        for y in range(min_y, max_y + 1):
            r = ""
            for x in range(min_x, max_x + 1):
                if (x, y) == self._pos:
                    r += "D"
                elif (x, y) == (0, 0):
                    r += "S"
                else:
                    r += self._canvas[(x, y)]
            print(r)
        print(f"Queue: {len(self._moves)}")

    def pop(self, _):
        """ Robot looking for input

            Algorithm is to keep a stack of directions robot came from (so that
            it can back up) and a list of directions to try to move.
        """
        move = self._moves[-1]
        while len(move["to-try"]):  # is there a direction to try?
            direction = move["to-try"].pop(0)
            move_adj = self.MOVEDIR[direction]
            new_pos = (self._pos[0] + move_adj[0], self._pos[1] + move_adj[1])
            if self._canvas[new_pos] != " ":
                continue  # don't go where we've been
            # record direction given
            self._last_move = direction
            return self._last_move + 1

        # no more moves left; need to backtrack
        self._moves.pop()  # remove node from the stack
        # ugly hack to stop the VM, but it works
        if move["move"] is None:
            raise FinishedException(f"We're done here: {self._pos} {len(self._moves)}")
        # set a backgrack flag and move the opposite direction from where
        # went to get to the current position
        self._last_move = self.OPPOSITE[move["move"]]
        self._backtrack = True
        return self._last_move + 1

    def send(self, val):
        """ Receive result of the move command
        """
        move_adj = self.MOVEDIR[self._last_move]
        new_pos = (self._pos[0] + move_adj[0], self._pos[1] + move_adj[1])
        if val == 0:  # hit wall; record wall position
            self._canvas[new_pos] = WALL
        else:  # move ok, or oxygen
            self._pos = new_pos
            if not self._backtrack:
                if val == 2:  # aka, oxygen; record it
                    self._canvas[self._pos] = "O"
                    self._oxygen = new_pos
                else:
                    self._canvas[self._pos] = HALL
                # need to push a new node onto the stack
                self._moves.append(
                    {
                        "move": self._last_move,
                        "to-try": [
                            # try all directions *except* the one that backtracks
                            x
                            for x in self.MOVES
                            if x != self.OPPOSITE[self._last_move]
                        ],
                    }
                )
            else:
                # on a backtrack, the node is gone and no other bookkeeping is
                # needed; reset the flag and resume until more input is needed
                self._backtrack = False

        self.draw()


def solve(canvas):
    """ Breadth-first tree search from start -> oxygen
    """
    MOVEDIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # (path length, co-ordinate)
    q = [(0, (0, 0))]
    seen = []
    while q:
        l, n = q.pop()
        seen.append(n)
        if canvas[n] == "O":
            return l  # found it!
        l += 1
        for d in MOVEDIR:
            new_n = (n[0] + d[0], n[1] + d[1])
            if canvas[new_n] == WALL:
                continue
            if new_n in seen:
                continue
            q.append((l, new_n))


def draw(canvas):
    """ Render canvas for floodfill
    """
    print("\033[2J")  # clear screen
    print("\033[0;0H")  # cursor to top of term
    min_x = min(x[0] for x in canvas)
    min_y = min(x[1] for x in canvas)
    max_x = max(x[0] for x in canvas)
    max_y = max(x[1] for x in canvas)
    for y in range(min_y, max_y + 1):
        r = ""
        for x in range(min_x, max_x + 1):
            r += canvas[(x, y)]
        print(r)


def floodfill(canvas, oxygen):
    MOVEDIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    working = [oxygen]
    time = 0
    draw(canvas)
    # sleep(1)
    while working:
        """ Invariant at work here is that a node that results in more oxygen
            filled will not, in a subsequent minute, generate more. Each node
            is pertinent in one and only one time interval.

            Thus, once no nodes result in additional oxygen, we're done.

            Further, all new oxygen in one interval happens simultaneously,
            so a queue doesn't work. Rather, the entire set of active nodes
            needs to be iterated over.
        """
        print(f"Active nodes: {len(working)}")
        new_working = []
        for w in working:
            for d in MOVEDIR:
                p = (w[0] + d[0], w[1] + d[1])
                if canvas[p] == HALL:
                    new_working.append(p)
                    canvas[p] = "O"
        time += 1
        working = new_working
        draw(canvas)
        # sleep(1)
    return time - 1


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    provider = InputOutputProvider()
    m = Apollo("A", code, provider)
    m.output = provider
    try:
        m.run()
    except FinishedException:
        print("Ok, now onto maze solver")

    pathlength = solve(provider.canvas)
    filltime = floodfill(provider.canvas, provider.oxygen)
    print(f"Length: {pathlength}")
    print(f"Time to fill: {filltime}")


if __name__ == "__main__":
    main()
