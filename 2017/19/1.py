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
    # starting direction
    direction = down
    letters = []
    max_x = max(len(x) for x in puzzle)
    max_y = len(puzzle)

    print max_x, max_y

    while True:
        while (puzzle[y][x] not in '+ '):
            # print x, y, puzzle[y][x]
            if puzzle[y][x] not in '|-.':
                letters.append(puzzle[y][x])
                print puzzle[y][x]
            puzzle[y][x] = '.'
            x += direction[0]
            y += direction[1]

        print x, y

        if direction == down or direction == up:
            # left or right
            if x+1 < max_x and puzzle[y][x+1] != ' ':
                print 'RIGHT'
                direction = right
                puzzle[y][x] = '>'
            elif x > 0 and puzzle[y][x-1] != ' ':
                print 'LEFT'
                direction = left
                puzzle[y][x] = '<'
            else:
                raise Exception(letters)
        else:
            if y+1 < max_y and puzzle[y+1][x] != ' ':
                print 'DOWN'
                direction = down
                puzzle[y][x] = 'v'
            elif y > 0 and puzzle[y-1][x] != ' ':
                print 'UP'
                direction = up
                puzzle[y][x] = '^'
            else:
                raise Exception(letters)

        x += direction[0]
        y += direction[1]

        print x, y

    print x, y


def main():
    puzzle = []
    for line in sys.stdin:
        puzzle.append([x for x in line.rstrip('\n')])
    
    starty = 0
    startx = puzzle[0].index('|')
    print 'START', startx, starty
    try:
        walk(puzzle, startx, starty)
    except Exception as exc:
        print 'LETTERS', ''.join(exc.message)

    # for row in puzzle:
    #    print ''.join(row)

if __name__ == '__main__':
    main()