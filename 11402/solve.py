def solve(n, k, m):
    if k == 0 or k == n:
        return 1
    else:
        if k > n // 2:
            k = n - k
        B = [1] * (k + 1)
        for i in range(n + 1):
            for j in range(min(i, k), 0, -1):
                if j == 0 or j == i:
                    B[j] = 1
                else:
                    B[j] += B[j - 1]
        return B[k] % m
        
N, K, M = map(int, input().split())
answer = solve(N, K, M)
print(answer)