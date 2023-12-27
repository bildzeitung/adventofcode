#!/usr/bin/env python
"""
    Day 9
"""
import sys
from pathlib import Path

from rich import print

SINGLE_RIGHT_TOP = "\u2510"  # 7
SINGLE_HORIZ_PIPE = "\u2500"  # -
SINGLE_VERTI_PIPE = "\u2502"  # |
SINGLE_LEFT_TOP = "\u250c"  # F
SINGLE_RIGHT_BOTTOM = "\u2518"  # J
SINGLE_LEFT_BOTTOM = "\u2514"  # L
maze = {}
maxx = -1
maxy = -1


def ppuzzle():
    for y in range(maxy):
        o = ""
        for x in range(maxx):
            p = (x, y)
            if not p in maze:
                o += " "
                continue
            c = maze[(x, y)]
            if c == "7":
                o += SINGLE_RIGHT_TOP
            elif c == "-":
                o += SINGLE_HORIZ_PIPE
            elif c == "F":
                o += SINGLE_LEFT_TOP
            elif c == "|":
                o += SINGLE_VERTI_PIPE
            elif c == "J":
                o += SINGLE_RIGHT_BOTTOM
            elif c == "L":
                o += SINGLE_LEFT_BOTTOM
            else:
                o += c
        print(o)

def check_inbound(p):
    x, y = p
    c = set()
    # up |, F, 7
    if (x, y-1) in maze and maze[(x,y-1)] in ('|', 'F', '7'):
        c.add( (x, y-1))
    
    # left L, -, F
    if (x-1, y) in maze and maze[(x-1, y)] in ('-', 'L', 'F'):
        c.add((x-1,y))
        
    # right J, -, 7
    if (x+1, y) in maze and maze[(x+1,y)] in ('-', 'J', '7'):
        c.add((x+1,y))

    # down J, |, L
    if (x, y+1) in maze and maze[(x, y+1)] in ('|', 'L', 'J'):
        c.add((x,y+1))
    return c


def main():
    global maxx
    global maxy

    start = None
    y = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            x = 0
            for c in line.strip():
                if c == ".":
                    x += 1
                    continue
                if c == 'S':
                    start = (x,y)
                maze[(x, y)] = c
                x += 1
            y += 1

    maxy = y
    maxx = len(line)
    ppuzzle()
    print(f"Start: {start}")

    print(check_inbound(start))


if __name__ == "__main__":
    print(main())
