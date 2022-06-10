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

    def add(self, item):
        temp = Node(item) # 데이터 value (여기서는 argument item에 입력하는 값)이 들어가고 Next-pointer은 None을 가리키는 상태
        temp.setNext(self.head)  # step1 기존의 head가 참조하는 데이터(old first node 가장 앞의 data)를 Next-pointer가 가리키도록 함
        self.head = temp  # step2 이번에 추가한 data를 새로운 head로 설정한다. #step 순서 지키는거 매우 중요함!!!

    def size(self):  # traversal
        current = self.head  # current(외부 참조 변수) 현재 위치는 list의 가장 늦게 추가된 데이터(즉 head가 참조하는 데이터) 커서와 유사한 기능
        count = 0
        while current is not None:  # 여기서도 head가 None을 가리키게 해놓으면 코드 짜기 편하다. 바로 0개 empty인 것 알 수 있다.
            count = count + 1  # 커서 이동하면서 count
            current = current.getNext()  # 이동

        return count
