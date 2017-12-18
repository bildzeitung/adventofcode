#!/usr/bin/env python
'''
    Day 18
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
        self.terminated = False
        self.waiting = False
        self.my_queue = list()
        self.other_queue = None
        self.sent_values = 0
 
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
            # print 'OP', op, 'ARGS', args
            self.__getattribute__('_' + instr)(*args)
            self.pc += 1

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

    def _mul(self, x, y):
        ''' x = <x> * <y>
        '''
        self.registers[x] *= self._resolve(y)

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

    # setup 2x VMs
    vm0 = VM(0, cmds)
    vm1 = VM(1, cmds)

    vm0.set_receiver(vm1.my_queue)
    vm1.set_receiver(vm0.my_queue)

    # run until some sort of termination condition is met
    while True:
        vm0.run()
        vm1.run()

        if vm0.waiting and vm1.waiting:
            # just because both are waiting doesn't mean that both are
            # deadlocked; it could be that just the wrong one is running,
            # so double-check the queues
            if vm0.is_queue_empty and vm1.is_queue_empty:
                print 'DEADLOCK'
                break

        if vm0.terminated and vm1.terminated:
            print 'ALL DONE'
            break

        if vm0.terminated and vm1.waiting:
            print 'POSSIBLY ABNORMAL'
            if vm1.is_queue_empty:
                break

        if vm1.terminated and vm0.waiting:
            print 'POSSIBLY ABNORMAL'
            if vm0.is_queue_empty:
                break

    # print 'VM0 registers', vm0.registers
    # print 'VM1 registers', vm1.registers
    print 'PROGRAM 1 SENT', vm1.sent_values, 'VALUES'


if __name__ == '__main__':
    main()
