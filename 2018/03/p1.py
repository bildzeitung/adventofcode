#!/usr/bin/env python
''' Day 3
'''
import re
import sys
from pathlib import Path

CLAIM_RE = re.compile(r'.+@ (\d+),(\d+): (\d+)x(\d+)')
ARRAY = 1000

master = []


def process_claim(l, t, w, h):
    for i in range(w):
        for j in range(h):
            master[t+j][l+i] += 1


def main():
    for i in range(ARRAY):
        master.append([0] * ARRAY)

    with Path(sys.argv[1]).open() as f:
        for line in f:
            from_l, from_t, w, h = [int(x)
                                    for x in CLAIM_RE.search(line).groups()]
            process_claim(from_l, from_t, w, h)

    # for i in range(ARRAY):
    #     print(''.join([str(x) for x in master[i]]))

    print('TOTAL:', sum([sum(x > 1 for x in i) for i in master]))


if __name__ == '__main__':
    main()
