#!/usr/bin/env python
"""
    Day 5
"""
import sys
from pathlib import Path
from collections import defaultdict


def main():
    stacks = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        for line in f:
            if "[" not in line:
                break
            line = (
                line.rstrip()
                .replace("    ", ".")
                .replace("[", "")
                .replace("]", "")
                .strip()
                .replace(" ", "")
            )
            print(line)
            for i, x in enumerate(line):
                if x == ".":
                    continue
                stacks[i].insert(0, x)

        next(f)  # skip blank line

        for line in f:
            line = (
                line.replace("move", "")
                .replace("from", "")
                .replace("to", "")
                .replace("  ", " ")
                .strip()
            )
            num, source, dest = [int(x) for x in line.split(" ")]

            stacks[dest - 1].extend(stacks[source - 1][-num:])
            stacks[source - 1] = stacks[source - 1][:-num]
            print(stacks)

        print("".join(stacks[s][-1] for s in sorted(stacks)))


if __name__ == "__main__":
    main()
