#!/usr/bin/env python
''' Day 7
'''
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE_TIME = 60  # base + offset (A == 1, B == 2, ...)
WORKERS = 5  # total number of workers

# Step Q must be finished before step I can begin.
DATA = re.compile(r'Step (.) must be finished before step (.) can begin')


def load_data():
    data = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        for line in f:
            prereq, step = DATA.search(line).groups()
            data[step].append(prereq)
            if prereq not in data:
                data[prereq] = []
    return data


def get_next(data):
    item = sorted(x for x in data if not data[x])
    if not item:
        return None, 0

    item = item[0]
    del data[item]

    return item, BASE_TIME + ord(item) - ord('A') + 1


def main():
    data = load_data()

    time = 0
    workers = [(None, 0)] * WORKERS
    while data:
        time += 1

        # assign work
        for i, t in enumerate(workers):
            if t[1] == 0:
                workers[i] = get_next(data)

        # complete work
        for i, w in enumerate(workers):
            workers[i] = (w[0], max(0, w[1] - 1))
            # if work was assigned, and the timer ran out, then
            # remove the work item from dependency lists
            if workers[i][1] == 0 and w[0]:
                for _, v in data.items():
                    try:
                        i = v.index(w[0])
                    except ValueError:
                        continue
                    del v[i]

    # final adjustment
    time += max(w[1] for w in workers)

    print('TIME', time)


if __name__ == '__main__':
    main()
