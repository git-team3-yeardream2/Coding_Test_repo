def prime(x):
    divisors = [num for num in range(1, x+1) if x%num == 0]
    if len(divisors) == 2:
        return True
    else:
        return False
    
## 쓰레기 코드
def solution(nums):
    answer = []
    for n1 in nums:
        for n2 in nums:
            if n1 != n2:
                for n3 in nums:
                    if n3 != n1 and n3 != n2:
                        if prime(n1+n2+n3):
                            if set([n1,n2,n3]) not in answer:
                                answer.append(set([n1, n2, n3]))
    return len(answer)


def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):  # 서로 다른 인덱스임을 주목
            for k in range(j+1,len(nums)):  # 단계적으로 인덱스 찾는 방법, 사람이랑 똑같음.
                if prime(nums[i] + nums[j] + nums[k]):
                    answer = answer + 1
    return answer
