#!/usr/bin/env python
""" Day 12 """

import json
import sys

SOURCE = json.load(open(sys.argv[1]))

def do_total(data):
    """ Sum all numbers """
    total = 0
    if hasattr(data, 'itervalues'):
        gen = data.itervalues()
    else:
        gen = data

    for item in gen:
        if isinstance(item, list):
            total += do_total(item)
        elif isinstance(item, dict):
            # drop the dict if any values are 'red'
            if [x for x in item.values() if isinstance(x, basestring) and x == 'red']:
                continue
            total += do_total(item)
        elif isinstance(item, basestring):
            continue
        elif isinstance(item, int):
            total += item
        else:
            raise ValueError('Help: %s' % item)

    return total

print 'FINAL: %s' % do_total(SOURCE)
