class Heap:
    def __init__(self, data= None):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 0:  # 방어 코드
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        insertedidx = len(self.heap_array) - 1  # insertedidx를 왜 지역변수로 선언했을까? while문 안에서만 돌게 하기 위해서.
        while self.moveup(insertedidx):
            parent_idx = insertedidx//2
            self.heap_array[insertedidx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                insertedidx]
            insertedidx = parent_idx

        return True

    def moveup(self,insertedidx):
        parent_idx = insertedidx // 2
        if insertedidx <= 1:
            return False
        if self.heap_array[insertedidx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:  # 데이터가 하나거나 없으면 삭제 안 한다. default가 데이터 1개 상태
            return None

        returned_data = self.heap_array[1]  # 루트 노드를 반환하기 위해 할당해둔다.
        self.heap_array[1] = self.heap_array[-1]  # 가장 마지막에 넣은 값을 루트노드로 덮어쓴다.
        del self.heap_array[-1]  # 가장 마지막에 넣은 값 삭제
        popped_idx = 1

        while self.movedown(popped_idx):  # 자식이 있는 경우만 바꿔주면 된다.
            leftchild_popped_idx = popped_idx * 2
            rightchild_popped_idx = popped_idx * 2 + 1

            if rightchild_popped_idx >= len(self.heap_array):  # 자식이 1명인 경우
                self.heap_array[leftchild_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], \
                                                                                     self.heap_array[
                                                                                         leftchild_popped_idx]  # 값 바꾸기
                popped_idx = leftchild_popped_idx  # 원래 값의 인덱스로 찾아가게
                # if self.heap_array[leftchild_popped_idx] > self.heap_array[popped_idx]:  # 이 조건문 굳이 필요한지?? 없이 돌려보기
                #     self.heap_array[leftchild_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[leftchild_popped_idx]  # 값 바꾸기
                #     popped_idx = leftchild_popped_idx  # 원래 값의 인덱스로 찾아가게
            else:  # 자식이 2명인 경우
                if self.heap_array[leftchild_popped_idx] > self.heap_array[rightchild_popped_idx]:  # 왼쪽 자식의 값이 오른쪽 자식의 값보다 클 경우.
                    self.heap_array[leftchild_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], \
                                                                                         self.heap_array[
                                                                                             leftchild_popped_idx]  # 값 바꾸기
                    popped_idx = leftchild_popped_idx  # 원래 값의 인덱스로 찾아가게
                    # if self.heap_array[leftchild_popped_idx] > self.heap_array[popped_idx]:  # 왼쪽 자식과 부모를 비교한다.
                    #     self.heap_array[leftchild_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[leftchild_popped_idx]  # 값 바꾸기
                    #     popped_idx = leftchild_popped_idx  # 원래 값의 인덱스로 찾아가게
                else:  # 오른쪽 자식의 값이 왼쪽 자식의 값보다 클 경우
                    self.heap_array[rightchild_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], \
                                                                                          self.heap_array[
                                                                                              rightchild_popped_idx]
                    popped_idx = rightchild_popped_idx  # 원래 값의 인덱스로 찾아가게
                    # if self.heap_array[rightchild_popped_idx] > self.heap_array[popped_idx]:  # 오른쪽 자식과 부모를 비교한다.
                    #     self.heap_array[rightchild_popped_idx], self.heap_array[popped_idx]= self.heap_array[popped_idx], self.heap_array[rightchild_popped_idx]
                    #     popped_idx = rightchild_popped_idx  # 원래 값의 인덱스로 찾아가게

        return returned_data

    def movedown(self, popped_idx):  # while에 불린형으로 쓰기 위한 함수
        leftchildidx = popped_idx * 2
        rightchildidx = popped_idx * 2 + 1

        if leftchildidx >= len(self.heap_array):  # case1 No child
            return  False
        elif rightchildidx >= len(self.heap_array):  # case2 only one child
            if self.heap_array[leftchildidx] > self.heap_array[popped_idx]:  # 작은 값이 위층에 있는 경우, 아래 층의 큰 수를 올린다.
                return True
            else:
                return False
        else:  # case3 two children, 자식 중 더 큰 값과 비교해야 한다.
            if self.heap_array[leftchildidx] > self.heap_array[rightchildidx]:  # 왼쪽 자식의 값이 오른쪽 자식의 값보다 클 경우.
                if self.heap_array[leftchildidx] > self.heap_array[popped_idx]:  # 왼쪽 자식과 부모를 비교한다.
                    return True  # 큰 값을 올려야한다.
                else:
                    return False
            else:  # 오른쪽 자식의 값이 왼쪽 자식의 값보다 클 경우
                if self.heap_array[rightchildidx] > self.heap_array[popped_idx]:  # 오른쪽 자식과 부모를 비교한다.
                    return True  # 큰 값을 올려야한다.
                else:
                    return False

test = Heap(20)
for num in range(1,15):
    test.insert(num)
print(test.heap_array)

print(test.pop())
print(test.pop())
print(test.heap_array)
