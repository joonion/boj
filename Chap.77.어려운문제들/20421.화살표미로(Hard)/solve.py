from heapq import heappush, heappop
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def move(t, i, j, l, r, x):
    if t == 0:
        return i + di[x], j + dj[x], l, r
    elif 1 <= t <= 3:
        x = (x - t) % 4
        return i + di[x], j + dj[x], l + t, r
    elif 4 <= t <= 6:
        x = (x + t - 3) % 4
        return i + di[x], j + dj[x], l, r + t - 3

def solve(n, m, k, maze):
    PQ = []
    mark = [[[1501] * 1501 for _ in range(m)] for _ in range(n)]
    heappush(PQ, (0, (0, 0, 0, 0)))
    mark[0][0][0] = 0
    while PQ:
        ui, uj, ul, ur = heappop(PQ)[1]
        # print(ui, uj, ul, ur)
        for t in range(7):
            vi, vj, vl, vr = move(t, ui, uj, ul, ur, maze[ui][uj])
            if 0 <= vi < n and 0 <= vj < m and vl <= k and vr <= k and mark[vi][vj][vl] > vr:
                if vi == n - 1 and vj == m - 1:
                    return True
                heappush(PQ, (vr, (vi, vj, vl, vr)))
                mark[vi][vj][vl] = vr
    return False

n, m, k = map(int, input().split())
A = [input() for _ in range(n)]
maze = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        maze[i][j] = "URDL".index(A[i][j])
print("Yes" if solve(n, m, k, maze) else "No")