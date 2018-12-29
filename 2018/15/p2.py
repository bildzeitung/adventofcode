#!/usr/bin/env python
''' Day 15

    Turn-based strategy simulation
'''
import sys
from pathlib import Path
from dataclasses import dataclass


class ElfDeathException(Exception):
    pass


@dataclass
class Unit:
    kind: str
    pos: tuple
    hp: int = 200
    ap: int = 3

    @property
    def enemy_kind(self):
        return 'E' if self.kind == 'G' else 'G'

    @property
    def is_alive(self):
        return self.hp > 0


@dataclass
class Game:
    board: list
    units: list

    def show(self):
        for idx, row in enumerate(self.board):
            rc = ''.join(row)
            scores = ', '.join(f"{y.kind}({y.hp})" for y in
                               sorted([x for x in self.units
                                       if x.pos[1] == idx],
                                      key=lambda z: z.pos[0])
                               )
            print(rc + '\t' + scores)

    def unit_by_kind(self, kind):
        return [x for x in self.units if x.is_alive and x.kind == kind]

    def in_bounds(self, x, y):
        if x < 0 or x == len(self.board[0]):
            return False

        if y < 0 or y == len(self.board[1]):
            return False

        return True

    def is_in_range(self, x, y):
        return self.in_bounds(x, y) and self.board[y][x] == '.'

    def attack(self, unit):
        # find all enemy units in range
        in_range = []
        for target in self.unit_by_kind(unit.enemy_kind):
            points = ((target.pos[0], target.pos[1] - 1),
                      (target.pos[0], target.pos[1] + 1),
                      (target.pos[0] - 1, target.pos[1]),
                      (target.pos[0] + 1, target.pos[1]))
            if unit.pos in points:
                in_range.append(target)
        in_range.sort(key=lambda x: (x.hp, x.pos[1], x.pos[0]))
        target = in_range[0]
        target.hp -= unit.ap
        if not target.is_alive:
            if target.kind == 'E':
                raise ElfDeathException()
            self.board[target.pos[1]][target.pos[0]] = '.'

    def unit_turn(self, unit):
        if not unit.is_alive:
            return True

        targets = self.unit_by_kind(unit.enemy_kind)

        # check that an enemy unit exists; if not, game ends
        if not targets:
            print('GAME OVER')
            return False

        # find squares in range
        in_range = []
        for target in targets:
            points = ((target.pos[0], target.pos[1] - 1),
                      (target.pos[0], target.pos[1] + 1),
                      (target.pos[0] - 1, target.pos[1]),
                      (target.pos[0] + 1, target.pos[1]))
            for pos in points:
                if unit.pos == pos or self.is_in_range(*pos):
                    in_range.append(pos)
                    # self.board[pos[1]][pos[0]] = '?'

        if not in_range:
            # print('Unit', unit.pos, 'HAS NOTHING IN RANGE')
            return True
        # print('IN RANGE', in_range)
        # self.show()

        if unit.pos in in_range:
            self.attack(unit)
            return True

        # find nearest target
        # BFS search
        oset = [(unit.pos, 0, None)]
        seen = []
        reachable = []
        cset = set()
        found_dist = 1_000_000_000
        while oset:
            target, dist, parent = oset.pop(0)

            if dist > found_dist:
                continue

            if target in in_range:
                reachable.append((target, dist, parent))
                found_dist = dist

            cset.add((target, dist, parent))

            if target in seen:
                continue
            seen.append(target)

            if target != unit.pos and self.board[target[1]][target[0]] not in ('.', '?'):
                continue

            # add directions
            points = ((target[0], target[1] - 1),
                      (target[0], target[1] + 1),
                      (target[0] - 1, target[1]),
                      (target[0] + 1, target[1]))
            for pos in points:
                if not self.in_bounds(*pos):
                    continue

                oset.append((pos, dist + 1, target))

        # print('REACHABLE', reachable)
        # for r, v, p in reachable:
        #     self.board[r[1]][r[0]] = '@'
        # self.show()
        if not reachable:
            # there are targets, but the unit cannot get to them
            return True

        # choose nearest target
        min_dist = min(x[1] for x in reachable)
        min_reachable = sorted([x[0] for x in reachable if x[1] == min_dist],
                               key=lambda x: (x[1], x[0]))
        # print('NEAREST', min_reachable)
        # for r in min_reachable:
        #     self.board[r[1]][r[0]] = '!'

        chosen = min_reachable[0]
        # self.board[chosen[1]][chosen[0]] = '+'
        # self.show()

        # print('CLOSED', cset)

        # get move direction
        parents = [x for x in cset if x[0] == chosen and x[1] == min_dist]
        while min_dist > 1:
            min_dist -= 1
            new_parents = []
            for _, _, p in parents:
                new_parents.extend(x for x in cset
                                   if x[0] == p and x[1] == min_dist)
            parents = new_parents
        move_to = sorted(set(x[0] for x in parents),
                         key=lambda x: (x[1], x[0]))[0]
        # print('MOVE TO', move_to)
        self.board[unit.pos[1]][unit.pos[0]] = '.'
        self.board[move_to[1]][move_to[0]] = unit.kind
        unit.pos = move_to

        if unit.pos in in_range:
            self.attack(unit)

        # turn complete
        return True

    def turn(self):
        not_done = True
        for unit in sorted(self.units, key=lambda x: (x.pos[1], x.pos[0])):
            if not self.unit_turn(unit):
                not_done = False
                break

        dead = [x for x in self.units if not x.is_alive]
        for died in dead:
            self.units.remove(died)

        return not_done


def load_map(elf_ap):
    ''' Load into 2D array
    '''
    with Path(sys.argv[1]).open() as f:
        board = [[y for y in x] for x in [line.strip() for line in f]]

    units = []
    for y, row in enumerate(board):
        for x, item in enumerate(row):
            if item == 'G':
                units.append(Unit(item, (x, y)))
            if item == 'E':
                units.append(Unit(item, (x, y), ap=elf_ap))

    return Game(board, units)


def main():
    ap = 3  # initial Attack Points
    while True:
        try:
            ap += 1
            game = load_map(elf_ap=ap)
            print('INITIAL')
            game.show()
            rounds = 0
            while game.turn():
                rounds += 1
                print('AFTER', rounds)
                game.show()
            print('ROUNDS', rounds)
            all_hp = sum(x.hp for x in game.units)
            print('HP REMAINING:', all_hp)
            print('SCORE:', rounds * all_hp)
            print('FINAL BOARD')
            game.show()
            break
        except ElfDeathException:
            print('ELF died; re-running with higher AP')
    print('DONE; FINAL AP', ap)


if __name__ == "__main__":
    main()
