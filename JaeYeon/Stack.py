class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def show(self):
        print(self.stack)

    def count(self):
        return len(self.stack)


stk = Stack()
for num in range(10):
    stk.push(num)

stk.show()
print(stk.pop())
stk.show()
print(stk.count())


class _Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.item.pop()
        # item = self.stack[-1]
        # del self.stack[-1]
        # return item

    def peek(self):
        return self.stack[-1]
        # retrun self.stack[len(self.stack)-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


class Reversed_stack:
    def __init__(self):
        self.stack = []

    def push(self, item):  # 리스트의 beginning을 top으로 본다.
        self.stack.insert(0, item)

    def pop(self):
        item = self.stack[0]
        del self.stack[0]
        return item
        # return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)
