#!/usr/bin/env python

with open('box.in') as f:
    grand_total = 0
    for line in f:
        a, b, c = sorted([int(x) for x in line.rstrip().split('x')])
        #
        # perimeter of smallest face is 2 * (a+b), since the list is sorted
        # volume is easy -- length * width * height (a*b*c)
        #
        perimeter = 2 * (a + b)
        volume = a * b * c
        box = perimeter + volume
        print "%s %s %s --> %s : %s --> %s" % (a, b, c, perimeter, volume, box)
        grand_total += box

    print "GRAND TOTAL: %s" % grand_total

