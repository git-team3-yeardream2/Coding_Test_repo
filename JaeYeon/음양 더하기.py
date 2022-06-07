def solution(absolutes, sign):
    answer = 0
    for i in range(len(sign)):
        if sign[i]:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]
    return answer
