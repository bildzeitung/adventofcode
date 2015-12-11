#!/usr/bin/env python

import itertools
import re
import sys

DOUBLE = re.compile(r'(.)\1.*(.)\2')

password = sys.argv[1]

def reversed_enumerate(sequence):
    return itertools.izip(reversed(xrange(len(sequence))),
                          reversed(sequence),)

def advance(item):
    litem = list(item)
    for k, v in reversed_enumerate(litem):
        new_i = ord(v) + 1
        if new_i <= ord('z'):
            litem[k] = chr(new_i)
            break;
        else:
            litem[k] = 'a'
    return ''.join(litem)

def is_ok(item):
    # no i, l, or o
    if ('i' in item) or ('l' in item) or ('o' in item):
        return

    # must have two pairs
    if not DOUBLE.search(item):
        return

    # must have sequence
    check = ord(item[0])
    seq = 0
    for i in item[1:]:
        if (ord(i) - check) == 1:
            seq += 1
        else:
            seq = 0

        if seq > 1:
            return True

        check = ord(i)

    return None


password = advance(password) 
while not is_ok(password):
    password = advance(password) 

print 'FINAL: %s' % password
