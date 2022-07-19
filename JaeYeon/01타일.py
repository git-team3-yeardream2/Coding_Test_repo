N = int(input())

solution = [0]*1000001
solution[1] = 1
solution[2] = 2
for idx in range(3, 1000001):
    solution[idx] = (solution[idx-1] + solution[idx-2]) % 15746

print(solution[N])

