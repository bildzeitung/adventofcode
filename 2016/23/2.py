#!/usr/bin/env python

import sys

# initial setting is A <= 12
# registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
pc = 0

with open(sys.argv[1]) as program:
    memory = [line.strip() for line in program]


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

    print 'Toggle', addr, memory[addr]

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


def print_program(line):
    for i in range(max(0, line - window), min(len(memory) - 1, line + window)):
        prefix = ' '
        if i == pc:
            prefix = '*'
        print i, prefix, memory[i]


instructions = {'cpy': _cpy, 'inc': _inc, 'dec': _dec, 'jnz': _jnz, 'tgl': _tgl}

running = False
run_once = False
breakpoints = []
window = 3
last_cmd = ''

while True:
    if pc >= len(memory):
        break

    if running or run_once:
        op = memory[pc].split()
        pc = instructions[op[0]](pc, *op[1:])

        run_once = False
        if pc in breakpoints:
            running = False
    else:
        print registers
        print_program(pc)
        cmd = raw_input('> ')
        if not cmd:
            cmd = last_cmd
        last_cmd = cmd
        cmd = cmd.split()

        if not cmd:
            continue

        if cmd[0] == 'q':  # quit
            break
        elif cmd[0] == 'g':  # go
            running = True
        elif cmd[0] == 's':  # step
            run_once = True
        elif cmd[0] == 'b':  # show / set breakpoint
            if len(cmd) < 2:
                print 'Breakpoints:', breakpoints
                continue
            bp = int(cmd[1])
            if bp in breakpoints:
                breakpoints.remove(bp)
            else:
                breakpoints.append(bp)
            print 'Breakpoints:', breakpoints
        elif cmd[0] == 'l':  # list
            print_program(int(cmd[1]))
        else:
            print 'Illegal command:', ' '.join(cmd)

print registers
