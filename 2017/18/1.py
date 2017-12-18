#!/usr/bin/env python
'''
    Day 18
'''
import sys

from collections import defaultdict


class VM(object):
    def __init__(self, cmds):
        self.cmds = cmds
        self.pc = 0
        self.registers = defaultdict(int)
        self.sound = 0
        self.ok = False

    def run(self):
        self.ok = True
        while self.ok and self.pc < len(self.cmds):
            op = self.cmds[self.pc][0]
            args = self.cmds[self.pc][1:]
            # print 'OP', op, 'ARGS', args
            getattr(self, '_' + op)(*args)
            self.pc += 1

    def _resolve(self, arg):
        ''' Return a raw int, either because arg is an int or from a register
        '''
        if isinstance(arg, int):
            return arg

        return self.registers[arg]

    def _snd(self, x):
        self.sound = self._resolve(x)

    def _set(self, x, y):
        self.registers[x] = self._resolve(y)

    def _add(self, x, y):
        self.registers[x] += self._resolve(y)

    def _mul(self, x, y):
        self.registers[x] *= self._resolve(y)

    def _mod(self, x, y):
        self.registers[x] %= self._resolve(y)

    def _rcv(self, x):
        if self._resolve(x) != 0:
            print 'RECOVER', self.sound
            self.ok = False  # part 1 termination condition

    def _jgz(self, x, y):
        if self._resolve(x) > 0:
            self.pc += self._resolve(y) - 1  # -1 adj for auto-increment
   

def transint(v):
    ''' a filter to quickly sort out what are numbers
    '''
    try:
        v = int(v)
    except ValueError:
        pass
    return v


def main():
    cmds = [[transint(x.strip()) for x in line.split()] for line in sys.stdin]
    print cmds
    vm = VM(cmds)
    vm.run()


if __name__ == '__main__':
    main()