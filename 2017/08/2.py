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
  all_maxs = []
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

    all_maxs.append(registers[max(registers, key=registers.get)])
    
  print all_maxs
  print 'MAX:', max(all_maxs)


if __name__ == '__main__':
  main()
