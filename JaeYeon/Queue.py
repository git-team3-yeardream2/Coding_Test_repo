class Q:  # 리스트는 가장 앞에 요소가 나중에 가장 나중에 들어온 요소인 것을 활용함.
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return 'No data'
        else:
            self.item = self.queue[0]
            del self.queue[0]

    def item(self):
        return self.item

    def size(self):
        return len(self.queue)

exq = Q()
for num in range(0,12):
    exq.enqueue(num)
    print(exq.queue)
for num in range(5):
    exq.dequeue()
    print(exq.item)
    print(exq.queue)
exq.enqueue(999)
print(exq.queue)
exq.dequeue()
print(exq.item)
print(exq.queue)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

