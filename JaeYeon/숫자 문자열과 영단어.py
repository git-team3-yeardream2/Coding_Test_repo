def solution(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answers = []
    idx = 0
    while idx < len(s):  # idx는 0부터라서 부등호로... 등호 넣으면 idx 오버함.
        if s[idx] in numbers:
            answers.append(s[idx])
            idx = idx + 1
        elif s[idx] == 'z':
            answers.append('0')
            idx = idx + 4
        elif s[idx] == 'o':
            answers.append('1')
            idx = idx + 3
        elif s[idx] == 't':
            if s[idx + 1] == 'w':
                answers.append('2')
                idx = idx + 3
            elif s[idx + 1] == 'h':
                answers.append('3')
                idx = idx + 5
        elif s[idx] == 'f':
            if s[idx + 1] == 'o':
                answers.append('4')
                idx = idx + 4
            elif s[idx + 1] == 'i':
                answers.append('5')
                idx = idx + 4
        elif s[idx] == 's':
            if s[idx + 1] == 'i':
                answers.append('6')
                idx = idx + 3
            elif s[idx + 1] == 'e':
                answers.append('7')
                idx = idx + 5
        elif s[idx] == 'e':
            answers.append('8')
            idx = idx + 5
        else:
            answers.append('9')
            idx = idx + 4
    return int(''.join(answers))
