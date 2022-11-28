def dfs(i, j, n, m, A):
    ni, nj = i, j
    cur = A[ni][nj]
    while ni < n and nj < m and A[ni][nj] == cur:
        A[ni][nj] = 'x'
        if cur == '-': nj += 1
        else: ni += 1

def solve(n, m, A):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] != 'x':
                cnt += 1
                dfs(i, j, n, m, A)
    return cnt

N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
print(solve(N, M, A))
