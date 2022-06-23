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


def devideby2(decimal):
    binary = _stack()
    while decimal > 0:  # The Divide by 2 algorithm assumes that we start with an integer greater than 0
        resi = decimal % 2
        binary.push(str(resi))
        decimal = decimal//2

    answer = ''
    for idx in range(binary.count()):
        answer = answer + binary.pop()

    return int(answer)


print(devideby2(4))
