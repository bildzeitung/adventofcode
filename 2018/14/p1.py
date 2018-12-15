#!/usr/bin/env python
''' Day 14
'''
import sys


def main():
    to_make = int(sys.argv[1])
    recipes = [3, 7]
    e1 = 0
    e2 = 1
    print(recipes)
    while len(recipes) < to_make + 10:
        e1 = (1 + recipes[e1] + e1) % len(recipes)
        e2 = (1 + recipes[e2] + e2) % len(recipes)
        t = [int(x) for x in str(recipes[e1] + recipes[e2])]
        recipes.extend(t)
        # print(recipes)

    print('FINAL:', ''.join(str(x) for x in recipes[to_make:to_make+10]))


if __name__ == "__main__":
    main()
