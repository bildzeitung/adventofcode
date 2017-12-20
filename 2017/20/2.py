#!/usr/bin/env python
'''
    Day 20
'''
import sys

from collections import Counter
from itertools import izip


def simulate(particles):
    for particle in particles:
        particle['v'] = tuple(sum(v)
                              for v in izip(particle['v'], particle['a']))
        particle['p'] = tuple(sum(v)
                              for v in izip(particle['p'], particle['v']))
    
    # check for collisions
    multiples = []
    for x in Counter(x['p'] for x in particles).most_common():
        if x[1] < 2:
            break
        multiples.append(x[0])
    
    # filter out destroyed particles
    return [x for x in particles if x['p'] not in multiples]


def main():
    particles = []
    for line in sys.stdin:
        p, v, a = [x.strip() for x in line.split(', ')]
        p = tuple(int(x) for x in p[3:-1].split(','))
        v = tuple(int(x) for x in v[3:-1].split(','))
        a = tuple(int(x) for x in a[3:-1].split(','))

        particles.append({'p': p, 'v': v, 'a': a})

    while True:
        print len(particles)
        particles = simulate(particles)


if __name__ == '__main__':
    main()
