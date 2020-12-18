#!/usr/bin/env python
"""
  Day 18
"""
import sys
from io import BytesIO
from tokenize import tokenize, NEWLINE, OP, NUMBER, ENDMARKER


def postfixer(f):
    opstack = []
    emitted = []
    for t in tokenize(f.readline):
        if t.type == OP:
            if t.string in ("*", "+"):
                # both ( and * have lower precedence, so emit any +'s
                while opstack and opstack[-1] == "+":
                    emitted.append(opstack.pop())
                opstack.append(t.string)
            if t.string == "(":
                opstack.append(t.string)
            if t.string == ")":
                while True:
                    arg = opstack.pop()
                    if arg == "(":
                        break
                    emitted.append(arg)
        if t.type == NUMBER:
            emitted.append(t.string)

        if t.type in (NEWLINE, ENDMARKER):
            emitted.extend(reversed(opstack))
            print(emitted)
            return emitted


def solve(p):
    operands = []
    for i in p:
        if i in ("*", "+"):
            arg0, arg1 = operands.pop(), operands.pop()
            operands.append(str(eval(f"{arg0} {i} {arg1}")))
        else:
            operands.append(i)
    return int(operands.pop())


def main():
    with open(sys.argv[1], "rb") as f:
        s = [solve(postfixer(BytesIO(line))) for line in f]
        print(s)
        return sum(s)


if __name__ == "__main__":
    print(main())
