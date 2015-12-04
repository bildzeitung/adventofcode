#!/usr/bin/env python

import hashlib
import sys

secret = sys.argv[1]

i = 1
while not hashlib.md5('{0}{1}'.format(secret, i))\
        .hexdigest().startswith('000000'):
    i += 1

print i
