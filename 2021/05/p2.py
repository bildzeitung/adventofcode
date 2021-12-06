#!/usr/bin/env python
"""
    Day 5
"""
import math
import sys
from collections import Counter
from pathlib import Path

import attr
from rich import print


@attr.s
class Line:
    start = attr.ib()
    fin = attr.ib()

    def __attrs_post_init__(self):
        self.start = (int(self.start[0]), int(self.start[1]))
        self.fin = (int(self.fin[0]), int(self.fin[1]))

    @property
    def is_horiz(self):
        return self.start[1] == self.fin[1]

    @property
    def is_vert(self):
        return self.start[0] == self.fin[0]


def main():
    with Path(sys.argv[1]).open() as f:
        lines = [Line(*(x.strip().split(",") for x in l.split("->"))) for l in f]

    p = []
    for l in lines:
        if l.is_horiz:
            f, t = sorted((l.start[0], l.fin[0]))
            p.extend((x, l.start[1]) for x in range(f, t + 1))
            continue

        if l.is_vert:
            f, t = sorted((l.start[1], l.fin[1]))
            p.extend((l.start[0], x) for x in range(f, t + 1))
            continue

        # diagonal
        dx = -(l.start[0] - l.fin[0]) / math.fabs(l.start[0] - l.fin[0])
        dy = -(l.start[1] - l.fin[1]) / math.fabs(l.start[1] - l.fin[1])
        c = (l.start[0], l.start[1])
        while c != l.fin:
            p.append(c)
            c = (c[0] + dx, c[1] + dy)
        p.append(l.fin)

    total = sum(map(lambda x: x[1] > 1, Counter(p).items()))
    print(total)


if __name__ == "__main__":
    main()
