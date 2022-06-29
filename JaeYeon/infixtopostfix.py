class _stack:
    def __init__(self):
        self.stack  = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        return item

    def isEmpty(self):
        return self.stack == []

    def count(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

def infixtopostfix(infixexpr):
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    prec = {"**" : 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}  # operator의 우선 순위 딕셔너리 (why? 연산자를 보고 우선 순위를 숫자로 hashing해서 비교하기 쉽게)
    opstack = _stack()  # 이 알고리즘이 기본적으로 stack을 써야함.
    output = []  # 결과물을 넣기 위한 리스트
    tokens = infixexpr.split()  # 인자로 받은 문자열을 리스트(why? 수정하기 쉽게 바꿈)
    for token in tokens:  # 리스트를 순회하면서 봅니다.
        if token in operands:  # 피연산자는?
            output.append(token)  # 결과 리스트에 넣는다.
        elif token == '(':  # 좌 괄호(가장 연산 순위가 낮은 괄호라서 그냥 무지성으로 스택에 깔아줌)
            opstack.push(token)
        elif token == ')':  # 우 괄호(가장 연산 순위가 높다고 생각해도 됨) 스택의 head를 알려준다.
            top_token = opstack.pop()  # 스택에 넣어둔 연산자를 하나씩 꺼낸다.
            while top_token != '(':  # 하나씩 꺼내다보면 가장 밑 바닥의 좌괄호를 만나고 멈춘다.
                output.append(top_token)
                top_token = opstack.pop()  # why? 이렇게 반복문과 스택을 활용할까. 연산자가 여러 개 나올 수 있기 때문이다. 그리고 사람이 읽는 순서랑 같게 연산할 수 있다.
        else:  # 괄호가 아닌 연산자의 경우
            while (not opstack.isEmpty()) and prec[opstack.peek()] >= prec[token]:
                # 스택이 비어있는 경우는, 왼쪽에서 읽다가 괄호 없이 시작하는 경우인데, A + B 같은 경우다.
                # 현재 stack의 peek = * , token = + 라면 *를 먼저 결과에 보내야한다.
                output.append(opstack.pop())  # stack의 peek인 *를 결과로 먼저 보내는 코드
            opstack.push(token)  # stack이 비면 stack에 바로 token을 넣어주고, token의 우선순위가 높다면 token을 넣어준다.
            # 이 코드를 통해서 결과적으로 stack에 우선순위가 반영되서 저장됨을 알 수 있다!!
    while not opstack.isEmpty():
        output.append(opstack.pop())  # token 순회가 끝나고, 스택에 남아있는(정렬되어 있음) 연산자를 다 때려 넣으면 끝이다.
    return " ".join(output)


print(infixtopostfix("5 * 3 ** ( 4 - 2 )"))
