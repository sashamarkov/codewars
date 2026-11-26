def solve(s):
    stack = [1]
    op = 1
    result = []
    for ch in s:
        if ch == '+':
            op = 1
        elif ch == '-':
            op = -1
        elif ch == '(':
            stack.append(stack[-1] * op)
            op = 1
        elif ch == ')':
            stack.pop()
        else:
            sign = stack[-1] * op
            p = '' if not result else '+'
            result.append(('-' if sign < 0 else p) + ch)
            op = 1
    return ''.join(result)