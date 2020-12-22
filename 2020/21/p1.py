#!/usr/bin/env python
"""
  Day 21
"""
import sys
from collections import defaultdict
from functools import reduce


def main():
    rbya = defaultdict(list)
    all_ingredients = defaultdict(int)
    with open(sys.argv[1]) as f:
        for line in f:
            ingredients, allergens = [
                x.strip()
                for x in line.replace(")", "").replace("contains", "").split("(")
            ]
            ingredients = set(x.strip() for x in ingredients.split(" "))
            allergens = [x.strip() for x in allergens.split(",")]
            for a in allergens:
                rbya[a].append(ingredients)
            for x in ingredients:
                all_ingredients[x] += 1

    def grab():
        for a, i in rbya.items():
            # print(f"{a} -> {i}")
            incommon = reduce(lambda x, y: x & y, i)
            if len(incommon) == 1:
                ingredient = incommon.pop()
                print(f"{ingredient} -> {a}")
                return ingredient, a

    assignments = {}
    while rbya:
        ingredient, allergen = grab()
        for i in rbya.values():
            for j in i:
                if ingredient in j:
                    j.remove(ingredient)
        del rbya[allergen]
        assignments[ingredient] = allergen

    # grab the sum from the master count, cause of dupes
    return sum(v for i, v in all_ingredients.items() if i not in assignments)


if __name__ == "__main__":
    print(main())
