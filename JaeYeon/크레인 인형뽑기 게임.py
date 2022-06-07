def solution(board, moves):
    basket = []
    count = 0
    for i in range(len(moves)):  #n번째 크레인 작동
        num = moves[i] - 1  # 인덱스 일치시키기 0부터
        for j in range(len(board)):  # 맨 윗줄부터 1줄씩 검색
            if board[j][num] != 0:  # 1행에서 몇 번재 열이냐?
                basket.append(board[j][num])  #담고
                board[j][num] = 0  # 없애고
                break
        new_idx = len(basket) - 1  # basket의 인덱스 만들기
        last_idx = new_idx - 1
        if last_idx < 0:  # 빈 바구니에 암거도 없는 경우 방지
            continue
        if basket[new_idx] == basket[last_idx]:
            del basket[last_idx:]  # 2개 겹치면 터트리는거
            count = count + 2  # 개수 세기

    return count
