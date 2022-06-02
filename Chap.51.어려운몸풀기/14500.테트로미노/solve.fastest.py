def dfs(d, s, i, j, n, m, A):
    print(d, i, j, s)
    if d == 0:
        return s
    else:
        right = 0 if i == n - 1 else dfs(d - 1, s + A[i+1][j], i+1, j, n, m, A)
        top = 0 if i == 0 else dfs(d - 1, s + A[i-1][j], i-1, j, n, m, A)
        bottom = 0 if j == m - 1 else dfs(d - 1, s + A[i][j+1], i, j+1, n, m, A)
        return max(right, top, bottom)

def solve(n, m, A):
    opt = 0
    for i in range(n):
        for j in range(n):
            opt = max(opt, dfs(3, A[i][j], i, j, n, m, A))
    # ㅗ ㅜ
    h, w = 2, 3 
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+1]);
            opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]+A[i][j+1]);
    # ㅏ ㅓ
    h, w = 3, 2
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+1][j+1]);
            opt = max(opt, A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]+A[i+1][j]);
    return opt

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, A))