#!/usr/bin/env python
''' Day 9

    Build a list, collecting data along the way.

    In this case, I used a list. In hindsight, not the best choice, but using
    that and manipulating indices, managed to construct the example precisely.
'''
import sys


def main():
    # load input
    max_players = int(sys.argv[1])
    max_points = int(sys.argv[2])

    ring = [0]
    idx = 0
    players = [0] * max_players  # the number of players is smallish; pre-alloc
    player_idx = 0

    def print_ring():
        strlist = [f"[{player_idx}]"]
        for k, v in enumerate(ring):
            if k == idx:
                strlist.append(f"({v})")
            else:
                strlist.append(f"{v}")
        print(' '.join(strlist))

    for i in range(1, max_points + 1):
        if not (i % 23):
            new_idx = (idx - 7) % len(ring)
            players[player_idx] += i
            players[player_idx] += ring.pop(new_idx)
            player_idx = (player_idx + 1) % max_players
            idx = new_idx
            # print_ring()
            continue

        idx = (idx + 2) % len(ring)
        if idx == 0:
            ring.append(i)  # appends are O(1)
            idx = len(ring) - 1
        else:
            ring.insert(idx, i)

        # print_ring()
        player_idx = (player_idx + 1) % max_players

    for k, v in enumerate(players):
        print(k, v)

    print('MAX', max(players))


if __name__ == "__main__":
    main()
