#!/usr/bin/env python
"""
  Day 18
"""
import sys
from io import BytesIO
from tokenize import tokenize, NEWLINE, OP, NUMBER, ENDMARKER


def evaluator(f):
    opstack = []
    datastack = []
    for t in tokenize(f.readline):
        # print(f"Processing {t}  D: {datastack}  O: {opstack}")
        if t.type == OP:
            if t.string in ("*", "+"):
                opstack.append(t.string)
            if t.string == "(":
                datastack.append(t.string)
            if t.string == ")":
                arg0 = datastack.pop()
                datastack.pop()
                if opstack and datastack and datastack[-1] != "(":
                    arg0 = str(eval(f"{arg0} {opstack.pop()} {datastack.pop()}"))
                datastack.append(arg0)
        if t.type == NUMBER:
            if opstack and datastack and datastack[-1] != "(":
                datastack.append(
                    str(eval(f"{datastack.pop()} {opstack.pop()} {t.string}"))
                )
            else:
                datastack.append(t.string)

        if t.type in (NEWLINE, ENDMARKER):
            return datastack.pop()


def main():
    with open(sys.argv[1], "rb") as f:
        s = [int(evaluator(BytesIO(line))) for line in f]
        print(s)
        return sum(s)


if __name__ == "__main__":
    print(main())
