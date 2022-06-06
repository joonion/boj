def solve(n, m):
    if m > n // 2: m = n - m
    D = [1] * (m + 1)
    for i in range(n):
        for j in range(min(i, m), 0, -1):
            D[j] += D[j - 1]
    return D[m]
        
n, m = map(int, input().split())
print(solve(n, m))