#!/usr/bin/env python
''' Day 12
    
    1D-cellular automaton with a 2 cell window
'''
import sys
from itertools import count
from pathlib import Path


def load_data():
    ''' Data has a header line with the initial state,
        then a blank line,
        then the rules
    '''
    with Path(sys.argv[1]).open() as f:
        initial = f.readline().split(':')[1].strip()
        f.readline()  # blank line
        rules = {rule[0].strip(): rule[1].strip()
                 for rule in
                 [line.split('=>') for line in f]
                 }

    return initial, rules


def main():
    initial, rules = load_data()
    print(initial)
    for k, v in rules.items():
        print(k, '->', v)

    offset = 0
    for i in count(1):
        ''' empty pots are important;
            prepending or appending empty pots seemed easiest from
            a simulation standpoint
        '''
        if not all(x == '.' for x in initial[:4]):
            initial = ['.', '.', '.', '.', *initial]
            offset += -4
        if not all(x == '.' for x in initial[-4:]):
            initial.extend(['.', '.', '.', '.'])

        nextgen = ['.'] * len(initial)

        ''' step through each window

            compose the windows via:
                zip(initial, initial[1:], ... initial[4:])

            which gives, e.g. a = [1, 2, 3, 4, 5, 6]
                => [1, 2, 3, 4, 5]
                   [2, 3, 4, 5, 6]

            the entries combined can then be looked up as a rule
        '''
        for idx, c in enumerate(zip(*[initial[j:] for j in range(5)])):
            try:
                nextgen[idx+2] = rules[''.join(c)]
            except KeyError:
                nextgen[idx+2] = '.'
        initial = nextgen

        print(f"{i}:", ''.join(initial))
        print(f"{i}:", offset, sum(x == '#' for x in initial))
        print('SUM', sum(j+offset if x == '#' else 0 for j, x in enumerate(initial)))


if __name__ == "__main__":
    main()
