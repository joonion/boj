def solve(n):
    S = 0
    for i in range(1, n):
        S += (i*n + i)
    return S
    
N = int(input())
answer = solve(N)
print(answer)