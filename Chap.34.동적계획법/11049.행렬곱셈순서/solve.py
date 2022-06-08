def solve(n, d):
    INF = 0xFFFFFFFF
    D = [[0] * (n + 1) for _ in range(n + 1)]
    for diag in range(1, n):
        for i in range(1, n - diag + 1):
            j = i + diag
            D[i][j] = INF
            for k in range(i, j):
                D[i][j] = min(D[i][j], D[i][k] + D[k+1][j] + d[i-1]*d[k]*d[j])
    return D[1][n]

n = int(input())
d = [0] * (n + 1)
d[0], d[1] = map(int, input().split())
for i in range(2, n + 1):
    d[i] = int(input().split()[1])
print(solve(n, d))