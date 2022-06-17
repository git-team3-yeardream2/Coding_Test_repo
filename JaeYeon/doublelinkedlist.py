class Node:
    def __init__(self, data, prev=None, next_=None):
        self.data = data
        self.prev = prev
        self.next = next_


class NodeMGMT:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = Node(data)

    def insert(self, item):  # head 부터 찾아서 tail에 새로운 Node 삽입.
        current = self.head
        while current.next:
            current = current.next
        new = Node(item)
        current.next = new
        new.prev = current
        self.tail = new

    def desc(self):  # head to tail 모든 Node의 데이터 출력
        current = self.head
        while current:  # 여기 실수하기 좋음.
            print(current.data)
            current = current.next

    def front_insert(self, item):  # head에 새로운 Node 삽입.
        new = Node(item)
        new.next = self.head
        self.head.prev = new
        self.head = new

    def reverse_desc(self):  # tail to head 모든 Node의 데이터 출력
        tail = self.tail
        while tail.prev:
            print(tail.get_data())
            tail = tail.prev

    def append(self, item, target):  # target 바로 앞에 item Node를 넣는 메소드
        current = self.tail
        previous = self.tail.prev
        found = False
        while not found:
            if current.data is not target:
                current = current.prev
                previous = current.prev
            else:
                new = Node(item)
                previous.next = new
                new.prev = previous
                current.prev = new
                new.next = current
                found = True
        if previous is None:  # 찾는 숫자가 head일 경우
            new = Node(item)
            current.prev = new  # 기존 head의 prev_pointer을 새로운 Node로
            new.next = current  # 새로운 Node의 Next_pointer을 기존의 head로
            self.head = new  # 링크드리스트의 헤드를 새로 추가한 Node로

    def append2(self, item, target):
        current = self.head
        nextn = current.next
        found = False
        while not found:
            if current.data is not target:
                current = current.next
                nextn = nextn.next
            else:
                new = Node(item)
                current.next = new
                new.prev = current
                nextn.prev = new
                new.next = nextn
                found = True
        if nextn is None:  # current가 tail인 경우
            new = Node(item)
            current.next = new
            new.prev = current
            self.tail = new


double_linked_list = NodeMGMT(0)
for num in range(1, 10):
    double_linked_list.insert(num)
double_linked_list.append(555, 3)
double_linked_list.append2(777, 3)
double_linked_list.desc()