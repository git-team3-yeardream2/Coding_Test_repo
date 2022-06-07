def solution(new_id):
    admitted_characters = ['-', '_', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  # 허용문자 리스트 만들기
    new_id = new_id.lower()  # 1단계 소문자 치환

    new_list = []  #2단계 허용문자 빼고 제거
    for char in new_id:
        if char in admitted_characters:
            new_list.append(char)
    new_id = ''.join(new_list)

    new_id = new_id.replace('.',' ')  # 3단계 4단계 동시에 진행.
    new_id = '.'.join(new_id.split())

    if new_id == '':  # 5단계 빈 문자열이면 'a' 추가
        new_id = new_id + 'a'

    if len(new_id) >= 16:  # 6단계 길이 제한
        new_id = new_id[:15]
    new_id = new_id.replace('.', ' ')  
    new_id = '.'.join(new_id.split())

    if len(new_id) <= 2:  # 7단계 
        new_id = new_id + new_id[-1]*(3-len(new_id))

    return new_id

