#!/usr/bin/env python
''' Day 9
'''
from collections import deque
import sys


def main():
    # load input
    max_players = int(sys.argv[1])
    max_points = int(sys.argv[2])

    ring = deque([0])
    players = [0] * max_players
    player_idx = 0

    ''' lists in python are O(n) for pop(), when it's not the end item.
        This makes part 2 too slow without a different data structure.

        Deque's are a double-linked list, sort of, so they're O(1) for
        insertion and deletion, so long as you can pick an end.

        I choose the 0th element as the one to insert in front of, and
        to remove.
    '''
    for i in range(1, max_points + 1):
        if not (i % 23):
            ring.rotate(7)  # move the 7th last element to the front
            players[player_idx] += i
            players[player_idx] += ring.popleft()
            player_idx = (player_idx + 1) % max_players
            continue

        ring.rotate(-2)  # move the 3rd element to the front
        ring.appendleft(i)

        player_idx = (player_idx + 1) % max_players

    print('MAX', max(players))


if __name__ == "__main__":
    main()
