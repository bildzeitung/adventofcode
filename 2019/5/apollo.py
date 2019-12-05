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
                vals.append(self.code[idx])
            else:
                # position
                vals.append(self.code[self.code[idx]])

        # print("decoding:", to_decode, vals)

        return reversed(vals)

    def run(self):
        while True:
            instr = self.instr

            if instr == 99:  # HALT
                break
            if instr == 1:  # ADD
                arg0, arg1 = self.args(2)
                self.code[self.code[self.pc + 3]] = arg0 + arg1
                self.pc += 4
            elif instr == 2:  # MUL
                arg0, arg1 = self.args(2)
                self.code[self.code[self.pc + 3]] = arg0 * arg1
                self.pc += 4
            elif instr == 3:  # IN
                self.code[self.code[self.pc + 1]] = int(input("> "))
                self.pc += 2
            elif instr == 4:  # OUT
                print("OUT:", *self.args(1))
                self.pc += 2
            else:
                raise Exception(f"Dirty computer: {instr}")

        return self
