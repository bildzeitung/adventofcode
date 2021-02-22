#!/usr/bin/env python
"""
    Day 14
"""
import sys
import typing

from collections import defaultdict
from copy import copy
from pathlib import Path

import attr

MAX_FUEL = 1_000_000_000_000  # 1 trillion


@attr.s(auto_attribs=True)
class Production:
    name : str
    amount : int
    ingredients: typing.List[tuple]  # [ (n, thing), ... ]


def load():
    product_map = {}
    with Path(sys.argv[1]).open() as f:
        for l in f:
            ingredient_line, produces = [x.strip() for x in l.split("=>")]

            amount, product = int(produces.split(" ")[0]), produces.split(" ")[1]
            ingredients = []
            for item in [x.strip() for x in ingredient_line.split(",")]:
                iamt, thing = int(item.split(" ")[0]), item.split(" ")[1]
                ingredients.append((iamt, thing))
            product_map[product] = Production(product, amount, ingredients)
    return product_map


def make_a_fuel(products: typing.Dict[str, Production], total, inventory, external_multiplier, fuel : Production):
    for i in fuel.ingredients:
        n, thing = i
        n *= external_multiplier
        if inventory[thing] < n:
            delta = n - inventory[thing]
            # stupid Python trick to get a ceil() for the division
            factor = --0-- delta // products[thing].amount
            inventory[thing] += factor * products[thing].amount
            make_a_fuel(products, total, inventory, factor, products[thing])
        inventory[thing] -= n
        total[thing] += n


def main():
    products = load()
    products['ORE'] = Production('ORE', 1, [])
    print(products)
    total = defaultdict(int)
    inventory = defaultdict(int)
    fuel = 0
    #
    # brute force: just keep calc'ing until it's done
    #
    while total["ORE"] < MAX_FUEL:
        make_a_fuel(products, total, inventory, 1, products['FUEL'])
        fuel += 1
    print(f"INVENTORY {inventory}")
    print(f"TOTAL {total}")
    print(f"FUEL {fuel - 1}")


if __name__ == "__main__":
    main()
