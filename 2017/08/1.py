#!/usr/bin/env python
'''
  Day 8
'''
import sys

from collections import defaultdict

ops = { '>': lambda x,y: x > y, '<': lambda x,y: x < y,
        '==': lambda x,y: x == y, '!=': lambda x,y: x != y,
        '>=': lambda x,y: x >= y, '<=': lambda x,y: x <= y,
      }


def main():
  registers = defaultdict(int)
  for line in sys.stdin:
    reg, regop, value, _, condreg, condop, exprval = line.strip().split()
    value = int(value)
    exprval = int(exprval)
    if ops[condop](registers[condreg], exprval):
      if regop == 'inc':
        registers[reg] += value
      else:
        registers[reg] -= value
    
  print registers
  maxreg = max(registers, key=registers.get)
  print maxreg, '->', registers[maxreg]



if __name__ == '__main__':
  main()
