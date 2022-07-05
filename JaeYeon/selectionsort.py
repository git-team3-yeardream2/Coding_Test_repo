def selectionsort(array):
    for recentlymovedidx in range(len(array)-1):  # n-1번 turn을 반복한다.
        # recentlymovedidx = turn  #  가장 왼쪽에 최소값이 존재한다. 비교값은 가장 최근에 옮긴 값이다. 왜? 가장 최근에 옮겼다 = 이전 turn에서 최소값 /0번 인덱스는 시작점이면서 최근에 옮겨졌다고 가정
        for idx in range(recentlymovedidx+1, len(array)):  # 기준 바로 오른쪽 부터 하나 하나씩 비교한다. 한 turn에서 여려 번 옮길 수 있다는 점 기억! 여러번 옮겨야 최소값이 옮겨진다.
            if array[recentlymovedidx] > array[idx]:  # 비교해서 작으면? 즉 최소값이 아니면?
                array[recentlymovedidx], array[idx] = array[idx], array[recentlymovedidx]  # swap
    return array


import random
data = random.sample(range(100), 50)  # random으로 리스트 만들기
print(data)
stlist = selectionsort(data)
print(stlist)
