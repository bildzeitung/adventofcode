#!/usr/bin/env python
'''
    Day 19: Back to the VM

'''
import sys
from pathlib import Path


class Machine:
    def __init__(self):
        self.program = []
        self.pc_reg = None
        self.pc = 0
        self.reg = [0] * 6
        self.opcodes = ['addr', 'addi', 'mulr', 'muli',
                        'banr', 'bani', 'borr', 'bori',
                        'setr', 'seti',
                        'gtir', 'gtri', 'gtrr',
                        'eqir', 'eqri', 'eqrr',
                        ]

    def set_pc_reg(self, r):
        self.pc_reg = r

    def set_program(self, p):
        self.program = p

    def addr(self, a, b, c):
        self.reg[c] = self.reg[a] + self.reg[b]

    def addi(self, a, b, c):
        self.reg[c] = self.reg[a] + b

    def mulr(self, a, b, c):
        self.reg[c] = self.reg[a] * self.reg[b]

    def muli(self, a, b, c):
        self.reg[c] = self.reg[a] * b

    def banr(self, a, b, c):
        self.reg[c] = self.reg[a] & self.reg[b]

    def bani(self, a, b, c):
        self.reg[c] = self.reg[a] & b

    def borr(self, a, b, c):
        self.reg[c] = self.reg[a] | self.reg[b]

    def bori(self, a, b, c):
        self.reg[c] = self.reg[a] | b

    def setr(self, a, b, c):
        self.reg[c] = self.reg[a]

    def seti(self, a, b, c):
        self.reg[c] = a

    def gtir(self, a, b, c):
        self.reg[c] = 1 if a > self.reg[b] else 0

    def gtri(self, a, b, c):
        self.reg[c] = 1 if self.reg[a] > b else 0

    def gtrr(self, a, b, c):
        self.reg[c] = 1 if self.reg[a] > self.reg[b] else 0

    def eqir(self, a, b, c):
        self.reg[c] = 1 if a == self.reg[b] else 0

    def eqri(self, a, b, c):
        self.reg[c] = 1 if self.reg[a] == b else 0

    def eqrr(self, a, b, c):
        self.reg[c] = 1 if self.reg[a] == self.reg[b] else 0

    def run(self):
        while len(self.program) > self.pc >= 0:
            self.reg[self.pc_reg] = self.pc
            opcode, *args = self.program[self.pc]
            # rc = f"ip={self.pc} {self.reg} {opcode} {' '.join(str(x) for x in args)}"
            getattr(self, opcode)(*args)
            self.pc = self.reg[self.pc_reg] + 1
            # print(rc, self.reg)


def main():
    m = Machine()
    with Path(sys.argv[1]).open() as f:
        hashline = f.readline().strip().split(' ')[1]
        m.set_pc_reg(int(hashline))
        program = []
        for line in f:
            opcode, *args = line.strip().split(' ')
            program.append([opcode] + [int(x) for x in args])

    m.set_program(program)
    m.run()
    print(m.reg)


if __name__ == '__main__':
    main()
