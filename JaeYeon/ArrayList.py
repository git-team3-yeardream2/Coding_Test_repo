class BaseList:
  # 데이터의 추가
  def append(self, data):
      raise NotImplemented
  # 데이터의 탐색
  def search(self, data):
      raise NotImplemented
  # 데이터의 참조하기
  def get(self, index):
      raise NotImplemented
  # 데이터의 꺼내오기
  def pop(self):
      raise NotImplemented
  # 데이터의 삭제
  def remove(self, index):
      raise NotImplemented
  # 리스트 전체 출력
  def display(self):
      raise NotImplemented


class ArrayList(BaseList):  # BaseList 상속
  def __init__(self):
      self.list = []
      self.count = 0  # list안의 자료개수를 보여줌

  def append(self, data):
      self.list.append(data)
      self.count += 1

  def search(self, data):
      return [index for index, stored in enumerate(self.list) if stored == data] 
 # 왜 enumerate를 썼는가에 주목. element 값을 비교하는게 조건이고, return은 인덱스로

  def get(self, index):
      if 0 <= index < self.count:  # 원소개수가 n개인 list의 인덱스가 0부터 n-1까지임을 확인할 수 있다.
          return self.list[index]
      else:
          raise IndexError  # 인덱스 벗어나면 에러

  def pop(self):
      val = self.list[self.count - 1]  # 가장 마지막 요소(인덱스 값이 가장 큼)
      self.remove(self.count - 1)  # 제거
      return val  # 꺼내옴

  def remove(self, index):
      for _index in range(index, self.count - 1):  # 중요함, 배열에서 제거한 요소 다음 element들의 인덱스 다 한 칸씩 당겨옴
          self.list[_index] = self.list[_index + 1]

      del self.list[self.count - 1]
      self.count -= 1

  def display(self):
      for index in range(self.count):
          print(self.list[index])
