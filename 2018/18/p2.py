#!/usr/bin/env python
'''
    Day 18
'''
import sys
from pathlib import Path


def around(area, y, x):
    ''' Use a generator to grab the neighbourhood
    '''
    for i in range(y-1, y+2):
        if i < 0 or i > len(area) - 1:
            continue

        for j in range(x-1, x+2):
            if j < 0 or j > len(area[0]) - 1:
                continue
            yield area[i][j]


def check_open(area, y, x):
    return '|' if sum(t == '|' for t in around(area, y, x)) > 2 else '.'


def check_trees(area, y, x):
    return '#' if sum(t == '#' for t in around(area, y, x)) > 2 else '|'


def check_lumber(area, y, x):
    total_lumberyard = 0
    total_trees = 0

    for t in around(area, y, x):
        total_lumberyard += t == '#'
        total_trees += t == '|'

    total_lumberyard -= 1

    return '#' if total_lumberyard > 0 and total_trees > 0 else '.'


def tick(area):
    new_area = [x[:] for x in area]
    for y in range(len(area)):
        for x in range(len(area[0])):
            if area[y][x] == '.':
                new_area[y][x] = check_open(area, y, x)
            elif area[y][x] == '|':
                new_area[y][x] = check_trees(area, y, x)
            else:
                new_area[y][x] = check_lumber(area, y, x)

    return new_area


def display(area):
    return '\n'.join(''.join(row) for row in area)


def main():
    area = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            area.append([x for x in line.strip()])

    # for a cycle, need to track the entire game state
    solutions = [display(area)]
    while (True):
        area = tick(area)

        d = display(area)
        if d in solutions:
            # ok, we have a cycle
            print('CYCLE', len(solutions))
            # the trim set is the items in the cycle
            trim = solutions[solutions.index(d):]
            print('LENGTH', len(trim))
            # figure out the index of the solution at the n'th generation
            c = (1_000_000_000 - (len(solutions) - len(trim))) % len(trim)
            # calculate the product of just that solution
            total_trees = 0
            total_lumberyards = 0
            for col in trim[c]:
                total_trees += col == '|'
                total_lumberyards += col == '#'
            print('FINAL', total_trees * total_lumberyards)
            break
        else:
            solutions.append(d)


if __name__ == "__main__":
    main()
