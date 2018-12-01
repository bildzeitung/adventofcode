#!/usr/bin/env python
from pathlib import Path


def main():
    total = 0
    p = Path('./input.txt')
    with p.open() as f:
        for line in f:
            r = line.strip()
            if r.startswith('+'):
                r = int(r[1:])
            else:
                r = int(r)
            total += r

    print(f"TOTAL: {total}")


if __name__ == '__main__':
    main()
