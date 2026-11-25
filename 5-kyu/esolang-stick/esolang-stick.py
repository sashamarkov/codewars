def interpreter(tape):
    return StickMachine(tape).run()
​
class StickMachine:
    def __init__(self, tape):
        self.tape = tape
        self.stack = [0]
        self.out = []
        self.ip = 0
​
    def top(self):
        return self.stack[-1]
​
    def pop(self):
        return self.stack.pop()
​
    def push(self, value):
        self.stack.append(value)
​
    def op_pop(self):
        self.pop()
​
    def op_push_zero(self):
        self.push(0)
​
    def op_increment(self):
        self.stack[-1] = (self.stack[-1] + 1) % 256
​
    def op_decrement(self):
        self.stack[-1] = (self.stack[-1] - 1) % 256
​
    def op_output(self):
        self.out.append(chr(self.top()))
​
    def op_loop_start(self):
        if self.top() == 0:
            self.ip = self.tape.index(']', self.ip)
​
    def op_loop_end(self):
        if self.top() != 0: