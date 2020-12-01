#!/usr/bin/env python
#
import sys


def main():
  """ Linear time algorithm

      Take 2020 - current item and see if it's an item we've seen.
      If so, we're done. Otherwise, store the item and keep reading data.
  """
  items = []
  with open(sys.argv[1]) as f:
    for line in f:
      i = int(line)
      complement = 2020 - i
      if complement in items:
        return i, complement, i * complement
      items.append(i)


if __name__ == "__main__":
  print(main())