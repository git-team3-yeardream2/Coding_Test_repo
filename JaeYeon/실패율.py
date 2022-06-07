# Full ver

def solution(N, stages):
    temp = {}  # Hashing 용 딕셔너리 만들기
    count = 0  # 걸러진 사람수 누적
    for num in range(1,N+1):  # N+1 까지 확인
        stage_num = stages.count(num)  # num의 숫자를 세서 이번 스테이지 진행 중인 사람 계산
        participation = len(stages)  # 참여자 수
        failure = stage_num/(participation-count+0.001)  # 실패율 계산
        temp[num] = failure  # Hashing
        count = count + stage_num
    item_list = temp.items()  #  딕셔너리의 items (Key,Value) 각 요소는 튜플로 전체 자료구조는 리스트로 반환
    sorted_item = sorted(item_list, key=lambda item: item[1], reverse=True)
    # 내림차순 정렬 + lambda를 이용한 Key Function, 각 요소별(item)로 접근해서 lambda function apply함
    # (Key,Value)중 [1] 1번 인덱스인 Value를 뽑고, Value를 Sorting Key로 사용한다.
    answer_dict = dict(sorted_item)  # 정렬이 완료된 item 리스트를 다시 딕셔너리로 바꾼다.
    answer = list(answer_dict.keys())  # 정렬된 딕셔너리에서 Key들만 리스트 자료구조로 뽑는다.
    print(answer_dict)
    return answer

# Short_code

def solution(N, stages):
    temp = {}
    count = 0
    for num in range(1,N+1):
        stage_num = stages.count(num)
        participation = len(stages)
        failure = stage_num/(participation-count+0.01)  # 실패율 계산
        temp[num] = failure  # Hashing
        count = count + stage_num
    return list(dict(sorted(temp.items(), key=lambda item: item[1], reverse=True)).keys())

# 시간복잡도 조정
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

