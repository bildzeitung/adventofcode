#!/usr/bin/env python
"""
  Day 8
"""
import sys


class VM:

  def __init__(self, code):
    self.code = code
    self.pc = 0
    self.methods = {'acc': self.acc,
               'jmp': self.jmp,
               'nop': self.nop}
    self.accumulator = 0

  def acc(self, arg):
    self.accumulator += arg
    self.pc += 1


  def jmp(self,arg):
    self.pc += arg

  def nop(self, _):
    self.pc += 1

  def step(self):
    instr, arg = self.code[self.pc]
    self.methods[instr](arg)


def main():
  with open(sys.argv[1]) as f:
    code = [(y[0], int(y[1])) for y in [x.strip().split(' ') for x in f]]

  vm = VM(code)
  seen = set([0])
  while True:
    vm.step()
    if vm.pc in seen:
      return vm.accumulator
    seen.add(vm.pc)

  return "DEBUG"


if __name__ == "__main__":
    print(main())