#!/usr/bin/env python
"""
    Day 23
"""
from pathlib import Path

from apollo2 import Apollo


class NAT:
    def __init__(self, zmachine):
        self._buffer = []
        self._zmachine = zmachine
        self._io = False

    def push(self, x, y):
        self._buffer.append((x, y))
        # print(f"NAT received {x}, {y}")

    def send(self):
        x, y = self._buffer.pop()
        print(f"NAT sent {x}, {y} to 0")
        self._zmachine.input_buffer.tx(x, y)

    def reset(self):
        self._io = False


class RouterProvider:
    def __init__(self, name, machines, nat):
        self._machines = machines
        self._out = []
        self._msgs = [name]
        self._nat = nat
        self._name = name

    def pop(self, _):
        if len(self._msgs):
            # print(f"[{self._name}] reading {self._msgs[0]}... {len(self._msgs)}")
            self._nat._io = True
            return self._msgs.pop(0)
        return -1

    def tx(self, x, y):
        self._msgs.append(x)
        self._msgs.append(y)
        self._nat._io = True

    def send(self, val):
        self._out.append(val)
        if len(self._out) == 3:
            dst, x, y = self._out
            if dst == 255:
                self._nat.push(x, y)
                self._out = []
                return
            # print(f"[{self._name}] sent {x}, {y} to {dst}")
            self._machines[dst].input_buffer.tx(x, y)
            self._out = []
            self._nat._io = True


def main():
    with Path("input.txt").open() as f:
        code = [int(x) for x in f.read().strip().split(",")]

    machines = [Apollo(i, code) for i in range(50)]
    nat = NAT(machines[0])
    routers = [RouterProvider(i, machines, nat) for i in range(50)]
    for r, m in zip(routers, machines):
        m.input_buffer = r
        m.output = r

    while True:
        for m in machines:
            m.run()
        # print(f"NAT I/O: {nat._io}")
        if not nat._io:
            assert all(len(x._msgs) == 0 for x in routers)
            assert all(len(x._out) == 0 for x in routers)
            # print("Idle")
            nat.send()
        nat.reset()


if __name__ == "__main__":
    main()
