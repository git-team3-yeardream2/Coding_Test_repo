class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[-1]
        self.stack.pop()
        return item

    def isempty(self):
        return self.stack == []


def parchecker(symbol_strings):
    stack_list = Stack()

    for char in symbol_strings:
        if char == '(':
            stack_list.push(0)
        elif char == ')':
            if stack_list.isempty():
                stack_list.push(0)
            else:
                stack_list.pop()
        else:
            continue

    return stack_list.isempty()

print(parchecker('(()()())'))


def parChecker(symbolString): # textbook
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        # 인덱스를 전부 돈다. 0부터 시작하기 때문에 부등호. unblanced 되면 while 문 종료
        # ( 가 더 많은 경우 끝까지 다 돈다. ) 가 더 많은 경우 balnced == False로 바로 종료
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isempty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isempty():  # isEmpty가 False면 즉 ( 가 더 많은 경우 unblanced이기 때문에 False return
        return True
    else:
        return False

print(parChecker('()()()'))