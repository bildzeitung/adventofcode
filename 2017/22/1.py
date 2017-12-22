#!/usr/bin/env python
'''
    Day 22
'''
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


def display(grid, pos):
    ''' Show the grid, given the compact representation
    '''
    max_x = max(p[0] for p in grid)
    min_x = min(p[0] for p in grid)
    max_y = max(p[1] for p in grid)
    min_y = min(p[1] for p in grid)

    print 'Extents: (%s, %s) -> (%s, %s)' % (min_x, min_y, max_x, max_y)
    print 'Pos:', pos
    for y in xrange(min_y - BORDER, max_y + 1 + BORDER):
        row = ''
        items = []
        for x in xrange(min_x - BORDER, max_x + 1 + BORDER):
            if (x, y) in grid:
                items.append('#')
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


def run(grid, pos):
    just_pos = (pos[0], pos[1])
    new_dir = pos[2]
    did_infect = False

    if just_pos in grid:  # infected
        # turn right
        new_dir = (new_dir + 1) % len(directions)
        grid.remove(just_pos)
    else:
        new_dir = (new_dir - 1) % len(directions)
        grid.add(just_pos)
        did_infect = True

    return (just_pos[0] + directions[new_dir][0],
            just_pos[1] + directions[new_dir][1],
            new_dir), did_infect


def main():
    rawgrid = [line.strip() for line in sys.stdin]
    h = len(rawgrid)
    w = len(rawgrid[0])

    grid = set()
    for y, row in enumerate(rawgrid):
        for x, col in enumerate(row):
            if col == '#':
                grid.add((x, y))

    # (x, y, direction)
    pos = (w/2, h/2, 0)
    tick = 0
    infections = 0
    while tick < MAX_TICKS:
        # display(grid, pos)
        pos, did_infect = run(grid, pos)
        if did_infect:
            infections += 1
        tick += 1

    print 'FINAL', infections
    display(grid, pos)


if __name__ == '__main__':
    main()
