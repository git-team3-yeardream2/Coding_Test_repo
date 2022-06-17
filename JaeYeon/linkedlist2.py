class Node:  # Node
    def __init__(self, data, next_=None):  #  data를 입력하고, default로 next_pointer는 None을 가리킨다.
        self.data = data
        self.next = next_


class NodeMGMT:  # Linkedlist
    def __init__(self, data):
        self.header = Node(data)

    def add(self, data):  # 링크드 리스트의 가장 마지막에 새로운 노드를 추가하는 메소드
        cursor = self.header
        while cursor.next:  # curosr가 가리키는 Node의 Next가 None이면 종료 조건
            cursor = cursor.next
        cursor.next = Node(data)

    def append(self, item):  # 가장 처음 header_Node에 새로운 데이터를 추가하는 메소드
        temp = self.header  # 임시로 기존 header의 데이터 할당
        self.header = Node(item)
        self.header.next = temp # 임시에 할당해둔 데이터에 Next_pointer로 연결

    def desc(self):  # linked_list의 모든 data를 describe하는 메소드
        cursor = self.header
        while cursor:
            print(cursor.data)
            cursor = cursor.next

    def delete(self, item):
        cursor = self.header
        previous_cursor = None  # 외부 참조 변수 하나 더 추가 한다. linked_list의 근본적인 문제점은 전진 밖에 못한다는 점
        found = False
        while not found:
            if cursor.data == item:  # cursor가 보는 data와 우리가 찾는 item가 같으면
                found = True  # 찾았다.
            else:
                previous_cursor = cursor  # 이전 커서를 다음 칸으로 민다.
                cursor = cursor.next  # Cursor도 다음 칸으로 민다.
        # 이제 cursor가 찾는 item에 위치하고 있는 상태임
        if previous_cursor is None:  # 만약에 찾을 item이 head에 있다면?
            self.header = cursor.next  # 새로 헤더를 다음 Node로 지정한다.
            del cursor
        else:  # 나머지 경우
            previous_cursor.next = cursor.next  # 이전 커서의 next_pointer 위치를 찾을 item 다음 Node로 바꿔 준다.
            del cursor

    def search(self, item):
        cursor = self.header
        found = False
        while not found:
            if cursor.data is item:
                found = True
                return cursor.data
            else:
                cursor = cursor.next

liked_list = NodeMGMT(1)
for num in range(2, 10):
    liked_list.add(num)
liked_list.append(100)
liked_list.desc()
liked_list.search(100)

liked_list.delete(8)
liked_list.desc()