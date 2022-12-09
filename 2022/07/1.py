#!/usr/bin/env python
"""
    Day 7
"""
import sys
from pathlib import Path
from rich import print


def main():
    tree = {".": 0}
    up = []
    curr = tree
    with Path(sys.argv[1]).open() as f:
        line = next(f).strip()
        while True:
            try:
                if line.startswith("$"):  # command
                    p, c = line.split(" ", 1)
                    if c.startswith("cd"):
                        c, d = c.split(" ")
                        if d == "..":
                            curr = up.pop()
                        elif d == "/":
                            up = []
                            curr = tree
                        else:
                            curr[d] = {".": 0}
                            up.append(curr)
                            curr = curr[d]
                    else:  # ls
                        line = next(f).strip()
                        while not line.startswith("$"):
                            if not line.startswith("dir"):  # file
                                s, n = line.split(" ")
                                curr["."] += int(s)
                            line = next(f).strip()
                        continue
                line = next(f).strip()
            except StopIteration:
                break

    # roll up sums
    def rollup(tree):
        s = tree["."]
        for k, v in tree.items():
            if k == ".":
                continue
            s += rollup(v)
        tree["."] = s
        return tree["."]

    rollup(tree)
    print(tree)

    def under100k(tree):
        s = []
        if tree["."] < 100_000:
            s.append(tree["."])
        for k, v in tree.items():
            if k == ".":
                continue
            s.extend(under100k(v))
        return s

    allunder = under100k(tree)
    print(allunder)
    print(f"Sum: {sum(allunder)}")


if __name__ == "__main__":
    main()
