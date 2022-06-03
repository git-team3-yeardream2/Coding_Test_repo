def solution(N, stages):
    temp = {}
    count = 0
    stage_count = {}
    for stage in range(1,N+1):
        stage_count[stage] = stages.count(stage)  # 시간복잡도 생각해서 for 문 밖으로 뺌
    for num in range(1,N+1):
        stage_num = stage_count[num]
        participation = len(stages)
        if participation != count:
            failure = stage_num / (participation - count)  # 실패율 계산
        else:
            failure = 0
        temp[num] = failure  # Hashing
        count = count + stage_num
    return sorted(temp, key=lambda x : temp[x], reverse=True)  # sorted 딕셔너리의 iterable element는  디폴트가 key입니다.


