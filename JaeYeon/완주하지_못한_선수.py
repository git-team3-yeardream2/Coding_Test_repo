def solution(participant, completion):
    temp = 0  # Hash_value는 int이기 때문에 0을 기준으로 +- 연산가능
    dic = {}  # Python의 Hashing 방법 == dictionary
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]  #겹치는 Hash_value들은 0이되어서 없어지고 남는게 단 1개
    return answer
