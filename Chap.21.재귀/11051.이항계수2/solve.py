def solve(n, k):
    if k == 0 or k == n:
        return 1
    else:
        if k > n // 2:
            k = n - k
        B = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                if j == 0 or j == i:
                    B[i][j] = 1
                else:
                    B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
        return B[n][k] % 10007
        
N, K = map(int, input().split())
answer = solve(N, K)
print(answer)