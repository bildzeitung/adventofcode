#!/usr/bin/env python
"""
  Day 21
"""
import sys
from collections import defaultdict
from functools import reduce


def main():
    rbya = defaultdict(list)
    with open(sys.argv[1]) as f:
        # the data structure for this is:
        #   <allergen> -> list of ingredient sets
        #
        for line in f:
            ingredients, allergens = [
                x.strip()
                for x in line.replace(")", "").replace("contains", "").split("(")
            ]
            ingredients = set(x.strip() for x in ingredients.split(" "))
            allergens = [x.strip() for x in allergens.split(",")]
            for a in allergens:
                rbya[a].append(ingredients)

    def grab():
        # go through all the allergens and see if a set intersection
        # of all the food ingredients yields a single assignment
        for a, i in rbya.items():
            # print(f"{a} -> {i}")
            incommon = reduce(lambda x, y: x & y, i)
            # if the set intersection is 1 element, then it's the only one
            # it could be, so stop here, give it back adjustments can be made
            if len(incommon) == 1:
                ingredient = incommon.pop()
                print(f"{ingredient} -> {a}")
                return ingredient, a

    assignments = {}
    while rbya:
        ingredient, allergen = grab()
        # drop the found ingredient from everywhere
        for i in rbya.values():
            for j in i:
                if ingredient in j:
                    j.remove(ingredient)
        # done with that allergen; discard
        del rbya[allergen]
        assignments[ingredient] = allergen

    # in Perl, this would be a Schwartzian Transform. In Python it's just
    # an everyday lambda; how mundane
    return ",".join(sorted(assignments, key=lambda x: assignments[x]))


if __name__ == "__main__":
    print(main())
