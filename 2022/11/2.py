#!/usr/bin/env python
"""
    Day 11
"""
import sys
from pathlib import Path
from attrs import define
from typing import Any
from operator import mul, add
from rich import print
from math import prod


@define
class Monkey:
    items: list
    operation: str
    rightop: Any
    divby: int
    true_throw: int
    false_throw: int
    inspected: int = 0

    def inspect(self, lcm, monkeys):
        for item in self.items:
            if self.rightop != "old":
                if self.operation == "+":
                    worry = item + self.rightop
                else:
                    worry = item * self.rightop
            else:
                worry = item * item
            worry = worry % lcm
            m = worry % self.divby
            if m:
                monkeys[self.false_throw].items.append(worry)
            else:
                monkeys[self.true_throw].items.append(worry)
        self.inspected += len(self.items)
        self.items = []


def main():
    monkeys = []
    with Path(sys.argv[1]).open() as f:
        while True:
            try:
                next(f)  # Monkey X
                items = [
                    int(x.strip()) for x in next(f).strip().split(":")[1].split(",")
                ]
                l, op, r = next(f).split("=")[1].strip().split(" ")  # op
                if "old" not in r:
                    r = int(r)
                d = int(next(f).split(" ")[-1].strip())  # test
                tt = int(next(f).split(" ")[-1].strip())  # if true
                ft = int(next(f).split(" ")[-1].strip())  # if false
                monkeys.append(Monkey(items, op, r, d, tt, ft))
                next(f)  # empty
            except StopIteration:
                break

        lcm = prod(m.divby for m in monkeys)
        for z in range(10_000):
            for i, monkey in enumerate(monkeys):
                monkey.inspect(lcm, monkeys)
        print(
            prod(x.inspected for x in sorted(monkeys, key=lambda x: -x.inspected)[0:2])
        )


if __name__ == "__main__":
    main()
