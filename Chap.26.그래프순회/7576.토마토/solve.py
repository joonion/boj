import sys
input = sys.stdin.readline

from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(n, m, A):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and A[ni][nj] == 0:
                queue.append((ni, nj))
                A[ni][nj] = A[i][j] + 1
    depth = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0: return -1
            depth = max(depth, A[i][j])
    return depth - 1

M, N = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
print(bfs(N, M, A))