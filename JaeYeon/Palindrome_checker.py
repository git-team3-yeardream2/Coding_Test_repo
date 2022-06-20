class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)  # insert(idx, element)

    def addRear(self, item):
        self.items.append(item)  # append 는 가장 처음에 들어감

    def removeFront(self):
        self.items.pop(0)  # 0번째 인덱스, 즉 front를 pop

    def removeRear(self):
        self.items.pop()  # -1번째 인덱스, 즉 Rear을 pop

    def isEmpty(self):
        return self.items == []
        # if len(self.items) == 0:
        #     return True
        # else:
        #     False

    def size(self):
        return len(self.items)


def palindrome_checker(string):
    temp = Deque()
    for char in string:
        temp.addFront(char)  # 각 문자를 Deque에 넣는다.

    while temp.size > 1:
        if temp.items[0] == temp.items[-1]:
            temp.removeFront()
            temp.removeRear()
        else:
            return False

    if temp.size <= 1:
        return True


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillequal = True  # boolean형 하나 설정 해놓기

    while chardeque.size() > 1 and stillequal:  # 종료 조건 먼저 설정하기
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual








