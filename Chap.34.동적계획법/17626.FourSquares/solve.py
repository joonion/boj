from math import sqrt, floor
            
def solve(n):
    D = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        minimum = 5
        for j in range(1, floor(sqrt(i)) + 1):
            minimum = min(minimum, D[i - j**2])
        D[i] = minimum + 1
    return D[n]

n = int(input())
answer = solve(n)
print(answer)