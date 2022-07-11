def mergesplit(arr):
    if len(arr) == 1:
        return arr
    else:
        mididx = len(arr)//2  # Quotient is Integer, When slicing Only Integer can be used
        left = arr[:mididx]
        right = arr[mididx:]
        return merge(mergesplit(left), mergesplit(right))


def merge(leftarr, rightarr):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(leftarr) and right_idx < len(rightarr):  # len(arr) = Max_idx + 1이다.
        if leftarr[left_idx] < rightarr[right_idx]:
            result.append(leftarr[left_idx])
            left_idx = left_idx + 1
        else:
            result.append(rightarr[right_idx])
            right_idx = right_idx + 1
    if left_idx < len(leftarr):  # while문 끝나고, 왼쪽 배열만 남았다면?
        result = result + leftarr[left_idx:]
    if right_idx < len(rightarr):  # while문 끝나고, 오른쪽 배열만 남았다면?
        result = result + rightarr[right_idx:]
    return result


import random
test_date = random.sample(range(1000), 30)

print(test_date)
print(mergesplit(test_date))
