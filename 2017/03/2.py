#!/usr/bin/python
'''
  Day 3
'''
import math
import sys

# start by travelling right; left turns only
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def sum_around(grid, x, y):
  s = 0
  for xx in range(x-1, x+2):
    if (xx < 0) or (xx >= len(grid)):
      continue

    for yy in range(y-1, y+2):
      if (yy < 0) or (yy >= len(grid)):
        continue

      s += grid[yy][xx]

  return s


def move(grid, x, y, i, r, t):
  ok = False
  while not ok:
    nx = x + dirs[i][0] 
    ny = y + dirs[i][1]
    # print x, '->', nx, y, '->', ny

    if t == 0:  # need to switch directions
      i = (i + 1) % len(dirs)
      t = r
      continue

    # out of bounds; switch directions
    if (nx < 0) or (nx >= len(grid)):
      i = (i + 1) % len(dirs)
      continue

    # out of bounds; switch directions
    if (ny < 0) or (ny >= len(grid)):
      i = (i + 1) % len(dirs)
      continue

    # changed directions, but colliding with existing
    # so: - reset direction
    #     - increase radius
    #     - increase travel by one more (for the next spiral)
    if grid[ny][nx] != 0:
      r += 1
      t = 1
      i = (i - 1) % len(dirs)
      continue

    # all ok!
    break

  return nx, ny, i, r, t - 1


def main():
  n = int(sys.argv[1])
  sn = int(math.ceil(math.sqrt(n)))
  grid = [[0 for _ in range(sn)] for _ in range(sn)]

  x, y = sn/2, sn/2
  didx = 0
  last = 0
  grid[y][x] = 1
  radius = 1
  to_travel = 1
  while (last <= n):
    x, y, didx, radius, to_travel = move(grid, x, y, didx, radius, to_travel)
    grid[y][x] = sum_around(grid, x, y)

    last = grid[y][x]

    # for l in grid:
    #   print ' '.join([str(m) for m in l])
    # print

  print 'NEXT: ', last


if __name__ == "__main__":
  main()
