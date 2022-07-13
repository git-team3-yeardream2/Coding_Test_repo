import time

import random
exam = random.sample(range(10000), 1000)
print(exam)

def qsort(array=[]):
    if len(array) <= 1:  # 0이면 빈 리스트 return해서 List 더하기, 1이면 [pivot] 이런식
        return array

    pivot = array[0]
    left, right = [], []
    for idx in range(1, len(array)):
        if array[idx] < pivot:
            left.append(array[idx])  # pivot의 왼쪽
        else:
            right.insert(0, array[idx])  # pivot의 오른쪽
    return qsort(left) + qsort([pivot]) + qsort(right

def qsort2(array=[]):
    if len(array) <= 1:  # 0이면 빈 리스트 return해서 List 더하기, 1이면 [pivot] 이런식
        return array

    pivot = array[0]
    left, right = [], []
    for idx in range(1, len(array)):
        if array[idx] < pivot:
            left.append(array[idx])  # pivot의 왼쪽
        else:
            right.append(array[idx])  # pivot의 오른쪽
    return qsort(left) + qsort([pivot]) + qsort(right))
