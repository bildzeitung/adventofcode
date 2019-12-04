#!/usr/bin/env python
"""
    Day 4
"""
import re


DOUBLE_DIGIT = re.compile(r"(.)\1")
RANGE = (248345, 746315)


def main():
    candidates = []
    for i in range(RANGE[0], RANGE[1]):
        if not DOUBLE_DIGIT.search(str(i)):
            continue

        is_ok = True
        for a, b in zip(str(i), str(i)[1:]):
            if a > b:
                is_ok = False
                break
        if is_ok:
            candidates.append(i)

    print("GOT:", len(candidates))


if __name__ == "__main__":
    main()
