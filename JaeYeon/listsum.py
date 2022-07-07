import time


def sum(array):
    if len(array) <= 1:
        return array[0]
    return array[0] + sum(array[1:])


def sum2(array):
    if len(array) == 1:
        return array[-1]
    return array.pop() + sum2(array)


example = [i for i in range(900)]

start = time.time()
print(sum(example))
end = time.time()
print(f"{end - start:.5f} sec")


start = time.time()
print(sum2(example))
end = time.time()
print(f"{end - start:.5f} sec")


