import sys
input = sys.stdin.readline

from collections import deque

di = [0, 0, 1, -1, 0, 0]
dj = [1, -1, 0, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

def bfs(n, m, h, A):
    queue = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if A[k][i][j] == 1:
                    queue.append((k, i, j))
    while queue:
        k, i, j = queue.popleft()
        for t in range(6):
            nk, ni, nj = k + dk[t], i + di[t], j + dj[t]
            if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and A[nk][ni][nj] == 0:
                queue.append((nk, ni, nj))
                A[nk][ni][nj] = A[k][i][j] + 1
        # for k in range(h):
        #     for i in range(n):
        #         print(A[k][i])
        # print()
                        
    depth = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if A[k][i][j] == 0: return -1
                depth = max(depth, A[k][i][j])
    return depth - 1

M, N, H = map(int, input().split())
A = [[[*map(int, input().split())] for _ in range(N)] for _ in range(H)]
# for k in range(H):
#     for i in range(N):
#         print(A[k][i])
# print()
print(bfs(N, M, H, A))