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


def matches(open,close):  # True & False로 반환
    opens = '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)


def generalparchecker(symbolString): # textbook
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        # 인덱스를 전부 돈다. 0부터 시작하기 때문에 부등호. unblanced 되면 while 문 종료
        # ( 가 더 많은 경우 끝까지 다 돈다. ) 가 더 많은 경우 balnced == False로 바로 종료
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isempty():  # 닫는 괄호의 수가 더 많은 경우 cut
                balanced = False
            else:
                recent = s.pop()  # 일단 대칭이던 아니던 빼고
                if not matches(recent, symbol):  # 대칭이면 balanced == True
                    balanced = False  # 대칭이 아니면 balanced == False
        index = index + 1

    if balanced and s.isempty():  # isEmpty가 False면 즉 여는 괄호가 더 많은 경우 unblanced이기 때문에 False return
        return True
    else:
        return False
# 대칭이면 문제 없이 while 다 돌아감
print(generalparchecker('((((())'))

