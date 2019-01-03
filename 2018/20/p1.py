#!/usr/bin/env python
'''
    Day 20: REGEX

    ** both parts in this one file, since there's no logic change

    A two-part solution:
        (a) build the maze
        (b) solve the maze

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
    ''' Generate the maze

        Work through the regex, using a stack to handle the ( .. | .. )
        alternations
    '''
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
        if c in '^$':  # ignore; not needed
            continue
        if c in 'NEWS':  # if it's a direction, then walk
            p = (pos[0] + DM[c][0], pos[1] + DM[c][1])
            base[p] = DMC[c]  # draw a door; n.b. this will overwrite an '?'
            pos = (p[0] + DM[c][0], p[1] + DM[c][1])
            base[pos] = '.'  # draw the room
            for i in 'NEWS':  # draw unknown exits
                p = (pos[0] + DM[i][0], pos[1] + DM[i][1])
                if p not in base:
                    base[p] = '?'
            # draw walls around the current room
            base[(pos[0] - 1, pos[1] - 1)] = '#'
            base[(pos[0] + 1, pos[1] - 1)] = '#'
            base[(pos[0] - 1, pos[1] + 1)] = '#'
            base[(pos[0] + 1, pos[1] + 1)] = '#'
            # display(base, pos)
        if c == '(':  # open capture; push the current position
            stack.append(pos)
        if c == ')':  # close capture; restore the last saved position and pop
            pos = stack.pop()
        if c == '|':    # alternation; restore the saved position, but peek
                        # (since other options will need to start from the
                        # capture open point)
            pos = stack[-1]

    # base is defined; all ? are presumed to be walls
    for k, v in base.items():
        if v == '?':
            base[k] = '#'

    print('FINAL')
    display(base)
    return base


def find_path(base):
    ''' Use a breadth-first search to determine shortest paths

        Save the longest path, and count any rooms whose path is >=1k rooms
    '''
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
            if nn in seen:  # in other words, exclude door walked through last
                continue
            if base[n] in '|-':  # next room!
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
