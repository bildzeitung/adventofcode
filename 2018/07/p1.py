#!/usr/bin/env python
""" Day 7

    A partial order on a graph.

"""
import re
import sys
from collections import defaultdict
from pathlib import Path

# Step Q must be finished before step I can begin.
DATA = re.compile(r"Step (.) must be finished before step (.) can begin")


def load_data():
    data = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        for line in f:
            # Store a list of steps and the dependencies of each step,
            # ie. A -> [ B, C, D ]
            #
            prereq, step = DATA.search(line).groups()
            data[step].append(prereq)
            # If a pre-requisite was encountered, but is not yet a key,
            # then make it a key. This builds a structure such that the
            # items without initial dependencies are findable.
            if prereq not in data:
                data[prereq] = []
    return data


def main():
    data = load_data()

    done = []
    while data:
        # Select the alphabetically first item with no dependencies;
        # this is the next available task to complete
        item = sorted(x for x in data if not data[x])[0]
        # that item is now complete!
        done.append(item)
        # remove the item from the dependency lists
        for v in data.values():
            try:
                i = v.index(item)
            except ValueError:
                continue
            del v[i]
        # finally, remove the item key (otherwise it will be re-selected)
        del data[item]

    print("".join(done))


if __name__ == "__main__":
    main()
