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
                assert(m.end() - m.start() == 1)
                symbols.add((m.start(),row))
            puzzle.append(line)
            row += 1
    
    def check_number(n) -> bool:
        for coord in n[1]:  # iterate through co-ords
            x, y = coord[0], coord[1]
            if (x-1, y) in symbols or (x+1, y) in symbols:
                return True
            if (x-1,y-1) in symbols or (x,y-1) in symbols or (x+1,y-1) in symbols:
                return True
            if (x-1,y+1) in symbols or (x,y+1) in symbols or (x+1,y+1) in symbols:
                return True

        return False

    # now that the puzzle is loaded, get to work

    good_numbers = []
    good_ints = []
    for n in all_numbers:
        if check_number(n):
            good_numbers.extend(n[1])
            good_ints.append(n[0])

    for y in range(len(puzzle)):
        line = ''
        for x in range(0, len(puzzle[0])):
            if (x, y) in good_numbers:
                line += f'[red]{puzzle[y][x]}[/red]'
            else:
                line += puzzle[y][x]
        c.print(line)
    print(good_ints)
    return sum(good_ints)

if __name__ == "__main__":
    print(main())
