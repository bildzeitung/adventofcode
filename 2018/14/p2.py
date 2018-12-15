#!/usr/bin/env python
''' Day 14
'''
import sys
from itertools import count


LIMIT = 1_000_000


def main():
    to_make = sys.argv[1]
    recipes = [3, 7]
    e1 = 0
    e2 = 1
    oldi = 0
    recipe_string = ""
    for i in count():
        e1 = (1 + recipes[e1] + e1) % len(recipes)
        e2 = (1 + recipes[e2] + e2) % len(recipes)
        t = [int(x) for x in str(recipes[e1] + recipes[e2])]
        recipes.extend(t)

        # check only once in a while
        if not (i % LIMIT) and i:
            print(i)
            recipe_string += ''.join(str(x) for x in recipes[oldi:])
            f = recipe_string.find(to_make)
            if f != -1:
                print('DONE:', f)
                # print(recipe_string)
                return
            oldi = len(recipes)


if __name__ == "__main__":
    main()
