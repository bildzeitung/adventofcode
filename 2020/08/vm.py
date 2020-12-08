"""
  AoC 2020 VM

  - single register
  - 3 instructions
  - terminate if program counter moves past code
"""


class VM:
    """ VM

        Only fancy part is that this conforms to an iterable, and
        a next() call will step the VM
    """

    def __init__(self, code):
        self.code = code
        self.pc = 0
        self.methods = {"acc": self.acc, "jmp": self.jmp, "nop": self.nop}
        self.accumulator = 0

    def acc(self, arg):
        self.accumulator += arg
        self.pc += 1

    def jmp(self, arg):
        self.pc += arg

    def nop(self, _):
        self.pc += 1

    def step(self):
        instr, arg = self.code[self.pc]
        self.methods[instr](arg)

    def __iter__(self):
        return self

    def __next__(self):
        if self.pc >= len(self.code):
            raise StopIteration()
        self.step()
        return self.accumulator
