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
