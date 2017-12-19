#!/usr/bin/env python
'''
    Day 19
'''
import sys

down = (0, 1)
up = (0, -1)
right = (1, 0)
left = (-1, 0)


def walk(puzzle, x, y):
    ''' Step through the maze

        A '+' is a corner, so change directions there and only there.
        Run until a space is hit.
        If a non-space, non-plus character is seen, it's a letter.

    '''
    direction = down  # starting direction
    steps = 0
    max_x = max(len(x) for x in puzzle)
    max_y = len(puzzle)
    done = False

    while not done:
        while (puzzle[y][x] not in '+ '):
            x += direction[0]
            y += direction[1]
            steps += 1

        if puzzle[y][x] == ' ':
            return steps

        if direction in (down, up):
            # must switch left or right
            if x+1 < max_x and puzzle[y][x+1] != ' ':
                direction = right
            elif x > 0 and puzzle[y][x-1] != ' ':
                direction = left
        else:  # switch to up or down
            if y+1 < max_y and puzzle[y+1][x] != ' ':
                direction = down
            elif y > 0 and puzzle[y-1][x] != ' ':
                direction = up
        
        # step past the +
        x += direction[0]
        y += direction[1]
        steps += 1

    raise Exception('WTF')


def main():
    puzzle = []
    for line in sys.stdin:
        puzzle.append([x for x in line.rstrip('\n')])
    
    starty = 0  # at the top!
    startx = puzzle[0].index('|')  # find the entry pipe
    print 'STEPS', walk(puzzle, startx, starty)


if __name__ == '__main__':
    main()