def binom(n, k):
    B = [[0] * (i + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j] + B[i-1][j-1]
    return B[n][k]

n, k = map(int, input().split())
print(binom(n - 1, k - 1))