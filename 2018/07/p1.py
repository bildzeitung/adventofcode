#!/usr/bin/env python
''' Day 7
'''
import re
import sys
from collections import defaultdict
from pathlib import Path

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


def main():
    data = load_data()

    done = []
    while data:
        item = sorted(x for x in data if not data[x])[0]
        done.append(item)
        for _, v in data.items():
            try:
                i = v.index(item)
            except ValueError:
                continue
            del v[i]
        del data[item]

    print(''.join(done))


if __name__ == '__main__':
    main()
