#!/usr/bin/env python
''' Day 11

    Use dynamic programming to calculate the max subsquare of size k x k.

'''
import sys

GRID = 300 + 1
SERIAL = int(sys.argv[1])


def calc_grid():
    ''' Magic grid calculation algorithm
    '''
    grid = [x[:] for x in [[0] * GRID] * GRID]
    for y in range(1, GRID):
        for x in range(1, GRID):
            rid = x + 10
            pl = rid * y
            pl += SERIAL
            pl *= rid
            pl = (pl // 100) % 10
            pl -= 5
            grid[y][x] = pl
    return grid


def main():
    grid = calc_grid()

    def calc_stripsums(k):
        stripsums = [x[:] for x in [[0] * GRID] * GRID]
        for column in range(1, GRID):
            total = sum(grid[i][column] for i in range(1, k + 1))
            stripsums[1][column] = total

            for row in range(1 + 1, GRID - k + 1):
                total += grid[row+k-1][column] - grid[row-1][column]
                stripsums[row][column] = total
        return stripsums

    all_maxes = {}
    for k in range(1, GRID - 1):
        stripsums = calc_stripsums(k)

        # calculation
        max_sum = -sys.maxsize - 1
        for column in range(1, GRID - k + 1):
            total = 0
            total += sum(stripsums[column][1:1+k])
            if total > max_sum:
                max_sum = total
                pos = (1, column)

            for row in range(1 + 1, GRID - k + 1):
                total += stripsums[column][row+k-1] - stripsums[column][row-1]

                if total > max_sum:
                    max_sum = total
                    pos = (row, column)

        print(k, pos, max_sum)
        all_maxes[k] = (pos, max_sum)

    print(max(all_maxes.items(), key=lambda x: x[1][1]))


if __name__ == "__main__":
    main()
