import sys
input = sys.stdin.readline

D = "URDL"
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def minimum(t, u, v, D, W):
    d1, d2, d3 = D[u][v], D[u][t], D[t][u]
    if d1 == 0:
        if d2 != 0 and d3 != 0:
            return (d2[0] + d3[0], d2[1] + d3[1])
    elif d2 != 0 and d3 != 0:
        d4 = (d2[0] + d3[0], d2[1] + d3[1])
        return min(d1, d4, key = lambda x : x[0] + x[1])
    return d1

def move(t, u, n, m, A):
    l = r = 0
    i, j = u // m, u % m
    x = D.index(A[i][j])
    if 1 <= t <= 3:
        x, l = (x - t) % 4, t
    if 4 <= t <= 6:
        x, r = (x + t - 3) % 4, t - 3
    ni, nj = i + di[x], j + dj[x]
    return ni * m + nj, l, r, (0 <= ni < n and 0 <= nj < m)

def solve(n, m, k, A):
    W = [[0] * (n * m) for _ in range(n * m)]
    for u in range(n * m):
        for t in range(7):
            v, l, r, valid = move(t, u, n, m, A)
            if valid:
                if W[u][v] == 0:
                    W[u][v] = [(l, r)]
                else:
                    W[u][v].append((l, r))

    D = [[0] * (n * m) for _ in range(n * m)]
    for u in range(n * m):
        for v in range(n * m):
            if W[u][v] == 0:
                D[u][v] = 0
            elif len(W[u][v]) == 1:
                D[u][v] = W[u][v][0]
            else:
                if sum(W[u][v][0]) <= sum(W[u][v][1]):
                    D[u][v] = W[u][v][0]
                elif sum(W[u][v][0]) > sum(W[u][v][1]):
                    D[u][v] = W[u][v][1]

    for t in range(n * m):
        for u in range(n * m):
            for v in range(n * m):
                D[u][v] = minimum(t, u, v, D, W)
    if D[0][n*m-1] != 0:
        if D[0][n*m-1][0] <= k and D[0][n*m-1][1] <= k:
            return True
    return False

n, m, k = map(int, input().split())
A = [input().strip() for _ in range(n)]
print("Yes" if solve(n, m, k, A) else "No")
