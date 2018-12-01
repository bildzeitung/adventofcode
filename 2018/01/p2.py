#!/usr/bin/env python
from pathlib import Path
from itertools import cycle

seen = {0}  # set, primed with 0


def main():
    ''' Read the program (all the integers)
    '''
    items = []
    with Path('./input.txt').open() as f:
        items = [int(l) for l in f]

    ''' Loop assuming the data will cause it to halt.

        Keep a running total, checking that any given value has not yet been
        seen. Run through the array repeatedly, as per the problem description
    '''
    total = 0
    for item in cycle(items):
        total += item
        if total in seen:
            print(f"TOTAL: {total}")
            return
        seen.add(total)


if __name__ == '__main__':
    main()
