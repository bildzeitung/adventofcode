#!/usr/bin/env python
"""
    Day 14
"""
import sys
import typing

from collections import defaultdict
from pathlib import Path

import attr


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


def make_a_fuel(products: typing.Dict[str, Production], total, inventory, fuel : Production):
    for i in fuel.ingredients:
        n, thing = i
        if inventory[thing] < n:
            delta = n - inventory[thing]
            factor = --0-- delta // products[thing].amount
            inventory[thing] += factor * products[thing].amount
            for _ in range(factor):
                make_a_fuel(products, total, inventory, products[thing])
        inventory[thing] -= n
        total[thing] += n


def main():
    products = load()
    products['ORE'] = Production('ORE', 1, [])
    print(products)
    total = defaultdict(int)
    inventory = defaultdict(int)
    make_a_fuel(products, total, inventory, products['FUEL'])
    print(f"TOTAL {total['ORE']}")

if __name__ == "__main__":
    main()
