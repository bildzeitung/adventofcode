#!/usr/bin/env python
"""
    Day 10
"""
import sys
from pathlib import Path
from rich import print


def main():
    when_to_check = (20, 60, 100, 140, 180, 220)
    signal_strenth = []
    X = 1  # starting register value
    pc = 1
    wait = False
    val = 0
    with Path(sys.argv[1]).open() as f:
        while True:
            if not wait:
                try:
                    line = next(f).strip()
                except StopIteration:
                    break
                if "noop" in line:
                    pass
                else:  # it's an addx
                    val = int(line.split(" ")[1])
                    wait = True
            else:
                wait = False
                X += val
            pc += 1
            # print(f"Cycle: {pc}  X: {X}")

            if pc in when_to_check:
                print(f"Signal strength: {pc * X}")
                signal_strenth.append(pc * X)
    print(f"Sum: {sum(signal_strenth)}")


if __name__ == "__main__":
    main()
