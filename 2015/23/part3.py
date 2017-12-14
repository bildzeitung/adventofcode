#!/usr/bin/env python
""" Day 23 """

import sys

with open('code.in') as infile:
    PROGRAM = [x.rstrip() for x in infile]

REGISTERS = {'a': int(sys.argv[1]), 'b': 0}
PC = 0

while True:
    if PC >= len(PROGRAM):
        break

    INSTR = [x.replace(',', '') for x in PROGRAM[PC].split(' ')]

    if INSTR[0] == 'hlf':
        REGISTERS[INSTR[1]] /= 2
    elif INSTR[0] == 'tpl':
        REGISTERS[INSTR[1]] *= 3
    elif INSTR[0] == 'inc':
        REGISTERS[INSTR[1]] += 1
    elif INSTR[0] == 'jmp':
        PC += int(INSTR[1])
        continue
    elif INSTR[0] == 'jie':
        if not REGISTERS[INSTR[1]] % 2:
            PC += int(INSTR[2])
            continue
    elif INSTR[0] == 'jio':
        if REGISTERS[INSTR[1]] == 1:
            PC += int(INSTR[2])
            continue

    PC += 1

print ' '.join([sys.argv[1], str(REGISTERS['b'])])
