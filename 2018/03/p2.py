#!/usr/bin/env python
''' Day 3

    Brute force mark and evaluate

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

    claims = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            from_l, from_t, w, h = [int(x)
                                    for x in CLAIM_RE.search(line).groups()]
            claims.append((from_l, from_t, w, h))
            process_claim(from_l, from_t, w, h)

    ''' Loop through the claims a second time.

        If the sum of the elements is the same as the area of the
        rectangle, then there is no overlap
    '''
    for i, claim in enumerate(claims):
        l, t, w, h = claim
        total = sum(sum(master[t+j][l:l+w]) for j in range(h))
        if total == w * h:
            print("UNTOUCHED:", i+1)
            break  # done!


if __name__ == '__main__':
    main()
