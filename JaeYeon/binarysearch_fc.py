import datetime

N = 5
N_list = [4, 1, 5, 2, 3]
M = 5
M_list = [1, 3, 7, 9, 5]

print (datetime.datetime.now())
for item in M_list:
    if item in N_list:
        print(1)
    else:
        print(0)
print (datetime.datetime.now())

def binarysearch(target,arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        if target == arr[0]:
            return 1
        else:
            return 0
    mediumidx = len(arr)//2
    if target > arr[mediumidx]:
        return binarysearch(target, arr[mediumidx:])
    elif target < arr[mediumidx]:
        return binarysearch(target, arr[:mediumidx])
    else:
        return 1


print (datetime.datetime.now())
for item in M_list:
    print(binarysearch(item,sorted(N_list)))
print (datetime.datetime.now())


def binary_search2(value, start, end):
    if start > end:
        return False

    median = (start + end) // 2
    if N_list[median] > value:
        return binary_search2(value, start, median - 1)
    elif N_list[median] < value:
        return binary_search2(value, median + 1, end)
    else:
        return True

print (datetime.datetime.now())
for item in M_list:
    if binary_search2(item, 0, N - 1):
        print(1)
    else:
        print(0)
print (datetime.datetime.now())
