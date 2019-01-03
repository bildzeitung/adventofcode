#!/usr/bin/env python
'''
    Day 20: REGEX
'''
import sys
from pathlib import Path

DM = {'N': (0, -1),
      'E': (1, 0),
      'S': (0, 1),
      'W': (-1, 0)}
DMC = {'N': '-', 'S': '-',
       'E': '|', 'W': '|'}
START = (500, 500)  # arbitrary center point


def display(base, p=START):
    min_x = min(pos[0] for pos in base)
    max_x = max(pos[0] for pos in base)
    min_y = min(pos[1] for pos in base)
    max_y = max(pos[1] for pos in base)

    for y in range(min_y, max_y + 1):
        rc = ''
        for x in range(min_x, max_x + 1):
            if (x, y) == p:
                rc += 'X'
            elif (x, y) in base:
                rc += base[(x, y)]
            else:
                rc += ' '
        print(rc)
    print()


def run(regex):
    stack = []
    pos = START
    base = {  # initial starting configuration, completely drawn
            (pos[0] - 1, pos[1] - 1): '#',
            (pos[0], pos[1] - 1): '?',
            (pos[0] + 1, pos[1] - 1): '#',
            (pos[0] - 1, pos[1]): '?',
            (pos[0], pos[1]): '.',
            (pos[0] + 1, pos[1]): '?',
            (pos[0] - 1, pos[1] + 1): '#',
            (pos[0], pos[1] + 1): '?',
            (pos[0] + 1, pos[1] + 1): '#',
            }
    # display(base)
    for c in regex:
        x = pos[0]
        y = pos[1]
        if c in '^$':
            continue
        if c in 'NEWS':
            p = (x + DM[c][0], y + DM[c][1])
            base[p] = DMC[c]
            pos = (p[0] + DM[c][0], p[1] + DM[c][1])
            base[pos] = '.'
            for i in 'NEWS':
                p = (pos[0] + DM[i][0], pos[1] + DM[i][1])
                if p not in base:
                    base[p] = '?'
            base[(pos[0] - 1, pos[1] - 1)] = '#'
            base[(pos[0] + 1, pos[1] - 1)] = '#'
            base[(pos[0] - 1, pos[1] + 1)] = '#'
            base[(pos[0] + 1, pos[1] + 1)] = '#'
            # display(base, pos)
        if c == '(':  # open capture
            stack.append(pos)
        if c == ')':  # close capture
            pos = stack.pop()
        if c == '|':  # alternation
            pos = stack[-1]

    # change ? -> #
    for k, v in base.items():
        if v == '?':
            base[k] = '#'

    print('FINAL')
    display(base)
    return base


def find_path(base):
    oset = [(START, 0)]
    seen = set()
    maxpath = 0
    above_1k = 0
    while oset:
        p, pathlength = oset.pop()
        above_1k += 1 if pathlength > 999 else 0
        if p in seen:
            continue
        seen.add(p)
        is_deadend = True
        for i in 'NEWS':
            n = (p[0] + DM[i][0], p[1] + DM[i][1])
            nn = (n[0] + DM[i][0], n[1] + DM[i][1])
            if nn in seen:
                continue
            if base[n] in '|-':
                oset.append(
                        ((n[0] + DM[i][0], n[1] + DM[i][1]), pathlength + 1)
                        )
                is_deadend = False
        if is_deadend:
            maxpath = pathlength if pathlength > maxpath else maxpath
    print('LONGEST', maxpath, 'NUMBER OF >=1K PATHS', above_1k)


def main():
    # read the base description
    with Path(sys.argv[1]).open() as f:
        regex = f.readline().strip()

    # create the base
    base = run(regex)

    # find the path in the base
    find_path(base)


if __name__ == "__main__":
    main()
