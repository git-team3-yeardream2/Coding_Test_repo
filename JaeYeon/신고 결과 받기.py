def data_processing(id_list, report):
    table = {}  # 신고 결과 table 만듬, 중복 신고를 제거하기 위한 set
    for id in id_list:
        table[id] = set()

    processed_report = []
    for data in report:
        processed_report.append(data.split(" "))  # report 리스트의 각 요소를 또 리스트로 만듬

    for data in processed_report:  # table에 mapping
        key = data[0]
        value = data[1]
        table[key].add(value)  # set.add(element)

    return table

def solution(id_list, report, k):
    table = data_processing(id_list, report)  # 딕셔너리 호출
    total = []  # 총 신고회수 계산용 리스트
    for key in table:
        total = total + list(table.get(key))  # set을 list로 바꿔서 더함
    banned = []  # 정지된 아이디 목록을 리스트로
    for id in id_list:
        if total.count(id) >= k:
            banned.append(id)
    answer = []
    for id in id_list:
        my_ban = table.get(id).intersection(set(banned))
		# 각 id 별 자기 신고가 성공한 목록을 교집합으로
        answer.append(len(my_ban))  # 교집합의 길이가 결과 메일 수
    return answer
