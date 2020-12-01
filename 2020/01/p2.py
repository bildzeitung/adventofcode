#!/usr/bin/env python
#
import sys
import math


def main():
  """ Dynamic programming sol'n

      We're looking for x_i + x_j + x_k = 2020

      where x is the problem input and i != j != k

      All combinations of (x_i + x_j) need to be unique, otherwise the sol'n
      is non-unique.

      Build up a dictionary of:
        2000 - x_i - x_j ==> x_j

      For each new input item m, we can check to see if m is a key in the
      dictionary. If it is, then we have x_j, and m = x_k, and can calculate x_i.

      Otherwise, 
        - step through all x and add the partial calculations.
        - add m to set x.

      At each step, we can make an O(1) decision on whether m solves the
      problem, and O(n) steps for the additional partial calc's. I think this
      gives us an O(n^2) solution, which ought to be cheaper than C(n, 3).
  """
  items = {}
  with open(sys.argv[1]) as f:
    a = int(next(f))
    b = int(next(f))
    items =  { 2020 - a - b: b}
    pool = [a, b]
    for line in f:
      c = int(line)
      if c in items:
        print(f"Number of items: {len(pool)}")
        print(f"Partials: {len(items)}")
        result = (c, items[c], 2020 - c - items[c])
        return result, math.prod(result)

      for i in pool:
        items[2020 - i - c] = c

      pool.append(c)


if __name__ == "__main__":
  print(main())
