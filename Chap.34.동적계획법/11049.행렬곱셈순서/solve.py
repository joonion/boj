def solve(n, d):
    global INF
    D = [[0] * (n + 1) for _ in range(n + 1)]
    for diag in range(1, n):
        for i in range(1, n - diag + 1):
            j = i + diag
            D[i][j] = INF
            for k in range(i, j):
                D[i][j] = min(D[i][j], D[i][k] + D[k+1][j] + d[i-1]*d[k]*d[j])
    return D[1][n]

import sys
lines = sys.stdin.readlines()
n = int(lines[0])
d = [0] * (n + 1)
d[0] = int(lines[1].split()[0])
for i in range(1, n + 1):
    d[i] = int(lines[i].split()[1])
INF = 2 ** 32 - 1
answer = solve(n, d)
print(answer)