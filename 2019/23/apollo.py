#!/usr/bin/env python
""" Machine class
"""
from collections import defaultdict


class Apollo:
    WAIT = "WAIT"
    HALT = "HALT"

    def __init__(self, name, code):
        self.name = name
        self.code = defaultdict(int, {i: v for i, v in enumerate(code)})
        self.input_buffer = None
        self.pc = 0
        self.state = self.WAIT
        self.output = None
        self._last_output = None
        self._relative_base = 0
        self._loop_detect = [None, None, None, None, None, None]
        self._is_in_loop = False

    @property
    def input(self):
        return self.input_buffer.pop(0)

    def args(self, n):
        to_decode = self.code[self.pc] // 100
        vals = []
        idx = self.pc + 1
        for i in range(n):
            mode = to_decode % 10
            if mode == 1:
                # immediate
                vals.append(idx)
            elif mode == 2:
                # relative
                vals.append(self._relative_base + self.code[idx])
            else:
                # position
                vals.append(self.code[idx])
            to_decode //= 10
            idx += 1

        return vals

    def single_arg(self):
        mode = (self.code[self.pc] // 100) % 10
        idx = self.pc + 1
        if mode == 1:
            return idx
        elif mode == 2:
            return self._relative_base + self.code[idx]

        return self.code[idx]

    def run(self):
        while True:
            self.step()

    @property
    def is_loop(self):
        if self._loop_detect == [3, 8, 6, 6, 6, 3] and not self._is_in_loop:
            self._is_in_loop = True
            print(f"[{self.name}] in loop")
        return self._is_in_loop

    def reset(self):
        self._is_in_loop = False

    def ld(self, instr):
        self._loop_detect.pop(0)
        self._loop_detect.append(instr)

    def step(self):
        instr = self.code[self.pc] % 100
        self.ld(instr)

        if instr == 99:  # HALT
            self.state = self.HALT
            print(f"[self.name] HALT")
            return
        if instr == 1:  # ADD
            arg0, arg1, dst = self.args(3)
            self.code[dst] = self.code[arg0] + self.code[arg1]
            self.pc += 4
        elif instr == 2:  # MUL
            arg0, arg1, dst = self.args(3)
            self.code[dst] = self.code[arg0] * self.code[arg1]
            self.pc += 4
        elif instr == 3:  # IN
            dst = self.single_arg()
            from_input = self.input
            self.code[dst] = from_input
            self.pc += 2
        elif instr == 4:  # OUT
            val = self.code[self.single_arg()]
            self.output.send(val)
            self._last_output = val
            self.pc += 2
        elif instr == 5:  # JMP-IF-TRUE
            tst, target = self.args(2)
            if self.code[tst]:
                self.pc = self.code[target]
            else:
                self.pc += 3
        elif instr == 6:  # JMP-IF-FALSE
            tst, target = self.args(2)
            if not self.code[tst]:
                self.pc = self.code[target]
            else:
                self.pc += 3
        elif instr == 7:  # LT
            arg0, arg1, dst = self.args(3)
            if self.code[arg0] < self.code[arg1]:
                self.code[dst] = 1
            else:
                self.code[dst] = 0
            self.pc += 4
        elif instr == 8:  # EQ
            arg0, arg1, dst = self.args(3)
            if self.code[arg0] == self.code[arg1]:
                self.code[dst] = 1
            else:
                self.code[dst] = 0
            self.pc += 4
        elif instr == 9:  # ADJ-RELBASE
            self._relative_base += self.code[self.single_arg()]
            self.pc += 2
        else:
            raise Exception(f"[{self.name}] Dirty computer: {instr} {self.pc}")
