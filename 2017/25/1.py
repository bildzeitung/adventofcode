#!/usr/bin/env python
'''
    Day 25
'''
from collections import defaultdict


TICKS = 12208951


def write(value):
    ''' Return a function that writes a value to the tape
    '''
    def wval(machine):
        ''' Call machine to write a tape value at the current cursor position
        '''
        machine.write(value)

    return wval


def move(value):
    ''' Return a functiona that moves the cursor
    '''
    def mval(machine):
        ''' Move the cursor; 1 == right, -1 == left
        '''
        machine.move(value)

    return mval


def change_state(value):
    ''' Return a function that changes the machine state
    '''
    def sval(machine):
        ''' Alter state to new character value
        '''
        machine.state = value

    return sval


''' Ok, so getting lazy here.

    Instead of parsing the input, just use partial
    function application to create the full state table.
'''
STATES = {
    'A': {0: [write(1), move(1), change_state('B')],
          1: [write(0), move(-1), change_state('E')]},
    'B': {0: [write(1), move(-1), change_state('C')],
          1: [write(0), move(1), change_state('A')]},
    'C': {0: [write(1), move(-1), change_state('D')],
          1: [write(0), move(1), change_state('C')]},
    'D': {0: [write(1), move(-1), change_state('E')],
          1: [write(0), move(-1), change_state('F')]},
    'E': {0: [write(1), move(-1), change_state('A')],
          1: [write(1), move(-1), change_state('C')]},
    'F': {0: [write(1), move(-1), change_state('E')],
          1: [write(1), move(1), change_state('A')]}
}


class Machine(object):
    ''' Turing Machine '''

    def __init__(self):
        self.state = 'A'
        self.cursor = 0
        self.tape = defaultdict(int)

    def move(self, value):
        ''' Update cursor position '''
        self.cursor += value

    def write(self, value):
        ''' Update value at current cursor position '''
        self.tape[self.cursor] = value

    @property
    def current_cursor_value(self):
        ''' Return the value at the current cursor position '''
        return self.tape[self.cursor]


def main():
    ''' Instantiate a Turing Machine and run for specified number of operations
    '''
    machine = Machine()
    for _ in xrange(TICKS):
        for function in STATES[machine.state][machine.current_cursor_value]:
            function(machine)

    print 'CHECKSUM', sum(machine.tape.values())


if __name__ == '__main__':
    main()
