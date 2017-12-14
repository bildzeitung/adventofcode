#!/usr/bin/env python
""" Day 21 """

from itertools import combinations
from math import ceil


with open('weapons.in') as f:
    WEAPONS = [[int(x) for x in line.rstrip().split(',')[1:]] for line in f]

with open('armour.in') as f:
    ARMOUR = [[int(x) for x in line.rstrip().split(',')[1:]] for line in f]

with open('rings.in') as f:
    RINGS = [[int(x) for x in line.rstrip().split(',')[1:]] for line in f]

STATS = {}
with open('boss.in') as f:
    for line in f:
        stat, value = [x.strip() for x in line.split(':')]
        STATS[stat] = int(value)

def configurations():
    """ Generate hero inventory """
    # select one weapon
    for weapon in WEAPONS:
        # select one armour (including no armour)
        for armour in ARMOUR:
            # select two rings (including no rings)
            for rings in combinations(RINGS, 2):
                config = [weapon, armour]
                config.extend(rings)
                yield config

def get_winners():
    """ Go through all configurations and return a cost """
    for config in configurations():
        cost = sum(x[0] for x in config)
        attack = sum(x[1] for x in config)
        defense = sum(x[2] for x in config)

        net_attack = max(1, attack - STATS['Armor'])
        boss_attack = max(1, STATS['Damage'] - defense)

        turns_to_kill = ceil(STATS['Hit Points'] / float(net_attack))
        turns_to_live = ceil(100 / float(boss_attack))

        if turns_to_live < turns_to_kill:
            continue

        print 'cost: %s a: %s (%s) def: %s (%s)' % (cost, net_attack, attack, defense, boss_attack)
        print 'TTK: %s TTL: %s' % (turns_to_kill, turns_to_live)
        yield cost

print 'Lowest cost: %s' % min(get_winners())
