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


def baseconverter(number, base):
    digits = "0123456789ABCDEF"  # string의 index 사용
    temp = _stack()
    while number > 0:
        resi = digits[number % base]
        temp.push(resi)
        number = number//base
    answer = ''  # string 더하기
    for i in range(temp.count()):
        answer = answer + temp.pop()
    return answer

print(baseconverter(14, 14))


def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = _stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
#  When a remainder is removed from the stack, it can be used to index into the digit string and the correct resulting digit can be appended to the answer.
    return newString

print(baseConverter(26, 26))
