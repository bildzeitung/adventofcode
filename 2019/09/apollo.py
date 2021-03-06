#!/usr/bin/env python
""" Machine class
"""
from collections import defaultdict


class Apollo:
    WAIT = "WAIT"
    HALT = "HALT"

    def __init__(self, name, code, input_buffer):
        self.name = name
        self.code = defaultdict(int, {i: v for i, v in enumerate(code)})
        self._input_buffer = input_buffer
        self.pc = 0
        self.state = self.WAIT
        self.output = None
        self._last_output = None
        self._relative_base = 0

    @property
    def input(self):
        if self._input_buffer:
            return self._input_buffer.pop(0)

        return None

    def send(self, val):
        self._input_buffer.append(val)

    @property
    def instr(self):
        return self.code[self.pc] % 100

    def args(self, n):
        to_decode = self.code[self.pc] // 100
        vals = []
        for i in range(n):
            idx = self.pc + i + 1
            mode = (to_decode // (10 ** i)) % 10
            if mode == 1:
                # immediate
                vals.append(idx)
            elif mode == 2:
                # relative
                vals.append(self._relative_base + self.code[idx])
            else:
                # position
                vals.append(self.code[idx])

        return vals

    def run(self):
        while True:
            instr = self.instr

            if instr == 99:  # HALT
                self.state = self.HALT
                break
            if instr == 1:  # ADD
                arg0, arg1, dst = self.args(3)
                self.code[dst] = self.code[arg0] + self.code[arg1]
                self.pc += 4
            elif instr == 2:  # MUL
                arg0, arg1, dst = self.args(3)
                self.code[dst] = self.code[arg0] * self.code[arg1]
                self.pc += 4
            elif instr == 3:  # IN
                dst = self.args(1)[0]
                from_input = self.input
                if from_input is None:  # need to wait for input
                    break
                self.code[dst] = from_input
                self.pc += 2
            elif instr == 4:  # OUT
                val = self.code[self.args(1)[0]]
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
                self._relative_base += self.code[self.args(1)[0]]
                self.pc += 2
            else:
                raise Exception(f"Dirty computer: {instr}")

        return self
