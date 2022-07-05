def bubblesort(array):
    for turn in range(len(array)-1):  # 길이가 n이면 n-1 turn 돈다.
        swap = False
        for idx in range(len(array)-1-turn):  # turn이 0부터 하나씩 늘어나면서 비교 횟수는 1개씩 줄어든다.
            if array[idx] > array[idx+1]:  # 앞,뒤의 값을 비교한다.
                array[idx], array[idx+1] = array[idx+1], array[idx]
                swap = True
        if swap is False:  # 1번째 turn 했는데 swap이 발생하지 않았다면?
            return array
    return array

import random
data = random.sample(range(100), 50)
print(data)
stlist = bubblesort(data)
print(stlist)

