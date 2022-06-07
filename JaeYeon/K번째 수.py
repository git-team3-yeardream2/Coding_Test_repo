def solution(array, commands):
    answer = []
    for arr in commands:
        start = arr[0]
        end = arr[1]
        k_key = arr[2]
        sliced_list = []
        for idx in range(start, end+1):
            sliced_list.append(array[idx-1])
        k_value = sorted(sliced_list)[k_key-1]
        answer.append(k_value)
    return answer

