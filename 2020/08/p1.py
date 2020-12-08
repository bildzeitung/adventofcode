#!/usr/bin/env python
"""
  Day 8
"""
import sys

from vm import VM


def main():
    with open(sys.argv[1]) as f:
        code = [(y[0], int(y[1])) for y in [x.strip().split(" ") for x in f]]

    vm = VM(code)
    seen = set([0])
    for a in vm:
        if vm.pc in seen:
            return a
        seen.add(vm.pc)


if __name__ == "__main__":
    print(main())
