#!/usr/bin/env python
""" Day 22 """

from copy import copy

BOSS = {}
with open('boss.in') as infile:
    for line in infile:
        key, val = [x.strip() for x in line.split(':')]
        BOSS[key] = int(val)

print 'BOSS: %s' % BOSS

PLAYER = {'Hit Points': 50, 'Mana': 500, 'Armour': 0}

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
    """ Do a game turn """
    new_effects = []
    boss = copy(state['boss'])
    player = copy(state['player'])

    # HARD MODE
    player['Hit Points'] -= 1
    if player['Hit Points'] < 1:
        return

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
            # cannot cast this spell
            return

    player['Mana'] -= spell['cost']
    player['Armour'] += spell['armour']
    if player['Mana'] < 0:
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

    if boss['Hit Points'] < 1:
        return state['total'] + spell['cost']

    player['Hit Points'] -= max(boss['Damage'] - player['Armour'], 1)

    if player['Hit Points'] < 1:
        return

    return {'total': state['total'] + spell['cost'],
            'player': player,
            'boss': boss,
            'effects': newer_effects,
           }

STATES = [GAME]
RESULTS = []
while STATES:
    STATS = len(RESULTS)

    STATE = STATES.pop(0)
    NEXT_TURN = [turn(STATE, x) for x in SPELLS.values()]
    RESULTS.extend([x for x in NEXT_TURN if isinstance(x, int)])
    STATES.extend([x for x in NEXT_TURN if isinstance(x, dict)])

    if len(RESULTS) != STATS:
        print 'First result set: %s' % sorted(RESULTS)
        break
