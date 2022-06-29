class _stack:
    def __init__(self):
        self.stack  = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        return item

    def isEmpty(self):
        return self.stack == []

    def count(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfixeval(expr):
    operandstack = _stack()
    tokenlist = expr.split()
    nums = '0123456789'

    for token in tokenlist:
        if token in nums:
            operandstack.push(int(token))
        else:
            operator = token
            op2 = operandstack.pop()
            op1 = operandstack.pop()
            operandstack.push(doMath(operator, op1, op2))
    return int(operandstack.pop())

print(postfixeval('7 8 + 3 2 + /'))
