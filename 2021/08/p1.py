#!/usr/bin/env python
"""
    Day 8    
"""
import sys
from pathlib import Path


def main():
    LENGTHS = (2, 3, 4, 7)
    results = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            _, output = line.strip().split("|")
            # need length for 1, 4, 7, and 8
            # .. which are (2, 4, 3, 7) ...
            items = len(
                [
                    *filter(
                        lambda x: x in LENGTHS,
                        (len(x) for x in output.strip().split(" ")),
                    )
                ]
            )
            results.append(items)
    print(sum(results))


if __name__ == "__main__":
    main()
