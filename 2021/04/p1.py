#!/usr/bin/env python
"""
    Day 4
"""
import sys
from collections import defaultdict
from pathlib import Path

import attr
from rich import print

G = lambda: defaultdict(int)


@attr.s
class Board:
    data = attr.ib()
    dabbed: set = attr.ib(default=attr.Factory(set))
    _all_bingo_numbers: set = attr.ib(default=None)
    _matrix = attr.ib(default=attr.Factory(dict))
    _rows = attr.ib(default=attr.Factory(G))
    _cols = attr.ib(default=attr.Factory(G))
    _dim: int = attr.ib(default=int)

    def __attrs_post_init__(self):
        for y, r in enumerate(self.data):
            for x, n in enumerate(r):
                self._matrix[n] = (x, y)
        self._dim = len(self.data)

    def dab(self, n: int) -> None:
        if n in self.all_bingo_numbers:
            self.dabbed.add(n)
            x, y = self._matrix[n]
            self._rows[x] += 1
            self._cols[y] += 1

    @property
    def is_a_winner(self):
        return any(x == self._dim for x in self._rows.values()) or any(
            x == self._dim for x in self._cols.values()
        )

    @property
    def all_bingo_numbers(self):
        if not self._all_bingo_numbers:
            self._all_bingo_numbers = set()
            for r in self.data:
                self._all_bingo_numbers.update(r)

        return self._all_bingo_numbers

    @property
    def unmarked(self):
        return self._all_bingo_numbers - self.dabbed


def main():
    with Path(sys.argv[1]).open() as f:
        chosen = [int(x) for x in next(f).strip().split(",")]
        next(f)  # blank line
        boards = []
        rows = []
        for line in f:
            if not line.strip():
                # ok, create a new board
                boards.append(Board(rows))
                rows = []
                continue
            rows.append([int(x) for x in line.strip().split()])
        boards.append(Board(rows))

    for c in chosen:
        for b in boards:
            b.dab(c)
            if b.is_a_winner:
                return c, b

    # print(boards)


if __name__ == "__main__":
    last_number, board = main()
    print(board, last_number, sum(board.unmarked) * last_number)
