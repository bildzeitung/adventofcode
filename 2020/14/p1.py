#!/usr/bin/env python
"""
  Day 14
"""
import re
import sys

memre = re.compile("\[(\d+)\].+?(\d+)$")


def main():
    memory = {}
    mask_1 = 0
    mask_0 = 0

    with open(sys.argv[1]) as f:
        while line := f.readline().strip():
            if "mask" in line:
                m = line.split("=")[1].strip()
                # positive mask
                mask_1 = int(m.replace("X", "0"), 2)
                mask_0 = int(m.replace("X", "1"), 2)
            else:
                dest, value = [int(x) for x in memre.search(line).groups()]
                memory[dest] = value & mask_0 | mask_1

    return sum(memory.values())


if __name__ == "__main__":
    print(main())
