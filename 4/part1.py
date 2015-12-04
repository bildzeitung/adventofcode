#!/usr/bin/env python

from hashlib import md5
import sys

secret = sys.argv[1]

i = 1
while not md5('{0}{1}'.format(secret, i)).hexdigest().startswith('00000'):
    i += 1

print i
