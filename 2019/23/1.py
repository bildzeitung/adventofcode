#!/usr/bin/env python
"""
    Day 23
"""
from pathlib import Path

from apollo import Apollo


class RouterProvider:
    def __init__(self, name, machines):
        self._machines = machines
        self._out = []
        self._msgs = [name]

    def pop(self, _):
        if len(self._msgs):
            return self._msgs.pop(0)
        return -1

    def tx(self, x, y):
        self._msgs.append(x)
        self._msgs.append(y)

    def send(self, val):
        self._out.append(val)
        if len(self._out) == 3:
            dst, x, y = self._out
            if dst == 255:
                print(f"Destination 255: {x}, {y}")
                raise Exception("Done.")
            print(f"Sending ({x}, {y}) to {dst}")
            self._machines[dst].input_buffer.tx(x, y)
            self._out = []


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    machines = [Apollo(i, code) for i in range(50)]
    for i, m in enumerate(machines):
        p = RouterProvider(i, machines)
        m.input_buffer = p
        m.output = p

    while True:
        for m in machines:
            m.step()


if __name__ == "__main__":
    main()
