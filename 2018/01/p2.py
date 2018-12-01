#!/usr/bin/env python
from pathlib import Path

seen = {0}


def get_val(line):
    r = line.strip()
    if r.startswith('+'):
        return int(r[1:])
    return int(r)


def main():
    total = 0
    p = Path('./input.txt')
    items = []
    with p.open() as f:
        items = [get_val(l) for l in f]

    while (True):
        for item in items:
            total += item
            if total in seen:
                print(f"TOTAL: {total}")
                return
            seen.add(total)


if __name__ == '__main__':
    main()
