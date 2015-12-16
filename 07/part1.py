#!/usr/bin/env python

import sys

# master results table
master = {}

# suck in the whole file
lines = [x.rstrip() for x in open(sys.argv[1]).readlines()]

while lines:
    line = lines.pop(0)  # consume
    items = line.split(' ')  # parse

    # sort out LHS from RHS
    lhs = []
    while items:
        item = items.pop(0)
        if item == '->':
            break
        lhs.append(item)

    assert len(items) == 1, 'Bad: %s (%s)' % (line, items)
    rhs = items[0]
    assert not rhs.isdigit()

    # .. operations follow ..
    #
    # assignment
    if len(lhs) == 1:
        if lhs[0].isdigit():
            op = int(lhs[0])
        else:
            if lhs[0] in master:
                op = master[lhs[0]]
            else:
                lines.append(line)
                continue

        print line
        master[rhs] = op
        continue

    # logical not
    if len(lhs) == 2:
        assert lhs[0] == 'NOT'
        if lhs[1] in master:
            print line
            master[rhs] = ~master[lhs[1]]
        else:
            lines.append(line)

        continue

    # AND / OR / LSHIFT / RSHIFT
    if lhs[0].isdigit():
        op1 = int(lhs[0])
    elif lhs[0] in master:
        op1 = master[lhs[0]]
    else:
        lines.append(line)
        continue

    if lhs[2].isdigit():
        op2 = int(lhs[2])
    elif lhs[2] in master:
        op2 = master[lhs[2]]
    else:
        lines.append(line)
        continue

    print 'Resolving: %s' % line        

    resolvers = {'RSHIFT': lambda x,y: x >> y,
                 'LSHIFT': lambda x,y: x << y,
                 'AND': lambda x,y: x & y,
                 'OR': lambda x,y: x | y,
                }
    master[rhs] = resolvers[lhs[1]](op1, op2)

for key, val in sorted(master.iteritems()):
    print '%s: %s' % (key, val)
