class hashchaining:
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
            for idx in range(len(self.hash_table[hash_address])):  # self.hash_table[hash_address] = slot의 value를 list로 순회한다. (이중리스트)
                if self.hash_table[hash_address][idx][0] == idx_key:  # 만약에 기존의 idx_key를 가지는 value가 있으면?
                    self.hash_table[hash_address][idx][1] = value  # 새로운 value로 update한다.
            self.hash_table[hash_address].append([idx_key, value]) # 만약에 slot의 list를 모두 돌았는 idx_key와 같은게 없다면, 새로운 vlaue를 추가한다.
        else:
            self.hash_table[hash_address] = [[idx_key,value]]  # 주소의 slot에 이중리스트로 넣는다.

    def read_data(self, data):
        idx_key = self.getting_key(data)
        hash_address = self.hash_func(idx_key)
        if self.hash_table[hash_address] != 0:
            for idx in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][idx][0] == idx_key:
                    return self.hash_table[hash_address][idx][1]  # 이중리스트를 순회하고 자료가 있으면 value를 반환
            return None
        return None
