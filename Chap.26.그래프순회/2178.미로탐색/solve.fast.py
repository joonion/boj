di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
Q = [(0, 0, 1)]
V = [[1] * M for _ in range(N)]
V[0][0] = 0
X = 10**9
while Q:
    i, j, d = Q.pop(0)
    if i == N - 1 and j == M - 1:
        X = min(X, d)
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0<=ni<N and 0<=nj<M and A[ni][nj] and V[ni][nj]:
            Q += [(ni, nj, d+1)]
            V[ni][nj] = 0
print(X)
