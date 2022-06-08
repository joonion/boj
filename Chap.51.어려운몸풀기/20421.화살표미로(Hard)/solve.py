from heapq import heappush, heappop

D = "URDL"
imv = [-1, 0, 1, 0]
jmv = [0, 1, 0, -1]

def move(t, i, j, L, R, A):
    x, nL, nR = D.index(A[i][j]), L, R
    if 1 <= t <= 3:
        x, nL = (x - t) % 4, L + t
    if 4 <= t <= 6:
        x, nR = (x + t - 3) % 4, R + t - 3
    return i + imv[x], j + jmv[x], nL, nR

def promising(i, j, L, R, n, m, k, mark):
    return 0 <= i < n and 0 <= j < m and mark[i][j] == 0 and L <= k and R <= k

def solve(n, m, k, A):
    PQ = []
    mark = [[0] * m for _ in range(n)]
    heappush(PQ, (0, (0, 0, 0, 0)))
    while len(PQ) > 0:
        (i, j, L, R) = heappop(PQ)[1]
        mark[i][j] = 1
        for t in range(7):
            ni, nj, nL, nR = move(t, i, j, L, R, A)
            if promising(ni, nj, nL, nR, n, m, k, mark):
                if (ni, nj) == (n - 1, m - 1):
                    return True
                heappush(PQ, (nL+nR, (ni, nj, nL, nR)))
    return False

import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
A = [input().strip() for _ in range(n)]
print("Yes" if solve(n, m, k, A) else "No")
