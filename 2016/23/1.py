#!/usr/bin/env python
'''
    Day 23
'''
import sys


def _cpy(pc, src, dst):
    # illegal; skip
    if dst not in 'abcd':
        print 'WARNING: Illegal cpy', src, dst
        return

    if src in 'abcd':
        registers[dst] = registers[src]
    else:
        registers[dst] = int(src)
    return pc + 1


def _inc(pc, reg):
    registers[reg] += 1
    return pc + 1


def _dec(pc, reg):
    registers[reg] -= 1
    return pc + 1


def _jnz(pc, reg, dst):
    if reg in 'abcd':
        value = registers[reg]
    else:
        value = int(reg)

    if dst in 'abcd':
        dst = registers[dst]
    else:
        dst = int(dst)

    if value != 0:
        return pc + dst

    return pc + 1


def _tgl(pc, reg):
    if reg in 'abcd':
        addr = pc + registers[reg]
    else:
        addr = pc + int(reg)

    # cannot toggle out of range
    if addr >= len(memory) or addr < 0:
        print 'WARNING: toggling out of range', addr
        return pc + 1

    # read program
    op = memory[addr].split()

    if op[0] == 'inc':
        op[0] = 'dec'
    elif op[0] in ('tgl', 'dec'):
        op[0] = 'inc'
    elif op[0] == 'jnz':
        op[0] = 'cpy'
    elif op[0] == 'cpy':
        op[0] = 'jnz'
    else:
        raise 'Bad Instruction'

    # write program back
    memory[addr] = ' '.join(op)

    return pc + 1

instructions = {'cpy': _cpy, 'inc': _inc, 'dec': _dec, 'jnz': _jnz, 'tgl': _tgl}


if __name__ == '__main__':
    with open(sys.argv[1]) as infile:
        memory = [line.strip() for line in infile]

    # initial setting is A <= 7
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    pc = 0
    while pc < len(memory):
        # print 'PC', pc, '|', memory[pc], '|', registers
        op = memory[pc].split()
        pc = instructions[op[0]](pc, *op[1:])

    print registers
