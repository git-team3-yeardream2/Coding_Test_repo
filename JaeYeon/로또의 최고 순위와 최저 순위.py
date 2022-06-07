def solution(lottos, win_nums):
    no_zero = [lottos[i] for i in range(len(lottos)) if lottos[i] > 0]
    rank = [6, 6, 5, 4, 3, 2, 1]  # 등수표

    min = 0
    for i in range(len(no_zero)):
        if no_zero[i] in win_nums:
            min = min + 1

    max = min + len(lottos) - len(no_zero)
    score = [max, min]
    return [rank[max] ,rank[min]]
