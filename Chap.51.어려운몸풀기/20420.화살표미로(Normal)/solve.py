from heapq import heappush, heappop

D = "URDL"
imv = [-1, 0, 1, 0]
jmv = [0, 1, 0, -1]

def move(t, i, j, l, r, A):
    x = D.index(A[i][j])
    if 1 <= t <= 3: # rotate left
        x = (x - t) % 4
        l = l + t
    elif 4 <= t <= 6: # rotate right
        x = (x + t - 3) % 4
        r = r + t - 3
    return i + imv[x], j + jmv[x], l, r

def bfs(n, m, k, A):
    PQ = []
    heappush(PQ, (0, (0, 0, 0, 0)))
    mark = [[False] * m for _ in range(n)]
    while len(PQ) > 0:
        i, j, l, r = heappop(PQ)[1]
        for t in range(7):
            ni, nj, nl, nr = move(t, i, j, l, r, A)
            if 0 <= ni < n and 0 <= nj < m and not mark[ni][nj] and nl <= k and nr <= k:
                if ni == n - 1 and nj == m - 1:
                    return True
                heappush(PQ, (nl + nr, (ni, nj, nl, nr)))
        mark[i][j] = True
    return False
    
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
A = [input().strip() for _ in range(n)]
print("Yes" if bfs(n, m, k, A) else "No")