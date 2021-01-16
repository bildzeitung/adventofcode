#!/usr/bin/env python
"""
  Day 20
"""
import regex as re
import sys


class Puzzle:
    def __init__(self, id, puzzle) -> None:
        self.id = id
        self.puzzle = puzzle
        self.labels = {}

    def __repr__(self) -> str:
        return f"|id: {self.id}|"

    @property
    def top(self):
        return self.puzzle[0]

    @property
    def bottom(self):
        return self.puzzle[-1]

    @property
    def left(self):
        return "".join(x[0] for x in self.puzzle)

    @property
    def right(self):
        return "".join(x[-1] for x in self.puzzle)

    def get(self, edge):
        return self.__getattribute__(edge)

    def has_rot(self, side):
        # reverse string all items
        return side in (
            self.top[::-1],
            self.bottom[::-1],
            self.left[::-1],
            self.right[::-1],
        )

    def has_any(self, side):
        return self.has_rot(side) or side in (
            self.top,
            self.bottom,
            self.right,
            self.left,
        )

    def find(self, side):
        if side == self.top:
            return "top"
        if side == self.bottom:
            return "bottom"
        if side == self.left:
            return "left"
        if side == self.right:
            return "right"

    def find_rot(self, side):
        if side == self.top[::-1]:
            return "top"
        if side == self.bottom[::-1]:
            return "bottom"
        if side == self.left[::-1]:
            return "left"
        if side == self.right[::-1]:
            return "right"

    def flip_vertical(self):
        self.puzzle = self.puzzle[::-1]

    def flip_horizontal(self):
        self.puzzle = [p[::-1] for p in self.puzzle]

    def rotate(self):
        # f(x, y) --> (-y + <length of side> - 1, x)
        t = []
        offset = len(self.puzzle) - 1
        for p in self.puzzle:
            t.append([x for x in p])
        n = [""] * len(t)
        for i in range(len(t)):
            for j in range(len(t)):
                n[i] += t[-j + offset][i]

        self.puzzle = n

    def is_topleft_corner(self):
        return not self.labels["top"] and not self.labels["left"]

    @property
    def oneline(self):
        return "".join(self.puzzle)


OPPOSITE = {"left": "right", "top": "bottom", "bottom": "top", "right": "left"}


def label_puzzle(puzzles, p, source):
    opposite = OPPOSITE[source]
    edge = p.get(source)

    # already done this?
    if source in p.labels:
        return

    # find a matching puzzle piece on an opposite edge (easy case)
    match = [x for x in puzzles if x.id != p.id and x.get(opposite) == edge]
    if match:
        match = match[0]
        p.labels[source] = match
        match.labels[opposite] = p
        # print(f"{source} <-> {match}; source -> {p.labels}")
        return match

    # no easy matches; do we match anywhere? if not, we've seen an edge
    anywhere = [x for x in puzzles if x.id != p.id and x.has_any(edge)]
    if not anywhere:
        # print(f"{source} is an edge")  # this is ok; do nothing
        p.labels[source] = None
        return
    anywhere = anywhere[0]

    # ok, so there *is* a match someplace
    # two cases:
    # (a) need to rotate
    # (b) need to flip
    #
    # check flip case first
    z = [x for x in puzzles if x.id != p.id and x.has_rot(edge)]
    if z:
        z = z[0]
        target_edge = z.find_rot(edge)
        if target_edge in ("left", "right"):
            z.flip_vertical()
        else:
            z.flip_horizontal()
        return label_puzzle(puzzles, p, source)

    # ok, so the match is there -- it's just not lining up, so like
    # a right source is matching with a down edge or something; so it's going
    # to need to rotate
    # print(f"Found {anywhere}, but source -> {source} and match -> {anywhere.find(edge)}")
    anywhere.rotate()
    return label_puzzle(puzzles, p, source)


def main():
    with open(sys.argv[1]) as f:

        def getpuzzle():
            while i := f.readline():
                id = int(i.strip().replace("Tile ", "").replace(":", ""))
                puzzle = []
                while line := f.readline().strip():
                    puzzle.append(line)
                yield Puzzle(id, puzzle)

        puzzles = [p for p in getpuzzle()]

    # pick a tile as an anchor; walk through the rest (breadth-first),
    # making some assumptions about uniqueness of edges and everything being
    # a single connected component
    queue = [puzzles[0]]
    while queue:
        p = queue.pop(0)

        # match top with any
        acquired = (
            label_puzzle(puzzles, p, "top"),
            label_puzzle(puzzles, p, "bottom"),
            label_puzzle(puzzles, p, "left"),
            label_puzzle(puzzles, p, "right"),
        )
        queue.extend(filter(None, acquired))

    # ok, so each tile has a complete set of labels
    # walk through the puzzle, starting at the top-left corner
    topleft = [x for x in puzzles if x.is_topleft_corner()][0]
    print(f"TL: {topleft}")
    rows = len(topleft.puzzle)
    together = []
    while topleft:
        for i in range(1, rows - 1):
            p = ""
            x = topleft
            while x:
                p += x.puzzle[i][1:-1]
                x = x.labels["right"]
            together.append(p)
        topleft = topleft.labels["bottom"]

    # finding the sea monster is a regex problem
    #
    # translate the sea monster into a regex padded by the puzzle size.
    # then, look for potentially overlapping matches
    #
    # the final puzzle may need to be rotated or flipped, so put it into the
    # class b/c I already have the rotation written ther
    #
    maxpattern = 20
    delta = len(together[0]) - maxpattern
    MONSTER_STR = (
        "..................#."
        + "." * delta
        + "#....##....##....###"
        + "." * delta
        + ".#..#..#..#..#..#"
    )
    MONSTER = re.compile(MONSTER_STR)
    final = Puzzle(0, together)
    for _ in range(3):
        p = MONSTER.findall(final.oneline, overlapped=True)
        if p:
            monsters = MONSTER_STR * len(p)
            return final.oneline.count("#") - monsters.count("#")
        final.rotate()


if __name__ == "__main__":
    print(main())
