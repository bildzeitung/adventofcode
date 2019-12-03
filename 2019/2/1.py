#!/usr/bin/env python
""" Day 2
"""
import sys

from pathlib import Path


def main():
    with Path(sys.argv[1]).open() as f:
        code = [int(x) for x in f.read().strip().split(',')]

    pc = 0
    while True:        
        instr = code[pc]
        if instr == 99:
            break  # HALT
        
        arg0, arg1, dst = code[pc+1], code[pc+2], code[pc+3]
        if instr == 1:
            code[dst] = code[arg0] + code[arg1]
        elif instr == 2:
            code[dst] = code[arg0] * code[arg1]
        else:
            raise Exception("Dirty computer")
        
        pc += 4

    print("DONE", code)

if __name__ == "__main__":
    main()