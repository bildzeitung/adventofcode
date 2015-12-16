#!/usr/bin/env python

instr = list(open('paren.in').read().rstrip())
santa = 0
idx = 0

for i in instr:
    idx += 1
    if i == '(':
        santa += 1
    else:
        santa -= 1

    if santa < 0:
        break;

print idx
