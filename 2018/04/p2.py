#!/usr/bin/env python
''' Day 4

    See p1.py for general comments
'''
import re
import sys
from collections import defaultdict
from pathlib import Path

GUARD_RE = re.compile(r'#(\d+)')
MINUTE_RE = re.compile(r':(\d\d)')


def main():
    ledger = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        guard = None
        start_nap = None
        end_nap = None
        for line in f:
            if 'Guard' in line:
                guard = GUARD_RE.search(line).groups()[0]

            minute = int(MINUTE_RE.search(line).groups()[0])
            if 'falls asleep' in line:
                start_nap = minute
            if 'wakes up' in line:
                end_nap = minute
                ledger[guard].append((start_nap, end_nap))
                start_nap = None
                end_nap = None

    summary = {}
    for guard in ledger:
        minutes = [0] * 60
        for item in ledger[guard]:
            start, finish = item
            for i in range(start, finish):
                minutes[i] += 1
            summary[guard] = {'minutes': minutes,
                              'max': max(minutes)
                              }

    ''' Similar to part 1, but different key.

        In this case, we look at the maximum minutes, not the total
    '''
    most_sleepy = max(summary, key=lambda k: summary[k]['max'])
    print(summary[most_sleepy]['minutes'])
    most_overlap = max(summary[most_sleepy]['minutes'])
    most_minutes = summary[most_sleepy]['minutes']
    print('OVERLAP', most_overlap)
    idx = most_minutes.index(most_overlap)
    print('IDX', idx)
    print('CODE', int(most_sleepy) * idx)


if __name__ == "__main__":
    main()
