tshape = [[[1, 1, 1], [0, 1, 0]],   # ㅜ
          [[0, 1, 0], [1, 1, 1]],   # ㅗ
          [[1, 0], [1, 1], [1, 0]], # ㅏ
          [[0, 1], [1, 1], [0, 1]]] # ㅓ

imove = [0, 1, 0, -1]
jmove = [1, 0, -1, 0]

best = []

def dfs(d, w, i, j, mark, A):
    global imove, jmove
    if d == 0:
        return w + A[i][j]
    else:
        maxvalue = 0
        for k in range(4):
            ni, nj = i + imove[k], j + jmove[k]
            if not (0 <= ni < len(A) and 0 <= nj < len(A[0])):
                continue
            if not mark[ni][nj]:
                mark[ni][nj] = True
                maxvalue = max(maxvalue, dfs(d - 1, w + A[i][j], ni, nj, mark, A))
                mark[ni][nj] = False
        return maxvalue

def tvalue(i, j, T, A):
    value = 0
    for r in range(len(T)):
        for c in range(len(T[0])):
            if T[r][c] == 1:
                value += A[i + r][j + c]
    return value
    
def solve(n, m, A):
    opt = 0
    for i in range(n):
        for j in range(m):
            mark = [[False] * m for _ in range(n)]
            mark[i][j] = True
            opt = max(opt, dfs(3, 0, i, j, mark, A))
    for k in range(len(tshape)):
        T = tshape[k]
        for i in range(n - len(T)):
            for j in range(m - len(T[0])):
                opt = max(opt, tvalue(i, j, T, A))
    return opt

import sys
input = sys.stdin.readline
                
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = solve(N, M, A)
print(answer)