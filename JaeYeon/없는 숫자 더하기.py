def solution(numbers):
    answer = 0
    for num in range(10):
        if num not in numbers:  # not in 하나씩 비교하면서 아닌거 찾기.
            answer = answer + num
    return answer
