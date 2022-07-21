def isPrime(num):
    div = 0
    for i in range(1,num+1):
        if num % i == 0:
            div = div + 1
    if div == 2:
        return True
    else:
        return False


def primecount():
    Found = False
    num = 1
    count = 0
    while not Found:
        num = num + 1
        if isPrime(num):
            count = count + 1
        if count == 10001:
            Found = True
    return num

print(primecount())
