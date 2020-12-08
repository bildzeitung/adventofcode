#!/usr/bin/env python
"""
  Day 8
"""
import sys
from copy import copy

from vm import VM


def trial(vm):
    """ Turn the infinite loop check into a function
  """
    seen = set([0])
    for a in vm:
        if vm.pc in seen:
            return False
        seen.add(vm.pc)
    return True


def main():
    with open(sys.argv[1]) as f:
        code = [(y[0], int(y[1])) for y in [x.strip().split(" ") for x in f]]

    idx = 0
    cc = copy(code)
    while True:
        vm = VM(cc)
        if trial(vm):  # did VM complete?
            return vm.accumulator

        """ Brute force:
        - swap a given nop or jmp
        - re-run
        - assume the data is good, so will terminate above
    """
        cc = copy(code)
        swapped = False
        while not swapped:
            if cc[idx][0] == "nop":
                print(f"nop swap at {idx}")
                cc[idx] = ("jmp", cc[idx][1])
                swapped = True
            if cc[idx][0] == "jmp":
                print(f"jmp swap at {idx}")
                cc[idx] = ("nop", cc[idx][1])
                swapped = True
            idx += 1

    return "DEBUG"


if __name__ == "__main__":
    print(main())
