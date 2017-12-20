#!/usr/bin/env python
'''
    Day 20
'''
import sys

from itertools import izip


def simulate(particles):
    for particle in particles:
        particle['v'] = tuple(sum(v)
                              for v in izip(particle['v'], particle['a']))
        particle['p'] = tuple(sum(v)
                              for v in izip(particle['p'], particle['v']))

def main():
    particles = []
    idx = 0
    for line in sys.stdin:
        # print line
        p, v, a = [x.strip() for x in line.split(', ')]
        p = tuple(int(x) for x in p[3:-1].split(','))
        v = tuple(int(x) for x in v[3:-1].split(','))
        a = tuple(int(x) for x in a[3:-1].split(','))

        particles.append({'p': p, 'v': v, 'a': a, 'idx': idx,
                          })
        idx += 1

    while True:
        print sorted(particles, key=lambda x: sum(map(abs, x['p'])))[0]
        simulate(particles)


if __name__ == '__main__':
    main()
