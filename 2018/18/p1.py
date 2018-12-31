#!/usr/bin/env python
'''
    Day 18
'''
import sys
from pathlib import Path


def around(area, y, x):
    for i in range(y-1, y+2):
        if i < 0 or i > len(area) - 1:
            continue

        for j in range(x-1, x+2):
            if j < 0 or j > len(area[0]) - 1:
                continue
            yield area[i][j]


def check_open(area, y, x):
    total = 0
    for t in around(area, y, x):
        total += t == '|'

    return '|' if total > 2 else '.'


def check_trees(area, y, x):
    total = 0
    for t in around(area, y, x):
        total += t == '#'

    return '#' if total > 2 else '|'


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
    print('\n'.join(''.join(row) for row in area))
    print()


def main():
    area = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            area.append([x for x in line.strip()])

    display(area)
    for i in range(10):
        area = tick(area)
        display(area)

    total_trees = 0
    total_lumberyards = 0
    for row in area:
        for col in row:
            total_trees += col == '|'
            total_lumberyards += col == '#'

    print('TREES', total_trees, 'LUMBER', total_lumberyards, 'PRODUCT', total_trees * total_lumberyards)


if __name__ == "__main__":
    main()
