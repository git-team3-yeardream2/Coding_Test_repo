def solution(N):
    if N > 5:
        answer_sheet = [0] * (N + 1)
        answer_sheet[1] = 1
        answer_sheet[2] = 1
        answer_sheet[3] = 1
        answer_sheet[4] = 2
        answer_sheet[5] = 2
        for idx in range(6, N + 1):
            answer_sheet[idx] = answer_sheet[idx - 1] + answer_sheet[idx - 5]
    else:
        answer_sheet = [0,1,1,1,2,2]
    return answer_sheet[N]
