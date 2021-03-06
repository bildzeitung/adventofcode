#!/usr/bin/env python
""" Day 24 """

import sys

with open(sys.argv[1]) as infile:
    WEIGHTS = sorted([int(x.strip()) for x in infile])

K = sum(WEIGHTS)
TARGET = K / 3

def algorithm_u(ns, m):
    def visit(n, a):
        ps = [[] for i in xrange(m)]
        for j in xrange(n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def f(mu, nu, sigma, n, a):
        if mu == 2:
            yield visit(n, a)
        else:
            for v in f(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                if sum(v[0]) == TARGET:
                    yield v
        if nu == mu + 1:
            a[mu] = mu - 1
            item = visit(n, a)
            if sum(item[0]) == TARGET:
                yield item
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                item = visit(n, a)
                if sum(item[0]) == TARGET:
                    yield item
        elif nu > mu + 1:
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = mu - 1
            else:
                a[mu] = mu - 1
            if (a[nu] + sigma) % 2 == 1:
                for v in b(mu, nu - 1, 0, n, a):
                    if sum(v[0]) == TARGET:
                        yield v
            else:
                for v in f(mu, nu - 1, 0, n, a):
                    if sum(v[0]) == TARGET:
                        yield v
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in b(mu, nu - 1, 0, n, a):
                        if sum(v[0]) == TARGET:
                            yield v
                else:
                    for v in f(mu, nu - 1, 0, n, a):
                        if sum(v[0]) == TARGET:
                            yield v

    def b(mu, nu, sigma, n, a):
        if nu == mu + 1:
            while a[nu] < mu - 1:
                yield visit(n, a)
                a[nu] = a[nu] + 1
            yield visit(n, a)
            a[mu] = 0
        elif nu > mu + 1:
            if (a[nu] + sigma) % 2 == 1:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] < mu - 1:
                a[nu] = a[nu] + 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = 0
            else:
                a[mu] = 0
        if mu == 2:
            yield visit(n, a)
        else:
            for v in b(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v

    n = len(ns)
    a = [0] * (n + 1)
    for j in xrange(1, m + 1):
        a[n - m + j] = j - 1
    return f(m, n, 0, n, a)

#KEEPERS = [x for x in algorithm_u(WEIGHTS, 3) if sum(x[0]) == TARGET and sum(x[1]) == TARGET]
#print '\n'.join([str(x) for x in KEEPERS])

for x in algorithm_u(WEIGHTS, 3):
    if sum(x[0]) == TARGET and sum(x[1]) == TARGET:
        print '--> ', x
