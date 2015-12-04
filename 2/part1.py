#!/usr/bin/env python

with open('box.in') as f:
    grand_total = 0
    for line in f:
        a, b, c = sorted([int(x) for x in line.rstrip().split('x')])
        #
        # total area is twice each unique face (a*b, b*c, a*c) 
        # slack is the *smallest* face, which in our sorted list is a*b
        #
        box = 2 * (a*b + b*c + a*c) + a*b
        print "%s %s %s --> %s" % (a, b, c, box)
        grand_total += box

    print "GRAND TOTAL: %s" % grand_total

