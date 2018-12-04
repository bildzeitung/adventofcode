#!/usr/bin/env python
''' Day 4
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

    print(ledger)
    summary = {}
    largest = -1
    largest_guard = None
    for guard in ledger:
        minutes = [0] * 60
        for item in ledger[guard]:
            start, finish = item
            for i in range(start, finish):
                minutes[i] += 1
            summary[guard] = minutes
            total = sum(minutes)
            if largest < total:
                largest = total
                largest_guard = guard

    print(summary)
    print('MOST MINUTES', largest_guard, 'TOTAL', largest)
    largest = -1
    largest_minute = 0
    for idx, minute in enumerate(summary[largest_guard]):
        if largest < minute:
            print('found', minute, idx)
            largest = minute
            largest_minute = idx

    print('BIGGEST SLEEP MINUTE', largest_minute, 'TOTAL', largest)
    print('CODE', int(largest_guard), largest_minute)


if __name__ == "__main__":
    main()
