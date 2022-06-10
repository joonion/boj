import sys
input = sys.stdin.readline
INF = 10 ** 10

def solve(n, W):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = min(W[i][j], W[i][k] + W[k][j])

n = int(input())
m = int(input())
W = [[INF] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if W[u-1][v-1] > w:
        W[u-1][v-1] = w
for i in range(n):
    W[i][i] = 0
solve(n, W)
for i in range(n):
    for j in range(n):
        if W[i][j] == INF:
            W[i][j] = 0
    print(" ".join(map(str, W[i])))
