#!/usr/bin/env python
'''
    Day 22
'''
import time
import sys

MAX_TICKS = int(sys.argv[1])
BORDER = 2  # for display

# clockwise
directions = [
        (0, -1),  # up
        (1, 0),  # right
        (0, 1),  # down
        (-1, 0),  # left
        ]
dir_display = ['^', '>', 'v', '<']

state_dir_adjustment = [-1, 0, 1, 2]
state_display = ['.', 'W', '#', 'F']


def display(grid, states, pos):
    ''' Show the grid, given the compact representation
    '''
    max_x = max(p[0] for p in grid)
    min_x = min(p[0] for p in grid)
    max_y = max(p[1] for p in grid)
    min_y = min(p[1] for p in grid)

    sys.stderr.write("\x1b[2J\x1b[H")
    print 'Extents: (%s, %s) -> (%s, %s)' % (min_x, min_y, max_x, max_y)
    print 'Pos:', pos
    for y in xrange(min_y - BORDER, max_y + 1 + BORDER):
        row = ''
        items = []
        for x in xrange(min_x - BORDER, max_x + 1 + BORDER):
            if (x, y) in grid:
                items.append(state_display[states[(x, y)]])
            else:
                items.append('.')

            row = ' '.join(items)

        if y == pos[1]:
            items = list(row)
            if pos[0] - min_x + BORDER > 0:
                items[2*(pos[0] - (min_x - BORDER)) - 1] = dir_display[pos[2]]
            items[2*(pos[0] - (min_x - BORDER)) + 1] = dir_display[pos[2]]
            row = ''.join(items)

        print row

    time.sleep(0.01)


def run(grid, states, pos):
    just_pos = (pos[0], pos[1])
    new_dir = pos[2]
    did_infect = False

    if just_pos not in grid:
        grid.add(just_pos)
        states[just_pos] = 0

    state = states[just_pos]
    dir_adjust = state_dir_adjustment[state]
    new_dir = (new_dir + dir_adjust) % len(directions)

    states[just_pos] = (states[just_pos] + 1) % len(state_dir_adjustment)

    if states[just_pos] == 2:
        did_infect = True

    return (just_pos[0] + directions[new_dir][0],
            just_pos[1] + directions[new_dir][1],
            new_dir), did_infect


def main():
    rawgrid = [line.strip() for line in sys.stdin]
    h = len(rawgrid)
    w = len(rawgrid[0])

    grid = set()
    states = {}
    for y, row in enumerate(rawgrid):
        for x, col in enumerate(row):
            if col == '#':
                grid.add((x, y))
                states[(x, y)] = 2

    # (x, y, direction)
    pos = (w/2, h/2, 0)
    tick = 0
    infections = 0
    while tick < MAX_TICKS:
        display(grid, states, pos)
        pos, did_infect = run(grid, states, pos)
        if did_infect:
            infections += 1
        tick += 1

    print 'FINAL', infections
    display(grid, states, pos)


if __name__ == '__main__':
    main()
