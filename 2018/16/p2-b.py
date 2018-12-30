#!/usr/bin/env python
'''
    Day 16: Run supplied input program
'''
import sys
from pathlib import Path


class Machine:
    def __init__(self):
        self.reg = [0] * 4
        # opcodes now in order, according to derived values
        self.opcodes = ['gtir',
                        'mulr',
                        'seti',
                        'gtrr',
                        'bori',
                        'borr',
                        'banr',
                        'eqri',
                        'bani',
                        'addr',
                        'addi',
                        'eqrr',
                        'gtri',
                        'eqir',
                        'setr',
                        'muli']

    def run(self, opcode, input_a, input_b, output_c):
        getattr(self, self.opcodes[opcode])(input_a, input_b, output_c)

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


def main():
    with Path(sys.argv[1]).open() as f:
        while True:
            before_line = f.readline()
            instr = f.readline()
            f.readline()
            f.readline()  # space

            if before_line == instr:
                break

        # read test program
        prog = [[int(x) for x in line.strip().split(' ')] for line in f]

        # run test program
        m = Machine()
        for p in prog:
            m.run(*p)
        print("REGISTERS", m.reg)


if __name__ == '__main__':
    main()
