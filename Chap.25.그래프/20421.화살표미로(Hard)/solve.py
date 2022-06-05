import sys
input = sys.stdin.readline

D = "URDL"
imv = [-1, 0, 1, 0]
jmv = [0, 1, 0, -1]

def move(d, t, i, j):
    x, l, r = D.index(d), 0, 0
    if 1 <= t <= 3:
        x, l = (x - t) % 4, t
    if 4 <= t <= 6:
        x, r = (x + t - 3) % 4, t - 3
    return i + imv[x], j + jmv[x], l + r

def weight(u, v, A, m):
    global INF
    ui, uj = u // m, u % m
    vi, vj = v // m, v % m
    if abs(ui - vi) > 1 or abs(vj - vj) > 1:
        return INF
    for t in range(7):
        ni, nj, w = move(A[ui][uj], t, ui, uj)
        if ni == vi and nj == vj:
            return w
    return INF

def nearest(length):
    minlength, vnear = INF, 0
    for v in range(1, n):
        if 0 <= length[v] < minlength:
            minlength, vnear = length[v], v
    return vnear

def dijkstra(R, C, A):
    N = R * C
    length = [INF] * N
    length[0] = -1
    for v in range(1, N):
        length[v] = weight(0, v, A, C)
    for _ in range(N - 1):
        vnear = nearest(length)
        for v in range(1, N):
            W = weight(vnear, v, A)
            if length[vnear] + W < length[v]:
                length[v] = length[vnear] + W
        if vnear == N - 1 and length[vnear] < INF:
            return True
        length[vnear] = -1
    return False

R, C, K = map(int, input().split())
A = [input().strip() for _ in range(R)]
INF = 2 * K + 1
print("Yes" if dijkstra(R, C, A) else "No")