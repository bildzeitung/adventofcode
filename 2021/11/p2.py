#!/usr/bin/env python
"""
    Day 11
"""
import sys
from pathlib import Path

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

custom_theme = Theme(
    {
        "octopus": "bold red",
    }
)


class OctopusHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an octopus."""

    highlights = [r"(?P<octopus>0+)"]


console = Console(highlighter=OctopusHighlighter(), theme=custom_theme)


def tick(puzzle, mx, my):
    np = {}
    to_flash = []
    for y in range(my):
        for x in range(mx):
            p = (x, y)
            np[p] = puzzle[p] + 1
            if np[p] > 9:
                to_flash.append(p)
    have_flashed = set()
    while to_flash:
        f = to_flash.pop()
        if f in have_flashed:
            continue
        have_flashed.add(f)
        for x in range(f[0] - 1, f[0] + 1 + 1):
            for y in range(f[1] - 1, f[1] + 1 + 1):
                if x == f[0] and y == f[1]:
                    continue  # skip self
                p = (x, y)
                if p not in np:
                    continue  # bad puzzle coord
                np[p] += 1
                if np[p] > 9:
                    to_flash.append(p)
    # print(f"Have flashed -> {have_flashed}")
    for f in have_flashed:
        np[f] = 0
    return np, len(have_flashed) == (mx * my)


def render(puzzle, mx, my):
    for y in range(my):
        row = "".join(str(puzzle[(x, y)]) for x in range(mx))
        console.print(row)
    console.print()


def main():
    puzzle = {}
    with Path(sys.argv[1]).open() as f:
        y = 0
        for line in f:
            for x, v in enumerate(line.strip()):
                puzzle[(x, y)] = int(v)
            y += 1

    my = y
    mx = max(x[1] for x in puzzle) + 1

    total = 1
    while True:
        puzzle, f = tick(puzzle, mx, my)
        if f:
            break
        total += 1

    render(puzzle, mx, my)
    print(f"Flashes --> {total}")


if __name__ == "__main__":
    main()
