#!/usr/bin/env python
""" Day 22 """

from copy import copy
from Queue import PriorityQueue

BOSS = {}
with open('boss.in') as infile:
    for line in infile:
        key, val = [x.strip() for x in line.split(':')]
        BOSS[key] = int(val)

print 'BOSS: %s' % BOSS

PLAYER = {'Hit Points': 50, 'Mana': 500, 'Armour': 0}
CURRENT_BEST = float('inf')

"""
Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect for 6 turns. While active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect for 6 turns. At the start of each turn while it is
    active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect for 5 turns. At the start of each turn while it is
    active, it gives you 101 new mana.
"""

SPELLS = {'Magic Missle': {'cost': 53, 'damage': 4, 'heals': 0, 'armour': 0, 'timer': 1, 'mana': 0},
          'Drain': {'cost': 73, 'damage': 2, 'heals': 2, 'armour': 0, 'timer': 1, 'mana': 0},
          'Shield': {'cost': 113, 'damage': 0, 'heals': 0, 'armour': 7, 'timer': 6, 'mana': 0},
          'Poison': {'cost': 173, 'damage': 3, 'heals': 0, 'timer': 6, 'armour': 0, 'mana': 0},
          'Recharge': {'cost': 229, 'damage': 0, 'heals': 0, 'mana': 101, 'timer': 5, 'armour': 0}
         }

GAME = {'player': PLAYER, 'boss': BOSS, 'effects':[], 'total': 0}

def turn(state, spell):
    """ Do a game turn 

        Returns:
            None - loss or invalid state
            int - a player win; returns the mana cost
            dict - a game state; undecided outcome
    """
    new_effects = []
    boss = copy(state['boss'])
    player = copy(state['player'])

    # apply effects
    for effect in state['effects']:
        if not effect['timer']:
            player['Armour'] -= effect['armour']
            continue

        boss['Hit Points'] -= effect['damage']
        player['Hit Points'] += effect['heals']
        player['Mana'] += effect['mana']

        new_effects.append(copy(effect))
        new_effects[-1]['timer'] -= 1

    if boss['Hit Points'] < 1:
        return state['total']

    # cast something
    for effect in new_effects:
        if effect['timer'] and (spell['cost'] == effect['cost']):
            # cannot cast this spell (it's already active)
            return

    player['Mana'] -= spell['cost']
    player['Armour'] += spell['armour']

    # cannot cast this spell (not enough mana available)
    if player['Mana'] < 0:
        return

    # ok, spell is cast
    new_total = state['total'] + spell['cost']

    # prune branch if this is now more expensive than the best solution so far
    # (as it's already worse)
    if new_total > CURRENT_BEST:
        return

    new_effects.append(spell)

    # boss turn
    newer_effects = []
    for effect in new_effects:
        if not effect['timer']:
            player['Armour'] -= effect['armour']
            continue

        boss['Hit Points'] -= effect['damage']
        player['Hit Points'] += effect['heals']
        player['Mana'] += effect['mana']

        newer_effects.append(copy(effect))
        newer_effects[-1]['timer'] -= 1

    # check after effects
    if boss['Hit Points'] < 1:
        return new_total

    # boss attack
    player['Hit Points'] -= max(boss['Damage'] - player['Armour'], 1)

    # killing blow by boss?
    if player['Hit Points'] < 1:
        return

    # game isn't over; return game state
    return {'total': new_total,
            'player': player,
            'boss': boss,
            'effects': newer_effects,
           }

# breadth-first search
STATES = PriorityQueue()
STATES.put((0, GAME))
while not STATES.empty():
    _, STATE = STATES.get()

    for spell in SPELLS.values():
        result = turn(STATE, spell)

        if isinstance(result, dict):
            STATES.put((-result['total'], result))  # order by highest cost
        elif result:
            CURRENT_BEST = min(CURRENT_BEST, result)

print 'Final: %s' % CURRENT_BEST
