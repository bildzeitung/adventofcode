#!/usr/bin/env python
from pathlib import Path

seen = {0}  # set, primed with 0


def get_val(line):
    r = line.strip()
    if r.startswith('+'):
        return int(r[1:])
    return int(r)


def main():
    p = Path('./input.txt')

    ''' Read the program (all the integers)
    '''
    items = []
    with p.open() as f:
        items = [get_val(l) for l in f]

    ''' Loop assuming the data will cause it to halt.

        Keep a running total, checking that any given value has not yet been
        seen. Run through the array repeatedly, as per the problem description
    '''
    total = 0
    while (True):
        for item in items:
            total += item
            if total in seen:
                print(f"TOTAL: {total}")
                return
            seen.add(total)


if __name__ == '__main__':
    main()
