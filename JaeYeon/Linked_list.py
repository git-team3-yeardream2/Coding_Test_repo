class Node:
    def __init__(self,initdata):
        self.data = initdata  # node's data
        self.next = None  # Next-pointer

    def getData(self):  # 데이터를 얻는 메소드
        return self.data

    def getNext(self):  # Next-pointer가 가리키는 데이터 즉 다음 데이터를 반환하는 메소드
        return self.next

    def setData(self,newdata):  # 다음 새로운 data를 설정하는 메소드
        self.data = newdata

    def setNext(self,newnext):  # 다음 새로운 data의 Next-pointer가 가리키는 데이터를 설정하는 메소드
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None  # head를 왜 쓰냐 이유를 생각하면서!

    def isEmpty(self):
        return self.head is None

    def add(self, item):  # add의 이해가 중요함. self.next가 결정된다. 데이터를 넣고 Node를 조작하는 논리
        temp = Node(item) # 데이터 value (여기서는 argument item에 입력하는 값)이 들어가고 Next-pointer은 None을 가리키는 상태
        temp.setNext(self.head)  # step1 기존의 head가 참조하는 데이터(old first node 가장 앞의 data)를 Next-pointer가 가리키도록 함
        self.head = temp  # step2 이번에 추가한 data를 새로운 head로 설정한다. #step 순서 지키는거 매우 중요함!!!

    def size(self):  # traversal Node의 메소드를 활용해서 찾는다.
        current = self.head  # current(외부 참조 변수) 현재 위치는 list의 가장 늦게 추가된 데이터(즉 head가 참조하는 데이터) 커서와 유사한 기능
        count = 0
        while current is not None:  # 여기서도 head가 None을 가리키게 해놓으면 코드 짜기 편하다. 바로 0개 empty인 것 알 수 있다.
            count = count + 1  # 커서 이동하면서 count
            current = current.getNext()  # 이동

        return count

    def search(self, item):  # item: 찾는 대상 ,  목적은 있는지 확인하는 것 . Node 메소드 활용하는 논리
        current = self.head
        found = False
        while current != None and not found:
            # current(external reference set) = self.head 즉 head가 가리키는 자료, 이 자료가 none? 이면 list is empty라는 말이다.
            # 마지막 node의 Next_pointer은 None을 가리키게 설계함.
            # found = False라서 not found = True. Found가 False에서 True로 바뀌면 while문 종료 Not True = False이니까..
            if current.getData() == item:  # current = self.head가 가리키는 data, 그리고 이것은 node 객체이다.
                found = True  # While문 종료 조건
            else:
                current = current.getNext()  # 이동
        return found

    def remove(self, item):
        current = self.head  # currenct 커서
        previous = None  # 두번째 참조 변수, 커서 앞의 Node를 참조한다. 처음에는 head가 가리키는 첫번째 Node 앞에 아무것도 없어서 None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current  # 이 코드와 아래 줄 코드 순서가 중요하다. current가 가리키는 대상이 변하기 전에 previous가 가리키게 만들어야함
                current = current.getNext()  # 순서 중요 “inch-worming” 이라고 부른다.

        if previous == None:  # 특수한 경우. 삭제할 Node가 가장 앞에 있을 때
            self.head = current.getNext()  # 그냥 head가 가리키는 대상을 다음 Node로(즉 현재 current Node의 다음 Node)바꾸면 끝
        else:
            previous.setNext(current.getNext())  # 이전 Node(previous 가 참조하는 Node)의 Next_pointer가 Current가 참조하는 Node의 다음 Node를 가리키면 됨.
            # get.Next()는 다음 Node를 얻는 방법

