#!/usr/bin/env python
"""
  Day 14
"""
import itertools
import re
import sys

memre = re.compile("\[(\d+)\].+?(\d+)$")
floats = re.compile("X")
MEMSIZE = 36
MEMOM = 2 ** 36 - 1


def all_subsets(s):
    for x in itertools.chain.from_iterable(
        itertools.combinations(s, i) for i in range(len(s) + 1)
    ):
        yield MEMOM - sum(2 ** (MEMSIZE - y - 1) for y in x)


def to_zero(x):
    return MEMOM - 2 ** (MEMSIZE - x - 1)


def to_one(x):
    return 2 ** (MEMSIZE - x - 1)


def main():
    memory = {}
    mask = 0
    float_masks = []

    with open(sys.argv[1]) as f:
        while line := f.readline().strip():
            if "mask" in line:
                m = line.split("=")[1].strip()
                mask = int(m.replace("X", "0"), 2)
                floaters = [int(x.span()[0]) for x in floats.finditer(m)]
                floaters = [((to_zero(x), 0), (to_one(x), 1)) for x in floaters]
                float_masks = [x for x in itertools.product(*floaters)]
            else:
                dest, value = [int(x) for x in memre.search(line).groups()]
                dest = dest | mask
                for x in float_masks:
                    new_dest = dest
                    for m, i in x:
                        if i:
                            new_dest = new_dest | m
                        else:
                            new_dest = new_dest & m
                    memory[new_dest] = value

    return sum(memory.values())


if __name__ == "__main__":
    print(main())
