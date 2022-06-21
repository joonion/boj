import sys
input = sys.stdin.readline

INF = 10**10

def solve(n, W):
    D = [[INF] * (1<<n) for _ in range(n)]
    D[0][0] = 0
    for k in range(1<<n):
        for i in range(n):
            for j in range(n):
                if D[j][k|(1<<i)] > D[i][k] + W[i][j]:
                    D[j][k|(1<<i)] = D[i][k] + W[i][j]
    return D[0][(1<<n)-1]
                
n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, W))
