#!/usr/bin/env python
'''
    Day 16
'''
import sys
from pathlib import Path

#  OPCODE, INPUT A, INPUT B, OUTPUT C (register)


class Machine:
    def __init__(self):
        self.reg = [0] * 4
        self.opcodes = ['addr',
                        'addi',
                        'mulr',
                        'muli',
                        'banr',
                        'bani',
                        'borr',
                        'bori',
                        'setr',
                        'seti',
                        'gtir',
                        'gtri',
                        'gtrr',
                        'eqir',
                        'eqri',
                        'eqrr',
                        ]

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


def process(to_validate, instr, before, after):
    m = Machine()

    def run_instr(x):
        proc = instr[:]
        proc[0] = x
        m.reg = before[:]
        m.run(*proc)
        return m.reg == after

    return [run_instr(i) for i in to_validate]


def main():
    test_cases = []
    with Path(sys.argv[1]).open() as f:
        while True:
            before_line = f.readline()
            instr = f.readline()
            after_line = f.readline()
            f.readline()  # space

            if before_line == instr:
                break

            before_line = [int(x)
                           for x in
                           before_line.strip().split('[')[1][:-1].split(',')]
            after_line = [int(x)
                          for x in
                          after_line.strip().split('[')[1][:-1].split(',')]
            instr = [int(x) for x in instr.strip().split(' ')]
            test_cases.append((instr, before_line, after_line))

    instr_to_validate = [x for x in range(len(Machine().opcodes))]

    while instr_to_validate:
        results = set()
        to_remove = []
        for t in test_cases:
            instr, before, after = t
            rv = process(instr_to_validate, instr, before, after)
            if sum(rv) == 1:
                good_instr = instr_to_validate[rv.index(1)]
                results.add((Machine().opcodes[good_instr], good_instr, instr[0]))
                to_remove.append(t)

        print('R', results)
        for _, x, _ in results:
            instr_to_validate.remove(x)

        # print('STARTED WITH', len(test_cases))
        # for x in to_remove:
        #     test_cases.remove(x)
        # print('ENDED WITH', len(test_cases))

        # print('I', instr_to_validate)



if __name__ == '__main__':
    main()
