class Program:
    OPS = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: b - a,
        'mul': lambda a, b: a * b,
        'div': lambda a, b: b // a,
    }
​
    def __init__(self, stack):
        self.stack = stack
​
    def __call__(self, token):
        if token == 'end':
            return self.stack[-1]
        if token == 'push':
            return PushState(self.stack)
        if token in self.OPS:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(self.OPS[token](a, b))
            return Program(self.stack)
        raise ValueError(f"Unknown token: {token}")
​
​
class PushState:
    def __init__(self, stack):
        self.stack = stack
​
    def __call__(self, value):
        self.stack.append(value)
        return Program(self.stack)
​
​
def start():
    return Program([])
​
​
start = start()
end = 'end'
push = 'push'
add = 'add'
sub = 'sub'
mul = 'mul'
div = 'div'