left_line = [1, 4, 7, '*']
center_line = [2, 5, 8, 0]
right_line = [3, 6, 9, '#']  # key_pad 만들기
left_hand = '*'
right_hand = '#'

def distance(start,end):  # start = 현재위치, end는 항상 center_line
    if start in center_line:
        return abs(center_line.index(start)-center_line.index(end))
    elif start in left_line:  # 무조건 옆 라인으로 한번은 옮겨야하니까 +1
        return 1+ abs(left_line.index(start)-center_line.index(end))
    else:
        return 1+ abs(right_line.index(start)-center_line.index(end))

def solution(numbers, hand):
    global right_hand, left_hand
    answer = []
    for num in numbers:
        if num in left_line:
            left_hand = num
            answer.append("L")
        elif num in right_line:
            right_hand = num
            answer.append("R")
        else:
            if distance(left_hand, num) < distance(right_hand, num):
                left_hand = num
                answer.append("L")
            elif distance(left_hand, num) > distance(right_hand, num):
                right_hand = num
                answer.append("R")
            else:
                if hand == 'right':
                    right_hand = num
                    answer.append("R")
                else:
                    left_hand = num
                    answer.append("L")
    return "".join(answer)  # Join_method
