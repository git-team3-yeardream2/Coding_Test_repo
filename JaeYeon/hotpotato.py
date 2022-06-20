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

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

names = ["Bill","David","Susan","Jane","Kent","Brad"]

alpha = Queue()
for name in names:
    alpha.enqueue(name)  # Bill이 1빠
print(alpha.items)

for i in range(7):
    alpha.enqueue(alpha.dequeue())
    print(alpha.items)

alpha.dequeue()
print(alpha.items)

for i in range(7):
    alpha.enqueue(alpha.dequeue())
    print(alpha.items)

alpha.dequeue()
print(alpha.items)

for i in range(7):
    alpha.enqueue(alpha.dequeue())
    print(alpha.items)

alpha.dequeue()
print(alpha.items)

for i in range(7):
    alpha.enqueue(alpha.dequeue())
    print(alpha.items)

alpha.dequeue()
print(alpha.items)

for i in range(7):
    alpha.enqueue(alpha.dequeue())
    print(alpha.items)

alpha.dequeue()
print(alpha.items)