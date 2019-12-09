#!/usr/bin/env python
""" Machine class
"""


class Apollo:
    def __init__(self, code):
        self.code = code[:]
        self.pc = 0

    @property
    def instr(self):
        return self.code[self.pc] % 100

    def args(self, n):
        to_decode = self.code[self.pc] // 100
        vals = []
        for i in range(n):
            idx = self.pc + i + 1
            if (to_decode // (10 ** i)) % 10:
                # immediate
                vals.append(idx)
            else:
                # position
                vals.append(self.code[idx])

        return vals

    def run(self):
        while True:
            instr = self.instr

            if instr == 99:  # HALT
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
                self.code[self.args(1)[0]] = int(input("> "))
                self.pc += 2
            elif instr == 4:  # OUT
                print("OUT:", self.code[self.args(1)[0]])
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
            else:
                raise Exception(f"Dirty computer: {instr}")

        return self
