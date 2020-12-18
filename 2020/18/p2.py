#!/usr/bin/env python
"""
  Day 18

  The general steps here are:
    - tokenize the string
    - read the tokens and re-write the infix expression into a postfix one
    - evaluate the postfix expression

  In order to avoid an 'if' on the expression evaluation, use eval(); this is
  a super heavyweight way to do it, but lol.

"""
import sys
from io import BytesIO
from tokenize import tokenize, NEWLINE, OP, NUMBER, ENDMARKER


def postfixer(f):
    """ Convert line of tokens into a postfix expression
    """
    opstack = []
    for t in tokenize(f.readline):
        if t.type == OP:
            if t.string in ("*", "+"):
                # both ( and * have lower precedence, so emit any +'s
                while opstack and opstack[-1] == "+":
                    yield opstack.pop()
                opstack.append(t.string)
            if t.string == "(":
                opstack.append(t.string)
            if t.string == ")":
                while True:
                    arg = opstack.pop()
                    if arg == "(":
                        break
                    yield arg
        if t.type == NUMBER:
            yield t.string

        if t.type in (NEWLINE, ENDMARKER):
            for o in reversed(opstack):
                yield o
            return


def solve(p):
    """ Evaluate a postfix expression
    """
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
        return sum(solve(postfixer(BytesIO(line))) for line in f)


if __name__ == "__main__":
    print(main())
