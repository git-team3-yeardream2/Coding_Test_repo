  (use "git restore --staged <file>..." to unstage)

    processed_report = []
    for data in report:
        processed_report.append(data.split(" "))

    for data in processed_report:
        key = data[0]
        value = data[1]
        table[key].add(value)

    return table


def solution(id_list, report, k):
    table = data_processing(id_list, report)
    total = []
    for key in table:
        total = total + list(table.get(key))

    banned = []
    for id in id_list:
        if total.count(id) >= k:
            banned.append(id)

    answer = []
    for id in id_list:
        my_ban = table.get(id).intersection(set(banned))
        answer.append(len(my_ban))
    return answes
