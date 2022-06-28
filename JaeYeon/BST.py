import numpy


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        self.pointer = self.root
        while True:
            if self.pointer.data > data:
                if self.pointer.left is not None:
                    self.pointer = self.pointer.left
                else:
                    self.pointer.left = Node(data)
                    break
            else:
                if self.pointer.right is not None:
                    self.pointer = self.pointer.right
                else:
                    self.pointer.right = Node(data)
                    break

    def search(self, data):
        self.pointer = self.root
        while self.pointer:
            if self.pointer.data == data:
                return True
                break
            elif self.pointer.data < data:
                self.pointer = self.pointer.right
            else:
                self.pointer = self.pointer.left
        return False

    def delete(self, data):
        searched = False
        self.pointer = self.root
        self.parent = None  # 저는 부모 노드 None으로 시작
        while self.pointer:
            if self.pointer.data == data:
                searched = True
                break  # 반복문 while문 break
            elif self.pointer.data < data:
                self.parent = self.pointer  # pointer을 내려가는 과정, 부모 먼저 내려가야함.
                self.pointer = self.pointer.right
            else:
                self.parent = self.pointer  # pointer을 내려가는 과정, 부모 먼저 내려가야함.
                self.pointer = self.pointer.left

        if searched == False:
            return False  # why return??? 나중에 쓰려 그리고 함수 여기까지 멈추는게 효율적이다.

        if self.pointer.left == None and self.pointer.right == None:  # 자식이 없는 경우, 즉 삭제할 Node가 leaf일 때
            if data < self.parent.data:  # 부모의 데이터 보다 작은 경우 즉 삭제할 노드가 부모의 왼쪽 자식인 경우?
                self.parent.left = None  # None으로 만들어 주면 끝
            else:
                self.parent.right = None
            del self.pointer  # 객체 메모리 상에서 삭제

        elif self.pointer.left != None and self.pointer.right == None:  # 왼쪽 자식만 있는 경우
            if data < self.parent.data:  # 부모의 데이터 보다 작은 경우
                self.parent.left = self.pointer.left
            else:  # 부모의 데이터 보다 큰 경우, 즉 삭제할 노드가 부모의 오른쪽 자식인 경우
                self.parent.right = self.pointer.left # case B
        elif self.pointer.left == None and self.pointer.right != None:  # 오른쪽 자식만 있는 경우
            if data < self.parent.data:
                self.parent.left = self.pointer.right  # case A
            else:
                self.parent.right = self.pointer.right
        elif self.pointer.left != None and self.pointer.right != None:  # 삭제할 Node가 자식이 둘 다 있는 경우
            if data < self.parent.data:  # 삭제할 Node가 부모의 데이터 보다 작은 경우, 삭제할 Node의 오른쪽 자식 중 가장 작은 값(가장 왼쪽)을 부모 Node의 left에
                self.changenode = self.pointer.right  # 시작점이 삭제할 노드의 오른쪽 자식
                self.changenode_parent = self.pointer
                while self.changenode.left is not None:  # 오른쪽 자식들 중에서 찾는데, 이 중 가장 작은 값을 찾아야한다. 삭제할 Node의 부모의 왼쪽에 연결 해줘야 한다.
                    self.changenode_parent = self.changenode
                    self.changenode = self.changenode.left
                if self.changenode.right is not None:  # 가장 작은 값 후보에 근접했다. 만약에 왼쪽에 자식이 없어도, 오른쪽에 있는 경우라면 이 노드가 가장 작은 값이다.
                    self.changenode.parent.left = self.changenode.right  # 이 노드의 부모의 왼쪽 자식에 이 노드의 자식을 추가한다. (case A와 유사)
                else: # 가장 작은 값이 자식이 없는 경우
                    self.changenode.parent.left = None  # 이 노드의 부모의 왼쪽 자식이 없어지고 끝
                self.parent.left = self.changenode  # 위로 옮기는 과정 3줄
                self.changenode.right = self.pointer.right
                self.changenode.left = self.pointer.left

            else:  # 삭제할 Node가 부모의 데이터 보다 큰 경우, 삭제할 Node의 왼쪽 자식 중 가장 작은 큰(가장 오른쪽)을 부모 Node의 right에
                self.changenode = self.pointer.left  # 시작점이 삭제할 노드의 왼쪽 자식
                self.changenode_parent = self.pointer
                while self.changenode.right is not None:  # 왼쪽 자식들 중에서 찾는데, 이 중 가장 큰 값을 찾아야한다. 삭제할 Node의 부모의 오른쪽에 연결 해줘야 한다.
                    self.changenode_parent = self.changenode
                    self.changenode = self.changenode.right
                if self.changenode.left is not None:  # 가장 작은 값 후보에 근접했다. 만약에 오른쪽에 자식이 없어도, 왼쪽에 있는 경우라면 이 노드가 가장 작은 값이다.
                    self.changenode.parent.right = self.changenode.left  # 이 노드의 부모의 오른쪽 자식에 이 노드의 자식을 추가한다. (case B와 유사)
                else: # 가장 작은 값이 자식이 없는 경우
                    self.changenode.parent.right = None  # 이 노드의 부모의 오른쪽 자식이 없어지고 끝
                self.parent.right = self.changenode  # 위로 옮기는 과정 3줄
                self.changenode.right = self.pointer.right
                self.changenode.left = self.pointer.left
        return True


bst_nums = set()  # 임의로 추가할 숫자 100개 선택
for x in numpy.random.randint(999, size=100):
    bst_nums.add(x)
print(bst_nums)

test = BST(500)
for num in bst_nums:
    test.insert(num)

for num in bst_nums:  # 검색 기능 확인
    if test.search(num) is False:
        print('search failed', num)

del_num = set()  # 임의의 삭제할 숫자 10개 선택

for idx in numpy.random.randint(len(bst_nums), size=10):  # 총 인덱스 len(bst_nums), 아까 무작위 추출한 집합의 길이에서 10개 뽑는다.
    del_num.add(list(bst_nums)[idx])
print(del_num)

for num in del_num:
    if test.delete(num) is False:
        print('delete failed', num)  # 랜덤으로 트리에서 10개 뽑아서 삭제

print(del_num.intersection(bst_nums))  # 전부 삭제 된거 확인.
print(test.search(500))  # 루트 노드인 500 존재함 확인.
