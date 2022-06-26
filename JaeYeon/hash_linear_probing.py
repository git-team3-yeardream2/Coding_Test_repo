class hashlinearprobing:
    def __init__(self):
        self.hash_table = [0 for i in range(10)]

    def getting_key(self, data):  # key를 만드는 함수
        return hash(data)

    def hash_func(self, data):  # 간단하게 Hash_function을 10으로 나눈 나머지로.
        key = self.getting_key(data)  # 만약 key가 21,11인 data가 각각 있다면, 이들의 adress가 같아서 hash충돌이 일어날 것이다.
        return key % 10

    def storage_data(self, data, value):  # 데이터가 사람이름이고, value가 그 사람의 전화번호라는 예시
        idx_key = self.getting_key(data)  # index_key를 만든다. (key를 해쉬 함수에 넣은 adress)가 충돌할 예정이기 때문에 idx_key를 따로 지정한다.
        hash_address = self.hash_func(idx_key)  # key를 주소로 변환
        if self.hash_table[hash_address] != 0:  # 만약에 겹치면 즉 충돌이 발생하는 경우, 즉 이미 이 주소의 슬롯에 value가 들어있다.
            for idx in range(hash_address, len(self.hash_table)):
                if self.hash_table[idx] == 0:  # 동작 1번: 비었는지 확인
                    self.hash_table[idx] = [idx_key, value]  # 다음 주소 중 가장 가까운 빈 주소에 리스트 형태로 데이터를 넣는다.
                elif self.hash_table[idx][0] == idx_key:  # 동작 2번: 빈 slot이 아니더라도, slot의 이중리스트를 확인해서
                    self.hash_table[idx][1] = value  # update한다.
        else:
            self.hash_table[hash_address] = [idx_key, value]  # 주소에 충돌이 일어나지 않으면, 그냥 데이터를 넣는다.


    def read_data(self, data):
        idx_key = self.getting_key(data)
        hash_address = self.hash_func(idx_key)
        if self.hash_table[hash_address] != 0:
            for i in range(hash_address, len(self.hash_table)):
                if self.hash_table[i] == 0:  # 충돌과 데이터 존재 여부는 다르다. 충돌이 되면 데이터 존재 여부를 확인한다.
                    return None
                elif self.hash_table[i][0] == idx_key:  # 데이터 존재 여부를 idx_key로 확인한다.
                    return self.hash_table[i][1]
        else:  # 만약에 hash_table[hash_address] == 0의 경우 데이터가 없다는 말이다. 충돌이 안 되면 데이터는 반드시 없다.
            return None
