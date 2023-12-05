#!/usr/bin/env python
"""
    Day 3
"""
import re
import sys
from pathlib import Path

from rich.console import Console
from rich.theme import Theme

c = Console(theme=Theme(inherit=False))
find_numbers = re.compile(r"\d+")
find_operators = re.compile(r"[^\d\.]")


def main():
    puzzle = []
    all_numbers = []
    symbols = set()  # doesn't matter what the symbol is, just the location

    row = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            line = line.strip()
            for m in find_numbers.finditer(line):
                all_numbers.append(
                    (int(m[0]), [(a, row) for a in range(m.start(), m.end())])
                )
            for m in find_operators.finditer(line):
                if m[0] != "*":  # only need stars (gears) this time
                    continue
                symbols.add((m.start(), row))
            puzzle.append(line)
            row += 1

    def check_number(n) -> bool:
        for coord in n[1]:  # iterate through co-ords
            x, y = coord[0], coord[1]
            if (x - 1, y) in symbols or (x + 1, y) in symbols:
                return True
            if (
                (x - 1, y - 1) in symbols
                or (x, y - 1) in symbols
                or (x + 1, y - 1) in symbols
            ):
                return True
            if (
                (x - 1, y + 1) in symbols
                or (x, y + 1) in symbols
                or (x + 1, y + 1) in symbols
            ):
                return True

        return False

    good_numbers = [x for x in filter(check_number, all_numbers)]

    def is_a_near_b(a, b) -> bool:
        x, y = b[0], b[1]
        return a in (
            (x - 1, y),
            (x + 1, y),
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        )

    def check_gear(n) -> bool:
        r = []
        for g in good_numbers:
            for k in g[1]:
                if is_a_near_b(n, k):
                    r.append(g[0])
                    break

        return r

    sum = 0
    for gear in symbols:
        candidate = check_gear(gear)
        if len(candidate) == 2:
            sum += candidate[0] * candidate[1]

    return sum


if __name__ == "__main__":
    print(main())
