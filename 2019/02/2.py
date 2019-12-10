#!/usr/bin/env python
""" Day 2
"""
import sys

from pathlib import Path


class Apollo:
    def __init__(self, code):
        self.code = code[:]

    def run(self):
        pc = 0
        while True:        
            instr = self.code[pc]
            if instr == 99:
                break  # HALT
            
            arg0, arg1, dst = self.code[pc+1], self.code[pc+2], self.code[pc+3]
            if instr == 1:
                self.code[dst] = self.code[arg0] + self.code[arg1]
            elif instr == 2:
                self.code[dst] = self.code[arg0] * self.code[arg1]
            else:
                raise Exception("Dirty computer")
            
            pc += 4

        return self


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(',')]

    for noun in range(100):
        for verb in range(100):
            code[1] = noun
            code[2] = verb
            a = Apollo(code).run()
            if a.code[0] == 19690720:
                print("FINAL:", 100 * noun + verb)


if __name__ == "__main__":
    main()
