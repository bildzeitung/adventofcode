#!/usr/bin/env python
"""
  Day 20

  Makes a bunch of assumptions that turn out to be right, so ok :)

  Still kind of a terrible solution.

  Lovely part about this is that we don't have to assemble the tiles at all,
  so we're not composing what the entire map looks like. So that's cool,
  except we actually have to solve that for part 2, so this is an own-goal.
"""
import math
import sys
from collections import defaultdict
from itertools import chain


def main():
    tiles = {}
    catalog = defaultdict(list)
    with open(sys.argv[1]) as f:

        def getpuzzle():
            try:
                id = int(f.readline().strip().replace("Tile ", "").replace(":", ""))
            except ValueError:
                return
            puzzle = []
            while line := f.readline().strip():
                puzzle.append(line)
            return id, puzzle

        while p := getpuzzle():
            id, puzzle = p
            top = puzzle[0], puzzle[0][::-1]
            catalog[top[0]].append(id)
            catalog[top[1]].append(id)
            btm = puzzle[-1], puzzle[-1][::-1]
            catalog[btm[0]].append(id)
            catalog[btm[1]].append(id)
            # print(p)
            left = "".join(x[0] for x in puzzle)
            catalog[left].append(id)
            catalog[left[::-1]].append(id)
            right = "".join(x[-1] for x in puzzle)
            catalog[right].append(id)
            catalog[right[::-1]].append(id)
            tiles[id] = {
                "top": top,
                "btm": btm,
                "right": (right, right[::-1]),
                "left": (left, left[::-1]),
            }
        # print(catalog)
        # print(tiles)

    def finder(tile, edge):
        """ figure out if a specific edge is in the catalog for a tile other
            than the one given. i.e. who do you match with?

            fortunately, the data is such that this is either none (a border)
            or exactly one other tile matches
        """
        rv = set(
            chain.from_iterable([x for x in catalog[e] if x != tile] for e in edge)
        )
        assert len(rv) < 2, f"Ouch: {rv}"
        return rv.pop() if rv else None

    #
    # ok, examine all tiles, find edge mates, and use the # of mates to
    # discern position in the final layout.
    #
    # A B C  e.g. tile A has B, D or 2 mates, so it's a corner
    # D E F       All edge or middle have > 2 mates, so we know which
    # G H I       IDs to keep & multiply together
    #
    return math.prod(
        i
        for i, t in tiles.items()
        if len(
            [
                x
                for x in (
                    finder(i, t["top"]),
                    finder(i, t["btm"]),
                    finder(i, t["left"]),
                    finder(i, t["right"]),
                )
                if x
            ]
        )
        == 2  # a corner piece
    )


if __name__ == "__main__":
    print(main())
