def insertionsort(array):
    for stand in range(1, len(array)):  # n-1 turn 돈다
        for key in range(stand, 0, -1):  # key 부터 거꾸로 돌아오면서 비교한다. 여기가 중요
            if array[key] < array[key-1]:  # key와 바로 앞 데이터의 값을 비교한다.
                array[key], array[key-1] = array[key-1], array[key]  # swap
            else:
                break  # turn 1개 종료
    return array

import random
data = random.sample(range(100), 50)  # random으로 리스트 만들기
print(data)
stlist = insertionsort(data)
print(stlist)
