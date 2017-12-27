#!/usr/bin/env python
'''
    Day 23
'''
import sys

from collections import defaultdict


class VM(object):
    ''' A single process

        - keep register state
        - keep queue state
        - keep a reference to the *other* queue
        - track wait & termination state
        - track # of send() invocations
    '''

    def __init__(self, name, cmds):
        self.name = name
        self.cmds = cmds
        self.pc = 0
        self.registers = defaultdict(int)
        self.registers['p'] = name
        self.registers['a'] = 1
        self.terminated = False
        self.waiting = False
        self.my_queue = list()
        self.other_queue = None
        self.sent_values = 0
        self.multiplies = 0
 
    def set_receiver(self, queue):
        ''' Set the destination queue for this process
        '''
        self.other_queue = queue

    def pc_ok(self):
        ''' Return True if the program counter value is within range
        '''
        return self.pc < len(self.cmds) and self.pc > -1

    def run(self):
        ''' Execute the process

            Return control if:
                - program counter is out of range (TERMINATE)
                - process is waiting for input to its queue
        '''
        while not self.terminated and self.pc_ok():
            instr = self.cmds[self.pc][0]
            args = self.cmds[self.pc][1:]
            # print 'OP', instr, 'ARGS', args
            print ' '.join([str(x) for x in self.cmds[self.pc]])
            self.__getattribute__('_' + instr)(*args)
            self.pc += 1

            print self.registers
            if self.waiting:  # do not move on if waiting on a value
                return
        
        # ok, done
        print 'VM', self.name, 'TERMINATED; instrs:', len(self.cmds), 'pc = ', self.pc
        self.terminated = True

    def _resolve(self, arg):
        ''' Return a raw int
        
            If <arg> is an int, return it.
            Otherwise <arg> is a register, so dereference it
        '''
        if isinstance(arg, int):
            return arg

        return self.registers[arg]

    def _snd(self, x):
        ''' Append value to other process' queue
        '''
        self.other_queue.append(self._resolve(x))
        # print 'VM', self.name, 'sending a value; the other queue is:', self.other_queue
        self.sent_values += 1

    def _set(self, x, y):
        ''' Set register <x> to value <y>
        '''
        self.registers[x] = self._resolve(y)

    def _add(self, x, y):
        ''' Add value <y> to register <x>
        '''
        self.registers[x] += self._resolve(y)

    def _sub(self, x, y):
        ''' Subtract value <y> from register <x>
        '''
        self.registers[x] -= self._resolve(y)

    def _mul(self, x, y):
        ''' x = <x> * <y>
        '''
        self.registers[x] *= self._resolve(y)
        self.multiplies += 1

    def _mod(self, x, y):
        ''' x = <x> % <y>
        '''
        self.registers[x] %= self._resolve(y)

    @property
    def is_queue_empty(self):
        ''' Return True if message queue is empty
        '''
        return not len(self.my_queue)

    def _rcv(self, x):
        ''' Read a value from the message queue

            If the queue is empty, reset the program counter so that the
            instruction will be re-run; set a flag indicating that the
            process should yield

            Otherwise, set register x to the value retrieved from the queue
            and clear the flag
        '''
        if self.is_queue_empty:
            # print 'VM', self.name, 'waiting on a value'
            self.pc -= 1  # re-run this instruction
            self.waiting = True
            return
        
        self.registers[x] = self.my_queue.pop(0)
        # print 'VM', self.name, 'picking up a value; my queue is now:', self.my_queue
        self.waiting = False

    def _jgz(self, x, y):
        ''' Offset program counter by <y> iff <x> > 0
        '''
        if self._resolve(x) > 0:
            self.pc += self._resolve(y) - 1  # -1 adj for auto-increment

    def _jnz(self, x, y):
        ''' Offset program counter by <y> iff <x> != 0
        '''
        if self._resolve(x):
            self.pc += self._resolve(y) - 1


def transint(v):
    ''' a filter to quickly sort out what are numbers in the instruction set
    '''
    try:
        v = int(v)
    except ValueError:
        pass
    return v


def main():
    # load all commands; make sure everything is the correct type
    cmds = [[transint(x.strip()) for x in line.split()] for line in sys.stdin]

    vm0 = VM(0, cmds)
    vm0.run()
    print 'MULTIPLIES', vm0.multiplies


if __name__ == '__main__':
    main()
